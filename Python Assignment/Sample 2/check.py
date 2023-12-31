from method import *


assert(largestNumber([2,3,1,5,3,7,4])==7)
assert(secondLargestNumber([2,3,1,5,3,7,4])==5)
assert(evenOdd([2,3,1,5,3,7,4])==([2,4],[3,1,5,3,7]))
assert(ifListSSame([1,2,4,3,4],[1,2,3,4,4])==True)
assert(union([1,2,3],[3,1,4,5])==[1,1,2,3,3,4,5])
assert(intersection([1,2,3],[3,1,4,5])==[1,3])
assert(UnionInterSection([1,2,3],[3,1,4,5])==({1,2,3,4,5},{1,3}))
assert(squareNumberTuples(5)==[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])
assert(removeDuplicates([1,2,4,2,1,3,5])==([4,2,1,3,5]))
assert(findLongestLenghtWord(["sushruth","Sushruth E S","Sushruth E S"])==6)

assert(addKeyValue({"s":"sushruth",1:"r"},"s","site")==({"s":"sushruth",1:"r","s":"site"}))
assert(concatDict({1:1,2:4},{3:9})==({1:1,2:4,3:9}))
assert(ifKeyExists({1:1,2:4,3:9},2)==True)
assert(dictionaryOfSquare(4)==({1:1,2:4,3:9,4:16}))
assert(sumValues({1:1,2:4,3:9})==14)
assert(multiplyValues({1:1,2:4,3:9})==36)
assert(removeKey({1:1,2:4,3:9},2)==({1:1,3:9}))
assert(is_empty({})==True)
assert((makeDict([(1,1),(2,4)]))==({1:1,2:4}))

dict={'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 
'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 
'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 
'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': 
' ', 'w': 't'}
assert(encryption(dict,"cat")=="km ")

print(randomDict("Sushruth"))
print(newDictWithGrade({"Sushruth":{'ADS':80,'ABD':50},"ABC":{'ADS':40,'ABD':90}}))