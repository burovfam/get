import matplotlib.pyplot as plt


def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    
    # Рисуем график
    plt.plot(time, voltage, color='blue', linewidth=1)
    
    # Названия осей
    plt.title("Напряжение с АЦП (Бинарный поиск / SAR)")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    
    # Границы осей
    if time:
        plt.xlim(0, max(time))
    plt.ylim(0, max_voltage)
    
    # Сетка и отображение
    plt.grid(True)
    plt.show()
