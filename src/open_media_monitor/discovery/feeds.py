#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This module provides functions to find feeds from a given website.
'''

import requests

from bs4 import BeautifulSoup as bs


def _soup_of_website(website_url):
    '''
    Returns the beautifulsoup for the website. 

    :param website_url: The website to create the soup from.
    :type website_url: str
    :returns: BeautifulSoup object.
    :rtype: BeautifulSoup
    '''
    website_html = requests.get(website_url).text
    soup = bs(website_html, 'html.parser')
    return soup


def rss_feeds_of_website(website_url):
    '''
    Returns a list of rss feeds.

    :param website_url: The url of which to detect the feeds.
    :type website_url: str
    :returns: a dictionary mapping the feed urls to a dict of parameters.
    :rtype: dict
    '''
    if website_url[:4] != 'http':
        website_url = 'http://' + website_url
    soup = _soup_of_website(website_url)
    result = {}
    for link in soup.find_all("link", {"type" : "application/rss+xml"}):
        href = link.get('href')
        if href[:4] != 'http':
            href = website_url + href
        print href
        result[href] = link
    return result


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-u',
                        '--url',
                        help='The url from which to fetch the feeds.',
                        required=True)
    parser.add_argument('-r',
                        '--rss',
                        help='If ',
                        action='store_true',
                        default=False)
    args = parser.parse_args()
    if args.rss:
        rss_feeds_of_website(args.url)

if __name__ == '__main__':
    main()
