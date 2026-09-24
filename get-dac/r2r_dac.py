import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        if not (0 <= number <= 255):
            print(f"Число {number} вне диапазона 0-255. Установим 0.")
            number = 0
        binary = [int(b) for b in bin(number)[2:].zfill(8)]
        GPIO.output(self.gpio_bits, binary)
        
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print("Напряжение выходит за дин. диапазон ЦАП")
            print("Установим 0.0")
            self.set_number(0)
            return 
        number = int(voltage / self.dynamic_range * 255)
        self.set_number(number)


if __name__ == "__main__":
    dac= None
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")

    finally: 
        if dac is not None:
            dac.deinit()
