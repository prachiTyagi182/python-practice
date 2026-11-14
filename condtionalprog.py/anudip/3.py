list1=[1,2,3,4,5,6]
list2=[4,5,6,7,8,9]
set1=set(list1)
set2=set(list2)
# sbhi elements=a|b
common_list=set1.intersection(set2)
print("Common elements in both lists:",common_list)
unique_list1=set1.difference(set2)
print("Unique elements in list1:",unique_list1)
unique_list2=set2.difference(set1)
print("Unique elements in list2:",unique_list2)
symmetric_difference=set1.symmetric_difference(set2)
print("Symmetric difference:",symmetric_difference)