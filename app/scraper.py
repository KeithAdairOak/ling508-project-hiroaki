


def scrape_linear_a_site(url):
    # Here is a logging config if you would like to use it
    logging.basicConfig(filename='scraper.log',
                        encoding='utf-8',
                        level=logging.DEBUG,
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    try:
        html = urlopen("https://la-conjugaison.nouvelobs.com/du/verbe/aimer.php")
    except Exception as e:
        print("\nError:", e)
        return []
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

if __name__ == "__main__":
    url = 'https://la-conjugaison.nouvelobs.com/du/verbe/aimer.php'
    texts = scrape_linear_a_site(url)
    print(f"Parsed {len(texts)} texts.")
    print(texts[0])