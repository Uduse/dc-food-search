import requests
from HTMLParser import HTMLParser
from collections import defaultdict
import sys

dc = {
    "segundo": 'http://dining.ucdavis.edu/res-segundo-menu.html',
    "tercero": 'http://dining.ucdavis.edu/res-tercero-menu.html',
    "cuarto": 'http://dining.ucdavis.edu/res-cuarto-menu.html'
}


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        data = data.strip()
        if data:
            menu[self._dc_name].append(data.lower())


def get_menus():
    try:
        for dc_name, url in dc.items():
            # get response from url
            response = requests.get(url)
            # all valid html contents, including some useless information
            html_content = response.text.encode('utf-8')

            # parse html content, put everything in menu dictionary
            parser = MyHTMLParser()
            parser._dc_name = dc_name
            parser.feed(html_content)
    except Exception as e:
        print e
        print "Something wrong happened, probably ..."
        print "1) Your internet is down"
        print "2) DC changed their menu links"
        print "3) DC websites is down for maintenance"
        print "\nDon't doubt, there's no bug in my code :)"
    else:
        print "Menus successfully retrieved."
        print


def find_in_menu(something_delicious):
    something_delicious = something_delicious.lower()
    found = False
    dc_that_has_the_stuff = []
    for dc_name in menu.keys():
        if any(something_delicious in item for item in menu[dc_name]):
            dc_that_has_the_stuff.append(dc_name)
            found = True
    return dc_that_has_the_stuff


def not_found_msg(something_delicious):
    return "Sadly no DC has " + something_delicious \
          + " this week, forget about it so you may lose some weight.\n"


def found_msg(dc_name, something_delicious):
    return dc_name[0].upper() + dc_name[1:] \
           + " has " + something_delicious + "!  Check it out here: " \
           + dc[dc_name] + "\n"


def make_menu():
    global menu
    menu = defaultdict(list)
    get_menus()


if __name__ == "__main__":
    make_menu()
    for dish in sys.argv[1:]:
        dc_list = find_in_menu(dish)
        if dc_list:
            for dc_name in dc_list:
                print found_msg(dc_name, dish)
        else:
            print not_found_msg(dish)
