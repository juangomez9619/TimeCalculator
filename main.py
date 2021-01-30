# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


# print(add_time("11:40 AM", "28:00"))

# print(add_time("11:40 AM", "48:00",'sunday'))
# Run unit tests automatically
main(module='test_module', exit=False)

