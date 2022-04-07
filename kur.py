import webbrowser

url = "https://finans.mynet.com/doviz/usd-dolar/"
url2 = "https://finans.mynet.com/altin/xgld-spot-altin-tl-gr/"


chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)
chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url2)