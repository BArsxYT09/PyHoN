import webbrowser

url = ("https://media.discordapp.net/attachments/943889839240142852/943890418175737856/p6Iz52rWvB83sPOmloquTl4vbkMmDjDLQxpR4RAE8RR8iGv73SjnzFw7DEx4V9a0a_JNR4ANyIc5X1YTj74ztQ3D3D.png?width=359&height=675")

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)
print(f"{url} = GİRİLEN URL")