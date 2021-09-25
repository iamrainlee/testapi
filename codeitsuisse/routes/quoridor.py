#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import json
from sseclient import SSEClient
import requests

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/quoridor', methods=['POST'])
def quoridor():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    battleId = data.get("battleId")
    board_first = ['a','b','c','d','e','f','g','h','i']
    board_second = board_first[::-1]
    board = []
    for i in range(9):
        board.append(['','','','','','','','',''])
    youAre = ""
    gameOn = True
    players = ['e1','e9']
    while gameOn:
        url = 'https://cis2021-arena.herokuapp.com/quoridor/start/'+battleId
        headers = {'Accept': 'text/event-stream'}
        messages = SSEClient(url)
        for msg in messages:
            # r = requests.get('https://cis2021-arena.herokuapp.com/tic-tac-toe/start/'+battleId)
            data = msg.data
            logging.info("data sent from arena {}".format(data))
            # data = json.loads(msg.data.replace("'",'"'))
            if type(data) is str:
                try:
                    data = json.loads(data)
                except:
                    continue
            try:
                if( data['youAre'] != ""):
                    youAre = data['youAre']
                    if(data['youAre'] == "first"):
                        logging.info("Prepare to make move")
                        makemove2(board,youAre,battleId,players)
            except:
                try:
                    if(data['player'] == youAre):
                        continue
                    else:
                        rdata = {}
                        rdata['action'] = '(╯°□°)╯︵ ┻━┻'
                        requests.post("https://cis2021-arena.herokuapp.com/quoridor/play/"+battleId, data = rdata)
                        break
                        # try:
                        #     if(data['position'] not in board or played[board.index(data['position'])] != ''):
                        #         logging.info("Flip table")
                        #         gameOn = False
                        #         rdata = {}
                        #         rdata['action'] = '(╯°□°)╯︵ ┻━┻'
                        #         requests.post("https://cis2021-arena.herokuapp.com/quoridor/play/"+battleId, data = rdata)
                        #         break
                        #     played[board.index(data['position'])] = data['player']
                        #     logging.info("Prepare to makemove")
                        #     makemove2(board,youAre,battleId,players)
                        # except:
                        #     logging.info("Flip table")
                        #     gameOn = False
                        #     rdata = {}
                        #     rdata['action'] = '(╯°□°)╯︵ ┻━┻'
                        #     requests.post("https://cis2021-arena.herokuapp.com/quoridor/play/"+battleId, data = rdata)
                        #     break
                except:
                    try:
                        if(data['winner'] == "draw" or data['winner'] == youAre):
                            logging.info("Win game !")
                        else:
                            logging.info("Possibly lost game !")
                        gameOn = False
                        break
                    except:
                        gameOn = False
                        break
    return json.dumps(data)

def makemove2(board,youAre,battleId,players):
    data = {}
    data['action'] = "move"
    data["position"] = ""
    current_loc = int(players[0][1])
    data["position"] = "e"+(current_loc+1)
    players[0] = data["position"]
    logging.info("My move :{}".format(data))
    requests.post("https://cis2021-arena.herokuapp.com/quoridor/play/"+battleId, data = data)
