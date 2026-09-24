import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16, 20, 21, 25, 26, 17, 27, 22]
for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, 0)

def fecimal2binary(value):
    return GPIO.output(leds, [int(bit) for bit in bin(value)[2:].zfill(8)])

num = 3.3

def voltage_to_number(voltage):
    if not(0.0 <= voltage <= num):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {num:.2f} В")
        return 0
    return int(voltage / num * 255)

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            fecimal2binary(number)
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")
finally:
    GPIO.output(leds,0)
    GPIO.clenup()