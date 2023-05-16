from flask import Flask,jsonify,request

app = Flask(__name__)

tasks=[
    {
        'id':1,
        'title':u'Buy groceries',
        'description':u'shampoo,soap,milk,fruit,icecream',
        'done':False
    },
    {
        'id':2,
        'title':u'Electronics',
        'description':u'iPhone, Macbook, Apple Watch Ultra, RTX 4090, iPad, Airpods, Samsung S23 Ultra',
        'done':False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },400)
    task = {
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"Success",
        "message":"Tasks added successfully!"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
if __name__=="__main__":
    app.run(debug=True)
