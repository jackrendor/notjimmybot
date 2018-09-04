# !JimmyBot - Telegram bot

### What?

This bot is a fork of [kipters bot](https://github.com/kipters/jimmybot), but written in Python 3

### Configure

The bot runs correctly on _Linux_ system,
but first we need to configure it.

We need first to install *python 3* and some *packages*, then we
need to get Bot's Token and set them in the file *config.py*.

0. Installing _Python 3_ and _Virtual Environment_:
    * CentOS, RedHat, Fedora:
        ```sh
        dnf install python3 python3-pip python3-virtualenv
        ```
    * Debian, Ubuntu:
        ```sh
        apt install python3 python3-pip virtualenv
        ```
1. Create a Virtual Environment:

    ```sh
     virtualenv -p python3 venv
     ```
2. Activate the Virtual Environment:

   ```sh
   source venv/bin/activate
   ```

3. Install requirements:

    ```sh
    pip3 install -r requirements.txt
    ```

4. Get TelegramBot token:
    Go to [Telegram Bots](https://core.telegram.org/bots#creating-a-new-bot) and follow the instructions: "Creating a new bot"

5. Edit configuration:
    ```sh
    nano config.py
    ```
6. Run that damn bot!
    ```sh
    sh start.sh
    ```

