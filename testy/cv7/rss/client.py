import http.client as httplib
import xml.etree.ElementTree as ET

class Error(Exception):
    pass

class CannotRetrieveUrlError(Error):
    def __init__(self, url):
        self.msg = "Cannot retrieve URL: " + url


class FeedItem(object):
    """
    Reprezentuje jeden item ve feedu, tzn.
    <item>
    ...
    </item>
    """
    # TODO 5

class Feed(object):
    """
    Reprezentuje feed, tzn. kanal, ve kterem jsou jednotlive prispevky.
    <channel>
    </channel>
    """
        
    def __init__(self, feed_xml):
        # tato promenna udrzuje string s XML daty, ktera byla
        # stazena ze serveru. Pouzijte ji pro parsovani XML.    
        self.feed_xml = feed_xml
        
        self.title, self.desc, self.lang = self.parse_feed_info()

    def print_info(self):
        print("=====================")
        print("Feed info:")
        print("Title: {}".format(self.title))
        print("Desc: {}".format(self.desc))
        print("Lang: {}".format(self.lang))
        print("=====================")
        print()

    def parse_feed_info(self):
        # TODO 2:z XML dat vrati trojici obsahujici informace o feedu
        # title, description, language
        root = ET.fromstring(self.feed_xml)
        title = root.find("channel/title").text
        desc = root.find("channel/description").text
        lang = root.find("channel/language").text

        return (title, desc, lang)

    def items(self):
        # TODO 3:z XML dat vrati vsechny itemy, ktere feed obsahuje
        # generujte list tuplu (title, desc, guid)
        lst = []
        root = ET.fromstring(self.feed_xml)
        items = root.findall('channel/item') #list of Elements
        for item in items:
            title = item.find("title").text
            desc = item.find("description").text
            guid = item.find("guid").text
            #print(title, desc, guid)
            lst.append((title, desc, guid))

        #for item in lst:
            #print(item)

        # Pro TODO 5 generujte instance tridy FeedItem
        return lst

class Reader(object):
    """
    Reprezentuje RSS ctecku, ktera umi cist vice RSS feedu.
    Pro jednoduchost budeme pouze cist jeden RSS feed.
    """
    def __init__(self, url):
        self.url = url
        self.feed = None

    def fetch_feed(self):
        conn = httplib.HTTPConnection(self.url)
        conn.request("GET", "/")
        r = conn.getresponse()
        #print type(r.status), type(r.reason)
        if r.status != 200:
            raise CannotRetrieveUrlError(self.url)

        xml = r.read()
        #print(xml.decode('ascii'))
        # TODO 1: doplnit vytvoreni objektu Feed do promenne self.feed
        #pro overeni splneni TODO 2 zde take zavolat metodu feed.print_info()
        self.feed = Feed(xml)
        self.feed.print_info()
        self.feed.items()
        
        #self.read_feed()

        conn.close()

    def read_feed(self):
        # TODO 4, X:z feedu precist itemy pomoci funkce feed.items() 
        #a vytisknout na obrazovku
        print(self.feed.items())
        pass

def main():
    url = 'localhost:9000'
    reader = Reader(url)

    try:
        reader.fetch_feed()
        reader.read_feed()
    except CannotRetrieveUrlError as e:
        print(e)

if __name__ == '__main__':
    main()
