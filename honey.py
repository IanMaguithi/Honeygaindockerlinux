import os.path
import subprocess
from datetime import datetime

from connection_test import ping
from read_write_file import read_file

data_file = os.path.join(os.getcwd(), "data.txt")


def get_honey(_email, _password, _device_name):
    with open("/tmp/output.log", "a") as output:
        subprocess.call(
            f"docker run -d honeygain/honeygain -tou-accept -email {_email} -pass {_password} "
            f"-device {_device_name}", shell=True, stdout=output,
            stderr=output)


def run_get_honey():
    if ping():
        data = read_file(data_file)
        get_honey(data["email"], data["password"], data["device_name"])
    else:
        with open("/tmp/output.log", "a") as output:
            output.write(f"Honey gain task didn't start up due to connectivity issue at: {datetime.now()}")
