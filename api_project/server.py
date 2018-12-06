from flask import (
    Flask,
    request)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def primary_page():
    return 'Welcome to 6over6 server here you can do the following requests:\n' \
           '1. Make a post request using /api/write_text_to_file\n' \
           '2. Going to the index page - /api/index which will show you a nice message\n'


@app.route('/api/index', methods=['GET'])
def index():
    return 'Welcome'


@app.route('/api/write_text_to_file/', methods=['POST'])
def write_text_to_file():
    if request.method == 'POST':
        print(type(request.data))
        data = request.data.decode("utf-8")
        with open("data_folder/str.txt", "w+") as f:
            f.write(data)

    return data


@app.route('/api/write_text_to_file_get/<variable>', methods=['GET'])
def write_text_to_file_get(variable):
    if request.method == 'GET':
        with open("data_folder/str.txt", "w+") as f:
            f.write(variable)
    return variable


if __name__ == '__main__':
    app.run()


