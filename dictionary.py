data = {'Name': 'Daniel', 'Age': 30, 'City': 'Festac'}   #creating a dictionary with key-value pairs
print(data)              #prints the entire dictionary

#accessing values in a dictionary, to access values in a dictionary, we use the keys
print(data['Name'])      #prints the value associated with the key 'Name'
print(data['Age'])       #prints the value associated with the key 'Age'
print(data['City'])      #prints the value associated with the key 'City'

#modifying values in a dictionary, to modify values in a dictionary, we can assign new values to existing keys
data['Age'] = 21        #changes the value associated with the key 'Age'
data['Gender'] = 'Male'   #adds a new key-value pair to the dictionary
print(data)              #prints the updated dictionary

#removing key-value pairs from a dictionary, to remove key-value pairs from a dictionary, we can use the del keyword or the pop() method
del data['City']        #removes the key-value pair with the key 'City'
print(data)              #prints the updated dictionary
data.pop('Gender')     #removes the key-value pair with the key 'Gender'
print(data)              #prints the updated dictionary
