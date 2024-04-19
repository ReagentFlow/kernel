SCALES_PORT = '/dev/ttyACM0'
KEY = 'private.json'
COLLECTION = 'containers'
SCANNER_PORT = '/dev/tty.usbmodemS_N_G21AD97581'

# macbook pro egor scanner port /dev/tty.usbmodemS_N_G21AD97581
# run port.py to find port for SCALES and SCANNER
# or use python -m serial.tools.list_ports


# start code:
# python3 -m venv venv
# source venv/bin/activate
# pip3 install -r requirements.txt
#
# PYTHONPATH=. python src/main.py
