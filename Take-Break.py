import webbrowser
import time
print "this program started on",time.ctime()
for i in range(0,3):
    time.sleep(10)
    webbrowser.open("http://www.youtube.com")