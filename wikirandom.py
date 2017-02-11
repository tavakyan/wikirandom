#! /usr/bin/env python
import sys
import sumy
import wikipedia


URL = 'https://en.wikipedia.org/wiki/Special:Random'


def print_and_wait(article):
    print(article)
    print(wikipedia.summary(article))
    i = raw_input('')
    # can print entire page here if you want


def main(n):
    articles = wikipedia.random(pages=n)

    [print_and_wait(a) for a in articles]

    return 0


if __name__ == '__main__':
    status = 1
    try:
        status = main(sys.argv[1])
    except:
        status = 2
    sys.exit(status)
