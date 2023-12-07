#dict only support ==  !=  operator
d={101:'Aditya',102:'Sumedha',103:'Khushboo',104:'Suman'}
d1={101:'Aditya',102:'Sumedha',103:'Khushboo',104:'Suman'}
d2={103:'Khushboo',104:'Suman',101:'Aditya',102:'Sumedha'}
d3={101:'Aditya',102:'Sumedha',103:'Khushboo'}

print(d==d1)
print(d==d2)
print(d==d3)
print(d!=d3)
print(d!=d2)
