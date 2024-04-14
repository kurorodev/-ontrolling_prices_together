# from database.database import create_new_user
from flask import Flask, request, jsonify
from get_exel import get_exel_data

app = Flask(__name__)

# @app.route('/request', methods=['POST'])
# def process_data():
#     data = request.json['userdata']
#     cruser = create_new_user(data['username'],data['userpassword'])
#     return jsonify(data)

@app.route('/')
def index():
    return app.send_static_file('/app/src/pages/user.html')

@app.route('/get_shop_info', methods=['GET'])
def process_get_shop_info():
    print('ok')
    data = get_exel_data()
    return jsonify(data)


"""Для регистрации"""

@app.route('/register', methods=['POST'])
def process_register_new_user():
    data = request.json['userdata']
    """
    Функция в бд для регистрации
    newdata = func()

    Вернуть jsonify(готовый словарь)
    """
    return jsonify({'aaaa':10,'bbbb':10})


"""Для Входа"""

@app.route('/login', methods=['POST'])
def process_login_in():
    data = request.json['userdata']
    """
    Функция в бд для входа
    newdata = func()
    
    Вернуть jsonify(готовый словарь)
    """
    return jsonify({'aaaa':10,'bbbb':10})


"""Для магазинов"""

@app.route('/load_shop_info', methods=['GET'])
def load_shop_info():
    data = {'data':{'Magnit':'kosmonavtov 27', 'pyaterka': 'dzerjinskogo 222', '9%':'svobodi'}}
    """
    Функция в бд для получения данных
    newdata = func()
    
    Вернуть jsonify(готовый словарь)
    """
    print('ok')
    return jsonify(data)



@app.route('/save_file', methods=['POST'])
def save_file():
    try:
        data = request.files.get('file')
        data.save(f"./app/data/model_image/{data.filename}")
    except Exception:
        return jsonify({'resoult': False})
    return jsonify({'resoult': True})

if __name__ == '__main__':
    app.run(debug=True,port=5501)


@app.route('/get_file')
def get_file():
    print('y')
    file_path = './app/data/12_02.xlsx'
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True,port=5501)