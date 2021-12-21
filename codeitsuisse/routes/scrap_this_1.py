#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import json

from flask import request, jsonify, Response

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/scrap_this_1', methods=['GET'])
def scrap_this_1():
  return """<!DOCTYPE HTML>
  <html>
      <head>
          <title>Scrap Me!</title>
      </head>
      <body>
          <p>Nicole Xmas yau boy pui la</p>
          <p>MM sai me la</p>
          <p>ngo sad dou write this bei nei</p>
          <p>ngo so sad, nei dou mm find me, mm sai me, because nei yau boy pui la</p>
          <p>But mm guns la, ngo still write this note to u. Ngo doi nei so good, nei dou mm yiu ngo.</p>
      </body>
  </html>""";
