SCALES_PORT = 'COM3'
KEY = 'private.json'
COLLECTION = 'containers'
SCANNER_PORT = '/dev/tty.usbmodemS_N_G21AD97581'

# video port for macbook pro 2017 /dev/cu.usbmodem00000000001A1
# run port.py to find port for SCALES and SCANNER
# or use python -m serial.tools.list_ports


# start code:
# python3 -m venv venv
# source venv/bin/activate
# pip3 install -r requirements.txt
#
# PYTHONPATH=. python src/main.py
