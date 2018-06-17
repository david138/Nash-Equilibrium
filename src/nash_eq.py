import sys
from nash_grid import NashGrid

ng = NashGrid(sys.argv[1])
for arg in sys.argv:
    if arg == "-p":
        ng.compute_pure_strategies()
    if arg == "-m":
        ng.compute_mixed_strategies()
