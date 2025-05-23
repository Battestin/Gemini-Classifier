import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
CHOSEN_MODEL = "gemini-1.5-flash"  # Choose an available model

system_prompt = "You must classify the products provided by the user. "

llm = genai.GenerativeModel(
    model_name=CHOSEN_MODEL,  # Using the correct key
    system_instruction=system_prompt
)

question = "Bamboo toothbrush"

response = llm.generate_content(question)
print(f"The answer is: {response.text}")