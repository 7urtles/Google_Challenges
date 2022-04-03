import matplotlib.pyplot as plt
import numpy as np
from random import randint 
import random

def display(map):
    value = -1
    data = np.array(map)
    # data[data == 0] = 50
    data[data == 1] = 400
    masked_array = np.ma.masked_where(data == value, data)
    plt.ion()
    plt.gcf().set_facecolor("grey")
    plt.imshow(masked_array)
    plt.show()
    plt.pause(0.001)
    plt.clf()

def ascii_display(floor_plan_copy):
    print_string = ''
    for row in floor_plan_copy:
        for contents in row:
            if contents == 1:
                print_string += '='
            elif contents == 99:
                print_string += '.'
            else:
                print_string += ' '
        print_string += '\n'

    print(str(print_string + '\n\n'))

def map_maker():
    # Creating test floor plans
    floor_plan = []
    height = 1000
    width = 1000
    for yaxis in range(0,height):
        floor_plan.append([randint(0,2) for num in range(0,width)])
    # free up exit space
    floor_plan[0][0] = 0
    return floor_plan


 
