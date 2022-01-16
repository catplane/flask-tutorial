from flask import Flask, render_template, request, redirect, session
from markupsafe import escape
from models.dbhelper import SQLHelper

app = Flask(__name__)
app.secret_key = 'wqde2ccre!'
app.debug = True

print(__name__)
print(app.url_map)

@app.route('/')
def index():
    print(session.get('user'))
    return render_template('index.html', name='nihao')

@app.route('/hello')
def hello():
    result = SQLHelper.fetch_one('select * from roles', [])
    print(result)
    #return 'Hello, World'
    return str(result)

@app.route('/user/<username>', methods=['POST'])
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        if request.form.get('username') == 'nihao':
            session['user'] = request.form.get('username')
            return redirect('/')

# 交由客户端保管机制
# 开启session['ursernsm'] = request.form.get('username')
# {"username":anwen}
# 序列化字典 == 字符串
# 加密字符串 Secret key 密钥字符串
#
# 接受反序列化Session;从cookie中获取到一个session key的值
# 通过Secretkey 解密session
# 反序列化成字典

