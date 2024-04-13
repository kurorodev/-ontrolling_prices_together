# from database.database import create_new_user
from flask import Flask, request, jsonify
from test import testdata

app = Flask(__name__)

# @app.route('/request', methods=['POST'])
# def process_data():
#     data = request.json['userdata']
#     cruser = create_new_user(data['username'],data['userpassword'])
#     return jsonify(data)
 
@app.route('/get_shop_info', methods=['GET'])
def process_get_shop_info():
    print('aaaaaaaaaa')
    # data = request.json['getShopInfo']
    data = testdata()
    return jsonify(data)

@app.route('/register_new_user', methods=['POST'])
def process_register_new_user():
    data = request.json['userdata']
    """
    Функция в бд для регистрации
    newdata = func()
    """
    return jsonify(data)
 
if __name__ == '__main__':
    app.run(debug=True,port=5501)