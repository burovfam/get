
import time
import matplotlib.pyplot as plt

from mcp3021_driver import MCP3021


DYNAMIC_RANGE = 5.0
MEASUREMENT_TIME = 10.0


def main():
    adc = None

    times = []
    voltages = []
    durations = []

    try:
        adc = MCP3021(DYNAMIC_RANGE)

        start_time = time.perf_counter()

        while time.perf_counter() - start_time < MEASUREMENT_TIME:
            measurement_start = time.perf_counter()

            voltage = adc.get_voltage()

            measurement_end = time.perf_counter()

            times.append(measurement_end - start_time)
            voltages.append(voltage)
            durations.append(
                (measurement_end - measurement_start) * 1000
            )

            print(f"Напряжение: {voltage:.3f} В")

    except KeyboardInterrupt:
        print("\nИзмерения остановлены.")

    except OSError as error:
        print(f"Ошибка чтения АЦП: {error}")

    finally:
        if adc is not None:
            adc.deinit()

    if not durations:
        print("Нет данных для построения графиков.")
        return

    # График напряжения от времени
    plt.figure(figsize=(10, 5))
    plt.plot(times, voltages, "b.-")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.title("Напряжение на входе MCP3021")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("10-bit-i2c-adc-plot.png", dpi=150)

    # Гистограмма продолжительности измерений
    plt.figure(figsize=(10, 5))
    plt.hist(durations, bins="auto", edgecolor="black")
    plt.xlabel("Продолжительность измерения, мс")
    plt.ylabel("Количество измерений")
    plt.title("Распределение продолжительности измерений")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig("10-bit-i2c-adc-hist.png", dpi=150)

    print(f"\nВсего измерений: {len(durations)}")
    print(
        f"Средняя продолжительность: "
        f"{sum(durations) / len(durations):.3f} мс"
    )

    plt.show()


if __name__ == "__main__":
    main()
