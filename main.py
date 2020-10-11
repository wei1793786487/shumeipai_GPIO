import RPi.GPIO as GPIO
pwm=None
isDown=True

def init():
 global pwm
 GPIO.setmode(GPIO.BCM)
 GPIO.setwarnings(False)
 GPIO.setup(18, GPIO.OUT)
 pwm = GPIO.PWM(18, 50)  # PWM

def start():
  global  pwm
  global isDown
  if pwm==None:
   init()
  while isDown:
   if(pwm!=None):
    pwm.start(11)


def stop():
  global pwm
  global isDown
  isDown=False
  pwm.stop()
  pwm=None