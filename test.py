from pymongo import MongoClient
import urllib.parse
# Yahan apna real password daalo jo MongoDB Atlas me banaya tha
# < > ye brackets hata dena
username = "Anujkumarr45"
password = "75lTY2QWHmIYe9AO" 

uri = f"mongodb+srv://Anujkumarr45:75lTY2QWHmIYe9AO@cluster0.smb4mln.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)

# Connection test
try:
    client.admin.command('ping')
    print("✅ Connected! MongoDB chalu ho gaya")
except Exception as e:
    print("❌ Error:", e)