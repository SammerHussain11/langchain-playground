# PromptLens 🔍

**PromptLens** is a Streamlit-based GenAI tool that analyzes, scores, and improves user-written prompts for Large Language Models (LLMs). Instead of answering prompts, PromptLens critiques them — identifying weaknesses, ambiguity, and missing context — and then rewrites them into high-quality, professional prompts.

This project is designed to demonstrate **prompt engineering**, **meta-prompting**, and **LangChain chaining concepts**, making it ideal for learning and for showcasing GenAI skills on a resume.

---

## 🚀 Features

- 📊 **Prompt Quality Scoring (0–10)** based on clarity, context, and constraints
- 🔍 **Detailed prompt analysis** (issues & gaps)
- ✨ **Professionally rewritten prompt** for better LLM output
- 🔁 Optional alternative improved prompt
- 🧠 Uses **LangChain PromptTemplate + Chains**
- 🖥️ Clean, minimal **Streamlit UI**

---

## 🎯 Why PromptLens?

Most beginners build basic Q&A chatbots, which adds little real-world value.

PromptLens focuses on **how prompts are written**, not just how models respond. This reflects real industry usage where prompt quality directly impacts AI performance.

PromptLens demonstrates:

- GenAI thinking
- Prompt engineering best practices
- Tool-building mindset (not just chatbot cloning)

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** – UI layer
- **LangChain** – Prompt templating & chaining
- **Groq LLM (ChatGroq)** – Fast inference
- **python-dotenv** – Environment variable management

---

## 📂 Project Structure

```
PromptLens/
│── app.py
│── .env
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/PromptLens.git
cd PromptLens
```

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser.

---

## 🧪 Example Bad Prompt (Test Case)

```
Explain AI and machine learning in detail and make it good.
```

PromptLens will:

- Score it low
- Identify missing audience, constraints, and clarity
- Rewrite it into a professional, high-quality prompt

---

## 📚 Learning Outcomes

By building PromptLens, you learn:

- Prompt engineering principles
- Meta-prompting (analyzing prompts using AI)
- LangChain PromptTemplate usage
- Chain composition (`prompt | model`)
- Streamlit UI best practices

---

## 🔮 Future Improvements

- Prompt history & version comparison
- Side-by-side original vs improved prompt view
- Domain-specific prompt modes (resume, research, JD)
- Agent-based prompt evaluator

---

## 📖 References & Sources

- LangChain Prompt Templates (Official):
  [https://python.langchain.com/docs/concepts/prompt_templates/](https://python.langchain.com/docs/concepts/prompt_templates/)

- LangChain Chains Concept:
  [https://python.langchain.com/docs/concepts/chains/](https://python.langchain.com/docs/concepts/chains/)

- OpenAI Prompt Engineering Guide:
  [https://platform.openai.com/docs/guides/prompt-engineering](https://platform.openai.com/docs/guides/prompt-engineering)

- Streamlit Documentation:
  [https://docs.streamlit.io/](https://docs.streamlit.io/)

---

## 🧠 Author Notes

PromptLens is intentionally built as a **tool**, not a chatbot. It reflects how GenAI is used in production — improving inputs to maximize model performance.

If you understand PromptLens, you understand **prompt engineering fundamentals**.

---

⭐ If you find this project useful, consider starring the repository.
