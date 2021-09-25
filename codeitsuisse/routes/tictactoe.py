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
    messages = SSEClient('https://cis2021-arena.herokuapp.com/tic-tac-toe/start/'+battleId)
    board = ['NW','N','NE','W','C','E','SW','S','SE']
    played = ['','','','','','','','','']
    youAre = ""
    for msg in messages:
        logging.info("data sent from arena {}".format(msg))
        data = msg.get_json()
        try:
            if( data['youAre'] != ""):
                youAre = data['youAre']
                makemove(board,played,youAre,battleId)
        except:
            try:
                if(data['player'] == youAre):
                    continue
                else:
                    if(data["action"] == "putSymbol"):
                        played[board.index(data['position'])] = data['player']
                        makemove(board,played,youAre,battleId)
            except:
                continue
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def makemove(board,played,youAre,battleId):
    data = {}
    data['action'] = "putSymbol"
    if(played.count('') == 9):
        data["position"] = "NW"
    else:
        for i in range(len(played)):
            if(played[i] == ''):
                data["position"] = board[i]
                break
    requests.post("https://cis2021-arena.herokuapp.com/tic-tac-toe/play/"+battleId, data = json.dumps(data))
