import pwm_dac as pwm
import signal_generator as sg
import time


amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000

dac = None
try:
    dac = pwm.PWM_DAC(12, 500, 3.290, True)

    t = 0.0
    while True:
        voltage = amplitude * sg.get_sin_wave_amplitude(signal_frequency, t)
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
        t += 1.0 / sampling_frequency

finally:
    if dac is not None:
        dac.deinit()
