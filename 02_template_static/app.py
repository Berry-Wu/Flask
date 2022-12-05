name = 'wzy'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

from flask import Flask, render_template

app = Flask(__name__)

# 使用 render_template() 函数可以把模板渲染出来，必须传入的参数为模板文件名（相对于 templates 根目录的文件路径）
@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)

if __name__ == '__main__':
    app.debug = True # 加上之后会开启调试模式，修改代码后服务器自动重新载入
    app.run('0.0.0.0')