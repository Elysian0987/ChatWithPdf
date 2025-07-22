# ChatWithPdf

ChatWithPdf is a Streamlit app that lets you ask questions about PDF content using natural language. It uses `sentence-transformers` for semantic search.

## Setup

1. Clone the repo:
```bash
   git clone https://github.com/Elysian0987/ChatWithPdf.git
   cd ChatWithPdf/askmypdf
```

2. Activate your virtual environment:
   ```bash
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install sentence-transformers streamlit
   ```

## Run the App

```bash
streamlit run app.py
```

## Requirements

* Python 3.8+
* sentence-transformers
* streamlit
* PyPDF2 or similar for PDF parsing
