import csv
import matplotlib.pyplot as plt

times, voltages = [], []
with open("data.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # пропускаем заголовок
    for row in reader:
        times.append(float(row[0]))
        voltages.append(float(row[1]))

plt.figure(figsize=(10, 6))
plt.plot(times, voltages)
plt.title("Зарядка и разрядка конденсатора в RC-цепи")
plt.xlabel("Время, с")
plt.ylabel("Напряжение, В")
plt.grid(True)
plt.savefig("rc-plot.png", dpi=300)
