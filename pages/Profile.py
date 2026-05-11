import streamlit as st
import time
with st.spinner("Loading..."):
    time.sleep(1)
import pymongo
myclient=pymongo.MongoClient("mongodb+srv://lalu6365d_db_user:3REHd1eJzvesy46L@cluster0.kdswfix.mongodb.net/?appName=Cluster0")
mydb=myclient["Bitcoin"]
my=mydb["system"]
c1,c2,c3,c4=st.columns(4)
#st.error("please signin first to view your profile")
if 'name' not in st.session_state:
    st.session_state['name']=""

if 'password' not in st.session_state:
    st.session_state['password']=""

    
name=st.session_state.get('name')
password=st.session_state.get('password')
st.success(f"Welcome : {name}")

if c1.button("See Profile"):
   str1=st.session_state['name']
   res=my.find({"name":str1})
   for data in res:
       st.success(f"Name: {data['name']}")
       st.success(f"Password : {data['password']}")
       st.success(f"Gender : {data['gender']}")
       st.success(f"Age : {data['age']}")
       st.success(f"Phone : {data['phone']}")
       st.success(f"E-mail : {data['email']}")

if c2.button("Change Pass"):
    st.switch_page("pages/Change Pass.py")

if c3.button("CV Analysis"):
    st.switch_page("pages/CV_analyzer.py")
if c4.button(":red[Logout]"):
    st.success("Logout Successfully")
    
    st.switch_page("pages/SignIn.py")
    st.rerun()
