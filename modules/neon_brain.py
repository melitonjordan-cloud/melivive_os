import os
from groq import Groq

def get_neon_response(user_prompt):
    """
    Connects to Groq (Free Tier) to process business logic.
    """
    api_key = os.environ.get("GROQ_API_KEY")
    
    if not api_key:
        return "⚠️ SYSTEM ALERT: API Key Missing. Please enter it in the Sidebar."

    try:
        client = Groq(api_key=api_key)
        
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "ACT AS NEON OLYMPUS (The Central Command). You are an advanced AI business operator."
                },
                {
                    "role": "user",
                    "content": user_prompt,
                }
            ],
            model="llama3-8b-8192",
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ CONNECTION ERROR: {str(e)}"