import mcp4725_driver as mcp
import translate_generator as tg
import time


amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000

dac = None
try:
    dac = mcp.MCP4725(5.0, 0x61, True)

    t = 0.0
    while True:
        voltage = amplitude * tg.get_triangle_wave_amplitude(signal_frequency, t)
        dac.set_voltage(voltage)
        tg.wait_for_sampling_period(sampling_frequency)
        t += 1.0 / sampling_frequency

finally:
    if dac is not None:
        dac.deinit()
