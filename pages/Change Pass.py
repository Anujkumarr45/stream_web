import streamlit as st
import time
import pymongo
myclient=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb=myclient["Bitcoin"]
my=mydb["system"]
st.title(":blue[Change Password]")
t1=st.text_input("Old Password", type="password")
t2=st.text_input("New Password", type="password")
if st.button("Change Pass"):
    res=my.update_one({"password":t1},{"$set":{"password":t2}})
    st.success("Password changed Successfully!!!")
    #st.success(f"value:{res}")
