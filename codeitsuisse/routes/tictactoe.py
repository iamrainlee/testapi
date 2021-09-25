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
                        played[board.index(data['position'])] = data['player']
                        logging.info("Prepare to makemove")
                        makemove(board,played,youAre,battleId)
                except:
                    try:
                        if(data['winner'] == "draw" or data['winner'] == "O"):
                            logging.info("Win game !")
                        else:
                            logging.info("Possibly lost game !")
                        gameOn = False
                    except:
                        gameOn = False
                        continue
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def makemove(board,played,youAre,battleId):
    data = {}
    data['action'] = "putSymbol"
    if(played.count('') == 9):
        data["position"] = "NW"
        played[0] = youAre
    else:
        for i in range(len(played)):
            if(played[i] == ''):
                played[i] = youAre
                data["position"] = board[i]
                break
    logging.info("My move :{}".format(data))
    requests.post("https://cis2021-arena.herokuapp.com/tic-tac-toe/play/"+battleId, data = data)
