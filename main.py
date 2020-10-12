import RPi.GPIO as GPIO
pwm=None

def init():
 global pwm
 GPIO.setmode(GPIO.BCM)
 GPIO.setwarnings(False)
 GPIO.setup(18, GPIO.OUT)
 pwm = GPIO.PWM(18, 50)  # PWM

def start():
  global  pwm
  if pwm==None:
   init()
  while True:
   if(pwm!=None):
    pwm.start(11)
   else:
       break

def stop():
  global pwm
  pwm.stop()
  pwm=None