"""This minimal example shows a problem in tkinter's wait_variable.
If one closes the root window while wait_variable is executing,
the prompt never comes back. ^C has no effect.
Using atexit does not help.
One can work around the problem by binding to <Destroy>
(see commented out code below).
"""
import tkinter

root = tkinter.Tk()
waitVar = tkinter.BooleanVar()
isDone = False


def trigger():
    global waitVar
    waitVar.set(True)


def script():
    global isDone, waitVar
    for count in range(10):
        print
        "script", count
        if not isDone:
            root.after(1000, trigger)
            root.wait_variable(waitVar)
        else:
            print
            "script cancelled"
            return
    print
    "script done"


# uncomment the following to work around the problem:
# def delWin(evt):
#	global isDone
#	print "delWin"
#	isDone = True
#	trigger()
# root.bind("<Destroy>", delWin)

script()

root.mainloop()