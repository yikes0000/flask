from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

# ==========================================
# 首頁選單 (避免進入主網址時出現 404)
# ==========================================
@app.route('/')
def main_page():
    return '''
    <h1>Flask 作業目錄</h1>
    <ul>
        <li><a href="/ex43">Exercise 43 (Index)</a></li>
        <li><a href="/ex44">Exercise 44 (Hello)</a></li>
        <li><a href="/user/Kevin">Exercise 45 (URL Info)</a></li>
        <li><a href="/home">Exercise 46 (Load HTML)</a></li>
        <li><a href="/ex47">Exercise 47 (Variables)</a></li>
        <li><a href="/ex48">Exercise 48 (Double)</a></li>
    </ul>
    '''

# ==========================================
# Exercise 43: Flask Online / Index Page
# 路由: /ex43
# ==========================================
@app.route('/ex43')
def index():
    return 'Index Page'

# ==========================================
# Exercise 44: Hello Flask
# 路由: /ex44
# ==========================================
@app.route('/ex44')
def hello():
    return 'Hello, World!'

# ==========================================
# Exercise 45: URL Info
# 路由: /user/<username>
# ==========================================
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

# ==========================================
# Exercise 46: Flask Load HTML
# 路由: /home
# ==========================================
@app.route('/home')
def home():
    return render_template('home.html')

# ==========================================
# Exercise 47: Show Variables
# 路由: /ex47
# ==========================================
@app.route('/ex47')
def show_variables():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return render_template('ex47.html', data=x)

# ==========================================
# Exercise 48: Show double of the inputted number
# 路由: /ex48
# ==========================================
@app.route('/ex48', methods=['GET', 'POST'])
def predict():
    result = None
    if request.method == 'POST':
        x_val = int(request.form["x"])
        result = x_val * 2
    return render_template("double.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)