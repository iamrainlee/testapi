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
    grid2 = []
    for i in data['grid']:
        grid2.append(i[:])
    changed = True
    tick = 0
    tick2 = 0
    while changed:
        changed1 = False
        changed2 = False
        oldgrid = []
        for i in grid:
            oldgrid.append(i[:])
        oldgrid2 = []
        for i in grid2:
            oldgrid2.append(i[:])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(oldgrid[i][j] == 3):
                    try:
                        if(grid[i+1][j] == 1):
                            grid[i+1][j] = 3
                            changed1 = True
                    except:
                        a = 1
                    try:
                        if(grid[i-1][j] == 1):
                            grid[i-1][j] = 3
                            changed1 = True
                    except:
                        a = 1
                    try:
                        if(grid[i][j+1] == 1):
                            grid[i][j+1] = 3
                            changed1 = True
                    except:
                        a = 1
                    try:
                        if(grid[i][j-1] == 1):
                            grid[i][j-1] = 3
                            changed1 = True
                    except:
                        a = 1
                if(oldgrid2[i][j] == 3):
                    try:
                        if(grid2[i+1][j] == 1):
                            grid2[i+1][j] = 3
                            changed2 = True
                    except:
                        a = 1
                    try:
                        if(grid2[i-1][j] == 1):
                            grid2[i-1][j] = 3
                            changed2 = True
                    except:
                        a = 1
                    try:
                        if(grid2[i][j+1] == 1):
                            grid2[i][j+1] = 3
                            changed2 = True
                    except:
                        a = 1
                    try:
                        if(grid2[i][j-1] == 1):
                            grid2[i][j-1] = 3
                            changed2 = True
                    except:
                        a = 1
                    try:
                        if(grid2[i-1][j-1] == 1):
                            grid2[i-1][j-1] = 3
                            changed2 = True
                    except:
                        a = 1
                    try:
                        if(grid2[i+1][j-1] == 1):
                            grid2[i+1][j-1] = 3
                            changed2 = True
                    except:
                        a = 1
                    try:
                        if(grid2[i-1][j+1] == 1):
                            grid2[i-1][j+1] = 3
                            changed2 = True
                    except:
                        a = 1
                    try:
                        if(grid2[i+1][j+1] == 1):
                            grid2[i+1][j+1] = 3
                            changed2 = True
                    except:
                        a = 1
        if(changed1):
            tick += 1
            for p1 in r["p1"]:
                ind = [int(i) for i in p1.split(',')]
                if(data['grid'][ind[0]][ind[1]] in [0,2,3]):
                    continue
                elif(r["p1"][p1] == -1):
                    if(grid[ind[0]][ind[1]] == 3):
                        r["p1"][p1] = tick
        if(changed2):
            tick2 += 1
        changed = changed1 or changed2
    uninfected1 = False
    uninfected2 = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] in [1,2]):
                uninfected = True
            if(grid2[i][j] in [1,2]):
                uninfected2 = True
        if(uninfected1 and uninfected2):
            break
    if(uninfected1):
        r["p2"] = -1
    else:
        r["p2"] = tick
    if(uninfected2):
        r["p3"] = -1
    else:
        r["p3"] = tick2
    r["p4"] = 0
    return r
