Travel Sathi — NLP Travel Companion
Domain: ✈️ Travel

Hackathon: Hack4Hour 2026

🌟 Overview
Travel Sathi is a full-stack conversational AI designed to solve the complexity of trip planning. It allows users to input natural language queries about destinations and budgets, providing context-aware responses through an interactive chat interface.

🧠 NLP Features (Min. 2 Required)
We have implemented the following NLP techniques on our Python backend:

- **Intent Detection (Feature A):**  
  <span style="color:#2C3E50;">Classifies user input into categories such as "Recommendation," "Weather Inquiry," or "Budget Planning".</span>  
  **Tools Used:** <span style="color:#E74C3C;">Sklearn / NLTK</span>  

- **Named Entity Recognition (Feature E):**  
  <span style="color:#2C3E50;">Extracts specific entities like destinations (GPE) and dates from user sentences to personalize responses.</span>  
  **Tools Used:** <span style="color:#E74C3C;">SpaCy</span>  

---

💻 **Tech Stack**  
- Backend: <span style="color:#2980B9;">Python with Flask/FastAPI</span>  
- Frontend: <span style="color:#2980B9;">HTML/CSS/JS (or your specific framework)</span>  
- NLP Libraries: <span style="color:#2980B9;">SpaCy, Sklearn, and NLTK</span>  

📊 **Dataset Reference**  
- Name: <span style="color:#D35400;">[Hugging face-  "https://datasets-server.huggingface.co/rows?dataset=bitext%2FBitext-travel-llm-chatbot-training-dataset&config=default&split=train&offset=0&length=100"]</span>  
- Usage: Used to train the Intent Classifier and provide destination-specific data for the chatbot's responses.  

---

🚀 **Getting Started**  
**Prerequisites**  
- Python 3.8+  
- `pip install -r requirements.txt`  

**Running the App**  
- Start Backend:  
  ```bash
  python app.py
