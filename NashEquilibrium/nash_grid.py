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

    def get_rows(self):
        return len(self.payout_grid);

    def get_cols(self):
        return len(self.payout_grid[0]);