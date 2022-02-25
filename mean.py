import csv

def calculate_upper_mean(frequencies, fraction):
    split_point = sum(frequencies) * fraction

    total_remaining = split_point

    weightings = [0] * len(frequencies)

    i = len(frequencies)-1
    stop = False
    while i >= 0 and not stop:
        if total_remaining - frequencies[i] >= 0:
            total_remaining -= frequencies[i]
            weightings[i] = 1
        else:
            weightings[i] = total_remaining/frequencies[i]
            stop = True
        
        i -= 1


    upper_mean = 0

    i = 0
    while i < len(frequencies):
        upper_mean += i * frequencies[i] * weightings[i]
        i += 1

    upper_mean /= split_point

    return upper_mean


def example():
    frequencies = [1,4,3,1,1,1]
    
    print(calculate_upper_mean(frequencies, 0.5))

example()