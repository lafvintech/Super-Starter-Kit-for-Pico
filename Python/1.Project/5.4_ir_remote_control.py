import time
from machine import Pin, freq
from ir_rx.print_error import print_error
from ir_rx.nec import NEC_8

pin_ir = Pin(17, Pin.IN)

def decodeKeyValue(data):
    if data == 0x52:
        return "0"
    if data == 0x16:
        return "1"
    if data == 0x19:
        return "2"
    if data == 0x0D:
        return "3"
    if data == 0x0C:
        return "4"
    if data == 0x18:
        return "5"
    if data == 0x5E:
        return "6"
    if data == 0x08:
        return "7"
    if data == 0x1C:
        return "8"
    if data == 0x5A:
        return "9"
    if data == 0x42:
        return "*"
    if data == 0x4A:
        return "#"
    if data == 0x46:
        return "UP"
    if data == 0x15:
        return "DOWN"
    if data == 0x40:
        return "OK"
    if data == 0x44:
        return "LEFT"
    if data == 0x43:
        return "RIGHT"
    return "ERROR"

# User callback
def callback(data, addr, ctrl):
    if data < 0:  # NEC protocol sends repeat codes.
        pass
    else:
        print(decodeKeyValue(data))

ir = NEC_8(pin_ir, callback)  # Instantiate receiver
ir.error_function(print_error)  # Show debug information

try:
    while True:
        pass
except KeyboardInterrupt:
    ir.close()
