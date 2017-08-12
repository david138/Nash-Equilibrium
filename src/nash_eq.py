import sys
from nash_grid import NashGrid

ng = NashGrid(sys.argv[1])
for arg in sys.argv:
    if arg == "-p":
        ng.print_pure_strategies()
    if arg == "-m":
        ng.print_mixed_strategies()
