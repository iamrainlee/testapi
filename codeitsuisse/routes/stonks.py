import logging
import json
import copy
import networkx as nx

from flask import request, jsonify
import random

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/stonks', methods=['POST'])
def stonks():
    data = request.get_json()
    logging.info("Data: {}".format(data))
    result = []
    for i in data:
        result.append(calstonks(i))
    logging.info("My result :{}".format(result))
    return json.dumps(result)
def calstonks(d):
    min = d['timeline']['2037']
    stocks = d['timeline']['2037'].keys()
    stockp = {}
    for i in stocks:
        stockp[i] = {}
        stockp[i]["min"] = d['timeline']['2037'][i]["price"]
        stockp[i]["min-year"] = 2037
        stockp[i]["max"] = d['timeline']['2037'][i]["price"]
        stockp[i]["max-year"] = 2037
    for i in range(1,len(d['timeline'].keys())):
        if(i>=d['energy']):
            break
        try:
            for j in d['timeline'][str(2037-i)]:
                if(d['timeline'][str(2037-i)][j]["price"]>stockp[j]["max"]):
                    stockp[j]["max"] = d['timeline'][str(2037-i)][j]["price"]
                    stockp[j]["max-year"] = 2037-i
                if(d['timeline'][str(2037-i)][j]["price"]<stockp[j]["min"]):
                    stockp[j]["min"] = d['timeline'][str(2037-i)][j]["price"]
                    stockp[j]["min-year"] = 2037-i
        except:
            a=1
    cur = 2037
    last = 2037
    output = []
    # while(cur in d['timeline']['2037'].keys()):
    #     if(last != 2037)
    #     hasTran = False
    #     for i in stockp:
    #         if(stockp[i]["min-year"] == cur):
    #             output.append("b-"+i+"-1000")
    #             hasTran = True
    #         elif(stockp[i]["max-year"] == cur):
    #             output.append("s-"+i+"-1000")
    #             hasTran = True
    #     if(not hasTran and cur != 2037):
    #         output.pop()
    maxp = 0
    s = None
    logging.info(stockp)
    for i in stockp:
        if(stockp[i]["max"]-stockp[i]["min"]>maxp):
            s = i
            maxp = stockp[i]["max"]-stockp[i]["min"]
    if(s != None):
        output.append("j-2037-"+str(stockp[s]["min-year"]))
        shares = d['capital']//stockp[i]["min"]
        output.append("b-"+s+'-'+str(shares))
        output.append("j-"+str(stockp[s]["min-year"])+'-'+str(stockp[s]["max-year"]))
        output.append("s-"+s+'-'+str(shares))
        if(stockp[s]["max-year"] != 2037):
            output.append("j-"+str(stockp[s]["max-year"])+'-2037')
    return output
