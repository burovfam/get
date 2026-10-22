import matplotlib.pyplot as plt


def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)

    plt.title("Зависимость напряжения от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")

    plt.xlim(0, max(time))
    plt.ylim(0, max_voltage)

    plt.grid(True)
    plt.show()


def plot_sampling_period_hist(time):
    # Продолжительность каждого измерения — разница соседних моментов времени
    sampling_periods = [time[i + 1] - time[i] for i in range(len(time) - 1)]

    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods, bins=20)

    plt.title("Распределение периодов измерения на одно измерение")
    plt.xlabel("Период измерения, с")
    plt.ylabel("Количество измерений")

    plt.grid(True)
    plt.show()
