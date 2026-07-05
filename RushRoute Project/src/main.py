import sys
from cli import process_file

failed = process_file("data/deliveries.json")

if failed:
    sys.exit(1)

sys.exit(0)