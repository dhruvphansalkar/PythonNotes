"""Retrieve and print words from url

Usage:
    python3 FirstDemo.py <url>

"""
import sys
from urllib.request import urlopen

def fetch_words(url):
    """fetch a list of words from url
        Args:
            url:
                the url of a text document
            Returns:
                A list of words
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    """print a list of words
            Args:
                items:
                 an iterable
            Returns:
                A list of words
    """
    for item in items:
        print(item)

def main(url):
    for arg in sys.argv:
        print(arg)
    words = fetch_words(url)
    print_items(words)

print('Running')
print(__name__)
if __name__ == '__main__' : # will be true when being executed as script

    main(sys.argv[1])