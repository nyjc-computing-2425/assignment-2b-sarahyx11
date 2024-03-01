num = input('Enter a number (decimal only): ')
# type your code here
clean = num[num.find(".")+1:]
dp = len(clean)


# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
