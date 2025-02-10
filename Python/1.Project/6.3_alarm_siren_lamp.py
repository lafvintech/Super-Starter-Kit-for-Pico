import machine
import time

# Initialize PWM for the buzzer (pin 15) and LED (pin 16)
buzzer = machine.PWM(machine.Pin(15))  # PWM for buzzer
led = machine.PWM(machine.Pin(16))  # PWM for LED
led.freq(1000)  # Set LED PWM frequency to 1kHz

# Initialize the slide switch (pin 17) as an input pin
switch = machine.Pin(17, machine.Pin.IN)

# Global variable to control whether the bell effect is running
bell_flag = False

# Function: Stop the buzzer
def noTone(pin):
    pin.duty_u16(0)  # Set PWM duty cycle to 0 to stop sound

# Function: Play a tone at a specified frequency
def tone(pin, frequency):
    pin.freq(frequency)  # Set buzzer frequency
    pin.duty_u16(30000)  # Set duty cycle to approximately 50% (30000/65535)

# Function: Map a value from one range to another
def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Function: Simulate the bell effect
def bell_effect():
    while bell_flag:  # Continue running as long as bell_flag is True
        for i in range(0, 400, 2):  # Loop from 0 to 100 in steps of 2
            if not bell_flag:  # If bell_flag becomes False, exit immediately
                break
            # Map i to LED brightness and buzzer frequency
            led.duty_u16(int(interval_mapping(i, 0, 100, 0, 65535)))  # LED brightness
            tone(buzzer, int(interval_mapping(i, 0, 100, 130, 800)))  # Buzzer frequency
            time.sleep_ms(10)  # Short delay for smooth transition
    # When bell_flag is False, turn off the buzzer and LED
    noTone(buzzer)
    led.duty_u16(0)

# Interrupt handler: Toggle the bell_flag state
def toggle(pin):
    global bell_flag
    bell_flag = pin.value()  # Set bell_flag based on the switch state
    print("bell_flag:", bell_flag)  # Print bell_flag state for debugging

# Set up interrupt to detect both rising and falling edges of the switch
switch.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=toggle)

# Main loop
while True:
    if bell_flag:
        bell_effect()  # If bell_flag is True, start the bell effect
    else:
        noTone(buzzer)  # If bell_flag is False, stop the buzzer
        led.duty_u16(0)  # Turn off the LED  