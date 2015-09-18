from . import app, mysql

@app.route("/connect")
def connect():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM helloworld.messages''')
	msgs = cur.fetchall()
	return str(msgs)