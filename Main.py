import streamlit as st
import pymongo
myclient=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb=myclient["Bitcoin"]
my=mydb["system"]
import time
with st.spinner("Loading..."):
    time.sleep(1)

st.title(":violet[An AI-powered CV Analysis]")
st.markdown("Artificial Intelligence (AI) powered CV Analysis is a modern approach to evaluating resumes using machine learning and natural language processing techniques. Instead of manually scanning through CVs, AI systems can automatically extract key information such as skills, education, work experience, and achievements. By applying algorithms, the system can match candidates’ profiles with job requirements, highlight strengths, and even detect gaps or inconsistencies.")
st.markdown("Essentially, AI-powered CV Analysis transforms traditional recruitment by making it faster, smarter, and data-driven, helping organizations identify the best candidates efficiently.")

st.snow()
