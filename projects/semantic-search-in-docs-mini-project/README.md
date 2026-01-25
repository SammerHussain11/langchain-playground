# Semantic Question Answering with Local Embeddings and Groq LLM

This project demonstrates a **semantic question-answering system** using **local embeddings** for similarity search and the **Groq LLM** for generating answers. It combines **SentenceTransformers** for embedding text, **cosine similarity** for retrieving relevant context, and the **ChatGroq API** to produce high-quality answers.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [License](#license)

---

## Features

- Convert documents and queries into **semantic embeddings**.
- Find the **most relevant document** for a given question using **cosine similarity**.
- Use **Groq LLM** (`llama3-8b-8192`) to generate natural language answers.
- CPU-friendly embedding model (`all-MiniLM-L6-v2`) for fast local processing.
- Easy-to-extend for multiple documents or dynamic queries.

---

## Installation

### Prerequisites

- Python **3.10+**
- [pip](https://pip.pypa.io/en/stable/)

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/semantic-qa-groq.git
cd semantic-qa-groq
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Install required packages**

```bash
pip install -r requirements.txt
```

**`requirements.txt` example:**

```
langchain_groq
sentence-transformers
scikit-learn
numpy
python-dotenv
```

4. **Set up environment variables**

Create a `.env` file in the root directory:

```
# .env
GROQ_API_KEY=your_groq_api_key_here
```

Load environment variables in the code:

```python
from dotenv import load_dotenv
load_dotenv()
```

---

## Usage

1. Add your documents and query in the script:

```python
documents = [
    "Quaid-e-Azam Muhammad Ali Jinnah was the founder of Pakistan.",
    "He was born on 25 December 1876 in Karachi.",
    "He studied law at Lincoln’s Inn in London.",
    "He became the first Governor-General of Pakistan.",
    "He believed in unity, faith, and discipline."
]

query = "Who is Quaid-e-Azam Muhammad Ali Jinnah?"
```

2. Run the script:

```bash
python main.py
```

3. Sample output:

```
Most relevant document:
Quaid-e-Azam Muhammad Ali Jinnah was the founder of Pakistan.

Answer:
Quaid-e-Azam Muhammad Ali Jinnah was the founder of Pakistan and the country's first Governor-General.
```

---

## How It Works

1. **Embeddings Creation**

   The script uses the `SentenceTransformer` model `all-MiniLM-L6-v2` to convert all documents and the query into numerical embeddings.

2. **Similarity Search**

   Using **cosine similarity**, it finds the document that best matches the semantic meaning of the query.

3. **Contextual Question Answering**

   The most relevant document is passed as context to the **Groq LLM** (`llama3-8b-8192`) to generate a natural language answer.

---

## Project Structure

```
semantic-qa-groq/
│
├── main.py             # Main script for embeddings, similarity, and LLM response
├── requirements.txt    # Python dependencies
├── .env                # API keys and environment variables
└── README.md           # Project documentation
```

---

## Dependencies

- **langchain_groq** – Interface for Groq LLM.
- **sentence-transformers** – Generate embeddings for semantic search.
- **scikit-learn** – Compute cosine similarity.
- **numpy** – Numerical operations on embeddings.
- **python-dotenv** – Load API keys and settings from `.env`.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## Optional Enhancements

- Expand to multiple documents with top-k similarity.
- Add a web interface using **Streamlit** or **Gradio**.
- Cache embeddings for faster repeated queries.
- Support multi-language documents using multilingual embedding models.
