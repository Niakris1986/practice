class FloodFiller:
    def __init__(self, arr, height, width):
        self.arr = arr
        self.processed = set()
        # self.cood = len(self.arr[0]) * height + width
        self.active = (len(self.arr)+1) * len(self.arr[0])
        self.pending = [len(self.arr[0]) * height + width]
        self.new_color = 2
        self.pp = [' ', '*', 'x']

    def flood_fill(self):
        while len(self.pending) > 0:
            self.processed.add(self.active)
            self.active = self.pending.pop()
            # print(self.active)
            # print(f'pending: {self.pending}')
            h, w = self.active//len(self.arr[0]), self.active % len(self.arr[0])
            if self.arr[h][w] > 0:
                continue
            self.arr[h][w] = self.new_color

            print(f'h: {h}, w: {w}')
            print(f'pending: {self.pending}')
            print(f'processed: {self.processed}')

            h_neighbors = []
            w_neighbors = []
            if h > 0:
                h_neighbors.append(h-1)
            if h < len(self.arr) - 1:
                h_neighbors.append(h+1)
            for h_new in h_neighbors:
                coord = h_new * len(self.arr[0]) + w
                if coord not in self.processed:
                    self.pending.append(coord)
            if w > 0:
                w_neighbors.append(w-1)
            if w < len(self.arr[0]) - 1:
                w_neighbors.append(w+1)
            for w_new in w_neighbors:
                coord = h * len(self.arr[0]) + w_new
                if coord not in self.processed:
                    self.pending.append(coord)
            print(f'---------------\n{self.pprint()}\n---------------\n')
        print(f'done')
        print(f'---------------\n{self.pprint()}\n---------------\n')
        return self.arr

    def pprint(self):
        acc = '|---------'
        for h in range(len(self.arr)):
            acc += '|\n|'
            for w in range(len(self.arr[0])):

                # acc += f'{self.arr[h][w]}, '
                acc += f'{self.pp[self.arr[h][w]]}'
        return acc + '|\n|---------|'


# img = [
#     [0,0,0,0,0,0,0,1,0],
#     [0,1,1,1,1,1,0,1,0],
#     [0,1,0,0,0,1,0,1,1],
#     [0,1,0,1,0,1,0,0,0],
#     [0,1,1,1,0,1,0,0,0],
#     [0,0,0,0,0,1,0,1,1],
#     [1,1,1,1,1,1,0,1,0],
#     [0,0,0,0,0,0,0,1,0],
#     ]

img = [
    [0,0,0,1,1,1,1,1],
    [1,0,1,1,1,1,1,1],
    [0,0,0,1,0,0,0,1],
    [0,0,0,0,0,1,0,1],
    [0,0,0,1,0,0,0,1],
    ]

# img = [[0,1,0,1,0],
#        [0,1,1,0,0],
#        [0,0,0,0,0]]

# fF = FloodFiller(img, 7, 0)
fF = FloodFiller(img, 3, 1)
fF.flood_fill()


