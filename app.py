from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import uvicorn
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor

# Custom modules
from nlp_processor import NLPManager
from model_handler import get_ai_response, generate_voice

app = FastAPI(title="Travel-Sathiii Backend")
executor = ThreadPoolExecutor(max_workers=10)

# 1. CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Folder Setup
if not os.path.exists("static"):
    os.makedirs("static")
app.mount("/static", StaticFiles(directory="static"), name="static")

nlp_tool = NLPManager()

# 3. Load Dataset using hf:// protocol
print("⏳ Loading full Travel Dataset from Hugging Face CSV...")
try:
    # This directly reads the CSV from the Hugging Face repo
    dataset_url = "hf://datasets/bitext/Bitext-travel-llm-chatbot-training-dataset/bitext-travel-llm-chatbot-training-dataset.csv"
    df = pd.read_csv(dataset_url)
    # Keeping only essential columns to save memory
    df = df[['instruction', 'response']]
    print(f"✅ Dataset ready! Loaded {len(df)} rows.")
except Exception as e:
    print(f"❌ Dataset Error: {e}")
    print("Tip: Run 'pip install huggingface_hub fsspec'")
    df = pd.DataFrame(columns=['instruction', 'response'])

# 4. Context Retrieval Logic
def get_travel_context(user_query):
    if df.empty:
        return "No travel data available."
    
    keywords = user_query.lower().split()
    # Search for any keyword match in the instruction column
    mask = df['instruction'].str.contains('|'.join(keywords), case=False, na=False)
    results = df[mask].head(3) 
    
    if not results.empty:
        context_lines = []
        for _, row in results.iterrows():
            instruction = str(row['instruction']).strip()
            response = str(row['response']).strip()
            if instruction and response:
                context_lines.append(f"Q: {instruction}\nA: {response}")
        return "\n---\n".join(context_lines) if context_lines else "Travel data found but format unclear."
    
    # If no exact match, provide generic travel context
    return "No specific travel data found. Using general travel guide."

class UserQuery(BaseModel):
    message: str

# 5. The Main Chat Route
@app.post("/chat")
async def chat(query: UserQuery):
    loop = asyncio.get_event_loop()
    print(f"📩 Message received: {query.message}")
    
    # NLP Analysis (Sentiment/Entities)
    nlp_results = nlp_tool.analyze(query.message)
    
    # Retrieval
    context = get_travel_context(query.message)
    print(f"📚 Context retrieved: {context[:100]}...")
    
    # LLM Call (Non-blocking)
    print("🤖 Requesting response...")
    answer = await loop.run_in_executor(executor, get_ai_response, query.message, context)
    print(f"✅ Response generated: {answer[:100]}...")
    
    # Audio Generation (Non-blocking)
    print("🔊 Generating Audio...")
    try:
        audio_file = await loop.run_in_executor(executor, generate_voice, answer)
        # Using relative path for the frontend
        audio_url = f"http://127.0.0.1:8000/static/{audio_file}"
    except Exception as e:
        print(f"🔊 Audio Error: {e}")
        audio_url = None

    print("✅ Chat request complete.")
    return {
        "reply": answer,
        "audio_url": audio_url,
        "nlp_metadata": nlp_results
    }

@app.get("/")
async def root():
    return {"status": "Travel-Sathiii is Online"}

if __name__ == "__main__":
    # Standard local port
    uvicorn.run(app, host="127.0.0.1", port=8000)