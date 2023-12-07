#add
s={1,4,2,5,3,6}
s.add(9)
print(s)

s={1,4,2,5,3,6}
s.add((8,9))  #puting tuple in set
print(s)

#update
s={1,4,2,5,3,6}
s.update((13,12,14))
print(s)

#Discard
s={1,4,2,5,3,6}
s.discard(20)
print(s)

#Remove
s={1,4,2,5,3,6}
s.remove(1)
print(s)

#Intersection
s={1,4,2,5,3,6}
s1={4,8,9,1,5}
print(s.intersection(s1))

s={1,4,2,5,3,6}
s1={4,8,9,1,5}
s2={9,4,1}
print(s.intersection(s1,s2))

#Union
s={1,4,2,5,3,6}
s1={4,8,9,1,5}
print(s.union(s1))

s={1,4,2,5,3,6}
s1={4,8,9,1,5}
s2={9,4,1,7}
print(s.union(s1,s2))

#Clear
s={1,4,2,5,3,6}
s.clear()
print(s)

#isSubset
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
print(s1.issubset(s2))

#isSuperset
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
print(s1.issuperset(s2))


#pop
my_set = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3}
removed_element = my_set.pop()
print("Removed element:", removed_element)
print("Updated set:", my_set)
