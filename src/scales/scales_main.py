import serial
import struct


def decode_scale_data(hex_string):
    # Convert the hex string to bytes
    byte_data = bytes.fromhex(hex_string)

    # Assuming little-endian format
    # The 'H' format code indicates an unsigned short (2 bytes)
    value = struct.unpack('<H', byte_data[2:4])[0]

    return value


def getting_weight():
    #ser = serial.Serial('/dev/cu.usbmodem00000000001A1', 9600, timeout=1)
    ser = serial.Serial('COM3', 9600, timeout=1)
    s = ser.readline()
    while s == b'':
        s = ser.readline()
    # print(s)
    data = '55'
    l = int(len(s) / 2)
    s = s[1:l]
    # print(s)
    for i in s:
        t = len(hex(i)[2:])
        if t != 2:
            data += '0' + hex(i)[2:]
        else:
            data += hex(i)[2:]

    # print(data)
    value_1 = decode_scale_data(data)
    print(f"Decoded Value: {value_1} grams")
    ser.close()
    return value_1
