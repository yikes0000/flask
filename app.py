from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

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
    # 根據簡報，這裡會顯示 URL 擷取到的變數 [cite: 224]
    return f'User {escape(username)}'

# ==========================================
# Exercise 46: Flask Load HTML
# 路由: /home
# ==========================================
@app.route('/home')
def home():
    # 載入 templates 資料夾中的 home.html [cite: 341]
    return render_template('home.html')

# ==========================================
# Exercise 47: Show Variables
# 路由: /ex47
# ==========================================
@app.route('/ex47')
def show_variables():
    # 建立一個 Python 字典物件 [cite: 871]
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    # 將變數傳遞給 HTML 模板
    return render_template('ex47.html', data=x)

# ==========================================
# Exercise 48: Show double of the inputted number
# 路由: /ex48
# ==========================================
@app.route('/ex48', methods=['GET', 'POST'])
def predict():
    result = None
    if request.method == 'POST':
        # 接收表單傳來的 'x' 並轉為整數，然後乘以 2 [cite: 888, 889]
        x_val = int(request.form["x"])
        result = x_val * 2
    return render_template("double.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)