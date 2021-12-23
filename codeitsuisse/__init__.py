from flask import Flask
app = Flask(__name__)
mastermind_records = {}
import codeitsuisse.routes.testget
import codeitsuisse.routes.testpost
import codeitsuisse.routes.exercise1
import codeitsuisse.routes.exercise2
import codeitsuisse.routes.mastermind
import codeitsuisse.routes.scrap_this_1
import codeitsuisse.routes.scrap_this_2
import codeitsuisse.routes.memories
