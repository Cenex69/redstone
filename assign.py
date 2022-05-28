from data import send, receive
block_names = send("block_names:list")
block_types = send("block_types:list")
cx = send('coords:x')
cy = send('coords:y')
bx = send('block_update:x')
by = send('block_update:y')
block = {
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


def assign(rx: str, rx2: str):
    bn, cdx, cdy = rx, int(rx2.split(':')[0]), int(rx2.split(':'))[1]
    if cdx or cdy > 100:
        print("provided Integer must be less than or equal to 100.")
    elif bn not in block_names:
        print("unknown block type")
