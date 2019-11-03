try:
    from picamera import PiCamera
except:
    print("fail load camera")
from gpiozero import Servo
from time import sleep

servoOne = Servo(22)
servoTwo = Servo(27)

while True:
    value = input()
    print(value)
    servoOne.value = value
servoTwo.min()

camera = PiCamera()
camera.start_preview()
sleep(0.5)
camera.capture('picture.jpg')
camera.stop_preview()
