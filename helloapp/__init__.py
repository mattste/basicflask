from flask import Flask
from flask.ext.mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'ifyouhavepass'
mysql.init_app(app)

import viewsA
import viewsB