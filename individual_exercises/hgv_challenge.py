
import random

print()

hgv_count = 10
freshness_threshold = 5

# Empty Dictionary that will later store information on each HGV
lorries = []

def generate_hgv_id():
    """Generates a random value for the HGV ID, 1000 - 9999"""
    return random.randint(1000, 9999)

def generate_information_age():
    """Generates a random value for the HGV Information Age, 0 - 10 minutes"""
    return random.randint(0, 10)

def generate_arrival_time():
    """Generates a random value for the HGV Arrival Time, 0 - 360 minutes"""
    time_in_minutes = random.randint(0, 360)
    hours = time_in_minutes // 60
    minutes = time_in_minutes % 60
    return "%02d:%02d" % (hours, minutes)

def determine_signal_zone(hgv):
    """Determines the signal strength: patchy on even numbers, none on every third"""
    if hgv % 3 == 0:
        return 'None'
    elif hgv % 2 == 0:
        return 'Patchy'
    else:
        return 'Good'

def determine_twin_status(hgv):
    """Determines twin status based on the signal zone"""
    signal_zone = determine_signal_zone(hgv)
    if signal_zone == 'None':
        return 'Unavailable'
    elif signal_zone == 'Patchy':
        return 'Updates Delayed'
    else:
        return 'Receiving Updates'
    
def determine_hgv_decision(hgv, information_age):
    """Determines the action the twin should take based on signal zone."""
    signal_zone = determine_signal_zone(hgv)
    if signal_zone == 'None' or information_age > freshness_threshold:
        return 'Delay Assignment'
    elif signal_zone == 'Patchy':
        return 'Monitor Closely'
    else:
        return 'Continue Normally'

def create_hgv_dict(hgv, hgv_id, information_age, arrival_time):
    """Creates a dictionary for the HGV including HGV ID, signal zone, and twin status"""
    signal_zone = determine_signal_zone(hgv)
    twin_status = determine_twin_status(hgv)
    hgv_decision = determine_hgv_decision(hgv, information_age)
    hgv_dict = {
        'ID': hgv_id, 
        'Signal Zone': signal_zone, 
        'Twin Status': twin_status, 
        'Information Age': information_age, 
        'Decision': hgv_decision, 
        'Arrival Time': arrival_time}
    lorries.append(hgv_dict)
    return hgv_dict

def display_hgv_information(hgv, hgv_id, information_age, arrival_time):
    """Displays the generated HGV ID, signal zone, twin status, and information age"""
    signal_zone = determine_signal_zone(hgv)
    twin_status = determine_twin_status(hgv)
    hgv_decision = determine_hgv_decision(hgv, information_age)
    print(f'HGV {hgv_id}')
    print(f'Signal Zone: {signal_zone}')
    print(f'Twin Status: {twin_status}')
    if information_age == 1:
        print(f'Information Age: {information_age} minute')
    else:
        print(f'Information Age: {information_age} minutes')
    print(f'ETA: {arrival_time}')
    print(f'HGV Decision: {hgv_decision}')

for hgv in range(1, hgv_count + 1):
    hgv_id = generate_hgv_id()
    information_age = generate_information_age()
    arrival_time = generate_arrival_time()
    display_hgv_information(hgv, hgv_id, information_age, arrival_time)
    create_hgv_dict(hgv, hgv_id, information_age, arrival_time)
    print()

for lorry in lorries:
    print(lorry)
    print()

good_signal_hgv = 0
patchy_signal_hgv = 0
no_signal_hgv = 0
delayed_hgv = 0
closely_monitored_hgv = 0
continuing_normally_hgv = 0

# Summary Statistics
for lorry in lorries:
    signal_zone = lorry['Signal Zone']
    hgv_decision = lorry['Decision']

    if signal_zone == 'Good':
        good_signal_hgv += 1
    elif signal_zone == 'Patchy':
        patchy_signal_hgv += 1
    elif signal_zone == 'None':
        no_signal_hgv += 1

    if hgv_decision == 'Delay Assignment':
        delayed_hgv += 1
    elif hgv_decision == 'Monitor Closely':
        closely_monitored_hgv += 1
    elif hgv_decision == 'Continue Normally':
        continuing_normally_hgv += 1

total_information_age = 0

for lorry in lorries:
    total_information_age += lorry['Information Age']

average_information_age = total_information_age / hgv_count


def display_hgv_statistics():
    """Displays the number of HGVs with various signals, various decisions, and average information age"""
    print(f'Number of HGVs with Good Signal: {good_signal_hgv}')
    print(f'Number of HGVs with Patchy Signal: {patchy_signal_hgv}')
    print(f'Number of HGVs with No Signal: {no_signal_hgv}')
    print(f'Number of HGVs Continued Normally: {continuing_normally_hgv}')
    print(f'Number of HGVs being Closely Monitored: {closely_monitored_hgv}')
    print(f'Number of Delayed HGVs: {delayed_hgv}')
    print(f'Average Information Age: {average_information_age} minutes')

display_hgv_statistics()

print()
