import logging
import json
import copy

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/parasite', methods=['POST'])
def parasite():
    data = request.get_json()
    logging.info("Data: {}".format(data))
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
        grid.append(i.copy())
    grid2 = []
    for i in data['grid']:
        grid2.append(i.copy())
    changed = True
    tick = 0
    tick2 = 0
    while changed:
        changed1 = False
        changed2 = False
        oldgrid = copy.deepcopy(grid)
        # for i in grid:
        #     oldgrid.append(i.copy())
        oldgrid2 = copy.deepcopy(grid2)
        # for i in grid2:
        #     oldgrid2.append(i.copy())
        # oldgrid[0][0] = 4
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
                        if(grid[i][j+1] == 1):
                            grid[i][j+1] = 3
                            changed1 = True
                    except:
                        a = 1
                    try:
                        if(grid[i-1][j] == 1 and (i-1) >= 0):
                            grid[i-1][j] = 3
                            changed1 = True
                    except:
                        a = 1
                    try:
                        if(grid[i][j-1] == 1 and (j-1) >= 0):
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
                        if(grid2[i][j+1] == 1):
                            grid2[i][j+1] = 3
                            changed2 = True
                    except:
                        a = 1
                    if((i-1) >= 0):
                        if(grid2[i-1][j] == 1):
                            grid2[i-1][j] = 3
                            changed2 = True
                        try:
                            if(grid2[i-1][j+1] == 1):
                                grid2[i-1][j+1] = 3
                                changed2 = True
                        except:
                            a = 1
                    if((j-1) >= 0):
                        if(grid2[i][j-1] == 1):
                            grid2[i][j-1] = 3
                            changed2 = True
                        try:
                            if(grid2[i+1][j-1] == 1):
                                grid2[i+1][j-1] = 3
                                changed2 = True
                        except:
                            a = 1
                        if((i-1) >= 0):
                            if(grid2[i-1][j-1] == 1):
                                grid2[i-1][j-1] = 3
                                changed2 = True
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
                if(data['grid'][ind[0]][ind[1]] != 1):
                    continue
                elif(r["p1"][p1] == -1):
                    if(grid[ind[0]][ind[1]] == 3):
                        r["p1"][p1] = tick
        if(changed2):
            tick2 += 1
        logging.info("grid2: {}".format(grid2))
        changed = changed1 or changed2
    uninfected1 = False
    uninfected2 = False
    energy = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == 1):
                uninfected1 = True
            if(grid2[i][j] == 1):
                uninfected2 = True
        if(uninfected1 and uninfected2):
            break
    if(not uninfected1):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == 1):
                    tenergy = 100
                    success = False
                    for k in range(1,len(grid)):
                        if(tenergy<=k):
                            break
                        try:
                            if(grid[i+k+1][j] == 3):
                                tenergy = min(k,tenergy)
                                success = True
                        except:
                            a = 1
                        try:
                            if(grid[i-k-1][j] == 3 and (i-k-1) >= 0):
                                tenergy = min(k,tenergy)
                                success = True
                        except:
                            a = 1
                        try:
                            if(grid[i][j+k+1] == 3):
                                tenergy = min(k,tenergy)
                                success = True
                        except:
                            a = 1
                        try:
                            if(grid[i][j-k-1] == 3 and (j-k-1) >= 0):
                                tenergy = min(k,tenergy)
                                success = True
                        except:
                            a = 1

                        try:
                            if(grid[i+k][j+k] == 3):
                                tenergy = min(k+k,tenergy)
                                success = True
                        except:
                            a = 1
                        try:
                            if(grid[i+k][j-k] == 3 and (j-k) >= 0):
                                tenergy = min(k+k,tenergy)
                                success = True
                        except:
                            a = 1
                        if((i-k)>=0):
                            if(grid[i-k][j-k] == 3 and (j-k) >= 0):
                                tenergy = min(k+k,tenergy)
                                success = True
                            try:
                                if(grid[i-k][j+k] == 3 and (i-k) >= 0):
                                    tenergy = min(k+k,tenergy)
                                    success = True
                            except:
                                a = 1
                        for l in range(1,k):
                            try:
                                if(grid[i+k][j+l] == 3):
                                    tenergy = min(k+l,tenergy)
                                    success = True
                            except:
                                a = 1
                            if(j-l)>=0:
                                try:
                                    if(grid[i+k][j-l] == 3):
                                        tenergy = min(k+l,tenergy)
                                        success = True
                                except:
                                    a = 1
                                if(grid[i-k][j-l] == 3 and (i-k) >= 0):
                                    tenergy = min(k+l,tenergy)
                                    success = True
                            try:
                                if(grid[i-k][j+l] == 3 and (i-k) >= 0):
                                    tenergy = min(k+l,tenergy)
                                    success = True
                            except:
                                a = 1
                            if(i-l) >= 0:
                                if(grid[i-l][j-k] == 3 and (j-k) >= 0):
                                    tenergy = min(k+l,tenergy)
                                    success = True
                                try:
                                    if(grid[i-l][j+k] == 3):
                                        tenergy = min(k+l,tenergy)
                                        success = True
                                except:
                                    a = 1
                            try:
                                if(grid[i+l][j-k] == 3 and (j-k) >= 0):
                                    tenergy = min(k+l,tenergy)
                                    success = True
                            except:
                                a = 1
                            try:
                                if(grid[i+l][j+k] == 3):
                                    tenergy = min(k+l,tenergy)
                                    success = True
                            except:
                                a = 1
                    if(success):
                        energy += tenergy
                        grid[i][j] = 3
                        changedGraph(grid,i,j)
                        break

    if(uninfected1):
        r["p2"] = -1
    else:
        r["p2"] = tick
    if(uninfected2):
        r["p3"] = -1
    else:
        r["p3"] = tick2
    r["p4"] = -20
    return r

def changedGraph(grid,i,j):
    try:
        if(grid[i+1][j] == 1):
            grid[i+1][j] = 3
            changedGraph(grid,i+1,j)
    except:
        a = 1
    try:
        if(grid[i-1][j] == 1 and (i-1) >= 0):
            grid[i-1][j] = 3
            changedGraph(grid,i-1,j)
    except:
        a = 1
    try:
        if(grid[i][j+1] == 1):
            grid[i][j+1] = 3
            changedGraph(grid,i,j+1)
    except:
        a = 1
    try:
        if(grid[i][j-1] == 1 and (j-1)>=0):
            grid[i][j-1] = 3
            changedGraph(grid,i,j-1)
    except:
        a = 1
