signal = input('Enter signal zone (good, patchy, or none):').lower()

if signal == 'good':
    print('Updates arriving normally.')
elif signal == 'patchy':
    print('Updates may be delayed.')
elif signal == 'none':
    print('No updates available.')
else:
    print('Invalid input.')