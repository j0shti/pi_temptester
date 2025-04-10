#!/usr/bin/env python
import smbus
import time

def main():
    i2cbus = smbus.SMBus(1)


    i2caddress = 0x40
    tempaddress = 0x00
    hmdaddress = 0x01

    
    while (True):
        i2cbus.write_byte(i2caddress, 0x00) 
        time.sleep(0.3)
        
        portA1 = i2cbus.read_byte(i2caddress, tempaddress)
        portA2 = i2cbus.read_byte(i2caddress, tempaddress)

        time.sleep(0.3)

        portB1 = i2cbus.read_byte(i2caddress,hmdaddress)
        portB2 = i2cbus.read_byte(i2caddress,hmdaddress)

        tempData = portA1 << 8 | portA2
        humidityData = PortB1 << 8 | portB2

        temp = (tempData * 165 / 65535.0) - 40.0
        hum = (humidityData / 65535.0) - 40.0

        print(f'temp(C): {temp}')
        print(f'hum(%RH): {hum}')
        time.sleep(1)

if __name__ == "__main__":
    main()
