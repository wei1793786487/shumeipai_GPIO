import threading

import RPi.GPIO as GPIO
pwm=None
IsDo=True
def init():
 print("新建")
 global pwm
 GPIO.setmode(GPIO.BCM)
 GPIO.setwarnings(False)
 GPIO.setup(18, GPIO.OUT)
 pwm = GPIO.PWM(18, 50)  # PWM

def start():
  global  pwm
  global IsDo
  if pwm==None:
   init()
  while IsDo:
   print("==============")
   print(pwm!=None)
   print("==============")
   if(pwm!=None):
     print(pwm)
     pwm.start(11)
   else:
       break

def stop():
    global IsDo
    global pwm
    if (pwm != False):
        IsDo = False
        pwm=None
        GPIO.cleanup(18)


def dodod():
    zhuan=True
    zhuan111=100000
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 50)  # PWM
    while zhuan:
      print(zhuan111)
      pwm.start(11)
      zhuan111=zhuan111-1
      if(zhuan111==0):
          zhuan=False