import pwm_dac as pwm
import translate_generator as tg
import time
amplitude = 1.5
signal_frequency = 10
sampling_frequency = 1000

dac = None
try:
    dac = pwm.PWM_DAC(12, 500, 3.183, True)

    t = 0.0

    while True:
        voltage = amplitude * tg.get_triangle_wave_amplitude(signal_frequency, t)
        dac.set_voltage(voltage)
        tg.wait_for_sampling_period(sampling_frequency)
        t += 1.0 / sampling_frequency

finally:
    if dac is not None:
        dac.deinit()

