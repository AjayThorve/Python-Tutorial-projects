import urllib
def read_text():
    quotes=open("movie_quotes.txt")
    text=quotes.read()
    quotes.close()
    check_profanity(text)

def check_profanity(text):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output=connection.read()
    connection.close()
    if "true" in output:
        print "profanity alert!"
    elif "false" in output:
        print "No curse words found in this document"
    else:
        print "scan error"
read_text()