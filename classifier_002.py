import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

llm = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # Using the correct key
    system_instruction="""
    You are a product categorizer.
    You must use the categories present in the list below:

    # List of valid categories:
    Green electronics
    Sustainable fashion
    Eco-friendly cleaning products
    Organic foods

    # Output format:
    Product: <product name>
    Category: <present the product category>

    # Example output:
    Product: Solar rechargeable electric toothbrush
    Category: Green electronics
    """

)

question = "Bamboo toothbrush"

response = llm.generate_content(question)
print(f"\nThe answer is: {response.text}")