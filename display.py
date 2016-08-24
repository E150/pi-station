#!/usr/bin/env python

import sys
import time
import datetime
import sqlite3
from RPiLiquidCrystal.HD44780 import HD44780
from RPiLiquidCrystal.LCD_i2C import LCD

from datetime import timedelta
DB_FILE_PATH='/var/lib/sensors.db'

def refresh(line1,line2):
    # Setup LCD Screen
    lcd = LCD(0x27, cols=16, lines=2)

    try:
        lcd.clear()
        lcd.setCursor(0, 0)
        lcd.write('{0}'.format(line1), justify=HD44780.JUSTIFY_CENTER)
        lcd.setCursor(1, 0)
        lcd.write('{0}'.format(line2), justify=HD44780.JUSTIFY_CENTER)

#===============================================================================
#         lcd.clear()
#         lcd.setCursor(0, 0)
#         lcd.write('Check It Out!')
#         lcd.setCursor(1, 0)
#         lcd.write('Right Aligned!', justify=HD44780.JUSTIFY_RIGHT)
#         lcd.setCursor(0, 0)
#         lcd.write('Centered!', justify=HD44780.JUSTIFY_CENTER)
#         lcd.setCursor(1, 0)
#         lcd.write('XXXXXXXXFILLXXXXXXXX')
#         time.sleep(2)
# 
#         lcd.clear()
#         lcd.createChar(0, CUSTOM_CHARS[0])
#         lcd.createChar(1, CUSTOM_CHARS[1])
#         lcd.setCursor(0, 0)
#         lcd.write('Custom Characters!', justify=HD44780.JUSTIFY_CENTER)
#         lcd.writeRaw(0, 1, 8)
#         lcd.writeRaw(1, 1, 9)
#         lcd.writeRaw(0, 2, 9)
#         lcd.writeRaw(0, 2, 8)
#         time.sleep(2)
#===============================================================================

    except KeyboardInterrupt:
        lcd.baclight=0
        pass

    lcd.cleanup()

def main(args):
    while (1):
        conn = sqlite3.connect(DB_FILE_PATH)
        c = conn.cursor()
        c.execute("SELECT MAX(DATE),SYS_TEMP,DHT_HUMI,DHT_TEMP,BMP_TEMP,BMP_PRES,BMP_ALTI,BMP_SLPR FROM READINGS")
        values = c.fetchone()
        conn.close()
        print values
        refresh('T {0}C H {1}%'.format(values[4],values[2]),'P {0} Pa'.format(values[7]))
        time.sleep(5)
        
        date = datetime.datetime.now()
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split('.')[0])
            uptime_string = str(timedelta(seconds = uptime_seconds))
            print uptime_string 
        refresh('{0}'.format(date),'UP {0}'.format(uptime_string))
        time.sleep(5)
    
    
if __name__ == '__main__':
    main(sys.argv)
