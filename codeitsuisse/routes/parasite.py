import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/parasite', methods=['POST'])
def parasite():
    data = request.get_json()
    result = []
    for i in data:
        result.append(calparasite(i))
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def calparasite(data):
    r = {}
    r["room"] = data["room"]
    r["p1"] = {}
    for i in data['interestedIndividuals']:
        r["p1"][i] = calparasitep1(i,data["grid"])
    r["p2"] = 1
    r["p3"] = 1
    r["p4"] = 0
    return r
def calparasitep1(ind, g):
    grid = []
    for i in g:
        grid.append(i[:])
    changed = True
    ind = [int(i) for i in ind.split(',')]
    tick = 0
    if(grid[ind[0]][ind[1]] in [0,2,3]):
        return -1
    while changed:
        tick += 1
        changed = False
        oldgrid = []
        for i in grid:
            oldgrid.append(i[:])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(oldgrid[i][j] == 3):
                    try:
                        if(grid[i+1][j] == 1):
                            grid[i+1][j] = 3
                            changed = True
                    except:
                        a = 1
                    try:
                        if(grid[i-1][j] == 1):
                            grid[i-1][j] = 3
                            changed = True
                    except:
                        a = 1
                    try:
                        if(grid[i][j+1] == 1):
                            grid[i][j+1] = 3
                            changed = True
                    except:
                        a = 1
                    try:
                        if(grid[i][j-1] == 1):
                            grid[i][j-1] = 3
                            changed = True
                    except:
                        a = 1
        if(grid[ind[0]][ind[1]] == 3):
            return tick
    return -1
