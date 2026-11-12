import csv
import matplotlib.pyplot as plt

time_values = []
voltage_values = []


with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок "Время[с], Напряжение[В]"
    
    for row in reader:
        time_values.append(float(row[0]))
        voltage_values.append(float(row[1]))


plt.figure(figsize=(10, 6), dpi=300)
plt.plot(time_values, voltage_values, 'b.-', label='Напряжение на конденсаторе')


if voltage_values:
    start_voltage = voltage_values[0]
    target_voltage = start_voltage * 0.37
    tau_time = 0

    for i in range(len(voltage_values)):
        if voltage_values[i] <= target_voltage:
            tau_time = time_values[i]
            break

  
    if tau_time > 0:
        plt.axvline(x=tau_time, color='red', linestyle='--', label=f'τ ≈ {tau_time:.3f} с')
        plt.axhline(y=target_voltage, color='green', linestyle=':', label='37% от начального')


plt.title("Зависимость напряжения на конденсаторе от времени при разряде", fontsize=14)
plt.xlabel("Время, с", fontsize=12)
plt.ylabel("Напряжение, В", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()


plt.savefig('rc-plot.png', dpi=300)
print(f"График сохранен в файл rc-plot.png. Постоянная времени τ = {tau_time:.3f} с.")
