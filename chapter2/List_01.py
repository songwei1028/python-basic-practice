bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

bicycles.append('trek')
bicycles.insert(0, 'trek0')
print(bicycles)

del bicycles[0]
print(bicycles)

pop1 = bicycles.pop()
print(pop1)
print(bicycles)

pop2 = bicycles.pop()
print(pop2)
print(bicycles)
