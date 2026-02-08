# Research Paper Summarizer 📄🤖

**Research Paper Summarizer** is a Streamlit-based GenAI application that generates structured summaries of famous AI research papers based on user-selected **explanation style** and **length**. The goal of this project is to demonstrate **prompt conditioning**, **parameterized prompts**, and **LangChain + LLM chaining** rather than simple text summarization.

This project is ideal for students, researchers, and developers who want quick, tailored explanations of landmark AI papers.

---

## 🚀 Features

* 📚 Predefined list of **influential AI research papers**
* 🎯 Customizable **explanation style**:

  * Beginner-Friendly
  * Technical
  * Code-Oriented
  * Mathematical
* 📏 Adjustable **summary length** (short, medium, long)
* 🧠 Uses **LangChain Prompt Templates** for controlled generation
* ⚡ Powered by **Groq LLM (ChatGroq)** for fast inference
* 🖥️ Clean and simple **Streamlit UI**

---

## 🎯 Why This Project Matters

Most summarization apps blindly shorten text.

This project shows how **the same content can be reframed** depending on:

* audience expertise
* explanation depth
* communication goal

That ability is core to **prompt engineering and GenAI product design**, which is why this project goes beyond a basic summarizer.

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Streamlit** – Frontend UI
* **LangChain** – Prompt loading and chaining
* **Groq LLM (ChatGroq)** – Large Language Model
* **python-dotenv** – Environment variable management

---

## 📂 Project Structure

```
Research-Paper-Summarizer/
│── app.py
│── system_prompt.json
│── .env
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/research-paper-summarizer.git
cd research-paper-summarizer
```

### 2️⃣ Create and activate a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set environment variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser.

---

## 🧪 Example Usage

**Input selections:**

* Paper: *Attention Is All You Need*
* Style: *Beginner-Friendly*
* Length: *Medium (3–5 paragraphs)*

**Output:**
A clear, structured explanation of the paper tailored to the selected audience and depth.

---

## 🧠 Learning Outcomes

By building this project, you gain hands-on experience with:

* Prompt conditioning using structured inputs
* Dynamic prompt variables (`paper_input`, `style_input`, `length_input`)
* LangChain prompt loading via JSON
* Chain composition (`prompt | model`)
* Designing GenAI tools with user-controlled behavior

---

## 🔮 Future Improvements

* Add PDF upload for custom research papers
* Include citation-style summaries
* Compare multiple papers side-by-side
* Add diagram or equation generation mode
* Support export to Markdown or PDF

---

## 📖 References & Reputable Sources

* LangChain Prompt Templates (Official):
  [https://python.langchain.com/docs/concepts/prompt_templates/](https://python.langchain.com/docs/concepts/prompt_templates/)

* LangChain Chains Concept:
  [https://python.langchain.com/docs/concepts/chains/](https://python.langchain.com/docs/concepts/chains/)

* OpenAI Prompt Engineering Guide:
  [https://platform.openai.com/docs/guides/prompt-engineering](https://platform.openai.com/docs/guides/prompt-engineering)

* Streamlit Documentation:
  [https://docs.streamlit.io/](https://docs.streamlit.io/)

---

## 🧠 Author Notes

This project is intentionally **prompt-driven**, not data-driven. It reflects how modern GenAI systems adapt outputs based on user intent rather than static logic.

If you understand this project, you understand **controlled text generation and prompt engineering fundamentals**.

---

⭐ If you find this project useful, consider starring the repository.

