terminal_state = input('Is the terminal open? yes/no:').lower()
information_age = int(input('How old is the information? (in minutes):'))
freshness_threshold = int(input('What is the freshness threshold? (in minutes):'))

if terminal_state == 'yes' and information_age <= freshness_threshold:
    print('Assign HGV to slot.')
elif terminal_state == 'yes' and information_age > freshness_threshold:
    print('Do not assign yet. Information is too old.')
elif terminal_state == 'no':
    print('Do not assign yet. No slot available.')
else:
    print('Invalid input. Please enter "yes" or "no" for terminal state.')
