from picamera import PiCamera
from gpiozero import Servo
from time import sleep

servoOne = Servo(22)
servoTwo = Servo(27)

servoOne.mid()
servoTwo.mid()

camera = PiCamera()
camera.start_preview()
sleep(0.5)
camera.capture('picture.jpg')
camera.stop_preview()
