from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()

# ------------------ SYSTEM PROMPT ------------------
system_prompt = """
You are an expert Prompt Engineering analyst and GenAI consultant.

Your task is to critically evaluate user-written prompts intended for large language models.

You must:
1. Analyze the prompt for clarity, context, specificity, role definition, constraints, and output format.
2. Identify weaknesses, ambiguities, or missing information.
3. Assign a quality score out of 10 based on prompt effectiveness.
4. Provide clear, actionable feedback in bullet points.
5. Rewrite the prompt into an improved, high-quality version.
6. Optionally suggest an alternative improved version.

Rules:
- Do NOT answer the original prompt.
- Focus only on improving the prompt.
- Be critical and direct.
- Output must be structured.
"""

prompt = PromptTemplate(
    input_variables=["user_prompt"],
    template=system_prompt + "\n\nUser Prompt:\n{user_prompt}"
)

# ------------------ MODEL ------------------
model = ChatGroq(
    model="groq/compound-mini",
    temperature=1.2
)

chain = prompt | model

# ------------------ STREAMLIT UI ------------------
st.set_page_config(page_title="PromptLens", layout="centered")
st.header("🔍 PromptLens")
st.write("Analyze and improve your AI prompts professionally.")

user_prompt = st.text_area(
    "Paste your prompt here:",
    height=200,
    placeholder="e.g. Explain AI"
)

if st.button("Analyze Prompt"):
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Analyzing prompt..."):
            result = chain.invoke({"user_prompt": user_prompt})
            st.success("Analysis Complete")
            st.write(result.content)
