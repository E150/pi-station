import sqlite3

DB_FILE_PATH='/var/lib/sensors.db'

class db:
    def createTables(self):
        conn = sqlite3.connect(DB_FILE_PATH)  # @UndefinedVariable
        c = conn.cursor() 
        #print ('''CREATE TABLE IF NOT EXISTS READINGS (ID INTEGER PRIMARY KEY NOT NULL,DATE TIMESTAMP,SYS_TEMP REAL,DS_TEMP REAL,DHT_HUMI REAL,DHT_TEMP REAL,BMP_TEMP REAL,BMP_PRES REAL,BMP_ALTI REAL,BMP_SLPR REAL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS READINGS (ID INTEGER PRIMARY KEY NOT NULL,DATE TIMESTAMP,SYS_TEMP REAL,DS_TEMP REAL,DHT_HUMI REAL,DHT_TEMP REAL,BMP_TEMP REAL,BMP_PRES REAL,BMP_ALTI REAL,BMP_SLPR REAL)''')
        # Save (commit) the changes
        conn.commit()
        conn.close()
        return None
    
    def readTable(self):
        conn = sqlite3.connect(DB_FILE_PATH)  # @UndefinedVariable
        c = conn.cursor() 
        c.execute("SELECT * FROM READINGS")
        #c.execute("SELECT datetime({0},'unixepoch') FROM {1}".format(column,table))
        data = c.fetchall()
        conn.commit()
        conn.close()
        return data
    
    def readLast(self):
        conn = sqlite3.connect(DB_FILE_PATH)  # @UndefinedVariable
        c = conn.cursor() 
        c.execute("SELECT MAX(ID),* FROM READINGS")
        row = c.fetchone()
        conn.commit()
        conn.close()
        return row

    def insertValues(self,cur_timestamp, sys_tmp, ds_tmp, dht_hum, dht_tmp, bmp_tmp, bmp_prs, bmp_alt, bmp_slp):
        conn = sqlite3.connect(DB_FILE_PATH)  # @UndefinedVariable
        c = conn.cursor() 
        #print ('''INSERT INTO READINGS (DATE,SYS_TEMP,DS_TEMP,DHT_HUMI,DHT_TEMP,BMP_TEMP,BMP_PRES,BMP_ALTI,BMP_SLPR) VALUES ('{0}','{1:0.1f}','{2:0.1f}','{3:0.1f}','{4:0.1f}','{5:0.1f}','{6:0.2f}','{7:0.2f}','{8:0.2f}')'''.format(str(cur_timestamp), sys_tmp, ds_tmp, dht_hum, dht_tmp, bmp_tmp, bmp_prs, bmp_alt, bmp_slp))
        c.execute('''INSERT INTO READINGS (DATE,SYS_TEMP,DS_TEMP,DHT_HUMI,DHT_TEMP,BMP_TEMP,BMP_PRES,BMP_ALTI,BMP_SLPR) VALUES ('{0}','{1:0.1f}','{2:0.1f}','{3:0.1f}','{4:0.1f}','{5:0.1f}','{6:0.2f}','{7:0.2f}','{8:0.2f}')'''.format(str(cur_timestamp), sys_tmp, ds_tmp, dht_hum, dht_tmp, bmp_tmp, bmp_prs, bmp_alt, bmp_slp))  
        # Save (commit) the changes
        conn.commit()
        conn.close()
        return None