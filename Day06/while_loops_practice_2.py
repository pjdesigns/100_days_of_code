# While loop practice 2


fruit = input('Enter your favorite fruit (q to quit):  ')

# 'While the fruit is not q'
while not fruit == 'q':
    # then execute this
    print(f'Your favorite fruit is {fruit}')
    # then this
    fruit = input('Enter another fruit (q to quit):  ')

print('bye')
