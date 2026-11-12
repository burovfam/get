import time
import csv
import RPi.GPIO as GPIO
import mcp3021_driver as mcp
# тест

DYNAMIC_RANGE = 5.0
CHARGE_PIN = 17
FILENAME = "data.csv"

GPIO.setmode(GPIO.BCM)
GPIO.setup(CHARGE_PIN, GPIO.OUT)
adc = mcp.MCP3021(DYNAMIC_RANGE)

try:
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Время[с]", "Напряжение[В]"])
        
        print("Зарядка конденсатора")
        GPIO.output(CHARGE_PIN, 1)
        time.sleep(3)
        
        print("Запись разряда конденсатора")
        GPIO.output(CHARGE_PIN, 0)
        
        start_time = time.time()
        while (time.time() - start_time) < 5.0:
            current_time = time.time() - start_time
            voltage = adc.get_voltage()
            writer.writerow([f"{current_time:.4f}", f"{voltage:.4f}"])
            time.sleep(0.02)

finally:
    GPIO.output(CHARGE_PIN, 0)
    GPIO.cleanup()
    adc.deinit()
    print(f"Записи сохранены в {FILENAME}")
