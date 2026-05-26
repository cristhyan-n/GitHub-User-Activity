
def display_activity(events):
    for event in events :
        print(f"{event['type']} - {event['repo']['name']}")