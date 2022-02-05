import os
import sys
import argparse
import requests

# URL for the imsdb scroipt
URL = "https://imsdb.com/scripts/Die-Hard.html"


def get_url_contents(url):
    """
    Get the contents of a url as text
    """
    response = requests.get(url)
    return response.text


def save_content_to_file(file_name):
    """
    Save the contents of the url to a file
    """
    contents = get_url_contents(URL)
    with open(file_name, "w") as f:
        f.write(contents)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scrape die hard script from imsdb")
    parser.add_argument("-f", "--file", help="File to save the contents to")
    args = parser.parse_args()
    if args.file:
        save_content_to_file(args.file)
    else:
        print("Please specify a file to save the contents to")
