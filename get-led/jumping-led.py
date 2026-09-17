import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
counter = 8
leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
light_time = 0.2
for led in leds:
    GPIO.output(led, 1)
    time.sleep(light_time)
    GPIO.output(led, 0)
led_obr = leds[::-1]
for led in led_obr:
    GPIO.output(led, 1)
    time.sleep(light_time)
    GPIO.output(led, 0)
