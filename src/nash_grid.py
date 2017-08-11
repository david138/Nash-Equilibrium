import numpy as np

P1 = 0
P2 = 1

class NashGrid:
    def __init__(self, addr):
        file = open(addr, "r")
        self.payout_grid = self.generate_payout_grid(file)
        self.row_labels = self.generate_labels(len(self.payout_grid))
        self.col_labels = self.generate_labels(len(self.payout_grid[0]))
        file.close()

    def generate_payout_grid(self, file):
        payout_grid = []
        for line in file:
            row_array = []
            for payouts in line.split(" "):
                row_array.append([int(payout) for payout in payouts.split(",")])
            payout_grid.append(row_array)
        return payout_grid;

    def generate_labels(self, labels_num):
        return [i for i in range(labels_num)];

    def remove_dominated_moves(self):
        while self.remove_dominated_p1() | self.remove_dominated_p2():
            pass

    def remove_dominated_p1(self):
        rows_to_keep = set()
        row_num = len(self.payout_grid)
        col_num = len(self.payout_grid[0])
        for c in range(col_num):
            max_payout = max([self.payout_grid[r][c][P1] for r in range(row_num)])
            for r in range(row_num):
                if (self.payout_grid[r][c][P1] == max_payout):
                    rows_to_keep.add(r)

        new_payout_grid = [self.payout_grid[i] for i in sorted(rows_to_keep)]
        self.payout_grid = new_payout_grid
        self.row_labels = [self.row_labels[i] for i in sorted(rows_to_keep)]
        return row_num != len(rows_to_keep);

    def remove_dominated_p2(self):
        cols_to_keep = set()
        row_num = len(self.payout_grid)
        col_num = len(self.payout_grid[0])
        for r in range(row_num):
            max_payout = max([self.payout_grid[r][c][P2] for c in range(col_num)])
            for c in range(col_num):
                if (self.payout_grid[r][c][P2] == max_payout):
                    cols_to_keep.add(c)

        new_payout_grid = [[] for _ in range(row_num)]
        for c in sorted(cols_to_keep):
            for r in range(row_num):
                new_payout_grid[r].append(self.payout_grid[r][c])
        self.payout_grid = new_payout_grid
        self.col_labels = [self.col_labels[i] for i in sorted(cols_to_keep)]
        return col_num != len(cols_to_keep);

    def pure_strategy_solutions(self):
        best_payouts = {}
        row_num = len(self.payout_grid)
        col_num = len(self.payout_grid[0])
        for c in range(col_num):
            max_payout = max([self.payout_grid[r][c][P1] for r in range(row_num)])
            for r in range(row_num):
                if (self.payout_grid[r][c] == max_payout):
                    best_payouts[(r, c)] = (self.row_labels[r], self.row_labels[c])

        best_payout_labels = []
        for r in range(row_num):
            max_payout = max([self.payout_grid[r][c][P2] for c in range(col_num)])
            for c in range(col_num):
                if (self.payout_grid[r][c] == max_payout):
                    if best_payouts.has_key((r, c)):
                        best_payout_labels.append(best_payouts[(r, c)])
        return best_payout_labels;

    def mixed_strategy_solutions(self):
        self.remove_dominated_moves()
        side_length = len(self.payout_grid)
        if (side_side == 1):
            return ([1], self.row_labels, [1], self.col_labels);

        p1_outcomes = [[1] for _ in range(side_length)]
        for c in range(1, side_length):
            p1_outcomes.append([self.payout_grid[r][c] - self.payout_grid[r][0] for r in range(side_length)])
        p1_solutions = [1] + [0 for i in range(side_length - 1)]
        p1_move_percents = np.linalg.solve(np.array(p1_outcomes), np.array(p1_solutions))

        p2_outcomes = [[1 for l in range(side_length)]]
        for r in range(1, side_length):
            p2_outcomes.append([self.payout_grid[r][c] - self.payout_grid[0][c] for c in range(side_length)])
        p2_solutions = [1] + [0 for i in range(side_length - 1)]
        p2_move_percents = np.linalg.solve(np.array(p2_outcomes), np.array(p2_solutions))

        return (p1_move_percents, self.row_labels, p2_move_percents, self.col_labels);
