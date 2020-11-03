import subprocess
import time

from gpiozero import OutputDevice


on_start = 75  #the fan will turn on at this temp
off_start = 45  #the fan will shut off at this temp
sleep_interval = 5  
gpio_pin = 'the pin for wich you use to plug in said pi to control fan, other than power'  

def get_temp():

    output = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True)
    temp_str = output.stdout.decode()
    try:
        return float(temp_str.split('=')[1].split('\'')[0])
    except (IndexError, ValueError):
        raise RuntimeError(' ')


if __name__ == '__main__':
    
    if off_start >= on_start:
        raise RuntimeError(' ')

    fan = OutputDevice(gpio_pin)

    while True:
        temp = get_temp()

        if temp > on_start and not fan.value:
            fan.on()

        elif fan.value and temp < on_start:
            fan.off()

        time.sleep(sleep_interval)
