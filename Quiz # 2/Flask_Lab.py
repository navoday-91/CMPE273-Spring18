
from flask import Flask, request, Response, jsonify, json

app = Flask(__name__)
data = {}


@app.route("/", methods=['GET'])
def hello():
    return "Welcome to flask app!"


@app.route('/users', methods=['POST'])
def new_name():
    content = request.form["name"]
    id = add_dict(content)
    response_msg = {
        'Name': content,
        'ID': id
    }
    resp = jsonify(response_msg)
    resp.status_code = 201
    return resp


@app.route('/users/<int:index>', methods=['GET'])
def view_name(index):
    global data
    if index not in data:
        response_msg = {
            'Error': "No Users Exist With This ID",
            'ID': index
        }
        resp = jsonify(response_msg)
        resp.status_code = 404
        return resp
    elif index in data:
        response_msg = {
            'Name': data[index],
            'ID': index
        }
        resp = jsonify(response_msg)
        resp.status_code = 200
        return resp


@app.route('/users/<int:index>', methods=['DELETE'])
def del_name(index):
    global data
    if index in data:
        del data[index]
    resp = ""
    resp.status_code = 204
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

def add_dict(x):
    global data
    i = len(data)
    data[i + 1] = x
    return i + 1