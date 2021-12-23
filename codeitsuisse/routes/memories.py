#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import json

from flask import request, jsonify, Response

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/memories', methods=['GET'])
def memories():
  return """<!DOCTYPE HTML>
  <html>
      <head>
          <title>Scrap Me!</title>
          <style>
            body{
                background-color: black
            }
            h1{
                color: red;
            }
            h2{
                color: pink;
            }
            .event{
                border: 1px solid pink;
                border-radius: 5px;
                padding: 15px;
                width: 80%;
                margin: auto;
                margin-top: 20px;
                margin-bottom: 20px;
                color: pink;
                display: flex;
                flex-direction: row;
            }
            .event_img{
                height: 33vh;
            }
            .event_content{
                flex: 1;
                flex-wrap: nowrap;
                display: flex;
                flex-direction: column;
                padding-top: 33px;
                padding-bottom: 10px;
            }
            .event_title{
                flex: 2;
                font-size: 1.5rem;

            }
            .event_time{
                flex: 1;
                font-size: 1rem;

            }
          </style>
      </head>
      <body>
        <center><h1>Scrap this!</h1></<center>
        <center><h1>Exercise 1!</h1></center>
        <div class="main_content">
            <center><h2>Memories</h2></center>
            <div class="contents">
                <div class="event">
                    <img class="event_img" src="http://nicole.great-site.net/22136c64-5e05-40e4-8d9b-7bd34eba2d27.JPG">
                    <div class="event_content">
                        <div class="event_title">A shy confession to you!</div>
                        <div class="event_time">2021-06-18</div>
                    </div>
                </div>
                <div class="event">
                    <div class="event_content">
                        <div class="event_title">First date!</div>
                        <div class="event_time">2021-06-20</div>
                    </div>
                    <img class="event_img" src="http://nicole.great-site.net/dda4acf9-9583-4697-953c-3abe256b3d17.JPG">
                </div>
                <div class="event">
                    <img class="event_img" src="http://nicole.great-site.net/d37ad17e-0e94-4a34-a278-7e0d72d09e11.JPG">
                    <div class="event_content">
                        <div class="event_title">Dinner with you mom! (Tell her I am sorry I didn't fulfill my promise to her&#128583;)</div>
                        <div class="event_time">2021-06-24</div>
                    </div>
                </div>
                <div class="event">
                    <div class="event_content">
                        <div class="event_title">Said something that hurts u&#128583;</div>
                        <div class="event_time">2021-06-25</div>
                    </div>
                    <img class="event_img" src="http://nicole.great-site.net/IMG_6051.jpg">
                </div>
                <div class="event">
                    <img class="event_img" src="http://nicole.great-site.net/04380407-7ddd-4aef-85f1-64d15a80855a.JPG">
                    <div class="event_content">
                        <div class="event_title">Confession again! Posted story!</div>
                        <div class="event_time">2021-06-27</div>
                    </div>
                </div>
                <div class="event">
                    <div class="event_content">
                        <div class="event_title">Cyberport dating during work!</div>
                        <div class="event_time">2021-06-30</div>
                    </div>
                    <img class="event_img" src="http://nicole.great-site.net/IMG_6090.jpg">
                </div>
                <div class="event">
                    <img class="event_img" src="http://nicole.great-site.net/IMG_6104.jpg">
                    <div class="event_content">
                        <div class="event_title">Cyberport dating after work!</div>
                        <div class="event_time">2021-07-02</div>
                    </div>
                </div>
                <div class="event">
                    <div class="event_content">
                        <div class="event_title">K11 Dating! Such a beautiful picture</div>
                        <div class="event_time">2021-07-04</div>
                    </div>
                    <img class="event_img" src="http://nicole.great-site.net/IMG_6127.jpg">
                </div>
                <div class="event">
                    <img class="event_img" src="http://nicole.great-site.net/IMG_6150.jpg">
                    <div class="event_content">
                        <div class="event_title">Ferris Wheel!</div>
                        <div class="event_time">2021-07-04</div>
                    </div>
                </div>
                <div class="event">
                    <div class="event_content">
                        <div class="event_title">Kwun Tong APM Dating!</div>
                        <div class="event_time">2021-07-08</div>
                    </div>
                    <img class="event_img" src="http://nicole.great-site.net/IMG_6177.jpg">
                </div>
                <div class="event">
                    <img class="event_img" src="http://nicole.great-site.net/2606679c-8fc6-4cbc-bf0b-e9aad60dd037.JPG">
                    <div class="event_content">
                        <div class="event_title">After-work Cyberport Dating! Again!</div>
                        <div class="event_time">2021-07-16</div>
                    </div>
                </div>
                <div class="event">
                    <div class="event_content">
                        <div class="event_title">Double Dating!</div>
                        <div class="event_time">2021-07-16</div>
                    </div>
                    <img class="event_img" src="http://nicole.great-site.net/c693f61c-e94c-45f7-9298-2b9a8e61193f.JPG">
                </div>
                <div class="event">
                    <img class="event_img" src="http://nicole.great-site.net/IMG_6302.jpg">
                    <div class="event_content">
                        <div class="event_title">One Month! What a memory!</div>
                        <div class="event_time">2021-07-18</div>
                    </div>
                </div>
                <div class="event">
                    <div class="event_content">
                        <div class="event_title">Disney! The most happy and sad day.</div>
                        <div class="event_time">2021-07-21</div>
                    </div>
                    <img class="event_img" src="http://nicole.great-site.net/IMG_6353.jpg">
                </div>
                <div class="event">
                    <img class="event_img" src="http://nicole.great-site.net/4368ff97-c146-499a-953e-c39832b66434.JPG">
                    <div class="event_content">
                        <div class="event_title">Get back together! So sorry I did such a bad thing.</div>
                        <div class="event_time">2021-07-23</div>
                    </div>
                </div>
                <div class="event">
                    <div class="event_content">
                        <div class="event_title">Make study plan in HKU. Plan our year ahead!</div>
                        <div class="event_time">2021-07-26</div>
                    </div>
                    <img class="event_img" src="http://nicole.great-site.net/810e99fe-e1cb-4b61-b4b8-1d4cc22cb24e.JPG">
                </div>
                <div class="event">
                    <img class="event_img" src="http://nicole.great-site.net/c178b159-5529-42ff-9c3e-613bb888fea7.JPG">
                    <div class="event_content">
                        <div class="event_title">Study tgt in Mos Cafe</div>
                        <div class="event_time">2021-08-03</div>
                    </div>
                </div>
                <div class="event">
                    <div class="event_content">
                        <div class="event_title">Bought u a flower, but it's too late. Both of us so tired, as we spoke on phone till 4am.</div>
                        <div class="event_time">2021-08-04</div>
                    </div>
                    <img class="event_img" src="http://nicole.great-site.net/2cf6fe34-0387-4829-9b70-0648390a35d1.JPG">
                </div>
                <div class="event">
                    <img class="event_img" src="http://nicole.great-site.net/101eb357-bfcc-4bba-8d5e-feb450a93c22.JPG">
                    <div class="event_content">
                        <div class="event_title">Dessert at night! Sweet!</div>
                        <div class="event_time">2021-08-05</div>
                    </div>
                </div>
                <div class="event">
                    <div class="event_content">
                        <div class="event_title">Went to Kai Tak Cruise Terminal. Last Day...&#128546;&#128546;</div>
                        <div class="event_time">2021-08-06</div>
                    </div>
                    <img class="event_img" src="http://nicole.great-site.net/IMG_6463.jpg">
                </div>
                <div class="event">
                    <img class="event_img" src="http://nicole.great-site.net/IMG_6828.jpg">
                    <div class="event_content">
                        <div class="event_title">Birthday Present and Surprise!</div>
                        <div class="event_time">2021-11-08</div>
                    </div>
                </div>
                <div class="event">
                    <div class="event_content">
                        <div class="event_title">Christmas Present!</div>
                        <div class="event_time">2021-12-21</div>
                    </div>
                    <img class="event_img" src="http://nicole.great-site.net/IMG_7272.jpg">
                </div>
            </div>
            <centre><h2>Do you remember these memories?</h2></centre>
            <centre><h2>I will never forget these</h2></centre>
            <centre><h2>Really hope I can create new memories with you......</h2></centre>
        </div>
      </body>
  </html>""";
