
# break can be used to exit a loop early when a certain condition is met.
# continue can be used to skip one loop iteration when a certain condition is met

# range() function can be used to create a sequence of numbers, which can be used in a for loop

# while loops can be used to repeat a block of code while a certain condition is met
# use ctrl + c to exit a while loop if it is running forever

lorry = 0

while lorry < 20:
    lorry += 1
    if lorry % 2 == 0:
        print(f"HGV {lorry} requires inspection.")
    