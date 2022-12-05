from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 解决跨域问题

@app.route('/')
@app.route('/index')
def hello():
    return "Welcome to my flask!"

@app.route('/gif')
def hello2():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

# 给 URL 添加变量部分，标记为 <variable_name> ，其会作为命名参数传递到函数
from markupsafe import escape
"""
输入的数据会包含恶意代码，所以不能直接作为响应返回，
需要使用 MarkupSafe(Flask 的依赖之一）提供的 escape() 函数
对 name 变量进行转义处理，比如把 < 转换成 &lt;
"""

@app.route('/user/<name>/<int:age>')
def user_page(name,age):
    # return f'User page: Name is {name}, age is {age}'
    return f'User page: Name is {escape(name)}, age is {escape(age)}'

# 生成视图函数对应的 URL
from flask import url_for

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 生成 hello 视图函数对应的 URL，将会输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='wzy', age='22'))  # 输出：/user/wzy/22

    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'

if __name__ == '__main__':
    app.run('0.0.0.0')