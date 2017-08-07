def remove_dominated_moves(nash_grid):
    removed_total = 0
    removed_num = -1
    while (removed != 0): 
        removed_num = remove_dominated_p1(nash_grid)
        removed_num += removeDominatedP2(nash_grid)
        removed_total += removed_num
    return ("Optimized! " + removed_total + " moves removed");

def remove_dominated_p1(nash_grid):
    rows_to_keep = set()
    payout_grid = nash_grid.get_payout_grid
    for c in range(nash_grid.get_cols):
        max_payout = max([payout_grid[r][c][P1] for r in range(nash_grid.get_rows)])
        for r in range(nash_grid.get_rows):
            if (payout_grid[r][c] == max_payout):
                rows_to_keep.update(r)

    new_payout_grid = [payout_grid[i] for i in sorted(rows_to_keep)]
    nash_grid.set_payout_grid(new_payout_grid)
    nash_grid.set_row_labels([nash_grid.get_row_labels[i] for i in sorted(rows_to_keep)])
    return len(payout_grid) - len(rows_to_keep);

def remove_dominated_p2(nash_grid):
    cols_to_keep = set()
    payout_grid = nash_grid.get_payout_grid
    for r in range(nash_grid.get_rows):
        max_payout = max([payout_grid[r][c][P2] for c in range(nash_grid.get_cols)])
        for c in range(nash_grid.get_cols):
            if (payout_grid[r][c] == max_payout):
                cols_to_keep.update(c)

    new_payout_grid = [[] for i in range(nash_grid.get_rows)]
    for c in sorted(cols_to_keep):
        for r in new_payout_grid:
            r.append(payout_grid[r][c])
    nash_grid.set_payout_grid(new_payout_grid)
    nash_grid.set_col_labels([nash_grid.get_col_labels[i] for i in sorted(cols_to_keep)])
    return len(payout_grid) - len(cols_to_keep);