import sys
from api import get_activity
from formatter import display_activity

if len(sys.argv) < 2:
    print("Insira um argumento válido.")
    sys.exit(1)

get_event = get_activity(sys.argv[1])
display_activity(get_event)
