from pymongo import MongoClient
from gridfs import GridFS

# Connect to MongoDB Atlas
mongo_uri = 'mongodb+srv://sm4825:VDSIdNRsYU9v9EVr@cluster0.gvo92qb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(mongo_uri)
db = client.get_database('test-db')  
fs = GridFS(db)

# Open and read the PDF file
file_path = 'HW3.pdf'  # Path to your PDF file
with open(file_path, 'rb') as file:
    # Store the PDF file in MongoDB Atlas using GridFS
    file_id = fs.put(file, filename='example.pdf')

print(f"PDF file uploaded to MongoDB Atlas. File ID: {file_id}")
