import random

def run():
    number_found = False
    random_number = random.randint(0,20)

    while not number_found:
        number = int(input('Try a number: '))

        if number == random_number:
            print('Congratulation, you found the number! ')
            print(random_number)
            number_found = True
        elif number > random_number:
            print('The number is more less')
        else:
            print('The number is more big')


if __name__ == '__main__':
    run()