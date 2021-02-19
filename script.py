import webbrowser
import os
import pandas as pd

def open_link():
    zoom_link = 'https://berkeley.zoom.us/j/99744847516?pwd=VEFDYS9kR1JoWG1JWVUrOEVZamVWQT09'
    chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    webbrowser.register('google_chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    os.system(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    webbrowser.get('google_chrome').open('https://berkeley.zoom.us/j/99744847516?pwd=VEFDYS9kR1JoWG1JWVUrOEVZamVWQT09')
    #webbrowser.get(chrome_path).open('https://ocf.io/~timtucker')

open_link()
