import streamlit as st
import os
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

import google.generativeai as genai
import PyPDF2 as pdf

genai.configure(api_key="AIzaSyD0Y-aGZ_BvwyqTzQQnlQNtLafLQC3WUhE")
def get_gemini_response(input):
  model=genai.GenerativeModel('gemini-1.5-pro')
  response=model.generate_content(input)
  return response.text

def input_pdf_text(uploaded_file):
  reader = pdf.PdfReader(uploaded_file)
  text = ""
  for page in reader.pages: #Chck this loop once on failure
    text += str(page.extract_text())
  return text

input_prompt="Act like a skilled and experienced Appication tracking system with a deep understanding in tech field,software engineering,data science,data analyst and big data engineering. your task is to evaluate the resume based on the given job description.you must consider the job market to be competitive and you should provide best assistance for improving the resume. assign the percentage match based on Jd and the missing keywords with high accuracy resume:{text} desciption:{jd} I want the response in one single string having the structure {{JD Match:%,MissingKeywords:[],Profile Summary:}}"

st.title("Resume Screening Tool")
st.text("Improve your resume")
jd=st.text_area("Paste the Job Description:")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="please upload the pdf")
submit=st.button("Submit")

if submit:
  if uploaded_file is not None:
    text=input_pdf_text(uploaded_file)
    input=input_prompt.format(text=text,jd=jd)
    response=get_gemini_response(input)
    st.subheader("Response")
    #st.write(response)
  else:
    st.warning("Please upload a PDF file.")
