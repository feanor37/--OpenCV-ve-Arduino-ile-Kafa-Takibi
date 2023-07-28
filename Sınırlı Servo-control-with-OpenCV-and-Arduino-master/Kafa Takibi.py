import cv2
import numpy as np
import serial
import struct
import time

a = 0
b = 0
-----------------------------------------------------


Lütfen Kodların Tamamı için İletişime Geçin

https://www.linkedin.com/in/nuh-kaan-gun-59172b248/

  ----------------------------------------------------



    try:
        for (x1, y1, w1, h1) in face:
            a = int((2 * x1 + w1) / 2)
            b = int((2 * y1 + h1) / 2)
            x = int(a / 3.66)
            y = int(b / 2.55)
            ser.write(struct.pack('>BB', x, y))
            cv2.rectangle(kaan, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)

    except:
        pass

    cv2.imshow('kaan', kaan)
    k = cv2.waitKey(20) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
