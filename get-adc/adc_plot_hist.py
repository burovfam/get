import matplotlib.pyplot as plt


def plot_sampling_period_hist(time):
    sampling_periods = []
    for i in range(1, len(time)):
        sampling_periods.append(time[i] - time[i - 1])

    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods)
    
    plt.title("Распределение периодов дискретизации")
    plt.xlabel("Период, с")
    plt.ylabel("Количество измерений")
    
    plt.xlim(0, 0.06)
    plt.grid(True)
    plt.show()
