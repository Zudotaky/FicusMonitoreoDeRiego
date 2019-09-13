
from pyfirmata import Arduino
import time

board = Arduino("/dev/ttyACM0")

print(board)
for x in range(10):
    print(board.taken)