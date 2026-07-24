# 1
my_age = 24

# 2
my_height = 1.63

# 3
complex_variable = 1 +2j

# 4
base = int(input('Enter base: '))
height = int(input('Enter height: '))
triangle_area = int((base*height)/2)
print('The area of the triangle is:', triangle_area)

# 5 
side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter = side_a +side_b + side_c
print('The perimeter of the triangle is',int(perimeter))

# 6 
length_rectangle = int(input('Enter length '))
width_rectangle = int(input('Enter width '))
area_rectangle = length_rectangle*width_rectangle
perimeter_rectangle = 2*(length_rectangle + width_rectangle)
print('Area is',area_rectangle)
print('Perimeter is',perimeter_rectangle)

# 7 
radius_circle = int(input('Enter a radius : '))
area_circle = 3.14 * radius_circle**2
circumference_circle = 2*3.14*radius_circle
print('Area of the circle is',area_rectangle)
print('Circumference of the circle is',perimeter_rectangle)

# 8
x1 = int(input('Enter x1: '))
x2 = int(input('Enter x2: '))
y1 = 2*x1 -2
y2 = 2*x2 -2
slope1 = int(((y2 -y1)/(x2-x1)))
print('The slope 1 is:',slope1)

# 9
x_1, x_2, y_1, y_2 = 2,6,2,10
slope2  = slope = int(((y_2 -y_1)/(x_2-x_1)))
E_Distance = (x_2 - x_1)**2 + (y_2 - y_1)**2
print('The slope 2 is : ', slope2)
print('E_Distance is :',E_Distance)

# 10
print('Slope 1 = Slope 2 ?', slope1 == slope2)
print('Slope 1 > Slope 2 ', slope1 >= slope2)
print('Slope 1 < Slope 2 ', slope1 <= slope2)
print('Slope 1 < Slope 2 ', slope1 is slope2)

# 11 
x = int(input('Enter a value of x :'))
y = x**2 +6*x+9
print('The value of y is :', y)
print('Is Y equal to zero ?', y==0)

# 12
word_1 = 'python'
word_2 = 'dragon'
print('The length of python is: ', len(word_1))
print('The length of dragon is: ', len(word_2))
print('Are they of different length', not(len(word_1) == len(word_2)))

# 13 
print('On is in python and dragon:', ('on' in 'python' and 'on' in 'dragon'))

# 14
sentence = 'I hope this course is not full of jargon'
print('jargon in sentence ? :', 'jargon' in sentence )

# 15
print('jargon in sentence ? :', not('jargon' in sentence ))

# 16
len_of_python = len('python')
print('Length of Python is' , len_of_python)
len_of_python_float = float(len_of_python)
len_of_python_string = str(len_of_python_float)
print('len_of_python_float: ',type(len_of_python_float))
print('len_of_python_string: ', type(len_of_python_string))

# 17
number = int(input('Enter number: '))
print('is number even ?:', number % 2 == 0)

# 18
print('are they equal ? :', (7//3)==int(2.7))

# 19
print('are types equal ?', type('10')==type(10))

# 20
print('are they equal ?', int(float('9.8')) == 10)

# 21
hours = input('Enter hours: ')
rate_hour = input('Enter rate per hour: ')
pay_person = int(hours) * int(rate_hour)
print('Your weekly earning is ',pay_person)

# 22
years_lived= input('Enter number of years you have lived: ')
number_of_seconds = int(years_lived)*365*24*60*60
print('You have lived for',number_of_seconds, 'seconds')

# 23 
list_numbers = '(1,1,1,1,1,2,1,2,4,8)'
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4 , 16, 64)
print(5, 1, 5, 25, 125)
