#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
"""
Client FreeLearning Book InfoScraper
@author: Oscar Lopez Luna
"""

import urllib2
import bs4


class BookClient(object):

    def get_web(self, url):
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    def run(self):

        # download webPage
        html = self.get_web("https://www.packtpub.com/packt/offers/free-learning/")

        # obtain html in which we are interested
        soup = bs4.BeautifulSoup(html, "lxml")
        title_information = soup.find_all("div", "dotd-title")

        # Obtaining the title
        for title_info in title_information:
            book_header = title_info.find("h2")
            book_title = book_header.text
            print ("Book Title:\n" + book_title.strip() + "\n")

        # Obtaining the summary
        summary_information = soup.find_all("div", "dotd-main-book-summary float-left")
        for summary in summary_information:
            summary_info = summary.find("div", "")
            summary_text = summary_info.text
            print ("Book Overview:\n" + summary_text.strip())


if __name__ == "__main__":
    client = BookClient()
    client.run()
