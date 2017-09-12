

from flask import Flask
from flask import request
from flask import render_template  # Jinja2 模板

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def serrch():
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')
@app.route('/test')
def test():
        return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
