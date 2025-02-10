import machine
import time

# Global variables initialization
timeStart = 0
count = 0
count_flag = False
last_interrupt_time = 0
DEBOUNCE_TIME = 200  # Debounce time in milliseconds

# 7-segment display codes for digits 0-9 (hex values)
SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

# Pin definitions for 74HC595 shift register
sdi = machine.Pin(18, machine.Pin.OUT)   # Serial Data Input
rclk = machine.Pin(19, machine.Pin.OUT)  # Register Clock (Latch)
srclk = machine.Pin(20, machine.Pin.OUT) # Shift Register Clock

# Initialize 4-digit display control pins
placePin = []
pin = [10,13,12,11]  # Pin numbers for common anodes
for i in range(4):
    placePin.append(machine.Pin(pin[i], machine.Pin.OUT))

def pickDigit(digit):
    """Select which digit to display (0-3)"""
    for i in range(4):
        placePin[i].value(1)  # Turn off all digits
    placePin[digit].value(0)  # Turn on selected digit

def clearDisplay():
    """Clear the display"""
    hc595_shift(0x00)

def hc595_shift(dat):
    """Send data to 74HC595 shift register"""
    rclk.low()
    time.sleep_us(200)
    for bit in range(7, -1, -1):
        srclk.low()
        time.sleep_us(200)
        value = 1 & (dat >> bit)
        sdi.value(value)
        time.sleep_us(200)
        srclk.high()
        time.sleep_us(200)
    time.sleep_us(200)
    rclk.high()

def display(num):
    """Display a number (0-9999) on the 4-digit display
    Format: XX.XX (seconds.centiseconds)"""
    # Units digit (centiseconds)
    pickDigit(0)
    hc595_shift(SEGCODE[num % 10])

    # Tens digit (centiseconds)
    pickDigit(1)
    hc595_shift(SEGCODE[num % 100 // 10])

    # Hundreds digit (seconds) with decimal point
    pickDigit(2)
    hc595_shift(SEGCODE[num % 1000 // 100] + 0x80)

    # Thousands digit (tens of seconds)
    pickDigit(3)
    hc595_shift(SEGCODE[num % 10000 // 1000])

# Initialize tilt switch
tilt_switch = machine.Pin(16, machine.Pin.IN)

def shake(pin):
    """Interrupt handler for tilt switch with debounce"""
    global timeStart, count_flag, last_interrupt_time
    current_time = time.ticks_ms()
    
    # Debounce check
    if time.ticks_diff(current_time, last_interrupt_time) < DEBOUNCE_TIME:
        return
    
    last_interrupt_time = current_time
    
    if not count_flag:
        timeStart = current_time  # Start timing
        count_flag = True
    else:
        count_flag = False  # Stop timing

# Set up tilt switch interrupt
tilt_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=shake)

# Main loop
while True:
    if count_flag:
        # Calculate elapsed time in centiseconds
        elapsed = time.ticks_diff(time.ticks_ms(), timeStart)
        count = int(elapsed / 10)
        # Prevent overflow
        if count > 9999:
            count = 9999
    display(count)
    time.sleep_ms(1)  # Small delay to reduce CPU load