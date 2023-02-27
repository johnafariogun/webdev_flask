from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "Sup"
# if __name__ == 