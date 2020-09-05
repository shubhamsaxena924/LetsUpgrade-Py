s1 = {1, 2, 3}
print("Set s1: ", s1)
s2 = set([2, 3, 4])
print("Set s2: ", s2)

print("\n\nIntersection of s1 and s2 & s2 and s1 is same: ")
print(s1.intersection(s2))  # returns intersection

print("\n\nUnion of s1 and s2 & s2 and s1 is same: ")
print(s1.union(s2))  # returns union

print("\n\nDifference of s1 and s2 & s2 and s1 is different: ")
print(s1.difference(s2))  # returns difference:- present in s1 but not in s2

print("\n\nDifference of s1 and s2 & s2 and s1 is different: ")
print(s1.difference(s2))  # returns difference:- present in s1 but not in s2

print("\n\nUpdate(): ")
# updates s1 with elements present in s2 but not in s1, returns None; Changes original
print(s1.update(s2))

print("\n\nRemove(): ")
print(s1.remove(4))  # removes a particular element, returns None; changes original

print("\n\nIssubset() and add(): ")
print(s1.issubset(s2))  # True if s1 is subset of s2

s2.add(1)
s1.remove(5)
print("Set s2 after adding 1: ", s2)
print("Set s1 after adding 1 and removing 5: ", s1)
