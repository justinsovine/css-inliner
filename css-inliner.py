#!/bin/env python

# # # # # # # # # # # # #
# Title: CSS Inliner
# Author: Justin Sovine
# Date: April 01, 2015
# # # # # # # # # # # # #

import mailchimp

def get_mailchimp_api():
    return mailchimp.Mailchimp('4ef9f73e3b3d1d5a7b2a71c1daf6ebf3-us8') #your api key here

def inline_css(html):
    try:
        m = get_mailchimp_api()
        return m.helper.inline_css(html)
    except mailchimp.Error, e:
        messages.error(request,  'An error occurred: %s - %s' % (e.__class__, e))

def main():
    with open ("example.html", "r") as html:
        data=html.read()

    html = str(data)
    inlinedHtml = inline_css(html)
    print '%s' % inlinedHtml['html']

if __name__ == "__main__":
    main()