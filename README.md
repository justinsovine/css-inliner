# css-inliner

## Description
CSS Inliner takes HTML with stylesheets and uses MailChimp's API to export an inlined version. This is mostly useful for email. 

There is an associated Sublime Text build file that makes inlining a document as simple as "CTRL + b"

## Usage
* $ css-inliner /path/to/file-to-inline.html

### Sublime Text Build:  
* Place CSS Inliner.sublime-build under Packages/User/  
* Select Tools > Build System > CSS Inliner  
* CTRL + b to inline current file  

## Install
* $ pip install -r requirements.txt

## Requirements
* mailchimp - https://pypi.python.org/pypi/mailchimp

## License
CSS Inliner is released under the MIT license, see LICENSE.TXT
