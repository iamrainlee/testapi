import logging
import json
import copy
import networkx as nx

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

curgrid = []

@app.route('/stock-hunter', methods=['POST'])
def stockhunter():
    data = request.get_json()
    logging.info("Data: {}".format(data))
    result = []
    for i in data:
        result.append(calstock(i))
    logging.info("My result :{}".format(result))
    return json.dumps(result)
def calstock(d):
    entry = (d["entryPoint"]["first"],d["entryPoint"]["second"])
    target = (d["targetPoint"]["first"],d["targetPoint"]["second"])
    leftmost = min(entry[0],target[0])
    width = max(entry[0],target[0]) - leftmost + 1
    upmost = min(entry[1],target[1])
    height = max(entry[1],target[1]) - upmost + 1
    # entry = (entry[0]-leftmost,entry[1]-upmost)
    # target = (target[0]-leftmost,target[1]-upmost)
    grid = []
    outgrid = []
    riskLevel = []
    for i in range(height+upmost+3):
        riskLevel.append([])
        grid.append([])
        for j in range(width+leftmost+3):
            grid[i].append(0)
            riskIndex = 0
            if(i == 0 and j == 0):
                riskIndex = 0
            elif(i == 0):
                riskIndex = j * d['horizontalStepper']
            elif(j == 0):
                riskIndex = i * d['verticalStepper']
            else:
                riskIndex = riskLevel[i-1][j] * riskLevel[i][j-1]
            if(target == (i,j)):
                riskIndex = 0
            riskLevel[i].append((riskIndex+d['gridDepth'])%d['gridKey'])
            grid[i][j] = 3 - riskLevel[i][j]%3

    for i in range(height):
        outgrid.append([])
        for j in range(width):
            outgrid[i].append('')
            if(grid[i+upmost][j+leftmost] == 3):
                outgrid[i][j] = "L"
            elif(grid[i+upmost][j+leftmost] == 2):
                outgrid[i][j] = "M"
            else:
                outgrid[i][j] = "S"
    global curgrid
    curgrid = grid
    G=nx.grid_graph(dim=[width+leftmost+3,height+upmost+3])
    r = {}
    r["gridMap"] = outgrid
    cost = 0
    logging.info(nx.astar_path(G,entry,target,dist))
    for i in nx.astar_path(G,entry,target,dist):
        cost += grid[i[0]][i[1]]
    cost -= grid[entry[0]][entry[1]]
    r["minimumCost"] = cost
    return r
def dist(a,b):
    global curgrid
    (x1, y1) = a
    (x2, y2) = b
    return curgrid[x1][y1]