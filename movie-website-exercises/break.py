import webbrowser
import time

total_break=3
total_count=0
print "your program starts at "+ time.ctime()
while total_count < total_break :
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=kpCJyQ2usJ4")
    total_count=total_count + 1
    
