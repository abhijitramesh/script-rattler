from shirt import Shirt

shirt_one = Shirt('red','L','long-sleeve',25)
print(shirt_one.price)
shirt_one.price = 10
print(shirt_one.price)
shirt_one.price = 20
print(shirt_one.price)
shirt_one.color = 'yellow'
print(shirt_one.color)
shirt_one.size = 'M'
print(shirt_one.size)
shirt_one.style = 'short_sleeve'
print(shirt_one.style)