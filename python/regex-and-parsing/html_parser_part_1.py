from html.parser import HTMLParser


if __name__ == '__main__':
    class Parse(HTMLParser):
        def handle_starttag(self, tag, attrs):
            print(" ".join(["Start :", tag]))

            for i in attrs:
                print("-> {} > {}".format(i[0], i[1]))

        def handle_endtag(self, tag):
            print(" ".join(["End   :", tag]))

        def handle_startendtag(self, tag, attrs):
            print(" ".join(["Empty :", tag]))

            for i in attrs:
                print("-> {} > {}".format(i[0], i[1]))

    p = Parse()

    for _ in range(int(input())):
        p.feed(input())
