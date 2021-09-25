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
        r["p1"][i] = -1
    grid = []
    for i in data['grid']:
        grid.append(i[:])
    changed = True
    tick = 0
    while changed:
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
        if(changed):
            tick += 1
            for p1 in r["p1"]:
                ind = [int(i) for i in p1.split(',')]
                if(data['grid'][ind[0]][ind[1]] in [0,2,3]):
                    continue
                elif(r["p1"][p1] == -1):
                    if(grid[ind[0]][ind[1]] == 3):
                        r["p1"][p1] = tick
    uninfected = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] in [1,2]):
                uninfected = True
                break
    if(uninfected):
        r["p2"] = -1
    else:
        r["p2"] = tick
    r["p3"] = calculatep3(data['grid'])
    r["p4"] = 0
    return r

def calculatep3(g):
    grid = []
    for i in g:
        grid.append(i[:])
    changed = True
    tick = 0
    while changed:
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
                    try:
                        if(grid[i-1][j-1] == 1):
                            grid[i][j-1] = 3
                            changed = True
                    except:
                        a = 1
                    try:
                        if(grid[i+1][j-1] == 1):
                            grid[i][j-1] = 3
                            changed = True
                    except:
                        a = 1
                    try:
                        if(grid[i-1][j+1] == 1):
                            grid[i][j-1] = 3
                            changed = True
                    except:
                        a = 1
                    try:
                        if(grid[i+1][j+1] == 1):
                            grid[i][j-1] = 3
                            changed = True
                    except:
                        a = 1
        if(changed):
            tick += 1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] in [1,2]):
                return -1
    return tick
