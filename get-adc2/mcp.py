import time
import matplotlib.pyplot as plt

from mcp3021_driver import MCP3021


DYNAMIC_RANGE = 5.0
MEASUREMENT_TIME = 10.0


def main():
    adc = None
    times = []
    voltages = []

    try:
        adc = MCP3021(DYNAMIC_RANGE)
        start_time = time.perf_counter()

        while time.perf_counter() - start_time < MEASUREMENT_TIME:
            voltage = adc.get_voltage()

            times.append(time.perf_counter() - start_time)
            voltages.append(voltage)

            print(f"Напряжение: {voltage:.3f} В")

    except KeyboardInterrupt:
        print("\nИзмерения остановлены.")

    except OSError as error:
        print(f"Ошибка чтения АЦП: {error}")

    finally:
        if adc is not None:
            adc.deinit()

    if not voltages:
        print("Нет данных для построения графиков.")
        return

    # --- ГРАФИК НАПРЯЖЕНИЯ (остается как был) ---
    fig1 = plt.figure(figsize=(10, 5))
    plt.plot(times, voltages, "b.-")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.title("Напряжение на входе MCP3021")
    plt.grid(True)
    plt.tight_layout()
    fig1.savefig("10-bit-i2c-adc-plot.png", dpi=150)

    # --- ГИСТОГРАММА (как в примере через разницу соседних измерений) ---
    sampling_periods = []
    for i in range(1, len(times)):
        diff = times[i] - times[i - 1]
        sampling_periods.append(diff)

    fig2 = plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods)
    plt.title("Распределение периодов дискретизации")
    plt.xlabel("Период, с")
    plt.ylabel("Количество измерений")
    plt.xlim(0, 0.06)  # Как в твоем примере
    plt.grid(True)
    plt.tight_layout()
    fig2.savefig("10-bit-i2c-adc-hist.png", dpi=150)

    print(f"Количество измерений: {len(voltages)}")
    plt.show()


if __name__ == "__main__":
    main()
