cx = {
    1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "",
    11: "", 12: "", 13: "", 14: "", 15: "", 16: "", 17: "", 18: "", 19: "", 20: "",
    21: "", 22: "", 23: "", 24: "", 25: "", 26: "", 27: "", 28: "", 29: "", 30: "",
    31: "", 32: "", 33: "", 34: "", 35: "", 36: "", 37: "", 38: "", 39: "", 40: "",
    41: "", 42: "", 43: "", 44: "", 45: "", 46: "", 47: "", 48: "", 49: "", 50: "",
    51: "", 52: "", 53: "", 54: "", 55: "", 56: "", 57: "", 58: "", 59: "", 60: "",
    61: "", 62: "", 63: "", 64: "", 65: "", 66: "", 67: "", 68: "", 69: "", 70: "",
    71: "", 72: "", 73: "", 74: "", 75: "", 76: "", 77: "", 78: "", 79: "", 80: "",
    81: "", 82: "", 83: "", 84: "", 85: "", 86: "", 87: "", 88: "", 89: "", 90: "",
    91: "", 92: "", 93: "", 94: "", 95: "", 96: "", 97: "", 98: "", 99: "", 100: "",
    "axis": "x"
}
cy = {
    1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "",
    11: "", 12: "", 13: "", 14: "", 15: "", 16: "", 17: "", 18: "", 19: "", 20: "",
    21: "", 22: "", 23: "", 24: "", 25: "", 26: "", 27: "", 28: "", 29: "", 30: "",
    31: "", 32: "", 33: "", 34: "", 35: "", 36: "", 37: "", 38: "", 39: "", 40: "",
    41: "", 42: "", 43: "", 44: "", 45: "", 46: "", 47: "", 48: "", 49: "", 50: "",
    51: "", 52: "", 53: "", 54: "", 55: "", 56: "", 57: "", 58: "", 59: "", 60: "",
    61: "", 62: "", 63: "", 64: "", 65: "", 66: "", 67: "", 68: "", 69: "", 70: "",
    71: "", 72: "", 73: "", 74: "", 75: "", 76: "", 77: "", 78: "", 79: "", 80: "",
    81: "", 82: "", 83: "", 84: "", 85: "", 86: "", 87: "", 88: "", 89: "", 90: "",
    91: "", 92: "", 93: "", 94: "", 95: "", 96: "", 97: "", 98: "", 99: "", 100: "",
    "axis": "y"
}
block_types = ["scaffolding", "dust", "torch", "repeater", "comparator", "observer", "output", "input"]
block_names = ["Stone", "Oak Planks", "Smooth Stone", "Redstone Dust", "Redstone Torch", "Redstone Repeater", "Redstone Comparator", "Observer", "Redstone Lamp", "Button", "Lever"]
block_organised = {
    block_names[0]: block_types[0],
    block_names[2]: block_types[0],
    block_names[1]: block_types[0],
    block_names[3]: block_types[1],
    block_names[4]: block_types[2],
    block_names[5]: block_types[3],
    block_names[6]: block_types[4],
    block_names[7]: block_types[5],
    block_names[8]: block_types[6],
    block_names[9]: block_types[7],
    block_names[10]: block_types[7],
}

0
def send(item: str):
    if item == "coords:x":
        return cx
    elif item == "coords:y":
        return cy
    elif item == "block_types":
        return block_types
    elif item == "block_names":
        return block_names
    elif item == "block_organised":
        return block_organised


def receive(item: str, char: str):
    if item == "coords:x":
        booleanIn, intIn = bool(char.split(':')[1]), int(char.split(':')[0])
        if intIn < 101 and intIn > 0:
            cx[intIn] = booleanIn
        else:
            if intIn < 1:
                print("provided Integer must be over 0.")
            elif intIn > 100:
                print("provided Integer must be less than or equal to 100.")
    elif item == "coords:y":
        booleanIn, intIn = bool(char.split(':')[1]), int(char.split(':')[0])
        if intIn < 101 and intIn > 0:
            cy[intIn] = booleanIn
        else:
            if intIn < 1:
                print("provided Integer must be over 0.")
            elif intIn > 100:
                print("provided Integer must be less than or equal to 100.")
