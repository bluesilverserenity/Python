list = [1, 2, 3, 4, "daniel"]   #a list can contain different types of data
print(list)              #prints the entire list

#multidimensional list
multi_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(multi_list[0][1])  #prints the value at index 1 of the first sublist
multi_list[0][1] = 20   #changes the value at index 1 of the first sublist to 20
print(multi_list)      #prints the updated multidimensional list

#some popular list methods, list is mutable, so we can change its contents
list.append(6)         #adds 6 to the end of the list
print(list)              #prints the updated list
list.insert(2, "python")  #inserts "python" at index 2
print(list)              #prints the updated list
list.remove(2)         #removes the first occurrence of 2 from the list
print(list)              #prints the updated list
list.pop()             #removes the last element from the list
print(list)              #prints the updated list
popping = list.pop(1)          #removes the element at index 1 from the list
print(list)              #prints the updated list
print("Popped value:", popping)           #prints the value that was removed from the list
