import socket
import json
import random
import time


HOST = "10.142.145.127"  # The server's hostname or IP address
PORT = 7000  # The port used by the server
# this list includes n, x ,y points
n = 10
coords=[]
for i in range(n*2):
    coords.append(0)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        # delay
        time.sleep(.02)
        for i in range(n*2):
            coord = coords[i]
            delta = random.random()-.5
            coord+= delta
            coords[i] = coord
        string_coordinates = json.dumps(coords)
        binary_string = string_coordinates.encode()
        s.sendall(binary_string)
