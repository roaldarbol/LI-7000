#!/usr/bin/python
# Filename: class_li7000.py

import serial
import time


class li7000:
    def __init__(self, port, baudrate, time):
        self.ser = serial.Serial(port, baudrate, timeout=time)

    def li7000_readline(self):
        output = self.ser.readline()
        return output

    def li7000_header(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        time.sleep(0.1)
        self.ser.write(bytes("(RS232(Sources?))\n".encode()))
        output = self.li7000_readline()
        return output

    def li7000_pollnow(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        time.sleep(0.1)
        self.ser.write(bytes("(RS232(Poll Now))\n".encode()))
        for i in range(0, 3):
            if i == 2:
                output = self.li7000_readline()
            else:
                self.li7000_readline()
        return output

    def li7000_setreference(self, units, H2O, CO2):
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.flush()
        time.sleep(0.1)
        str = "(Reference(H2O-units %s)(H2O %.3f)(CO2 %.3f))\n" % (units, H2O, CO2)
        self.ser.write(bytes(str.encode()))

    def li7000_matchCO2(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.flush()
        time.sleep(0.1)
        str = "(UserCal(CO2 (Match Now)))\n"
        self.ser.write(bytes(str.encode()))

    def li7000_matchH2O(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.flush()
        time.sleep(0.1)
        str = "(UserCal(H2O (Match Now)))\n"
        self.ser.write(bytes(str.encode()))

    def li7000_zeroh2o(self, interval):
         self.ser.flushInput()
         self.ser.flushOutput()
         time.sleep(0.1)
         self.ser.write(bytes("(UserCal (H2O (CellA-mm/m 0)))\n".encode()))
         time.sleep(interval)

    def li7000_h20calresult(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        time.sleep(0.1)
        self.ser.write(bytes("(Cal(H2O(#)))\n".encode()))
        output = self.li7000_readline()
        return output

    def li7000_spanh2o(self, span, interval):
         self.ser.flushInput()
         self.ser.flushOutput()
         time.sleep(0.1)
         str = "(UserCal (H2O (CellA-mm/m %.3f)))\n" % (span)
         self.ser.write(bytes(str.encode()))
         time.sleep(interval)

    def li7000_zeroco2(self, interval):
         self.ser.flushInput()
         self.ser.flushOutput()
         time.sleep(0.1)
         self.ser.write(bytes("(UserCal (CO2 (CellA-um/m 0)))\n".encode()))
         time.sleep(interval)

    def li7000_spanco2(self, span, interval):
         self.ser.flushInput()
         self.ser.flushOutput()
         time.sleep(0.1)
         str = "(UserCal (CO2 (CellA-um/m %.3f)))\n" % (span)
         self.ser.write(bytes(str.encode()))
         time.sleep(interval)

    def li7000_co2calresult(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        time.sleep(0.1)
        self.ser.write(bytes("(Cal(CO2(#)))\n".encode()))
        output = self.li7000_readline()
        return output