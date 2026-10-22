import RPi.GPIO as GPIO
import time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def __del__(self):
        # «Деструктор»: выставляет 0 на выход ЦАП и очищает настройки GPIO
        self.deinit()

    def number_to_dac(self, number):
        # Старший разряд первым, как в списке bits_gpio
        bits = [int(bit) for bit in bin(number)[2:].zfill(len(self.bits_gpio))]
        GPIO.output(self.bits_gpio, bits)

    def sequential_counting_adc(self):
        max_number = 2 ** len(self.bits_gpio) - 1

        for number in range(max_number + 1):
            self.number_to_dac(number)
            time.sleep(self.compare_time)

            # Компаратор выдаёт 0, когда напряжение ЦАП превысило входное
            if GPIO.input(self.comp_gpio) == 1:
                if self.verbose:
                    print(f"Компаратор сработал на числе {number}")
                return number

        # Напряжение ЦАП так и не превысило входное
        return max_number

    def get_sc_voltage(self):
        number = self.sequential_counting_adc()
        max_number = 2 ** len(self.bits_gpio) - 1
        voltage = number / max_number * self.dynamic_range

        if self.verbose:
            print(f"Число на ЦАП: {number}, напряжение: {voltage:.3f} В")

        return voltage


if __name__ == "__main__":
    try:
        
        adc = R2R_ADC(3.183)

        while True:
            voltage = adc.get_sc_voltage()
            print(f"Измеренное напряжение: {voltage:.3f} В")

    finally:
        adc.deinit()
