def unique_in_order(iterable):
    k = []
    for i in iterable:
        if k == []:
            k.append(i)
        elif k[-1] != i:
            k.append(i)
    return k
	
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
	
def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res
	
def unique_in_order(iterable):
 if len(iterable) == 0:
     return []
 else:
     result = [iterable[0]]
     for i in range(1,len(iterable)):
        if iterable[i] != iterable[i-1]:
          result.append(iterable[i])
     return result

-------------------------------------

Array.diff:

Your goal in this kata is to implement an difference function, which subtracts one list from another.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

Solution:
def array_diff(a, b):
    new = [value for value in a if value not in b]
    return new

Facebooks Likes

def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) <= 1:
        #print names[0]
        return '%s likes this' %(names[0])
    elif len(names) <= 2:
        return '%s and %s like this' %(names[0], names[1])
    elif len(names) <= 3:
        return '%s, %s and %s like this' %(names[0], names[1], names[2])
    elif len(names) >= 4:
        subs = len(names)-2
        return '%s, %s and ' %(names[0], names[1]) + str(subs) + ' others like this'
    else:
        pass