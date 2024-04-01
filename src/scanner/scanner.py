import cv2
import time
from pyzbar.pyzbar import decode


def barcode_scanner():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 680)

    camera = True
    code_detected = False
    window_name = 'ReagentFlow QR scan'
    start_time = time.time()
    result = None

    while camera == True:
        success, frame = cap.read()
        for code in decode(frame):
            result = code.data.decode('utf-8')
            code_detected = True

            if time.time() - start_time > 30000000:
                print("Function has been running for more than 30 seconds without a result.")
                break

        cv2.imshow(window_name, frame)

        if code_detected == True:
            break

        if time.time() - start_time > 30:
            print("Function has been running for more than 30 seconds without a result.")
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cv2.imshow(window_name, frame)

    cv2.destroyWindow(window_name)
    return result
