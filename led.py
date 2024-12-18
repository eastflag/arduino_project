from Arduino import Arduino
import time

board = Arduino("9600", port="COM5")  # plugged in via USB, serial com at rate 115200
board.pinMode(5, "OUTPUT")

while True:
    board.digitalWrite(5, "LOW")
    time.sleep(1)
    board.digitalWrite(5, "HIGH")
    time.sleep(1)