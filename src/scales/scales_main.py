import serial
import struct
import src.constants as cnst


def decode_scale_data(hex_string):
    # Convert the hex string to bytes
    byte_data = bytes.fromhex(hex_string)

    # Assuming little-endian format
    # The 'H' format code indicates an unsigned short (2 bytes)
    value = struct.unpack('<H', byte_data[2:4])[0]

    return value


def getting_weight():
    ser = serial.Serial(cnst.SCALES_PORT, 9600, timeout=1)
    s = ser.readline()
    while s == b'':
        s = ser.readline()
    data = '55'
    l = int(len(s) / 2)
    s = s[1:l]
    for i in s:
        t = len(hex(i)[2:])
        if t != 2:
            data += '0' + hex(i)[2:]
        else:
            data += hex(i)[2:]

    value_1 = decode_scale_data(data)
    print(f"Decoded Value: {value_1} grams")
    ser.close()
    return value_1
