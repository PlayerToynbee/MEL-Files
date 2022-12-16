def SelectedJoints(selected):
    objectList = []
    for x in range(len(selected)):
        testStr = selected[x].split("|")
        objectList.append(testStr[len(testStr)-1])
    selected = objectList
    for i in range(len(selected)): 


        stNum = nameOf.index("_")
        enNum = nameOf.rindex("_")

        rep = "_"
        suffix = nameOf.rpartition(rep)
        prefix = nameOf.partition(rep)
        prefix = prefix[0] + prefix[1]
        suffix = suffix[1] + suffix[2]
        fill = (enNum - stNum) - 1
        numStr = str(i+1)
        cmds.rename(selected[i],"%s%s%s" % (prefix, numStr.zfill(fill), suffix))
        
objects = cmds.ls(sl=True,long=True) or []
uScore = True
nameOf = input("Input something like 'NAME_#####_Jnt'\n")
if nameOf.count("_") <= 1:
    uScore = False

         
    
        
if uScore == True:
    SelectedJoints(objects)
else:
    print("Invalid Names")