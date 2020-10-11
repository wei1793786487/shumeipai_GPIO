from flask import Flask
import main
import threading
app = Flask(__name__)


@app.route('/start')
def start():
    main.start()
    return '开始旋转'


@app.route('/stop')
def stop():
    main.stop()
    return '结束旋转'


def rotate (type):
   if(type=="1"):
       main.start()
   else:
       main.stop()
