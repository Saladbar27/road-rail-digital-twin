
lorries = int(input('How many HGVs are arriving today?'))
slots = int(input('How many slots are available?'))

for hgv in range(1, lorries + 1):
    if slots >= hgv:
        print(f'HGV {hgv} assigned.')
    else:
        print(f'HGV {hgv} waiting.')