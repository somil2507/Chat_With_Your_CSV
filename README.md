# 📊 Chat with Your CSV — Powered by Local LLMs (Ollama + Streamlit + PandasAI)

A Streamlit-based web application that allows you to interactively query your CSV files using a local large language model (LLM) via [Ollama](https://ollama.com/). It uses [PandasAI](https://github.com/gventuri/pandas-ai) for intelligent data understanding and query handling.

---

## 🚀 Features

- Upload and preview multiple CSV files
- Ask questions about your data in plain English
- Powered by local LLMs (no internet connection required)
- Supports lightweight models like `phi`, `llama2`, and more (via Ollama)

---

## 📦 Setup Instructions

### ✅ 1. Clone this Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### ✅ 2. **Create a Virtual Environment (Recommended)**
python -m venv venv
venv\Scripts\activate

✅ 3. Install Dependencies
pip install -r requirements.txt

🤖 4. Install and Setup Ollama
Ollama lets you run LLMs locally on your machine.

➤ Install Ollama
Visit https://ollama.com/download and install it for your OS.

🧠 5. Pull an LLM Model with Ollama
You can use lightweight models that run well on mid-range devices:

🔹 Option 1: Phi (small, fast, ~1.8 GB)
ollama pull phi
🔹 Option 2: TinyLlama
ollama pull tinyllama
🔹 Option 3: LLaMA2 7B (needs ~7.5 GB RAM)
ollama pull llama2:7b
🔹 Option 4: CodeLLaMA (for better code understanding)
ollama pull codellama:7b-python

▶️ 6. Run the Streamlit App
Make sure Ollama is running (ollama serve), then:
streamlit run app.py

 Usage
Upload one or more CSV files.

Choose a file to preview.

Type a natural language query like:

"What is the Invoice Number for Customer Code AFBIR004?"

"Provide me item description for customer: ABENE002"

Click "Chat with CSV" to get results powered by your local LLM.

❓ Troubleshooting
404 Model Not Found: Make sure you’ve pulled the model using ollama pull <model>.

Memory Error: Use a smaller model like phi or tinyllama if your RAM is < 8 GB.

No Code Found in Response: Some models may not return valid Python code. Try switching to codellama:7b-python or llama2:7b.

📚 Resources
Ollama Documentation

PandasAI GitHub

Streamlit Docs
