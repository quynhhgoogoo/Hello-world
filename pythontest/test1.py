# first
games = ['rock', 'scissor', 'paper']
for idx, game in enumerate(games):
    print('#%d : %s' % (idx+1, game))

#second
nums = list(range(10))
squares = []
for num in nums:
    squares.append(num ** 2)
print(squares)   

#3
dictionary = {'gau':'xinh', 'chip':'to'}
print (dictionary.get('bee', 'N/A'))
print (dictionary.get('bee'))

#4
list = {(x, x+2) : x for x in range(5)} #dict
tuu1 = (3,5)   #tuple
tuu2 = {1,9}
tuu3 =(9)

print (type(tuu1), type(tuu3))
print (type(list))
print (list[(1,3)])
print (list[tuu1])

