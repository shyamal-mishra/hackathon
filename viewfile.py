from flask import Flask, send_file
from pymongo import MongoClient
from bson import ObjectId
from io import BytesIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
client = MongoClient("mongodb+srv://sm4825:VDSIdNRsYU9v9EVr@cluster0.gvo92qb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["test-db"]
collection = db["test-connection"]

@app.route('/pdf/<pdf_id>')
def view_pdf(pdf_id):
    # Retrieve the PDF data from MongoDB
    pdf_document = collection.find_one({"_id": ObjectId(pdf_id)})
    if pdf_document:
        pdf_data = pdf_document["pdf_data"]
        # Return the PDF file as response
        return send_file(BytesIO(pdf_data), mimetype='application/pdf')
    else:
        return "PDF not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
