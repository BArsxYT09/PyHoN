import webbrowser

istn = input("İstediğinz şehri yazınız : ")

url = f"https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il={istn}"
url2 = f"https://www.google.com.tr/search?q={istn}+hava+durumu&sxsrf=APq-WBs9IyUxZ_TxodB0-dypUFu1Nmi0vA%3A1645219369087&ei=KQ4QYufpBO-Vxc8P0Zap4Ag&ved=0ahUKEwinosngl4r2AhXvSvEDHVFLCowQ4dUDCA4&uact=5&oq=Ayd%C4%B1n+hava+durumu&gs_lcp=Cgdnd3Mtd2l6EAMyBwgjELADECcyBwgAEEcQsAMyCggAEEcQsAMQyQMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAELADEENKBAhBGABKBAhGGABQAFgAYLkEaAFwAXgAgAEAiAEAkgEAmAEAyAEKwAEB&sclient=gws-wiz"


chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)
chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url2)