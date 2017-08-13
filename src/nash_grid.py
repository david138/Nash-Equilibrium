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
        return list(range(labels_num));

    def remove_strictly_dominated_moves(self):
        while self.remove_strictly_dominated_p1() | self.remove_strictly_dominated_p2():
            pass

    def remove_strictly_dominated_p1(self):
        rows_to_keep = set()
        row_num = len(self.payout_grid)
        col_num = len(self.payout_grid[0])
        for c in range(col_num):
            max_payout = max([self.payout_grid[r][c][P1] for r in range(row_num)])
            for r in range(row_num):
                if self.payout_grid[r][c][P1] == max_payout:
                    rows_to_keep.add(r)

        new_payout_grid = [self.payout_grid[i] for i in sorted(rows_to_keep)]
        self.payout_grid = new_payout_grid
        self.row_labels = [self.row_labels[i] for i in sorted(rows_to_keep)]
        return row_num != len(rows_to_keep);

    def remove_strictly_dominated_p2(self):
        cols_to_keep = set()
        row_num = len(self.payout_grid)
        col_num = len(self.payout_grid[0])
        for r in range(row_num):
            max_payout = max([self.payout_grid[r][c][P2] for c in range(col_num)])
            for c in range(col_num):
                if self.payout_grid[r][c][P2] == max_payout:
                    cols_to_keep.add(c)

        new_payout_grid = [[] for _ in range(row_num)]
        for c in sorted(cols_to_keep):
            for r in range(row_num):
                new_payout_grid[r].append(self.payout_grid[r][c])
        self.payout_grid = new_payout_grid
        self.col_labels = [self.col_labels[i] for i in sorted(cols_to_keep)]
        return col_num != len(cols_to_keep);

    def remove_dominated_moves(self):
        while self.remove_dominated_p1() | self.remove_dominated_p2():
            pass

    def remove_dominated_p1(self):
        row_num = len(self.payout_grid)
        col_num = len(self.payout_grid[0])
        max_values = []
        for c in range(col_num):
            max_payout = max([self.payout_grid[r][c][P1] for r in range(row_num)])
            rows_to_keep = set()
            for r in range(row_num):
                if self.payout_grid[r][c][P1] == max_payout:
                    rows_to_keep.add(r)
            max_values.append(rows_to_keep)

        rows_to_keep = []
        while max_values:
            maximum_intersection = max_values[0].copy()
            for c in range(1, len(max_values)):
                if len(maximum_intersection & max_values[c]) != 0:
                    maximum_intersection = maximum_intersection & max_values[c]
            max_index = maximum_intersection.pop()
            rows_to_keep.append(max_index)
            max_values = [row for row in max_values if max_index not in row]

        new_payout_grid = [self.payout_grid[i] for i in sorted(rows_to_keep)]
        self.payout_grid = new_payout_grid
        self.row_labels = [self.row_labels[i] for i in sorted(rows_to_keep)]
        return row_num != len(rows_to_keep);

    def remove_dominated_p2(self):
        row_num = len(self.payout_grid)
        col_num = len(self.payout_grid[0])
        max_values = []
        for r in range(row_num):
            max_payout = max([self.payout_grid[r][c][P2] for c in range(col_num)])
            cols_to_keep = set()
            for c in range(col_num):
                if self.payout_grid[r][c][P2] == max_payout:
                    cols_to_keep.add(c)
            max_values.append(cols_to_keep)

        cols_to_keep = []
        while max_values:
            maximum_intersection = max_values[0].copy()
            for c in range(1, len(max_values)):
                if len(maximum_intersection & max_values[c]) != 0:
                    maximum_intersection = maximum_intersection & max_values[c]
            max_index = maximum_intersection.pop()
            cols_to_keep.append(max_index)
            max_values = [col for col in max_values if max_index not in col]

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
                if self.payout_grid[r][c][P1] == max_payout:
                    best_payouts[(r, c)] = (self.row_labels[r], self.col_labels[c])

        best_payout_labels = []
        for r in range(row_num):
            max_payout = max([self.payout_grid[r][c][P2] for c in range(col_num)])
            for c in range(col_num):
                if self.payout_grid[r][c][P2] == max_payout:
                    if (r, c) in best_payouts:
                        best_payout_labels.append(best_payouts[(r, c)])
        return best_payout_labels;

    def mixed_strategy_solutions(self):
        self.remove_dominated_moves()
        p1_move_percents = {}
        p2_move_percents = {}
        side_length = len(self.payout_grid)
        if side_length == 1:
            p1_move_percents[self.row_labels[0]] = 100
            p2_move_percents[self.col_labels[0]] = 100
            return (p1_move_percents, p2_move_percents);

        p1_outcomes = [[1] * side_length]
        for c in range(1, side_length):
            p1_outcomes.append([self.payout_grid[r][c][P2] - self.payout_grid[r][0][P2] for r in range(side_length)])
        p1_solutions = [1] + [0 * (side_length - 1)]
        p1_outcomes = np.linalg.solve(np.array(p1_outcomes), np.array(p1_solutions))
        for r in range(len(self.row_labels)):
            p1_move_percents[self.row_labels[r]] = p1_outcomes[r] * 100

        p2_outcomes = [[1] * side_length]
        for r in range(1, side_length):
            p2_outcomes.append([self.payout_grid[r][c][P1] - self.payout_grid[0][c][P1] for c in range(side_length)])
        p2_solutions = [1] + [0 * (side_length - 1)]
        p2_outcomes = np.linalg.solve(np.array(p2_outcomes), np.array(p2_solutions))
        for c in range(len(self.col_labels)):
            p2_move_percents[self.col_labels[c]] = p2_outcomes[c] * 100

        return (p1_move_percents, p2_move_percents);

    def compute_pure_strategies(self):
        equilibriums = self.pure_strategy_solutions()
        for s in equilibriums:
            print("Player 1 plays", s[P1], "and Player 2 plays", s[P2])
        if len(equilibriums) == 0:
            print("No pure strategies")

    def compute_mixed_strategies(self):
        equilibriums = self.mixed_strategy_solutions()
        for r in self.row_labels:
            print("Player 1 plays", r, equilibriums[0][r], "percent of the time")
        for c in self.col_labels:
            print("Player 2 plays", c, equilibriums[0][c], "percent of the time")
