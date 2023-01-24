
# pip install requests-html

import os
from requests_html import HTMLSession

os.system('cls' if os.name == 'nt' else 'clear')

Query = input('Enter Keywords to Scrape : ')
Limit = int(10)

file = open('Results.txt', 'w')

s = HTMLSession()

headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

params = {
    'q': Query,
    'num': Limit,
}

response = s.get('https://www.google.com/search', params=params)

if 'Our systems have detected unusual traffic from your computer' in response.text:
    exit('Captcha Triggered!\n')
else:
    links = list(response.html.absolute_links)
    titles = list(response.html.find("h3"))

    def titleDef(i):
        if (i+1 > len(titles)):
            return "UNKNOWN"
        return titles[i].text

        # print("Hello from a function")
    # print(title(), url)
    # for i in range(len(links)):
    #     url = links[i]
    #     title = titleDef(i)
    for i in range(len(links)):
        url = links[i]
        title = titleDef(i)

        if not 'google' in url:
            print(title+'/n'+url+'/n')
            print("bla")
            # file.write(title+'/n'+url+'/n')

    # for url in links:
    #     if not 'google' in url:
    #         print(url)
    #         file.write(url+'\n')

    # for each in titles[:]:
    #     print(titles.text)


"""
#POSSIBLE ADDITIONS

def parse_results(response):

    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"

    results = response.html.find(css_identifier_result)

    output = []

    for result in results:

        item = {
            'title': result.find(css_identifier_title, first=True).text,
            'link': result.find(css_identifier_link, first=True).attrs['href'],
            'text': result.find(css_identifier_text, first=True).text
        }

        output.append(item)

    return output
"""
