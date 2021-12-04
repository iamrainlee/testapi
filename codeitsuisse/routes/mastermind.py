#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import json
import random

from flask import request, jsonify, Response

from codeitsuisse import app, mastermind_records

logger = logging.getLogger(__name__)

@app.route('/mastermind', methods=['POST'])
def mastermind():
    global mastermind_records
    try:
        data = request.get_json()
    except:
        return jsonify({'error':'Invalid JSON'})
    rdata = {}
    if(data.get('action') is None):
        rdata["error"] = "Missing action"
    elif(data["action"] == "init"):
        hash = str(random.getrandbits(128))
        rdata['possibles'] = [0,1,2,3,4,5,6,7,8,9]
        rdata['id'] = hash
        mastermind_records[hash] = {}
        mastermind_records[hash]['answer'] = str(random.randrange(0, 10000)).zfill(5)
        mastermind_records[hash]['count'] = 0
    elif(data["action"] == "check"):
        if(data.get("id") is None):
            rdata['error'] = 'Missing id'
        elif(data['id'] not in rdata.keys()):
            rdata['error'] = "Wrong id. Please init."
        else:
            if(data.get("answer") is None):
                rdata['error'] = 'Please provide your answer.'
            else:
                good = False
                try:
                    a = int(data['answer'])
                    if(0<=a<10000):
                        good= True
                except:
                    rdata['error'] = 'Invalid answer'
                if(good):
                    hash = data['id']
                    mastermind_records[hash]['count'] = mastermind_records[hash]['count'] + 1
                    ans_count = [0,0,0,0,0,0,0,0,0,0,0]
                    count = [0,0,0,0,0,0,0,0,0,0,0]
                    for i in mastermind_records[hash]['answer']:
                        ans_count[int(i)] += 1
                    for j in data['answer']:
                        count[int(j)] += 1
                    same = 0
                    for i in range(10):
                        same += min(count[i],ans_count[i])
                    position = 0
                    if(same > 0):
                        for i in range(4):
                            if (mastermind_records[hash]['answer'][i] == data['answer'][i]):
                                position += 1
                    if(position == 4):
                        rdata['success'] = True
                        rdata['same_pos'] = position
                        rdata['diff_pos'] = same - position
                        rdata['count'] = mastermind_records[hash]['count']
                    else:
                        rdata['success'] = False
                        rdata['same_pos'] = position
                        rdata['diff_pos'] = same - position
                else:
                    rdata['error'] = 'Invalid answer'
    else:
        rdata["error"] = "Wrong action"
    return jsonify(rdata)
