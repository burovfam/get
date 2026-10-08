import r2r_dac as r2r
import translate_generator as tg
import time


amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000

dac = None
try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183)

    t = 0.0
    while True:
        voltage = amplitude * tg.get_triangle_wave_amplitude(signal_frequency, t)
        dac.set_voltage(voltage)
        tg.wait_for_sampling_period(sampling_frequency)
        t += 1.0 / sampling_frequency

finally:
    if dac is not None:
        dac.deinit()
