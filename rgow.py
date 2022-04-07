import webbrowser

rgow = input("Aramak istediğiniz kelimeyi giriniz ? ")

url = f"https://tr.wikipedia.org/wiki/{rgow}"
url2 = f"https://www.google.com/search?q={rgow}"

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)
chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url2)