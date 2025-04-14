#!/usr/bin/env python
import smbus
import time
import os

def main():
    i2cbus = smbus.SMBus(1)


    i2caddress = 0x40

    
    while (True):
        i2cbus.write_byte(i2caddress, 0x00) 
        time.sleep(0.3)
        
        portA1 = i2cbus.read_byte(i2caddress)
        portA2 = i2cbus.read_byte(i2caddress)

        time.sleep(0.3)

        i2cbus.write_byte(i2caddress, 0x01) 
        time.sleep(0.3)

        portB1 = i2cbus.read_byte(i2caddress)
        portB2 = i2cbus.read_byte(i2caddress)

        tempData = portA1 << 8 | portA2
        humidityData = portB1 << 8 | portB2

        temp = (tempData * 165 / 65535.0) - 40.0
        hum = (humidityData / 65535.0) * 100

        print(f'temp(C): {temp}')
        print(f'hum(%RH): {hum}')
        time.sleep(1)

        if temp > 27:
            print('temp too high -- rebooting')
            # os.system('sudo reboot')

if __name__ == "__main__":
    main()
