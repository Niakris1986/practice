from math import floor


class CircleDrawer123:
    def __init__(self, radius):
        self.radius = radius

    def calculate_char_lengths(self, h):
        spaces = int(round(self.radius - ((2 * self.radius - h) * h) ** 0.5, 0))
        return spaces, int(2 * (self.radius - spaces))


my_radius = 50
cD = CircleDrawer123(my_radius)

acc = ''
for h in range(floor(2 * my_radius)):
    w1_max, w2_max = cD.calculate_char_lengths(h)
    for w_outer in range(w1_max):
        acc += '     '
    for w_inner in range(w2_max):
        acc += '  *  '
    acc += '\n'

print(acc)





