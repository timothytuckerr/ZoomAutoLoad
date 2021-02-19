import webbrowser
import os
import pandas as pd
from datetime import datetime

def open_link(zoom_link):
    chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

    webbrowser.register('google_chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    os.system(r'C:\Program Files\Google\Chrome\Application\chrome.exe')

    webbrowser.get('google_chrome').open(zoom_link)


timingSheet = pd.read_csv('zooms.csv')
while True:
    now = datetime.now()
    nowTime = now.strftime("%H:%M")
    dayOfWeek = now.weekday()
    if nowTime in str(timingSheet['times']):
        row = timingSheet.loc[timingSheet['times'] == now]
        zoomDay = int(row.iloc[:,0])
        if zoomDay == dayOfWeek:
            zoomLink = row.iloc[:,2]
            open_link(zoomLink)
            time.sleep(60)
            print('joined zoom')
