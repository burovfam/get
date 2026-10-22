import r2r_sar_adc as sar_adc
import adc_plot_sar as plotter
import time

voltage_values = []
time_values = []
duration = 3.0

adc = None
try:
    # Создаем объект SAR-АЦП
    adc = sar_adc.R2R_ADC_SAR(3.183, compare_time=0.001)

    start_time = time.time()

    # Цикл измерений в течение 3 секунд
    while (time.time() - start_time) < duration:
        voltage = adc.get_sar_voltage()
        voltage_values.append(voltage)
        time_values.append(time.time() - start_time)

    # Вывод в консоль для проверки, что данные собрались
    print(f"Успешно собрано точек: {len(voltage_values)}")
    
    # Вызов графика из нового модуля
    if len(voltage_values) > 0:
        plotter.plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)
    else:
        print("Ошибка: список напряжений пуст!")

finally:
    if adc is not None:
        adc.deinit()
