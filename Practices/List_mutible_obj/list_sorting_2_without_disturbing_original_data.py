courses = ['History','Math','Physics','CompSci']
num = [1,5,2,4,3]


# sorted funstion does all of the work on a copy of the list
#Does not do the sorting in place.

#You need to receive the sorted version of the list and utilize that.
courses_sorted = sorted(courses)

print(courses)
print(courses_sorted)


#you may wanna look at the IDs of these two.
#just like we used to compare the hashCodes of objects in JAVA

print(id(courses))
print(id(courses_sorted))





#o/p:
#['History', 'Math', 'Physics', 'CompSci']
#['CompSci', 'History', 'Math', 'Physics']
#1767411754760         <--- these puppies would be changing the values everytime you run the programme
#1767411754248         <----^
