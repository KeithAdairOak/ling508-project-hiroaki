import requests
import re
import unicodedata
from bs4 import BeautifulSoup


class Larousse:

    def __init__(self, word):
        self.word = word
        self.soup = self.get_content()

    def get_definitions(self):
        """
        :return: A list containing all definitions of word
        """

        for ul in self.soup.find_all('ul'):
            if ul.get('class') is not None and 'Definitions' in ul.get('class'):
                return [unicodedata.normalize("NFKD", re.sub("<.*?>", "", str(li))) for li in
                        ul.find_all('li')], ul.find_all('li')
        return None, None

    def get_synonymes(self):
        """
            :return: A list containing all   synonymes of word
            """

        for ul in self.soup.find_all('ul'):
            if ul.get('class') is not None and 'Synonymes' in ul.get('class'):
                return [unicodedata.normalize("NFKD", re.sub("<.*?>", "", str(li))) for li in
                        ul.find_all('li')], ul.find_all('li')
        return None, None

    def get_citations(self):
        """
            :return: A list containing all citations of word
            """

        for ul in self.soup.find_all('ul'):
            if ul.get('class') is not None and 'ListeCitations' in ul.get('class'):
                return [unicodedata.normalize("NFKD", re.sub("<.*?>", "", str(li))) for li in
                        ul.find_all('li')], ul.find_all('li')
        return None, None

    def get_locutions(self):
        """
            :return: A list containing all locutions of word
            """
        for ul in self.soup.find_all('ul'):
            if ul.get('class') is not None and 'ListeCitations' in ul.get('class'):
                return [unicodedata.normalize("NFKD", re.sub("<.*?>", "", str(li))) for li in
                        ul.find_all('li')], ul.find_all('li')
        return None, None

    def get_content(self):
        url = "https://www.larousse.fr/dictionnaires/francais/" + self.word.lower()
        rq = requests.get(url=url)
        if rq.status_code != 200:
            raise Exception("Status code return an error")
        return BeautifulSoup(rq.text, 'html.parser')


def test(word):
    l = Larousse(word)

    print("-DEFINITION-")
    print(l.get_definitions())

    # Print the array containing all locution of "Fromage"
    print("LOCUTATION")
    print(l.get_locutions())

    # Print the array containing all synonymes of "Fromage"
    print("SYNONYMES")
    print(l.get_synonymes())

    # Print the array containing all citations of "Fromage"
    print("CITATIONS")
    print(l.get_citations())

    print("CONTENTS")
    print(l.get_content())
