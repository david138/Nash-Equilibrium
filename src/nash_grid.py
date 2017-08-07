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
        while self.remove_dominated_p1() || self.remove_dominated_p2()

    def remove_dominated_p1(self):
        rows_to_keep = set()
        row_num = len(self.payout_grid)
        col_num = len(self.payout_grid[0])
        for c in range(col_num):
            max_payout = max([self.payout_grid[r][c][P1] for r in range(row_num)])
            for r in range(row_num):
                if (self.payout_grid[r][c] == max_payout):
                    rows_to_keep.update(r)

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
                if (self.payout_grid[r][c] == max_payout):
                    cols_to_keep.update(c)

        new_payout_grid = [[] for i in range(row_num)]
        for c in sorted(cols_to_keep):
            for r in new_payout_grid:
                r.append(self.payout_grid[r][c])
        self.payout_grid = new_payout_grid
        self.col_labels = [self.col_labels[i] for i in sorted(cols_to_keep)]
        return col_num != len(cols_to_keep);