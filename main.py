import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            self.contents.extend([k] * v)
        #print(self.contents)

    def draw(self, number_of_balls):
        if number_of_balls >= len(self.contents):
            return self.contents
        else:
            #balls_in_urn = copy.deepcopy(hat.contents)
            balls_drawn = []
            for _ in range(number_of_balls):
                num_ball = random.randint(0, len(self.contents) - 1)
                balls_drawn.append(self.contents.pop(num_ball))
            return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = []
    #_expected_balls = []

    for num_experiment in range(num_experiments):
        _hat = copy.deepcopy(hat)
        balls_drawn = _hat.draw(num_balls_drawn)

        # make dict
        balls_drawn_dict = {}
        for i in balls_drawn:
            if i in balls_drawn_dict:
                balls_drawn_dict[i] += 1
            else:
                balls_drawn_dict[i] = 1

        expected_balls_pass = True
        for k, v in expected_balls.items():
            if k in balls_drawn_dict and balls_drawn_dict[k] >= v:
                continue
            else:
                expected_balls_pass = False
                break
        probability.append(expected_balls_pass)
    return sum(probability)/num_experiments

hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)