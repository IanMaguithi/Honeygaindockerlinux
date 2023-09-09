<p align="center">
   <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
   </a>
</p>

[Honeygain JumpTask Mode](https://youtu.be/VeH95ILo9s8) | [Honeygain Sign Up](https://r.honeygain.me/MAGUI9B52D)
<br>

## **Installation**

- Run the project locally by first cloning this repository and `cd` into its main directory.

   ```bash
   # clone the repository
   git clone https://github.com/IanMaguithi/Honeygaindockerlinux.git
   # Navigate to the newly cloned directory
   cd Honeygaindockerlinux
   ```

Then:

1. Create a new virtual environment:
    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/), run `virtualenv venv` and then `source venv/bin/activate`
    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/), run `mkvirtualenv venv`

2. Install the project requirements by running this command on your project terminal:

   ```bash
   pip install -r requirements.txt 
   ```

__Important:__ depending on your system, make sure to use `pip3` and `python3` instead.

## Docker Installation

1. Install and setup Docker using the following [link](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04?__cf_chl_managed_tk__=0q5JO5Q6D5hHeex7hKV5y.YuiSxw3IOqzoA2TcJKtfw-1643460564-0-gaNycGzNDD0) if you do not already have it installed in your machine.

2. All information on how to use Honeygain with Docker can be found in this link [here](https://hub.docker.com/r/honeygain/honeygain).

- Before running the Honeygain Docker Image, get the current copy of ToU by running:

   ```bash
   docker run honeygain/honeygain -tou-get
   ```

## **Running honeygaindoockerlinux**

1. Initialise the script by running the following command:

   ```bash
   python3 initialize.py your_email your_password your_device_name
   ```

2. Find the path to where the project is located. TDo this by running the following command:

   ```bash
   # print working directory
   pwd
   ```

- An example of the output of this command. `/home/user/folder/Honeygaindockerlinux/`

1. Execute the following command to make our script executable:

   ```bash
   chmod +x main.py
   ```

## **Crontab Task Schedule**

1. Setting up a crontab to run on reboot. Open the crontask list by using the following command:

   ```bash
   crontab -e
   ```

- You will be prompted to select an editor to update the cron task with if you have multiple text editors. Choose your preferred option.
In this case however, we'll use the default option Nano.
- Use the following command to set our script to run at every system boot.
@reboot [path to venv] [path to project] I'll use an example to elaborate using the path we had obtained earlier in step 4
and assuming our virtual environment is in the same root folder honey.

   ```bash
   @reboot /home/user/folder/Honeygaindockerlinux/venv/bin/python /home/user/folder/Honeygaindockerlinux/main.py >> ~/cron.log 2>&1
   ```

- '>> ~/cron.log 2>&1' for saving errors into a file in the home directory.
- Checkout this [link](https://phoenixnap.com/kb/crontab-reboot) for further information if you run into errors.
- Finally, save changes by pressing Control + S and exit Nano by pressing Control + X
- Your script is now ready. Shut down your pc and startup, open your terminal and run the following to confirm that your Honeygain docker image is up.

   ```bash
   docker ps
   ```

- After the script has started you should see your new device running on your dashboard.

## Manually executing the script

- You can run the script manually without a crontab task by executing the following command in the project terminal.

   ```bash
   python3 main.py
   ```

## Support

### Do you need help?

If you should encounter any issue, please first [search for similar issues](https://github.com/IanMaguithi/Honeygaindockerlinux/issues) and only if you can't find any, create a new issue.
