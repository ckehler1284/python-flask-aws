from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/time')
def time():    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return("Current Time = %s" % current_time)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
