from langchain_groq import ChatGroq 
from dotenv import load_dotenv
import streamlit as st 
from langchain_core.prompts import load_prompt

# load environment variables 
load_dotenv()

# load system prompt 
system_prompt = load_prompt('system_prompt.json')

# model configurations
model = ChatGroq(
  model="groq/compound-mini", 
  max_tokens=200, 
  temperature=1.5
)

# streamlit UI 
st.header("Research Paper Summarizer")

paper_input=st.selectbox("Select Research Paper Name",["Attenttion Is All You Need ","BERT: Pre-training of Deep Bidirection Transformers ","GPT-3: Language Models are Few-Shot Learners","Diffusion Models Beat GANs on Image Synthesis"])

style_input=st.selectbox("Select Expanation Style",["Beginner-Friendly","Technical","Code-Oriented","Mathematical"])

length_input=st.selectbox("Select Explanation Length",["Short(1-2 paragraphs)","Medium (3-5 paragraphs)","Long (detailed explanation)"])

# create button 
if st.button("Summarize"): 
  # Creating chain so that we avoid calling invoke multiple times
  chain = system_prompt | model

  result = chain.invoke(
    # fill the placeholders
    {  
      'paper_input':paper_input,
      'style_input': style_input,
      'length_input': length_input
    }
  )
  st.write(result.content)



