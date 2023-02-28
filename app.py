from flask import Flask, render_template, url_for, jsonify


app = Flask(__name__ , static_url_path='/static')


logs=[
    {
    'id':0,
    'title':'electoral papers',
     'pick-up': 'Edo state',
     'delivery': 'Benin'
},
{
    'id':1,
    'title':'electoral papers',
     'pick-up': 'ekiti state',
     'delivery': 'ado-ekiti'
},
{
    'id':2,
    'title':'electoral papers',
     'pick-up': 'Ebonyi state',
     'delivery': 'abakaliki'
},
    {
    'id':3,
    'title':'electoral papers',
     'pick-up': 'Plateau state',
     'delivery': 'Jos'
}]
@app.route('/')
def index():
    return render_template("index.html", logs=logs)

@app.route('/api/logs')
def api_log():
    return jsonify(logs)

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)