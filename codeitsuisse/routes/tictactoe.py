#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import json
from sseclient import SSEClient
import requests

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/tic-tac-toe', methods=['POST'])
def tictactoe():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    battleId = data.get("battleId")
    board = ['NW','N','NE','W','C','E','SW','S','SE']
    played = ['','','','','','','','','']
    youAre = ""
    gameOn = True
    while gameOn:
        url = 'https://cis2021-arena.herokuapp.com/tic-tac-toe/start/'+battleId
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
                    if(data['youAre'] == "O"):
                        logging.info("Prepare to make move")
                        makemove(board,played,youAre,battleId)
            except:
                try:
                    if(data['player'] == youAre):
                        continue
                    else:
                        try:
                            logging.info(played)
                            if(data['position'] not in board or played[board.index(data['position'])] != ''):
                                logging.info("Flip table")
                                gameOn = False
                                rdata['action'] = '(╯°□°)╯︵ ┻━┻'
                                requests.post("https://cis2021-arena.herokuapp.com/tic-tac-toe/play/"+battleId, data = rdata)
                                break
                            played[board.index(data['position'])] = data['player']
                            logging.info("Prepare to makemove")
                            makemove(board,played,youAre,battleId)
                        except:
                            logging.info("Flip table")
                            gameOn = False
                            rdata['action'] = '(╯°□°)╯︵ ┻━┻'
                            requests.post("https://cis2021-arena.herokuapp.com/tic-tac-toe/play/"+battleId, data = rdata)
                            break
                except:
                    try:
                        if(data['winner'] == "draw" or data['winner'] == youAre):
                            logging.info("Win game !")
                        else:
                            logging.info("Possibly lost game !")
                        gameOn = False
                    except:
                        gameOn = False
                        break
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def makemove(board,played,youAre,battleId):
    data = {}
    data['action'] = "putSymbol"
    data["position"] = ""
    if(played.count('') == 9):
        data["position"] = "NW"
        played[0] = youAre
    else:
        for i in range(len(played)):
            if(played[i] == ''):
                temp = played[:]
                temp[i] = youAre
                if(checkwin(temp,youAre)):
                    played[i] = youAre
                    data["position"] = board[i]
                    break
        if(data["position"] == ""):
            for i in range(len(played)):
                if(played[i] == ''):
                    played[i] = youAre
                    data["position"] = board[i]
                    break
    logging.info("My move :{}".format(data))
    requests.post("https://cis2021-arena.herokuapp.com/tic-tac-toe/play/"+battleId, data = data)

def checkwin(played,youAre):
    if(played[0] == youAre and played[3] == youAre and played[6] == youAre):
        return True
    elif(played[1] == youAre and played[4] == youAre and played[7] == youAre):
        return True
    elif(played[2] == youAre and played[5] == youAre and played[8] == youAre):
        return True
    elif (played[0] == youAre and played[1] == youAre and played[2] == youAre):
        return True
    elif(played[3] == youAre and played[4] == youAre and played[5] == youAre):
        return True
    elif (played[6] == youAre and played[7] == youAre and played[8] == youAre):
        return True
    elif(played[0] == youAre and played[4] == youAre and played[8] == youAre):
        return True
    elif (played[2] == youAre and played[4] == youAre and played[6] == youAre):
        return True
    else:
        return False
