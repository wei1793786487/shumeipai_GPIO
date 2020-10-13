from flask import Flask
import main
import threading
app = Flask(__name__)


@app.route('/start')
def start():
    print("start")
    main.start()
    return '开始旋转'


@app.route('/stop')
def stop():
    print("触发停止")
    main.stop()
    return '结束旋转'



