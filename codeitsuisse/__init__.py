from flask import Flask
app = Flask(__name__)
import codeitsuisse.routes.testget
import codeitsuisse.routes.testpost
import codeitsuisse.routes.exercise1
import codeitsuisse.routes.exercise2
import codeitsuisse.routes.mastermind

mastermind_records = {}
