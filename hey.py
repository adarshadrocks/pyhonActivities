#!/usr/bin/python
import time
import os
import webbrowser
option='''
press 1 : current date and time
press 2 : To create a file
press 3 : To create a directory
press 4 : To search on google
press 5 : logout your system
press 6 : Shutdown your os
press 7 : To check internet connection in your pc
press 8 : To login watsapp on browser
press 9 : To check all connected IP in your network
'''
print(option)
select = raw_input("kindly press atleat one")
if select == '1' :
        time = time.ctime().split()
        print "displaying current date&time" +time[3],time[1],time[2]

elif select == '2' :
        path = "/home/adarsh/Desktop/"
        filename=raw_input("enter the name of file")
        os.system('touch ' +path+filename)
        print "your file is created"

elif select == '3' :
        path = "/home/adarsh/Desktop/"
        dirname=raw_input("enter the name of directory")
        os.system('mkdir ' +path+dirname)
        print "your directory is created"

elif select == '4' :
        print "searching on google"
        msg = raw_input("type for search")
        webbrowser.open_new_tab('https://www.google.com/search?q='+msg)

elif select == '5' :
        print "turn off your application your system is going to be off"
        time.sleep(2)
        msg1 = "fr se bol rha hu last chance"
        os.system('echo '+msg1+' | festival --tts')
        time.sleep(2)
        os.system("pkill -KILL -u " + os.getlogin())

elif select == '6' :
        print "turn off your application your system is going to be off"
        time.sleep(2)
        msg1 = "fr se bol rha hu last chance"
        os.system('echo '+msg1+' | festival --tts')
        time.sleep(2)
        os.system('poweroff')

elif select == '8' :
        print "opening watsapp app on google"
        time.sleep(2)
        webbrowser.open_new_tab('https://www.watsapp.com')


else :
        print "chutiya h ka be"

