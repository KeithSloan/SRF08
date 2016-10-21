import smbus
import time
bus = smbus.SMBus(1)
address = 0x70

#SRF08 REQUIRES 5V

def write(value):
        bus.write_byte_data(address, 0, value)
        return -1

def lightlevel():
        light = bus.read_byte_data(address, 1)
        return light

def softwareRevision():
        software = bus.read_byte_data(address, 0)
        return software

def range():
        range1 = bus.read_byte_data(address, 2)
        range2 = bus.read_byte_data(address, 3)
        range3 = (range1 << 8) + range2
        return range3

soft = softwareRevision()
print soft 
lightlvl = lightlevel()
print lightlvl

while True:
        write(0x51)
        time.sleep(0.7)
        rng = range()
        print rng
