
'''
ID: smaylni1
LANG: PYTHON3
TASK: palsquare
'''

nums = {0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9', 10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F', 16 : 'G', 17 : 'H', 18 : 'I', 19 : 'J', 20 : 'K'}

def divine(number, base):
    global num
    if (number // base == 0):
        num = nums[number % base]
        return number % base
    else:
        divine(number // base, base)
        num += nums[number % base]
        return number % base

def ispalindrome(num):
    if len(num) <= 1:
        return True
    else:
        return num[0] == num[-1] and ispalindrome(num[1:-1])


f = open('palsquare.in', 'r')
base = int(f.read())
f.close()

f = open('palsquare.out', 'a')

for i in range(1, 301, 1):
    divine(i, base)
    num1 = num
    divine(i ** 2, base)
    if ispalindrome(num):
        f.write(str(num1) + ' ' + str(num) + '\n')
    else:
        continue

f.close()
