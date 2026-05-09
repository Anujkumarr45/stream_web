import streamlit as st
import pymongo
myclient=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb=myclient["Bitcoin"]
my=mydb["system"]
st.title(":blue[Sign In]")
name=st.text_input("Enter username")
password=st.text_input("Enter password", type="password")


if st.button(":red[sign in]"):

    
    str1=my.find({"name":name, "password":password})
    valid=0
    for data in str1:
        st.success(f"Welcome:{data['name']}")
        valid=valid+1
        st.session_state['name']=data['name']
        st.switch_page("pages\Profile.py")

    if valid==0:
        st.error("Invalid Login!!!")
    

