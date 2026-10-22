import r2r_sar_adc as sar_adc
import adc_plot
import time


voltage_values = []
time_values = []
duration = 3.0

adc = None
try:
    adc = sar_adc.R2R_ADC_SAR(3.183, compare_time=0.0001)

    start_time = time.time()

    while (time.time() - start_time) < duration:
        voltage = adc.get_sar_voltage()
        voltage_values.append(voltage)
        time_values.append(time.time() - start_time)

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)

finally:
    if adc is not None:
        adc.deinit()
