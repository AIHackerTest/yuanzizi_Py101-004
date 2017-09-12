from flask import Flask
from flask import request
from flask import render_template # Jinja2 模板

app = Flask(__name__)
# app.run(port=8888)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # return 111
        msg = str(request.form.get('order'))
        if request.form.get('help'):
            return render_template('index.html',
            message='help')
        elif request.form.get('search'):
            return render_template('index.html',
                        message='search')
        # username = request.form['username']
        # password = request.form['password']
        # if username=='admin' and password=='password':
        #     return render_template('signin-ok.html', username=username)
        # else:
        #     return render_template('form.html',
        #         message='Bad username or password', username=username)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
