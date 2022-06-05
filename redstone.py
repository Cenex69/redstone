import time


def dust():
    if setOn == True:
        global dustpowered
        global redpowered
        redpowered = True
        dustpowered = True
    else:
        redpowered = False
        dustpowered = False


def lever(poweredOn):
    if poweredOn == True:
        global dustpowered
        dustpowered = True
    else:
        dustpowered = False
    global setOn
    if poweredOn == True:
        setOn = True
    else:
        setOn = False


def torch():
    if setOn == False:
        global dustpowered
        dustpowered = True
    elif setOn == True:
        dustpowered = False


def repeater(s):
    time.sleep(s)


def andgate(inputone, inputtwo):
    if inputone == True and inputtwo == True:
        global dustpowered
        dustpowered = True
    else:
        dustpowered = False


def nand(inputone, inputtwo):
    if inputone == True and inputtwo == True:
        global dustpowered
        dustpowered = False
    else:
        dustpowered = True


def orgate(inputone, inputtwo):
    if inputone == True or inputtwo == True:
        global dustpowered
        dustpowered = True
    else:
        dustpowered = False


def nor(inputone, inputtwo):
    if inputone == True or inputtwo == True:
        global dustpowered
        dustpowered = False
    else:
        dustpowered = True


def xor(inputone, inputtwo):
    if inputone != inputtwo:
        global dustpowered
        dustpowered = True
    elif inputone != redpowered:
        dustpowered = True
    elif inputtwo != redpowered:
        dustpowered = True
    else:
        dustpowered = False


def out(output):
    if output == 'lamp':
        if dustpowered == True:
            print('Lamp is now on!')
        else:
            print('Lamp is now off.')
    elif output == 'door':
        if dustpowered == True:
            print('Door is now open!')
        else:
            print('Door is now closed.')
    elif output == 'tdoor':
        if dustpowered == True:
            print('The trapdoor is now open!')
        else:
            print('The trapdoor is now closed.')
    else:
        print('Error: Output should either be - lamp, door, tdoor.')
