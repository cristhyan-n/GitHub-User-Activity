
def display_activity(events):
    for event in events :
        if event["type"] == "PushEvent":
            print(f"Pushed to {event['repo']['name']}")
            
        elif event["type"] == "IssuesEvent":
            print(f"Opened an issue in {event['repo']['name']}")

        elif event["type"] == "WatchEvent":
            print(f"Starred {event['repo']['name']}")

        elif event["type"] == "ForkEvent":
            print(f"Forked {event['repo']['name']}")

        elif event["type"] == "CreateEvent":
            print(f"Created {event['repo']['name']}")

        elif event["type"] == "PullRequestEvent":
            print(f"Opened a pull request in {event['repo']['name']}")
        else:
            print(f"Unknown event: {event['type']} in {event['repo']['name']}")
