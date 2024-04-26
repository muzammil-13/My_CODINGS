"""
Make a list of your favourite Movies, the list should have minimum 8
elements.
Print a specified list after removing the 5th element.
Insert your favourite movie director name at the 4th index position of
the list and print out the list elements.
List out the 4th element in the list.
Add additional item to the current list and display the list.
"""

movies=['abcd','adhm','aashiqi 2','jailer','leo','vikram','premalu','manjummal boys']
print(movies)

movies.remove('leo')
print(movies)

movies.insert(3,'blessy')
print(movies)

print(movies[4])

movies.append('Leo')
print(movies)