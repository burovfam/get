import r2r_adc as adc
import time
import adc_plot


voltage_values = []
time_values = []
duration = 3.0

try:
    sensor = adc.R2R_ADC(3.183, compare_time=0.0001, verbose=False)
    
    start_time = time.time()
    
    while (time.time() - start_time) < duration:
        voltage = sensor.get_sc_voltage()
        voltage_values.append(voltage)
        time_values.append(time.time() - start_time)

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, sensor.dynamic_range)

finally:
    sensor.deinit()
