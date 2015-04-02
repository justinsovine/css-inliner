#!/usr/bin/python

# # # # # # # # # # # # #
# Title: CSS Inliner
# Author: Justin Sovine
# Date: April 01, 2015
# # # # # # # # # # # # #

import sys
import mailchimp

def get_mailchimp_api():
    return mailchimp.Mailchimp('4ef9f73e3b3d1d5a7b2a71c1daf6ebf3-us8') # your api key here

def inline_css(html):
    try:
        m = get_mailchimp_api()
        return m.helper.inline_css(html)
    except mailchimp.Error, e:
        messages.error(request,  'An error occurred: %s - %s' % (e.__class__, e))

def main(inputFilePath):

    # Import html from file
    htmlFile = inputFilePath
    with open(htmlFile , "r") as inputHtml:
        dataIn = inputHtml.read()

    html = str(dataIn)

    # Inline CSS
    inlinedHtmlJson = inline_css(html)

    # Print Inlined CSS
    inlinedHtml = inlinedHtmlJson['html']

    # Build new html file        
    # Output file path
    outputFilePath = "%s.inlined" % inputFilePath

    with open(outputFilePath, "w") as outputHtml:
        outputHtml.write(inlinedHtml)

    print "\nWrote to %s\n" % outputFilePath

if __name__ == "__main__":
    main(sys.argv[1])
