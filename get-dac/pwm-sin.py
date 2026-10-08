import RPi.GPIO as GPIO
import signal_generator as sg
import time


amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000

pwm_pin = 12
pwm_frequency = 500
dynamic_range = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, pwm_frequency)
pwm.start(0)

try:
    t = 0.0
    while True:
        # Нормализованный синус 0..1
        value = sg.get_sin_wave_amplitude(signal_frequency, t)
        # Напряжение 0..dynamic_range
        voltage = value * amplitude
        # Переводим в duty 0..100%
        duty = voltage / dynamic_range * 100.0
        if duty > 100.0:
            duty = 100.0
        pwm.ChangeDutyCycle(duty)
        sg.wait_for_sampling_period(sampling_frequency)
        t += 1.0 / sampling_frequency

finally:
    pwm.stop()
    GPIO.cleanup()
