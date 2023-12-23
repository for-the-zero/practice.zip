import core
from flask import Flask, render_template

token = ""   # your api key
cid = "UCbKWv2x9t6u8yZoB3KcPtnw"    # Alan Becker

app = Flask(__name__)


@app.route('/')
def webui():
	global token
	global cid
	vids, times, titles = core.get_list(token,cid)
	data = []
	for i in range(len(vids)):
		data.append({'vids': vids[i],'titles': titles[i],'times': times[i]})


	return render_template('t.html', items=data)

if __name__ == '__main__':
	app.run(debug=True) 
