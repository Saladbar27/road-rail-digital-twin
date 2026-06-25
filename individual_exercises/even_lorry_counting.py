
# this program prints even numbered values in a loop up to 20.

lorry = 0

while lorry < 20:
    lorry += 1
    if lorry % 2 == 0:
        print(f"HGV {lorry} requires inspection.")
    else:
        break