import RPi.GPIO as GPIO
import adc_plot
import mcp3021_driver as mcp
import time

CHARGE_PIN = 17
CHARGED_V = 4.7     # считаем конденсатор заряженным
DISCHARGED_V = 0.1  # считаем конденсатор разряженным
TIMEOUT = 60        # защита от бесконечного цикла, с

if __name__ == "__main__":
    adc = None
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(CHARGE_PIN, GPIO.OUT, initial=0)

    voltage_values = []
    time_values = []
    charging = True

    try:
        adc = mcp.MCP3021(5.19)

        GPIO.output(CHARGE_PIN, 1)
        start_time = time.time()

        while time.time() - start_time < TIMEOUT:
            t = time.time() - start_time
            v = adc.get_voltage()
            time_values.append(t)
            voltage_values.append(v)
            print(v)

            if charging and v > CHARGED_V:
                charging = False
                GPIO.output(CHARGE_PIN, 0)
            elif not charging and v < DISCHARGED_V:
                break

        adc_plot.plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)

    finally:
        GPIO.output(CHARGE_PIN, 0)
        if adc is not None:
            adc.deinit()
        GPIO.cleanup()
