import requests
from bs4 import BeautifulSoup
import json

start_url = 'https://ordi.eu/sulearvutid?___store=en&___from_store=et'
ordi_computers = []


def parse(start_urls):
    page = requests.get(start_urls)
    soup = BeautifulSoup(page.text, 'html.parser')

    ordi_computers_list = soup.find_all("li", class_='item')
    for ordi_computer in ordi_computers_list:
        data = {'Title': ordi_computer.h2.get_text(),
                'Price': ordi_computer.find('div', class_='price-box').span.text,
                'Picture href': ordi_computer.a.img['src']
                }
        ordi_computers.append(data)
        print(data)

    try:
        next_page = soup.find("a", class_='next')['href']
        if next_page:
            print(f"\n {next_page} \n")
            parse(next_page)
    except:
        print("The End")

    with open('ordi_soup_spider_output.json', 'w', encoding='utf-8') as file:
        file.write('[\n' +
                   ',\n'.join(json.dumps(i, ensure_ascii=False) for i in ordi_computers) +
                   '\n]')


if __name__ == '__main__':
    parse(start_url)
