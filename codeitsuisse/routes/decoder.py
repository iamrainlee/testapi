import logging
import json
import copy
import random
from itertools import permutations

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/decoder', methods=['POST'])
def decoder():
    data = request.get_json()
    logging.info("Data: {}".format(data))
    possible = data["possible_values"]
    num = data["num_slots"]
    realpossible = []
    for i in data["history"]:
        rpos, wpos = decodergetresult(i["result"])
        if(rpos+wpos == num):
            realpossible = i["output_received"]
    if(realpossible == [])
        realpossible = possible[:]
    # perm = permutations(realpossible,num)
    r = []
    for i in range(num):
        n = random.randint(0,len(realpossible-1))
        r.append(realpossible[n])
        del realpossible[n]
    result = {}
    result["answer"] = r
    # for i in list(perm):
    #     d =list(i)
    #     correct = True
    #     for j in data["history"]:
    #         if(decodercheckresult(d,j["output_received"]) != decodergetresult(j["result"])):
    #             correct = False
    #             break
    #     if(correct):
    #         result["answer"] = d
    #         break
    logging.info("My result :{}".format(result))
    return json.dumps(result)
def decodergetresult(x):
    if(x < 10):
        return x,0
    else:
        return x%10,x//10
def decodercheckresult(l1,l2):
    correct = 0
    for i in set(l2):
        correct += min(l2.count(i),l1.count(i))
    corpos = 0
    for i in range(len(l2)):
        if(l1[i] == l2[i]):
            corpos += 1
    return corpos,correct-corpos
