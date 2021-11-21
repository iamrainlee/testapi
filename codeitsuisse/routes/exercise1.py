#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import json

from flask import request, jsonify, Response

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/exercise1', methods=['POST'])
def exercise1():
    try:
        data = request.get_json()
    except:
        return jsonify({'error':'Invalid JSON'})
    rdata = {}
    if(data.get('number') is None):
        rdata["error"] = "Missing parameters"
    else:
        try:
            number = int(data['number'])
            rdata['result'] = number**2 -1
        except:
            rdata['error'] = "Invalid parameter"
    return jsonify(rdata)
