import requests
import subprocess
from time import sleep

from flask import Flask
from gpiozero import Button, LED

app = Flask(__name__)
button = Button(2)
led = LED(17)

@app.route('/ping')
def ping():
    led.on()
    sleep(1)
    led.off()
    return 'success'

while True:
    button.wait_for_press()
    requests.get('http://127.0.0.1:5000/ping')
