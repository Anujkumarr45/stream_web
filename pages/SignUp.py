import streamlit as st
import pymongo
myclient=pymongo.MongoClient("mongodb+srv://lalu6365d_db_user:3REHd1eJzvesy46L@cluster0.kdswfix.mongodb.net/?appName=Cluster0")
mydb=myclient["Bitcoin"]
my=mydb["system"]
st.title(":blue[Sign Up]")
c1,c2=st.columns(2)
name=c1.text_input("Enter unique username")
password=c2.text_input("Enter password", type="password")
gender=c1.selectbox("Select gender",['Male','Female','Others'])
age=c2.number_input("Fill age",min_value=18, max_value=120, format="%d")
phone=st.text_input("Phone Number", placeholder="+91")
email=st.text_input("Email")
b1=st.button(":red[Create Account]")

def get_data():
    my.insert_one({"name":name, "password":password, "gender":gender, "age":str(age), "phone":str(phone), "email":email})
    st.success("You are Registered Successfully!!!!")
    

if b1:
    get_data()
    st.balloons()
    


