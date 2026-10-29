
import smbus2


class MCP3021:
    def __init__(self, dynamic_range, verbose=False):
        self.bus = smbus2.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

    def get_number(self):
        message = smbus2.i2c_msg.read(self.address, 2)
        self.bus.i2c_rdwr(message)

        data = list(message)

        upper_data_byte = data[0]
        lower_data_byte = data[1]

        number = (
            ((upper_data_byte & 0x0F) << 6)
            | (lower_data_byte >> 2)
        )

        if self.verbose:
            print(
                f"Принятые данные: {data}, "
                f"Старший байт: {upper_data_byte:02x}, "
                f"Младший байт: {lower_data_byte:02x}, "
                f"Число: {number}"
            )

        return number

    def get_voltage(self):
        number = self.get_number()
        return number * self.dynamic_range / 1024


if __name__ == "__main__":
    import time

    adc = None

    try:
        adc = MCP3021(5.0, verbose=True)

        while True:
            voltage = adc.get_voltage()
            print(f"Напряжение: {voltage:.3f} В")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nИзмерения остановлены.")

    except OSError as error:
        print(f"Ошибка чтения АЦП: {error}")

    finally:
        if adc is not None:
            adc.deinit()
