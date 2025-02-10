import machine
import utime

x_joystick = machine.ADC(27)
y_joystick = machine.ADC(26)

while True:
    x_value = x_joystick.read_u16()
    y_value = y_joystick.read_u16()

    print('X: %d  Y: %d' % (x_value, y_value))
    utime.sleep_ms(200)