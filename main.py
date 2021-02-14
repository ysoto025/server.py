# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import socket
import sys
import argparse
from sys import argv
import time


class assignment2:

    age = 0
    name = ""
    list = []
    modString = ""
    host = ""

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)

# Task 1 (Constructor)

   #def __init__(self, age = 0):
    #    self.age = age

#Task 7

    def connectTcp2(self):

        #self.sock.settimeout(10)

        if len(argv) < 3:
            print("missing arguments")
            sys.exit()
        try:
            self.sock.connect((argv[1], int(argv[2])))

        except socket.error as err:
            print("Could not connect to host due error")


        file = open(argv[3], "rb")
        accio = ""


        while True:
            rec = (self.sock.recv(1).decode("utf-8"))
            if len(rec) < 1:
                break
            accio += rec

        if accio == 'accio':
            while True:

                send = file.read(1024)
                if len(send) < 1:
                    break
                self.sock.send(send)

        file.close()

        self.sock.close()




a = assignment2()
a.connectTcp2()




