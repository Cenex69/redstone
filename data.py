cx = {
    1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False,
    11: False, 12: False, 13: False, 14: False, 15: False, 16: False, 17: False, 18: False, 19: False, 20: False,
    21: False, 22: False, 23: False, 24: False, 25: False, 26: False, 27: False, 28: False, 29: False, 30: False,
    31: False, 32: False, 33: False, 34: False, 35: False, 36: False, 37: False, 38: False, 39: False, 40: False,
    41: False, 42: False, 43: False, 44: False, 45: False, 46: False, 47: False, 48: False, 49: False, 50: False,
    51: False, 52: False, 53: False, 54: False, 55: False, 56: False, 57: False, 58: False, 59: False, 60: False,
    61: False, 62: False, 63: False, 64: False, 65: False, 66: False, 67: False, 68: False, 69: False, 70: False,
    71: False, 72: False, 73: False, 74: False, 75: False, 76: False, 77: False, 78: False, 79: False, 80: False,
    81: False, 82: False, 83: False, 84: False, 85: False, 86: False, 87: False, 88: False, 89: False, 90: False,
    91: False, 92: False, 93: False, 94: False, 95: False, 96: False, 97: False, 98: False, 99: False, 100: False,
    "axis": "x"
}
cy = {
    1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False,
    11: False, 12: False, 13: False, 14: False, 15: False, 16: False, 17: False, 18: False, 19: False, 20: False,
    21: False, 22: False, 23: False, 24: False, 25: False, 26: False, 27: False, 28: False, 29: False, 30: False,
    31: False, 32: False, 33: False, 34: False, 35: False, 36: False, 37: False, 38: False, 39: False, 40: False,
    41: False, 42: False, 43: False, 44: False, 45: False, 46: False, 47: False, 48: False, 49: False, 50: False,
    51: False, 52: False, 53: False, 54: False, 55: False, 56: False, 57: False, 58: False, 59: False, 60: False,
    61: False, 62: False, 63: False, 64: False, 65: False, 66: False, 67: False, 68: False, 69: False, 70: False,
    71: False, 72: False, 73: False, 74: False, 75: False, 76: False, 77: False, 78: False, 79: False, 80: False,
    81: False, 82: False, 83: False, 84: False, 85: False, 86: False, 87: False, 88: False, 89: False, 90: False,
    91: False, 92: False, 93: False, 94: False, 95: False, 96: False, 97: False, 98: False, 99: False, 100: False,
    "axis": "y"
}
bx = {
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
by = {
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


def send(item: str):
    if item == "coords:x":
        return cx
    elif item == "coords:y":
        return cy
    elif item == "block_update:x":
        return bx
    elif item == "block_update:y":
        return by
    elif item == "block_types:list":
        return block_types
    elif item == "block_names:list":
        return block_names


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
    elif item == "block_update:x":
        strIn, intIn = str(char.split(':')[1]), int(char.split(':')[0])
        if intIn < 101 and intIn > 0:
            bx[intIn] = strIn
        else:
            if intIn < 1:
                print("provided Integer must be over 0.")
            elif intIn > 100:
                print("provided Integer must be less than or equal to 100.")
    elif item == "block_update:y":
        strIn, intIn = str(char.split(':')[1]), int(char.split(':')[0])
        if intIn < 101 and intIn > 0:
            by[intIn] = strIn
        else:
            if intIn < 1:
                print("provided Integer must be over 0.")
            elif intIn > 100:
                print("provided Integer must be less than or equal to 100.")
    elif item == "block_name:list" or "block_type:list":
        print("this list cannot be updated.")
