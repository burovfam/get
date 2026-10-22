import time

import adc_plot
from r2r_adc import R2R_ADC

dynamic_range = 3.16  # замените на своё значение

adc = R2R_ADC(dynamic_range)

time_values = []
duration = 3.0

try:
    start_time = time.time()

    while time.time() - start_time < duration:
        adc.get_sar_voltage()
        time_values.append(time.time() - start_time)

    adc_plot.plot_sampling_period_hist(time_values)

finally:
    adc.deinit()
