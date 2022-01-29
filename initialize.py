import sys
import os.path

from read_write_file import write_file
from validator import check_valid_email

data_file = os.path.join(os.getcwd(), "data.txt")

email = sys.argv[1]
password = sys.argv[2]
device_name = sys.argv[3]
if check_valid_email(email):
    write_file(email, password, device_name, data_file)
else:
    print("Invalid email. Try again")
