import numpy as np

#power function

def power(a, b):
    power = a**b
    return power


#finding pi funciton

def find_pi():

    radius = 0.5

    N = 10000000

    #generating test numbers
    np.random.seed(42)
    x_numbers = np.random.random(N)
    y_numbers = np.random.random(N)
    

    #calculating the distance from the center
    xc, yc = 0.5, 0.5

    distance = np.sqrt( power((x_numbers - xc), 2) + power((y_numbers - yc), 2))
   
    # filtering distances less than 0.5
    filteredDistances = distance[distance <= radius]

    M = np.size(filteredDistances)

    ratio = M / N

    estimate = ratio * 4

    print(estimate)

find_pi()



