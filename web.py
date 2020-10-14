from flask import Flask
from flask import request
import main
app = Flask(__name__)

@app.route('/start/<int:post_id>')
def start(post_id):
    main.doit(post_id)
    return '发送旋转指令成功，旋转时间'+str(post_id)+'秒'



