from . import app, mysql

@app.route("/helloworld")
def hello():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM helloworld.messages''')
	msgs = cur.fetchall()
	return str(msgs)