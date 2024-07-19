import os
output_file = open("../README.md", "a")


from html.parser import HTMLParser

data_string = ''

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        global data_string
        if "\n" in data:
            return
        else:
            data_string += f'{data}\n'


parser = MyHTMLParser()

f = open("index.html")
if f.mode == "r":
    contents = f.read()
    parser.feed(contents)


output_file.write("\n" + data_string)
output_file.close()