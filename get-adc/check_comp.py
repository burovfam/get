import RPi.GPIO as GPIO
import time

bits = [26, 20, 19, 16, 13, 12, 25, 11]
comp = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(bits, GPIO.OUT, initial=0)
GPIO.setup(comp, GPIO.IN)

try:
    for n in (0, 64, 128, 192, 255):
        GPIO.output(bits, [int(b) for b in bin(n)[2:].zfill(8)])
        time.sleep(0.05)
        print(n, GPIO.input(comp))
finally:
    GPIO.cleanup()
