from machine import Pin, PWM
import time

BeepPin = 15
ALedPin = 14

MORSECODE = {
    'A': '01', 'B': '1000', 'C': '1010', 'D': '100', 'E': '0', 'F': '0010', 'G': '110',
    'H': '0000', 'I': '00', 'J': '0111', 'K': '101', 'L': '0100', 'M': '11', 'N': '10',
    'O': '111', 'P': '0110', 'Q': '1101', 'R': '010', 'S': '000', 'T': '1',
    'U': '001', 'V': '0001', 'W': '011', 'X': '1001', 'Y': '1011', 'Z': '1100',
    '1': '01111', '2': '00111', '3': '00011', '4': '00001', '5': '00000',
    '6': '10000', '7': '11000', '8': '11100', '9': '11110', '0': '11111',
    '?': '001100', '/': '10010', ',': '110011', '.': '010101', ';': '101010',
    '!': '101011', '@': '011010', ':': '111000',
}

def setup():
    global beep_pwm, led
    beep_pwm = PWM(Pin(BeepPin))
    beep_pwm.freq(1000)  # Set frequency to 1kHz
    led = Pin(ALedPin, Pin.OUT)

def on():
    beep_pwm.duty_u16(32768)  # 50% duty cycle
    led.value(1)

def off():
    beep_pwm.duty_u16(0)
    led.value(0)

def beep(dt):  # dt for delay time.
    on()
    time.sleep(dt)
    off()
    time.sleep(dt)

def morsecode(code):
    pause = 0.25
    for letter in code:
        for tap in MORSECODE.get(letter, ''):
            if tap == '0':
                beep(pause / 2)
            if tap == '1':
                beep(pause)
        time.sleep(pause)

def main():
    while True:
        code = input("Please input the message: ")
        code = code.upper()
        print(code)
        morsecode(code)

def destroy():
    print("")
    off()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
