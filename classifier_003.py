import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)


def product_categorizer(product_name, possible_categories_list):
    llm = genai.GenerativeModel(
        model_name="gemini-1.5-flash",  # Using the correct key
        system_instruction=f"""
        You are a product categorizer.
        You must use the categories present in the list below:

        # List of valid categories:
        {possible_categories_list.split(", ")}

        # Output format:
        Product: <product name>
        Category: <present the product category>

        # Example output:
        Product: Solar rechargeable electric toothbrush
        Category: Green electronics
        """

    )

    response = llm.generate_content(product_name)
    return response.text

def main():

    possible_categories_list = "Green electronics, Sustainable fashion, Eco-friendly cleaning products, Organic foods"   
    
    question = "Bamboo toothbrush"

    print(f"\nThe answer is: {product_categorizer(question, possible_categories_list)}")

if __name__ == "__main__":
    main()