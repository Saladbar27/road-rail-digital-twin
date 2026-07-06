
import random

print()

SIGNAL_GOOD = 'Good'
SIGNAL_PATCHY = 'Patchy'
SIGNAL_NONE = 'None'

DECISION_DELAY = 'Delay Assignment'
DECISION_MONITOR = 'Monitor Closely'
DECISION_CONTINUE = 'Continue Normally'
DECISION_HIGH_PRIORITY = 'High Priority Review'

KEY_ID = 'ID'
KEY_SIGNAL_ZONE = 'Signal Zone'
KEY_TWIN_STATUS = 'Twin Status'
KEY_INFORMATION_AGE = 'Information Age'
KEY_DECISION = 'Decision'

# Number of HGVs in the Simulation
hgv_count = 10

# The number of minutes at which the information age is considered too old to be reliable
freshness_threshold = 5

# Empty Dictionary that will later store information on each HGV
lorries = []

# List of all transport hubs in the simulation, used to randomly assign a location to each HGV
transport_hub_list = [
    'Aberdeen Harbour', 
    'Cairnryan Port', 
    'Edinburgh Airport', 
    'Eurocentral',
    'Fourth Ports Locations',
    'Freightliners Coatbridge Terminal',
    'Glasgow Prestwick Airport',
    'Glensanda',
    'Hillington Park',
    'Orkley Islands Harbur Authority Locations'
]

def determine_current_location():
    """Randomly selects a transport hub from transport_hub_list"""
    return random.choice(transport_hub_list)

# List of all terminal slot options
terminal_slot_list = [
    'None',
    'A',
    'B',
    'C'
]

def determine_current_terminal_slot():
    """Randomly selects a terminal slot option from terminal_slot_list"""
    return random.choice(terminal_slot_list)

# List of most common types of cargo being transported on rail and road freight lines in the United Kingdom
cargo_type_list = [
    'Shipping Container',
    'Bulk Liquids',
    'Automotive',
    'Construction Materials',
    'Retail Consumer Goods'
]

def determine_cargo_type():
    """Randomly selects a type of cargo from cargo_type_list"""
    return random.choice(cargo_type_list)

hgv_status_list = [
    'Travelling',
    'Waiting',
    'Assigned',
    'Unloading'
]

def generate_hgv_id():
    """Generates a random value for the HGV ID, 1000 - 9999"""
    return random.randint(1000, 9999)

def generate_information_age():
    """Generates a random value for the HGV Information Age, 0 - 10 minutes"""
    return random.randint(0, 10)

def generate_arrival_time():
    """Generates ETA in minutes, 0 - 360 minutes"""
    return random.randint(0, 360)

def format_arrival_time(time_in_minutes):
    """Formats the arrival time as HH:MM"""
    hours = time_in_minutes // 60
    minutes = time_in_minutes % 60
    return "%02d:%02d" % (hours, minutes)

def determine_signal_zone(hgv):
    """Determines the signal strength: patchy on even numbers, none on every third"""
    if hgv % 3 == 0:
        return SIGNAL_NONE
    elif hgv % 2 == 0:
        return SIGNAL_PATCHY
    else:
        return SIGNAL_GOOD

def determine_hgv_status():
    return random.choice(hgv_status_list)

def determine_twin_status(hgv):
    """Determines twin status based on the signal zone"""
    signal_zone = determine_signal_zone(hgv)
    if signal_zone == SIGNAL_NONE:
        return 'Unavailable'
    elif signal_zone == SIGNAL_PATCHY:
        return 'Updates Delayed'
    else:
        return 'Receiving Updates'
    
def determine_hgv_decision(hgv, information_age, eta_minutes):
    """Determines the action the twin should take based on signal zone."""
    signal_zone = determine_signal_zone(hgv)

    if information_age > freshness_threshold and eta_minutes < 30:
        return DECISION_HIGH_PRIORITY
    elif signal_zone == SIGNAL_NONE or information_age > freshness_threshold:
        return DECISION_DELAY
    elif signal_zone == SIGNAL_PATCHY:
        return DECISION_MONITOR
    else:
        return DECISION_CONTINUE

def create_hgv_dict(hgv, hgv_id, information_age, arrival_time):
    """Creates a dictionary for the HGV including all relevant information"""
    signal_zone = determine_signal_zone(hgv)
    twin_status = determine_twin_status(hgv)
    hgv_decision = determine_hgv_decision(hgv, information_age, arrival_time)
    hgv_location = determine_current_location()
    hgv_terminal_slot = determine_current_terminal_slot()
    hgv_cargo_type = determine_cargo_type()
    hgv_status = determine_hgv_status()
    hgv_dict = {
        KEY_ID: hgv_id,
        KEY_SIGNAL_ZONE: signal_zone,
        KEY_TWIN_STATUS: twin_status,
        KEY_INFORMATION_AGE: information_age,
        KEY_DECISION: hgv_decision,
        'Arrival Time': arrival_time,
        'Location': hgv_location,
        'Terminal Slot': hgv_terminal_slot,
        'Cargo Type': hgv_cargo_type,
        'HGV Status': hgv_status}
    lorries.append(hgv_dict)
    return hgv_dict

def display_hgv_information(hgv_dict):
    """Displays the generated HGV Information"""
    hgv_decision = hgv_dict['Decision']
    hgv_location = hgv_dict['Location']
    hgv_terminal_slot = hgv_dict['Terminal Slot']
    hgv_cargo_type = hgv_dict['Cargo Type']
    hgv_status = determine_hgv_status()
    print(f"HGV {hgv_dict['ID']}")
    print(f"Signal Zone: {hgv_dict['Signal Zone']}")
    print(f"Twin Status: {hgv_dict['Twin Status']}")
    if hgv_dict['Information Age'] == 1:
        print(f'Information Age: {hgv_dict["Information Age"]} minute')
    else:
        print(f'Information Age: {hgv_dict["Information Age"]} minutes')
    print(f'ETA: {format_arrival_time(hgv_dict["Arrival Time"])}')
    print(f'HGV Decision: {hgv_decision}')
    print(f'HGV Current Location: {hgv_location}')
    print(f'HGV Terminal Slot: {hgv_terminal_slot}')
    print(f'HGV Cargo Type: {hgv_cargo_type}')
    print(f'HGV Status: {hgv_status}')

# Main Program Loop
for hgv in range(1, hgv_count + 1):
    hgv_id = generate_hgv_id()
    information_age = generate_information_age()
    arrival_time = generate_arrival_time()

    hgv_dict = create_hgv_dict(hgv, hgv_id, information_age, arrival_time)
    display_hgv_information(hgv_dict)
    print()

# Displays all HGVs in the Lorries List
for lorry in lorries:
    print(lorry)
    print()

# Summary Statistics Variables
good_signal_hgv = 0
patchy_signal_hgv = 0
no_signal_hgv = 0
delayed_hgv = 0
closely_monitored_hgv = 0
continuing_normally_hgv = 0
high_priority_review_hgv = 0

# Summary Statistics
for lorry in lorries:
    signal_zone = lorry[KEY_SIGNAL_ZONE]
    hgv_decision = lorry[KEY_DECISION]

    if signal_zone == SIGNAL_GOOD:
        good_signal_hgv += 1
    elif signal_zone == SIGNAL_PATCHY:
        patchy_signal_hgv += 1
    elif signal_zone == SIGNAL_NONE:
        no_signal_hgv += 1

    if hgv_decision == DECISION_DELAY:
        delayed_hgv += 1
    elif hgv_decision == DECISION_MONITOR:
        closely_monitored_hgv += 1
    elif hgv_decision == DECISION_CONTINUE:
        continuing_normally_hgv += 1
    elif hgv_decision == DECISION_HIGH_PRIORITY:
        high_priority_review_hgv += 1

# Variable to hold the total information age of all HGVs
total_information_age = 0

# Loop that updates the total information age variable with the information age of each HGV
for lorry in lorries:
    total_information_age += lorry[KEY_INFORMATION_AGE]

# Calculates the average information age for all HGVs
average_information_age = total_information_age / hgv_count

delayed_hgv_num = 0
monitored_hgv_num = 0
good_signal_hgv_num = 0
stale_information_hgv_num = 0

for lorry in lorries:
    if lorry[KEY_DECISION] == DECISION_DELAY:
        delayed_hgv_num += 1
    elif lorry[KEY_DECISION] == DECISION_MONITOR:
        monitored_hgv_num += 1

    if lorry[KEY_SIGNAL_ZONE] == SIGNAL_GOOD:
        good_signal_hgv_num += 1

    if lorry[KEY_INFORMATION_AGE] > freshness_threshold:
        stale_information_hgv_num += 1

percentage_hgv_delayed = (delayed_hgv_num / hgv_count) * 100
monitored_hgv_percentage = (monitored_hgv_num / hgv_count) * 100
good_signal_hgv_percentage = (good_signal_hgv_num / hgv_count) * 100
stale_information_hgv_percentage = (stale_information_hgv_num / hgv_count) * 100

def display_hgv_statistics():
    """Displays a number of statistics about the HGVs in the simulation"""
    print(f'Number of HGVs with Good Signal: {good_signal_hgv}')
    print(f'Number of HGVs with Patchy Signal: {patchy_signal_hgv}')
    print(f'Number of HGVs with No Signal: {no_signal_hgv}')
    print(f'Number of HGVs Continued Normally: {continuing_normally_hgv}')
    print(f'Number of HGVs being Closely Monitored: {closely_monitored_hgv}')
    print(f'Number of Delayed HGVs: {delayed_hgv}')
    print(f'Number of HGVs with High Priority Review: {high_priority_review_hgv}')
    print(f'Average Information Age: {average_information_age} minutes')
    print(f'Percentage of HGVs Delayed: {percentage_hgv_delayed:.2f}%')
    print(f'Percentage of HGVs Monitored: {monitored_hgv_percentage:.2f}%')
    print(f'Percentage of HGVs with Good Signal: {good_signal_hgv_percentage:.2f}%')
    print(f'Percentage of HGVs with Stale Information: {stale_information_hgv_percentage:.2f}%')

# Runs the display_hgv_statistics function to show the summary statistics of the HGVs
display_hgv_statistics()

print()
