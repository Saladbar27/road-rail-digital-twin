
lorries = int(input('How many HGVs are arriving today?'))

for hgv in range(1, lorries + 1):
    print(f'HGV {hgv} has arrived.')
    print('Assigning temporary ID...')

    if hgv % 3 == 0:
        print('No signal.')
    else:
        print('Good signal.')