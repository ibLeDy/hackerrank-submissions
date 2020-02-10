from html.parser import HTMLParser


if __name__ == "__main__":
    class MyHTMLParser(HTMLParser):
        def handle_comment(self, data):
            number_of_line = len(data.split("\n"))

            if number_of_line > 1:
                print(">>> Multi-line Comment")
            else:
                print(">>> Single-line Comment")

            if data.strip():
                print(data)

        def handle_data(self, data):
            if data.strip():
                print(">>> Data")
                print(data)

html = ""
for i in range(int(input())):
    html += input().rstrip() + "\n"

parser = MyHTMLParser()
parser.feed(html)
parser.close()
