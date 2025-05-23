# Gemini Classifier

AI-powered product classifier using Google’s Gemini 1.5 Flash.  
Given a product name, it returns the most suitable sustainable category from a predefined list.

## 🚀 How to Run

1. Clone the repo  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API key:  
   ```
   GEMINI_API_KEY=your_google_api_key_here
   ```

4. Run the script:  
   ```bash
   python gemini_classifier.py
   ```

## 🧠 Example

```
Input: Solar rechargeable electric toothbrush

Output:  
  Product: Solar rechargeable electric toothbrush  
  Category: Green electronics
```

## 🛠️ Customization

Edit `possible_categories_list` in `main()` to use your own category set.

## ⚠️ Note

This is a prototype using LLMs. Always validate the output before using it in real applications.
