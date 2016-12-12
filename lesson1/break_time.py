import webbrowser
import time

total_breaks = 3
breaks_taken = 0
work_period = 2*60*60
break_period = 5

print "Start break program at " + time.ctime()


while total_breaks > breaks_taken:
    time.sleep(work_period)
    webbrowser.open("https://www.youtube.com/")
    breaks_taken += 1
    numBreaks = str(breaks_taken)
    print "break #" + numBreaks + " at " + time.ctime()
    time.sleep(break_period)

