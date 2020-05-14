from phue import Bridge
from time import sleep

def blinky(b):
    bri_high = b.get_light(5,'bri')
    bri_low = bri_high-100 if bri_high-50>0 else 0
    b.set_light(5,'bri', bri_low, transitiontime=5)
    sleep(0.5)
    b.set_light(5,'bri', bri_high, transitiontime=5)
    sleep(1)
    b.set_light(5,'bri', bri_low, transitiontime=5)
    sleep(0.5)
    b.set_light(5,'bri', bri_high, transitiontime=10)

def get_bridge():
    b = Bridge('192.168.1.49')
    b.connect()
    b.get_api()    
    return b

def main():
    b = get_bridge()
    blinky(b)

if __name__=='__main__':
    main()

