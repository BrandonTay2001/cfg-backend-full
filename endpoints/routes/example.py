import logging
import json

from flask import request, jsonify
from tinydb import TinyDB, Query

from endpoints import app

logger = logging.getLogger(__name__)


@app.route('/example', methods=['GET'])
def example():
    db = TinyDB('testCol.json')
    User = Query()
    db.insert({'test1': 'test1', 'test2': 5})
    return "OK"

@app.route('/exampleTwo', methods=['GET'])
def example2():
    db = TinyDB('testCol.json')
    User = Query()
    data = db.search(User.test1 == 'test1')
    foundData = data[0]
    print(foundData)
    output = {
        "number": foundData["test2"]
    }
    return jsonify(output)