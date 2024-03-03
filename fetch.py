from flask import Flask, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

mongo_uri = 'mongodb+srv://sm4825:VDSIdNRsYU9v9EVr@cluster0.gvo92qb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = MongoClient(mongo_uri)
db = client.get_database('test-db')

@app.route('/api/data', methods=['GET'])
def get_all_data():
    collection = db['test-connection']
    data = list(collection.find({}))

    for item in data:
        item['_id'] = str(item['_id'])

    return jsonify(data)

@app.route('/api/data/<id>', methods=['GET'])
def get_data_by_id(id):
    try:
        object_id = ObjectId(id)
    except Exception as e:
        return jsonify({'error': 'Invalid ID'}), 400

    collection = db['test-connection']
    data = collection.find_one({'_id': object_id})

    if data:
        data['_id'] = str(data['_id'])
        return jsonify(data)
    else:
        return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

