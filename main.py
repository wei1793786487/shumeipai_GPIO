from datetime import datetime

import RPi.GPIO as GPIO

def doit(second):
    start_now = datetime.now()
    zhuan=True
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 50)  # PWM
    while zhuan:
      now = datetime.now()
      pwm.start(11)
      if((now-start_now).seconds==second):
       zhuan=False
