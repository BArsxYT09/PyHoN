import requests

html = requests.get('https://www.instagram.com/instagram/').text
print('Instagramdan cektigim html boyutu: ', len(html))