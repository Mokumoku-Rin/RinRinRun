from api import app

@app.route('/fuga')
def index_fuga():
    return 'Hello World!'