def average_temps(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps += temp
    return sum_of_temps / len(temps)

if __name__ == '__main__':
    temps = [12,32,23,24,28,24]

    result = average_temps(temps)
    print(result)