import RPi.GPIO as GPIO
import time


class R2R_ADC_SAR:
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

    def number_to_dac(self, number):
        binary = [int(b) for b in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, binary)

    def successive_approximation_adc(self):
        number = 0
        
        for bit in range(7, -1, -1):
            test_number = number | (1 << bit)
            self.number_to_dac(test_number)
            time.sleep(self.compare_time)
            
            if GPIO.input(self.comp_gpio):
                number = test_number
                
        return number

    def get_sar_voltage(self):
        number = self.successive_approximation_adc()
        return number * self.dynamic_range / 255


if __name__ == "__main__":
    adc = None
    try:
        adc = R2R_ADC_SAR(3.183, 0.01, True)
        while True:
            voltage = adc.get_sar_voltage()
            print(f"Напряжение (SAR): {voltage:.3f} В")
            time.sleep(0.5)
    finally:
        if adc is not None:
            adc.deinit()
