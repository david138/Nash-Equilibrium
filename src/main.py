from nash_grid import NashGrid
import nash_functions

pd = NashGrid("pd.txt")
print(pd.get_payout_grid())
print(pd.get_col_labels())