from bs4 import BeautifulSoup
import requests

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


def bs4_get_search_results(query):
    params = {
        'q': query,  # search query
        'gl': 'us',  # country to search from
        'hl': 'en',  # language
    }

    html = requests.get('https://www.google.com/search',
                        headers=headers, params=params).text
    soup = BeautifulSoup(html, 'lxml')

    data = []

    # DESKTOP RESULTS
    for result in soup.select('.tF2Cxc'):
        title = result.select_one('.DKV0Md').text
        link = result.select_one('.yuRUbf a')['href']
        try:
            snippet = result.select_one('#rso .lyLwlc').text
        except:
            snippet = None

        data.append({
            'title': title,
            'link': link,
            'snippet': snippet,
        })

    return data
