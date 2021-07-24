from urllib.request import urlopen
from bs4 import BeautifulSoup
import logging

def scrape_linear_a_site(url):
    # Here is a logging config if you would like to use it
    logging.basicConfig(filename='scraper.log',
                        encoding='utf-8',
                        level=logging.DEBUG,
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), 'html.parser')

    ''' 
    Your task is to populate this list with the 180 Linear A texts found on the page at
    http://people.ku.edu/~jyounger/LinearA/HTtexts.html
    The output texts[] will be a list of lists, with each sublist containing a dictionary:
    texts -> [ [ {}, {}, {} ], [ {}, {}, {}, ... ], ... ]
    
    Each text should be parsed as a list of dictionaries that looks something like this (for text 1):
    [{'line': '.1-2', 'statement': 'QE-RA2-U • \nKI-RO', 'logogram': '\xa0\xa0', 'number': '197', 'fraction': '\xa0\xa0'}, 
    {'line': '.2', 'statement': 'ZU-SU', 'logogram': '\xa0\xa0', 'number': '70', 'fraction': '\xa0\xa0'}, 
    {'line': '.2-3', 'statement': 'DI-DI-ZA-KE', 'logogram': '\xa0\xa0', 'number': '52', 'fraction': '\xa0\xa0'}, 
    {'line': '.3-4', 'statement': 'KU-PA3-NU', 'logogram': '\xa0\xa0', 'number': '109', 'fraction': '\xa0\xa0'}, 
    {'line': '.4', 'statement': 'A-RA-NA-RE', 'logogram': '\xa0\xa0', 'number': '105', 'fraction': '\xa0\xa0'}, 
    {'line': '.5', 'statement': 'vacat', 'logogram': '\xa0\xa0', 'number': '\xa0\xa0', 'fraction': '\xa0\xa0'}]

    Remember to add Error Handling!
    '''
    texts = []
    for table in bs.find_all("table"):
        tmp=[]
        head = table.find_all("font", {"color": "blue"})
        headers = [str(_.get_text()) for _ in head]
        found = table.find("font", {"color": "blue"})

        try:
            found = table.find("font", {"color": "blue"}).parent.parent.parent
        except AttributeError:
            try:
                found = table.find("font", {"color": "blue"}).parent.parent
            except AttributeError:
                try:
                    found = table.find("font", {"color": "blue"}).parent
                except AttributeError:
                    found = table.find("font", {"color": "blue"})
        try:
            test = found.tr
        except AttributeError:
            pass

        d = {}
        tmp = []

        if found is None:
            d[""] = found
            tmp.append(d)
            d = {}
        else:
            for cells in [_ for _ in found.tr.next_siblings if _ != "\n"]:
#            for cells in found.tr.next_siblings:
                if cells.find("tr") is None:
                    if cells.find("td") is None:
                        d[headers[len(d)]] = str(cells.get_text())
                    else:
                        for cell in cells.find_all("td"):
                            if cell.find("td") is None:
                                try:
                                    d[headers[len(d)]] = str(cell.get_text())
                                except IndexError:
                                    print("index0")
                                    break
                            else:
                                for subcell in cell.find_all("td"):
                                    d[headers[len(d)]] = str(cell.get_text())
                elif str(cells.string) != " ":
                    for cell in [_ for _ in cells.find_all("tr") if _ != "\n"]:
#                    for cell in cells.find_all("tr"):
                        for subcell in cell.find_all("td"):
                            try:
                                d[headers[len(d)]] = str(subcell.get_text())
                            except IndexError:
                                print("index2")
                                break
                else:
                    d[headers[len(d)]] = str(cells)
                tmp.append(d)
                d = {}
        texts.append(tmp)
        print(tmp)
        tmp = []
    return texts

if __name__ == "__main__":
    url = 'http://people.ku.edu/~jyounger/LinearA/HTtexts.html'
    texts = scrape_linear_a_site(url)
    print(f"Parsed {len(texts)} texts.")
    print(texts[0])
