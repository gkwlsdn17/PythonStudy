from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/1')
def test1page():
    return "1page ok"

@app.route('/2')
def test2page():
    return "2page ok"

@app.route('/test')
def testpage():
    return render_template('index.html')

def main():
    app.run(debug=True, port=80)

if __name__=='__main__':
    main()