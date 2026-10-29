import time

import adc_plot
from r2r_adc import R2R_ADC


dynamic_range = 3.183

adc = R2R_ADC(dynamic_range, compare_time=0.0001)

voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.time()

    while time.time() - start_time < duration:
        voltage_values.append(adc.get_sc_voltage())
        time_values.append(time.time() - start_time)

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range)

finally:
    adc.deinit()

