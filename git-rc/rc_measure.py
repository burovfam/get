import csv
import matplotlib.pyplot as plt

time_values = []
voltage_values = []

with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    
    for row in reader:
        time_values.append(float(row[0]))
        voltage_values.append(float(row[1]))

midpoint = len(time_values) // 2
discharge_times = time_values[midpoint:]
discharge_voltages = voltage_values[midpoint:]

start_time = discharge_times[0]
discharge_times = [t - start_time for t in discharge_times]

plt.figure(figsize=(10, 6), dpi=300)
plt.plot(discharge_times, discharge_voltages, 'b.-', label='Разрядка конденсатора')

start_voltage = discharge_voltages[0]
target_voltage = start_voltage * 0.37
tau_time = 0

for i in range(len(discharge_voltages)):
    if discharge_voltages[i] <= target_voltage:
        tau_time = discharge_times[i]
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
