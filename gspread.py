import time
import gspread
import json
from oauth2client.client import SignedJwtAssertionCredentials

GDOCS_OAUTH_JSON = 'oauth.json'
GDOCS_SPREADSHEET_NAME = 'sensors.xml'

class gspread:
    
    def login_open_sheet(self,oauth_key_file, spreadsheet):
            try:
                    json_key = json.load(open(oauth_key_file))
                    credentials = SignedJwtAssertionCredentials(json_key['client_email'],json_key['private_key'],['https://spreadsheets.google.com/feeds'])
                    print credentials
                    gc = gspread.authorize(credentials)
                    worksheet = gc.open(spreadsheet).sheet1
                    return worksheet
            except Exception as ex:
                    print 'Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!'
                    print 'Google sheet login failed with error:', ex

    def write_sheet(self):       
        worksheet = self.login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)
        humidity, temp = 20, 16
        try:
                worksheet.append_row((int(time.time()), temp, humidity))
        except:
                print 'Append error'
                worksheet = None
        print 'Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME)
