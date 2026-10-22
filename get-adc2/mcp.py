import mcp3021_driver as mcp
import adc_plot
import time


voltage_values = []
time_values = []
duration = 3.0

adc = None
try:
    adc = mcp.MCP3021(5.0, False)

    start_time = time.time()

    while (time.time() - start_time) < duration:
        voltage = adc.get_voltage()
        voltage_values.append(voltage)
        time_values.append(time.time() - start_time)

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)

finally:
    if adc is not None:
        adc.deinit()
