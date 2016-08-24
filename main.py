#!/usr/bin/python

import sys
import time
import sensors
import plotly_upload
import database
#import relay
import json
import csv
import logging

HTTP_FOLDER='www'
LOG_FILENAME = '/var/log/sensors.log'
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',filename=LOG_FILENAME,level=logging.DEBUG)

def ReadSensors(dbinstance):
    # Get readings from devices and store them in database
    # power = relay.Switch()
    # power.on()
    # time.sleep(2)
    print 'Reading sensors...'
    cur_timestamp = int(time.time())
    sys_tmp = sensors.readCPU()
    ds_tmp = sensors.readDS()
    dht_hum, dht_tmp = sensors.readDHT()
    bmp_tmp, bmp_prs, bmp_alt, bmp_slp = sensors.readBMP()
    dbinstance.insertValues(cur_timestamp, sys_tmp, ds_tmp, dht_hum, dht_tmp, bmp_tmp, bmp_prs, bmp_alt, bmp_slp)
    logging.info('CPU Temp: {0:0.1f} *C'.format(sys_tmp))
    logging.info('DS Temp= {0:0.1f} *C'.format(ds_tmp))
    logging.info('DHT Temp= {0:0.1f} *C'.format(dht_tmp))
    logging.info('BMP Temp = {0:0.1f} *C'.format(bmp_tmp))
    logging.info('Humidity= {0:0.1f} %'.format(dht_hum))
    logging.info('Pressure = {0:0} Pa'.format(bmp_prs))
    logging.info('Altitude = {0:0.2f} m'.format(bmp_alt))
    logging.info('Sea Level Pressure = {0:0.2f} Pa'.format(bmp_slp))
    # power.off()
    return None

def main(argv):

    # Spawn a new database instance
    instance = database.db()
    # Create tables if they don't exist
    instance.createTables()
    
    if len(argv) > 1:
        if argv[1] == 'plotly':
            # Upload data to plotly
            dump = instance.readTable()
            plotly_upload.upload(dump)
        elif argv[1] == 'gspread':
            # Upload data to google
            #spreadsheet = gspread.gspread()
            #spreadsheet.write_sheet()
            pass
        elif argv[1] == 'calibrate':
            # Calibrate BMP180 barometer
            sensors.calibrateBMP()
        elif argv[1] == 'export':
            # Dump data to CSV & JSON files
            with open('sensors.csv', 'wb') as csvfile:
                dump = instance.readTable()
                writer = csv.writer(csvfile)
                writer.writerows(dump)
                csvfile.close()        
            keys = ['id', 'timestamp','cpu_temp','ds_temp','dht_humi','dht_temp','bmp_temp','bmp_pres','bmp_alti','bmp_slps']
            csvfile = open('sensors.csv', 'r')
            jsonfile = open('/home/pi/pi-station/www/sensors.json', 'w')
            reader = csv.DictReader(csvfile, keys)
            out = json.dumps( [ row for row in reader ] )
            jsonfile.write(out)
            jsonfile.close()
            csvfile.close()
            return None
        elif argv[1] == 'read':
            datetime = sensors.getDateTime()
            ds = sensors.readDS()
            bmp = sensors.readBMP()
            dht = sensors.readDHT()
            print datetime,ds,bmp,dht
        else:
            print "Unknown option."
    else:
        ReadSensors(instance)

if __name__ == "__main__":
    main(sys.argv)

