from flask import Flask, jsonify
import core

app = Flask(__name__)

@app.route('/perfapi')
def perfapi():
    return jsonify(core.get())

if __name__ == '__main__':
    app.run(debug=True)