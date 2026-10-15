import RPi.GPIO as GPIO
import time

bits = [26, 20, 19, 16, 13, 12, 25, 11]
comp = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(bits, GPIO.OUT, initial=0)
GPIO.setup(comp, GPIO.IN)

def set_dac(number):
    binary = [int(b) for b in bin(number)[2:].zfill(8)]
    GPIO.output(bits, binary)

try:
    while True:
        num = int(input("Введите число 0–255: "))
        set_dac(num)
        time.sleep(0.1)
        state = GPIO.input(comp)
        print(f"ЦАП = {num}, компаратор = {state}")
        print(f"Напряжение на ЦАП ≈ {num * 3.183 / 255:.3f} В")
        print()
finally:
    GPIO.output(bits, 0)
    GPIO.cleanup()
