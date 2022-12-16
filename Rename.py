def SelectedJoints(selected):
    rawSelect = selected
    newRaw = []
    objectList = []
    for x in range(len(selected)):
        testStr = selected[x].split("|")
        objectList.append(testStr[len(testStr)-1])
    selected = objectList
    for i in range(len(selected)): 


        stNum = selected[i].index("_")
        enNum = selected[i].rindex("_")

        rep = "_"
        suffix = selected[i].rpartition(rep)
        prefix = selected[i].partition(rep)
        prefix = prefix[0] + prefix[1]
        suffix = suffix[1] + suffix[2]
        fill = (enNum - stNum) - 1
        numStr = str(i+1)
        rawB = rawSelect
        cmds.rename(rawSelect[i],"%s%s%s" % (prefix, numStr.zfill(fill), suffix))
        rawSelect[i] = cmds.ls(sl=True,long=True) or []
        rawA = rawSelect
        
objects = cmds.ls(sl=True,long=True) or []
uScore = True
for j in range(len(objects)):
    if "_" in objects[j]:
        uScore = True
    else:
        uScore = False
        break
        
if uScore == True:
    SelectedJoints(objects)
else:
    print("Invalid Names")