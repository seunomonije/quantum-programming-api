import socket
import select
import errno
import pickle
import sys

HEADERSIZE = 10
IP_ADDRESS = "localhost"
PORT = 1212

class InputData:
    def __init__(self, xVal, yVal):
        self.xVal = xVal
        self.yVal = yVal
        
        
xVal = float(input("input x:"))
yVal = float(input("input y:"))

data = InputData(xVal, yVal)

# Connection starting
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP_ADDRESS, PORT))

data_to_send = pickle.dumps(data)
"""Need to revisit this line later, headers are good"""
#data_to_send = bytes(f'{len(data_to_send):<{HEADERSIZE}}', "UTF-8") + data_to_send
client.send(data_to_send)
