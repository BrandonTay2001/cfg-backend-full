import logging
import json

from flask import request, jsonify
from tinydb import TinyDB, Query

from endpoints import app

logger = logging.getLogger(__name__)

@app.route('/getCompanyInfo', methods=['GET'])
def example2():
    args = request.args
    companyId = args.get('companyId')
    db = TinyDB('companyInfo.json')
    User = Query()
    data = db.search(User._id == companyId)
    companyInfo = data[0]
    print(companyInfo)
    output = {
        "status": 200,
        "data": companyInfo
    }
    return jsonify(output)