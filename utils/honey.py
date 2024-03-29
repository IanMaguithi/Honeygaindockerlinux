import pathlib
import subprocess
from datetime import datetime

from utils.connection_test import connection_test
from utils.read_write_file import read_file

data_file = pathlib.Path.home().joinpath("data.json")


def start_honeygain_service(_email, _password, _device_name):
    with open("/tmp/output.log", "a") as output:
        subprocess.call(
            f"docker run -d honeygain/honeygain -tou-accept -email {_email} -pass {_password} "
            f"-device {_device_name}", shell=True, stdout=output,
            stderr=output)


def run_get_honey():
    if connection_test():
        data = read_file(data_file)
        start_honeygain_service(data["email"], data["password"], data["device_name"])
    else:
        with open("/tmp/output.log", "a") as output:
            output.write(f"Honey gain task didn't start up due to connectivity issue at: {datetime.now()}")
