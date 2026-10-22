import time

import adc_plot
from r2r_adc import R2R_ADC

# Замените на динамический диапазон вашего ЦАП, измеренный мультиметром
dynamic_range = 3.16

adc = R2R_ADC(dynamic_range)

voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.time()

    while time.time() - start_time < duration:
        voltage_values.append(adc.get_sar_voltage())
        time_values.append(time.time() - start_time)

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
    adc_plot.plot_sampling_period_hist(time_values)

finally:
    adc.deinit()
