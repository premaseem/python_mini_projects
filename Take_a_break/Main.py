__author__ = 'premaseem'

import time
import webbrowser


print
try :
    wait_time = int(raw_input("Enter your break rhythm ? Enter 20 to take break after 20 min  "))
except :
    print "please try again and enter integer / number "
    wait_time = int(raw_input("Enter your break rhythm ? Enter 20 to take break after 20 min"))

print "Program started at {} Break music would repeat after every {} min".format(time.ctime(), wait_time)


while True :
# time.sleep(2*60*60)
    time.sleep(wait_time * 60)

# will open song in browser -  Give Your Heart a Break (Official Video)
    webbrowser.open("https://www.youtube.com/watch?v=1zfzka5VwRc")