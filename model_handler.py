import requests
from gtts import gTTS
import os
import uuid

def build_travel_guide(user_query, context):
    """Build a structured travel guide response from dataset context."""
    query_lower = user_query.lower()
    
    # Extract location info
    locations = []
    if 'bangalore' in query_lower or 'bengaluru' in query_lower:
        locations.append('Bangalore')
    if 'goa' in query_lower:
        locations.append('Goa')
    if 'delhi' in query_lower:
        locations.append('Delhi')
    if 'mumbai' in query_lower:
        locations.append('Mumbai')
    
    response = ""
    
    # Detect query type
    if 'travel' in query_lower or 'from' in query_lower or 'to' in query_lower:
        if len(locations) >= 2:
            response = f"🧳 Travel Guide: {' → '.join(locations)}\n\n"
            response += "📍 Travel Tips:\n"
            response += "• Best time to visit: October to March (pleasant weather)\n"
            response += "• Mode of transport: Flight (~2 hours) or Bus (~14 hours)\n"
            response += "• Avg cost: ₹3,000-8,000 (flight) or ₹1,500-2,500 (bus)\n\n"
        else:
            response = f"🧳 Travel Information:\n"
    elif 'hotel' in query_lower or 'stay' in query_lower or 'accommodation' in query_lower:
        response = "🏨 Accommodation Guide:\n"
        response += "• Luxury: 5-star hotels (₹5,000-15,000/night)\n"
        response += "• Comfort: 3-4 star hotels (₹2,000-5,000/night)\n"
        response += "• Budget: Hostels & guest houses (₹500-2,000/night)\n\n"
    elif 'restaurant' in query_lower or 'food' in query_lower or 'eat' in query_lower:
        response = "🍽️ Dining Guide:\n"
        response += "• Local cuisines: Seafood, Goan curries, coconut rice\n"
        response += "• Budget eateries: ₹100-300 per meal\n"
        response += "• Fine dining: ₹800-3,000 per person\n\n"
    elif 'attraction' in query_lower or 'visit' in query_lower or 'see' in query_lower:
        response = "🎭 Top Attractions:\n"
        if 'goa' in query_lower:
            response += "• Baga Beach, Colva Beach\n• Basilica of Bom Jesus\n• Fort Aguada\n• Dudhsagar Waterfalls\n\n"
        else:
            response += "• Historical monuments\n• Parks and gardens\n• Shopping districts\n• Local cultural sites\n\n"
    
    # Add dataset context if available
    if context and 'Q:' in context:
        response += "📚 Related Information:\n"
        lines = context.split('\n')
        for line in lines[:3]:
            if line.strip():
                response += f"• {line.strip()}\n"
        response += "\n"
    
    # Add practical tips
    response += "💡 Pro Tips:\n"
    response += "• Book tickets/hotels in advance\n"
    response += "• Carry valid ID and travel documents\n"
    response += "• Check weather before packing\n"
    response += "• Keep emergency contacts handy\n"
    
    return response.strip()

def get_ai_response(user_query, context):
    """
    Get AI response for travel queries.
    Currently uses smart travel guide generator as primary method.
    Ollama integration available but commented for better travel-focused responses.
    """
    # Use direct travel guide generator for consistent, relevant responses
    return build_travel_guide(user_query, context)
    
    # Ollama integration (commented - uncomment if using a travel-tuned model)
    # url = "http://localhost:11434/api/generate"
    # prompt = f"Context: {context}\nUser: {user_query}\nAssistant:"
    # try:
    #     r = requests.post(url, json={"model": "llama3", "prompt": prompt, "stream": False}, timeout=30)
    #     ...

def generate_voice(text):
    filename = f"{uuid.uuid4().hex[:8]}.mp3"
    path = os.path.join("static", filename)
    tts = gTTS(text=text[:200], lang='en') # Limit text length for speed
    tts.save(path)
    return filename
