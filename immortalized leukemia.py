
#Saving this code because it could potentially be the worst code that ive ever written in my life

#its the result of me not understanding what the fuck i needed to do before i coded it

#fucks sake

# find the snapshot .jar and delete it so that python doesnt get confused

find_snapshot = os.listdir("./")

# prep for aids btw

for i in find_snapshot:
    # split current element
    findme = i.split()

    # counter to save place
    counter = + 1

    # iterate through current element

    for i in findme:
        # if it sees snapshot, tell python
        if i.lower() == "snapshot":
            found = True
            break

        else:
            continue

    if found == True:
        delsnapshot(found, find_snapshot[counter])
        break

    elif not found:
        break




def delsnapshot(found, snapshot):
    if found == True:
        os.remove(snapshot)
        print("Deleted snapshot file (just so python doesnt get confused, its delicate <3)")
        return True
    elif not found:
        print("Could not find snapshot file, will continue anyway but marshalsec may error out.")
        return True

