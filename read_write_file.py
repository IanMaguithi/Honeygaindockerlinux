import json


def write_file(_email, _password, _device_name, _data_file):
    data = {
        "email": _email,
        "password": _password,
        "device_name": _device_name
    }
    with open(_data_file, "w") as file:
        file.write(json.dumps(data))


def read_file(_data_file):
    with open(_data_file) as file:
        data = json.loads(file.read())
    return data
