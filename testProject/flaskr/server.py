from flask import Flask
from flask import request
from flask import render_template # Jinja2 模板

history = []
app = Flask(__name__)
result = {}
@app.route('/', methods=['GET', 'POST'])
def serrch():
    if request.method == 'POST':
        location = request.form['cityname']
        history.append(location)
        if location =='q':
            return render_template('quit.html', his=history)
        elif location =='his':
            return render_template('index.html',
                his=history)
        elif location in ''
        else:
            return render_template('index.html',
                message='Bad username or password')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
