import numpy as np

#power function

def power(a: int, b: float) -> float:
    power = b**a
    return power


#finding pi funciton

def find_pi():

    radius = 0.5

    #this gave me a good estimation
    N = 10000000

    #generating test numbers
    np.random.seed(42)
    x_numbers = np.random.random(N)
    y_numbers = np.random.random(N)
    

    #calculating the distance from the center
    xc, yc = 0.5, 0.5

    distance = np.sqrt( power(2, (x_numbers - xc)) + power(2, (y_numbers - yc)))
   
    # filtering distances less than 0.5
    filteredDistances = distance[distance <= radius]

    M = np.size(filteredDistances)

    ratio = M / N

    estimate = ratio * 4

    print(estimate)

    

find_pi()



