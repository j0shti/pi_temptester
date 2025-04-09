#!/usr/bin/env python
from smbus import SMBus
import time

def main():
    i2cbus = SMBus(1)
    i2caddress = 0x40
    tempaddress = 0x00
    hmdaddress = 0x01

    while (True):
        portA = i2cbus.read_word_data(i2caddress, tempaddress);
        portB = i2caddress.read_word_data(i2caddress,hmdaddress);

        print(portA);
        print(portB);

if __name__ == "__main__":
    main()
