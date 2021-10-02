#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import json

from flask import request, jsonify, Response

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/testpost', methods=['POST'])
def testpost():
    try:
        data = request.get_json()
    except:
        return jsonify({'error':'Invalid JSON'})
    rdata = {}
    if(data.get('action') is None):
        rdata["error"] = "Missing action"
    elif(data["action"] == "get_Ms_HKU"):
        rdata = json.loads('{"id":2,"Name":"Nicole","Program":"BASc(FinTech)","Local":"TRUE","Position":1}')
    elif(data["action"] == "get_Ms_HKU_participants"):
        if(data.get("id") is None):
            rdata = json.loads('[{"id":1,"Name":"Merry","Program":"BBA","Local":"TRUE","Position":2,"Beautiful Index":86},{"id":2,"Name":"Nicole","Program":"BASc(FinTech)","Local":"TRUE","Position":1,"Beautiful Index":1000},{"id":3,"Name":"Cherry","Program":"BBA","Local":"False","Position":4,"Beautiful Index":75},{"id":4,"Name":"Katie","Program":"BEng","Local":"TRUE","Position":3,"Beautiful Index":80},{"id":5,"Name":"Susan","Program":"BA","Local":"TRUE","Position":5,"Beautiful Index":73}]')
        else:
            temp = json.loads('[{"id":1,"Name":"Merry","Program":"BBA","Local":"TRUE","Position":2,"Beautiful Index":86},{"id":2,"Name":"Nicole","Program":"BASc(FinTech)","Local":"TRUE","Position":1,"Beautiful Index":1000},{"id":3,"Name":"Cherry","Program":"BBA","Local":"False","Position":4,"Beautiful Index":75},{"id":4,"Name":"Katie","Program":"BEng","Local":"TRUE","Position":3,"Beautiful Index":80},{"id":5,"Name":"Susan","Program":"BA","Local":"TRUE","Position":5,"Beautiful Index":73}]')
            found = False
            for i in temp:
                if(i["id"] == data.get("id")):
                    rdata = i
                    found = True
            if(not found):
                rdata["error"] = "Participant not found"
    else:
        rdata["error"] = "Wrong action"
    return jsonify(rdata)
