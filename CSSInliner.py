import sublime, sublime_plugin
import sys
import mailchimp

# needed for getting local app data path on windows
#if sublime.platform() == 'windows':
#    import _winreg

inputFilePath = sys.argv[1]

class EmailInlinerCommand(sublime_plugin.WindowCommand):
    def inline_css(self):
        
        # Load user settings
        s = sublime.load_settings('Email Inliner.sublime-settings')

        # Load API key from user settings
        if s.get('mailchimp_api_key'):
            m = mailchimp.Mailchimp(s.get('mailchimp_api_key')

            # Check API key
            try:
                m.helper.ping()

            except mailchimp.Error:
                messages.error(request,  "Invalid API key")
                sys.exit

            # Inline CSS
            try:
                inlinedHtmlJson = m.helper.inline_css(inputFilePath)
                inlinedHtml     = inlinedHtmlJson['html']
                
            except mailchimp.Error, e:
                messages.error(request,  'An error occurred: %s - %s' % (e.__class__, e))
                sys.exit

            # Write new, inlined html file       
            outputFilePath = "%s.inlined" % inputFilePath
            with open(outputFilePath, "w") as outputHtml:
                outputHtml.write(inlinedHtml)

            print "\nWrote to %s\n" % outputFilePath

        else:
            # No API key
            print "Please insert your MailChimp API key"