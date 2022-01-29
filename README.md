- To run the project locally, first clone this repository and `cd` into its directory.
```bash 
$ git clone https://github.com/IanMaguithi/Honeygaindockerlinux.git
$ cd honey
```
Then:

1. Create a new virtual environment:
    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/), run `virtualenv venv` and then `source venv/bin/activate`
    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/), run `mkvirtualenv venv`
2. Install the project requirements by running this command on your project terminal:
```bash 
$ pip install -r requirements.txt 
```
3. Initialise the script by running the following command: for python3
```bash
$ python3 initialize.py your_email your_password your_device_name
```
4. Find the path to our project. To do this run the following command:
```bash
$ pwd
```
- An example of the output of this command. /home/user/folder/honey/
5. Crontab on reboot. Open the crontask list by using the following command:
```bash
$ crontab -e
```
- You will be prompted to select an editor to update the cron task with if you have multiple text editors. Choose your preferred option.
In this case however, we'll use the default option Nano.
- Use the following command to set our script to run at every system boot.
@reboot [path to venv] [path to project] I'll use an example to elaborate using the path we had obtained earlier in step 4
and assuming our virtual environment is in the same root folder honey.
```bash
@reboot /home/user/folder/honey/venv/bin/python /home/user/folder/honey/main.py >> ~/cron.log 2>&1
```
- '>> ~/cron.log 2>&1' for saving errors into a file in the home directory.
- Checkout this [link](https://phoenixnap.com/kb/crontab-reboot) for further information if you run into errors.
- Finally, save changes by pressing Control + S and exit Nano by pressing Control + X