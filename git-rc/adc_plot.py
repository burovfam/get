import matplotlib.pyplot as plt
import r2r_adc
import time

def plot_voltage_vs_time(time, voltage, max_voltage):

    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.title("График зависимости напряжения на входе АЦП от времени")
    plt.grid()
    plt.ylim(0, max_voltage + 0.5)
    plt.savefig("graph.png")
    plt.show()

def plot_sampling_period_hist(time_values):
    sampling_periods = []
    for i in range(len(time_values)-2):
        sampling_periods.append(time_values[i+1] - time_values[i])

    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods)
    plt.xlim(0, 0.06)
    plt.grid()
    plt.xlabel("Период измерения, с")
    plt.ylabel("Количество измерений")
    plt.title("Распределение периодов дискретизации измерений по времени на одно измерение")
    plt.hist(sampling_periods)

    plt.show()
