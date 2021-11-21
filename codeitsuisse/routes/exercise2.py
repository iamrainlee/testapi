#!/usr/bin/python
# coding=utf-8
# -*- coding: utf-8 -*-
import logging
import json
import random

from flask import request, jsonify, Response

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/exercise2', methods=['GET'])
def exercise2():
    print()
    songs = []
    songs.append({"Title": "記憶棉","Artist": "MC Cheung Tinfu","Album": "記憶棉 - Single"})
    songs.append({"Title": "下一位前度","Artist": "Terence Lam","Album": "下一位前度 - Single"})
    songs.append({"Title": "青春快門 (樹窿版)","Artist": "Roberto Madan","Album": "青春快門 (樹窿版) - Single"})
    songs.append({"Title": "櫻花樹下","Artist": "Hins Cheung","Album": "P.S. I Love You"})
    songs.append({"Title": "時光倒流一句話","Artist": "Terence Lam","Album": "時光倒流一句話 - Single"})
    songs.append({"Title": "反對無效","Artist": "MC Cheung Tinfu","Album": "反對無效 - Single"})
    songs.append({"Title": "2084","Artist": "Dear Jane","Album": "2084 - Single"})
    songs.append({"Title": "只是太愛你","Artist": "Hins Cheung","Album": "The Brightest Darkness"})
    songs.append({"Title": "銀河修理員","Artist": "Dear Jane","Album": "銀河修理員 - Single"})
    rdata = {}
    rdata['result'] = []
    while len(songs) > 0:
        num = random.randint(0, len(songs)-1)
        rdata['result'].append(songs[num])
        del songs[num]
    http_response = make_response(json.dumps(rdata))
    http_response.headers['Content-type'] = 'application/json; charset=utf-8'
    return http_response
