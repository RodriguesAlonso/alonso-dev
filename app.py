from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tag')
def tag():
    return render_template('tags.html')

@app.route('/tarefas')
def tarefas():
    return render_template('tarefas.html')


if __name__ == '__main__':
    app.run()
    