
print('1.Update Values in Dictionaries and Lists')

#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 

def changeSubListValue(list, subListIndex, index, newValue):
    subList = list[subListIndex]
    value = subList[index]
    subList[index] = newValue
    #print(value)
    #print(subList)
    list.pop()
    list .append(subList)
    #print(list)
    #result = list[subList] 
    return list

print(x)
newList = changeSubListValue(x, 1, 0, 15 )  # Input next parameters: List, Sub-List, Index, New Value
print( newList )

#or use next lines
x[1][0] = 15
print (x)

#Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

def changeSubListDictionaryValue(list, subListIndex, key, newValue):
    subListDictionary = list[subListIndex]
    subListDictionary[key] = newValue
    #print(list)
    return list

print(students)
newLastName = changeSubListDictionaryValue(students, 0, "last_name", 'Bryant' )
print(newLastName)

#or use next lines
students[0]['last_name'] = "Bryant"
print (students)

#In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

def changeSubDictionaryKeyValueList(dictionary, key, listIndex, newValue):
    subDictionary = dictionary[key]
    print(subDictionary)
    #subDictionary[key] = newValue
    #print(list)
    return list

print(sports_directory)
newKeyValue = changeSubListDictionaryValue(sports_directory, 'soccer', 0, 'Andres' )
print(newKeyValue)

#or use next lines
sports_directory['soccer'][0] = 'Andres'
print( sports_directory)


#Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]

print(z)
newValue = changeSubListDictionaryValue(z, 0, "y", 30 )
print(newValue)

#or use next lines
z[0]['y'] = 30
print(z)

print("----------End of exercise 1------------")



print('2.Iterate Through a List of Dictionaries')
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterate_dictionary(listStudents):
    for i in range(0, len(listStudents)):
        result = ""
        for key, value in listStudents[i].items():
            result = result + f" {key} - {value},"
        print(result)

iterate_dictionary(students)
print("----------End of exercise 2------------")

print('3.Get Values From a List of Dictionaries')

def iterate_dictionary2( key_title, listStudents):
    for i in range(0, len(listStudents)):
        for key, value in listStudents[i].items():
            #print(listStudents[i].items())
            if key == key_title:
                print(value)
print("List of first names")
iterate_dictionary2('first_name', students)
print("List of last names")
iterate_dictionary2('last_name', students)

print("----------End of exercise 3------------")

print('4.Iterate Through a Dictionary with List Values')
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for key, value in dojo.items():
        print ( f"{len(value)} {key.upper()}")
        for i in range(0, len(value)):
            print(value[i])

printInfo(dojo)


print("----------End of exercise 4------------")



