import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio, [int(element) for element in bin(number)[2:].zfill(8)])
    
    def sequential_counting_adc(self):
        for n in range(0, 256):
            self.number_to_dac(n)
            time.sleep(self.compare_time)
            if (GPIO.input(self.comp_gpio) == 1):
                return n-1
        return 255
    
    def get_sc_voltage(self):
        return self.sequential_counting_adc() * self.dynamic_range / 255

    def successive_approximation_adc(self):
        
        result = 0
        
        for bit in range(7, -1, -1):

            result |= (1 << bit)

            self.number_to_dac(result)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:
                result &= ~(1 << bit)
        
        return result
    
    def get_sar_voltage(self):
        return self.successive_approximation_adc() * self.dynamic_range / 255


if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.20)
        while True:
            print(f'{adc.get_sar_voltage():.2f}')

    finally:
        adc.deinit()
