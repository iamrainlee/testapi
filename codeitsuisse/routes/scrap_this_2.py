#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import json

from flask import request, jsonify, Response

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/scrap_this_2', methods=['GET'])
def scrap_this_2():
  return """<!DOCTYPE HTML>
  <html>
      <head>
          <title>Scrap Me!</title>
      </head>
      <body>
         <table id="violin" border="1">
          <tr><th colspan="3">Violin 5 grade songs</th></tr>
          <tr><th>List</th><th>Piece</th><th>Composer</th></tr>
          <tr><td rowspan="10">A</td><td>Folia<br/><small>Theme and selected variations from Sonata in D minor, Op. 5 No. 12</small></td><td>Corelli </td></tr>
          <tr><td> Allegro <br/><small>3rd movt from Sonata in B minor, Op. 5 No. 5</small></td><td> Leclair </td></tr>
          <tr><td> Allegro <br/><small>1st movt from Concerto in G, Op. 3 No. 3, RV 310</small></td><td> Vivaldi </td></tr>
          <tr><td> Presto <br/><small>3rd movt from Symphony No. 4</small></td><td> J. C. Bach </td></tr>
          <tr><td> Allegro <br/><small>1st movt from Symphony No. 4 in F</small></td><td> Boyce </td></tr>
          <tr><td> Bereite dich, Zion <br/><small>from Weihnachtsoratorium (Christmas Oratorio), BWV 248</small></td><td> J. S. Bach </td></tr>
          <tr><td> Tambourin </td><td> Gossec </td></tr>
          <tr><td> Café classique <br/><small>No. 5 from Coffee & Violin</small></td><td> Joachim Johow </td></tr>
          <tr><td> Giga <br/><small>4th movt from Sonata in G minor, Op. 5 No. 6</small></td><td> Jean Baptiste Loeillet </td></tr>
          <tr><td> Allegro (spiritoso) <br/><small>4th movt from Sonata No. 4 in D minor</small></td><td> Senaillé </td></tr>
          <tr><td rowspan="10">B</td><td> Elegy </td><td> Jacob </td></tr>
          <tr><td> Romance <br/><small>No. 12 from Premier guide du violoniste, Op. 75</small></td><td> C.-A. de Bériot </td></tr>
          <tr><td> Chanson triste <br/><small>No. 2 from 12 morceaux, Op. 40</small></td><td> Tchaikovsky </td></tr>
          <tr><td> Cradle Song <br/><small>H. 96</small></td><td> Bridge </td></tr>
          <tr><td> Berceuse </td><td> Ireland </td></tr>
          <tr><td> Sicilienne </td><td> attrib. Paradis </td></tr>
          <tr><td> Siciliano </td><td> Pergolesi </td></tr>
          <tr><td> Andante sostenuto<br/><small>2nd movt from Concertino in G, Op. 24</small></td><td> Rieding </td></tr>
          <tr><td> Elegie <br/></td><td> Shostakovich </td></tr>
          <tr><td> Waltz <br/><small>from Serenade for Strings</small></td><td> Tchaikovsky </td></tr>
          <tr><td rowspan="10">C</td><td> Hay Barn Blues </td><td> Nikki Iles </td></tr>
          <tr><td> Night Song and Pantomime <br/><small>from The Little Sweep, Op. 45</small></td><td> Britten </td></tr>
          <tr><td> Bamboo Stem and Jasmine Flower (SOLO) </td><td> Trad. Chinese </td></tr>
          <tr><td> The Secrets of the Dark Pool in the Pine Forest</td><td> Diana Burrell </td></tr>
          <tr><td> Intermezzo <br/><small>from Háry János</small></td><td> Kodály </td></tr>
          <tr><td> Cossack Dance</td><td> Timothy Kraemer and Natasha Kraemer </td></tr>
          <tr><td> Sugar with Cinnamon </td><td> Lavildevan </td></tr>
          <tr><td> Moderato<br/><small>1st movt from Sonatine for Violin</small></td><td> Tailleferre </td></tr>
          <tr><td> Hava Nagila (Let Us Rejoice) </td><td> Trad. Klezmer </td></tr>
          <tr><td> Barn Dance <br/><small>from Way Out West</small></td><td> Richard Wade </td></tr>
        </table>
      </body>
  </html>""";
