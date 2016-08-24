import time
import Adafruit_DHT   # @UnresolvedImport
import Adafruit_BMP.BMP085 as BMP085   # @UnresolvedImport

KNOWN_SLP=103550
KNOWN_ALT=225.0
CPU_FILE='/sys/devices/virtual/thermal/thermal_zone0/temp'
DS_FILE='/sys/bus/w1/devices/28-0315a24b4bff/w1_slave'
DHT_PIN=22

def getDateTime():
    datetime = time.strftime("%Y-%m-%d %H:%M:%S")
    return datetime

def readCPU():
    with open(CPU_FILE, 'r') as f:
        temperature = float(f.readline())/1000
    if temperature is not None:
        return temperature
    else:
        print 'Failed to get reading from CPU_THERMAL. Try again!'

def readDS():
    with open(DS_FILE, 'r') as f:
        text = f.read()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        temperature = temperature / 1000
    if temperature is not None:
        return temperature
    else:
        print 'Failed to get reading from DS18B20. Try again!'

def readDHT():
    sensor = Adafruit_DHT.DHT11
    pin =  DHT_PIN
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)   
    if humidity is not None and temperature is not None:
        return(humidity, temperature)
    else:
        print 'Failed to get reading from DHT11. Try again!'

def readBMP():
    sensor = BMP085.BMP085()
    temperature = sensor.read_temperature()
    pressure = sensor.read_pressure()
    altitude = sensor.read_altitude(KNOWN_SLP)
    sealevel_pressure = sensor.read_sealevel_pressure(KNOWN_ALT)
    if temperature is not None and pressure is not None and altitude is not None and sealevel_pressure is not None:
        return(temperature, pressure, altitude, sealevel_pressure)
    else:
        print 'Failed to get reading from BMP180. Try again!'

def calibrateBMP():
    # Read user input
    setting = raw_input('Set known [A]ltitude or [S]ea Level Pressure at current location: ')
    if setting in ('A','a'):
        known_altitude = raw_input('Set known [A]ltitude value in meters over sea level (e.g. 152.6): ')
        global KNOWN_ALT
        KNOWN_ALT = float(known_altitude)
        return None
    elif setting in ('S','s'):
        known_sealevelpressure = raw_input('Set known [S]ea Level Pressure value in Pa (e.g. 102950): ')
        global KNOWN_SLP
        KNOWN_SLP = int(known_sealevelpressure)
        return None
    else:
        return None

