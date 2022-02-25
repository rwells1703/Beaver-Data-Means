frequencies = [1,4,3,1,1,1]

def calculate_upper_mean(frequencies):
    midpoint = sum(frequencies) / 2

    total_remaining = midpoint

    weightings = [0] * len(frequencies)

    i = len(frequencies)-1
    stop = False
    while i > 0 and not stop:
        if total_remaining - frequencies[i] > 0:
            total_remaining -= frequencies[i]
            weightings[i] = 1
        else:
            weightings[i] = total_remaining/frequencies[i]
            stop = True
        
        i -= 1


    upper_mean = 0

    i = 0
    while i < len(frequencies):
        upper_mean += i * weightings[i]
        i += 1

    upper_mean /= midpoint

    return upper_mean

print(calculate_upper_mean(frequencies))