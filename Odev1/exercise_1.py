# Shut down program

def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted "
    else:
        return "Sorry"


choice = input("Want you to shut down your computer ? ")
print(shut_down(choice))
