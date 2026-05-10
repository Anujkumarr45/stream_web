import streamlit as st
import time
import pymongo
myclient=pymongo.MongoClient("mongodb+srv://anujkumarr45:75lTY2QWHmIYe9AO@cluster0.ukwltkn.mongodb.net/?appName=Cluster0")
mydb=myclient["Bitcoin"]
my=mydb["system"]
st.title(":blue[Change Password]")
t1=st.text_input("Old Password", type="password")
t2=st.text_input("New Password", type="password")
if st.button("Change Pass"):
    res=my.update_one({"password":t1},{"$set":{"password":t2}})
    st.success("Password changed Successfully!!!")
    #st.success(f"value:{res}")
