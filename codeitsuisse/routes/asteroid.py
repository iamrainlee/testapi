import logging
import json
import copy

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/asteroid', methods=['POST'])
def asteroid():
    data = request.get_json()
    logging.info("Data: {}".format(data))
    result = []
    for i in data["test_cases"]:
        result.append(calasteroid(i))
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def calasteroid(str):
    dict = {}
    for i in set(str):
        dict[i] = 0
    for i in str:
        dict[i] += 1
    max_score = 0
    for i in dict:
        if(dict[i] >= 10):
            max_score += dict[i]*2
        elif(dict[i] >= 7):
            max_score += dict[i]*1.5
        else:
            max_score += dict[i]
    score = 0
    mid = len(str)//2 - 1
    touchedMin = False
    touchedMax = True
    x = 0
    maxx = mid
    max = calscore(str,mid)
    # while True:
    #     x+=1
    #     if(max == max_score):
    #         break
    #     if((mid-x)<0 and (mid+x)>= len(str)):
    #         break
    #     if((mid-x)>=0 and calscore(str,mid-x)>max):
    #         max = calscore(str,mid-x)
    #         maxx = mid-x
    #     if((mid+x)<len(str) and calscore(str,mid+x)>max):
    #         max = calscore(str,mid+x)
    #         maxx = mid+x
    r = {}
    r['input'] = str
    r['score'] = max
    r['origin'] = maxx
    return r

def calscore(str,n):
    if(len(str) == 0):
        return 0
    char = str[n]
    x,y = searchstr(str,char,n)
    logging.info(str[x:y])
    if(len(str[x:y]) >= 10):
        if(x!= 0 and y != len(str)):
            return calscore(str[:x]+str[y+1:],x-1) + 2*len(str[x:y])
        elif(x!= 0):
            return calscore(str[:x]+str[y:],x-1) + 2*len(str[x:y])
        elif(y != len(str)):
            return calscore(str[y+1:],x) + 2*len(str[x:y])
        else:
            return 2*len(str[x:y])
    elif(len(str[x:y]) >= 7):
        if(x!= 0 and y != len(str)):
            return calscore(str[:x]+str[y+1:],x-1) + 1.5*len(str[x:y])
        elif(x!= 0):
            return calscore(str[:x]+str[y:],x-1) + 1.5*len(str[x:y])
        elif(y != len(str)):
            return calscore(str[y+1:],x) + 1.5*len(str[x:y])
        else:
            return 1.5*len(str[x:y])
    else:
        if(x!= 0 and y != len(str)):
            return calscore(str[:x]+str[y+1:],x-1) + len(str[x:y])
        elif(x!= 0):
            return calscore(str[:x]+str[y:],x-1) + len(str[x:y])
        elif(y != len(str)):
            return calscore(str[y+1:],x) + len(str[x:y])
        else:
            return len(str[x:y])
def searchstr(str,char,n):
    x,y = n,n
    while True:
        xmargin = False
        ymargin = False
        x -= 1
        y += 1
        if(x<0 or str[x] != char):
            xmargin = True
            x += 1
        if(y>=len(str) or str[y] != char):
            ymargin = True
            y -= 1
        if(xmargin and ymargin):
            break
    return x,y+1
