from org.transcrypt.stubs.browser import *
import random


def gen_random_int(number, seed):
    thislist = []
    random.seed(seed)
    for i in range(number):
        thislist.append(i)
    random.shuffle(thislist)
    return (thislist)


def generate():
    number = 10
    seed = 200
    # call gen_random_int() with the given number and seed
    # store it to the variable array

    array = gen_random_int(number, seed)
    # convert the items into one single string
    # the number should be separated by a comma
    # and a full stop should end the string.

    array_str = ""
    for i in array:
        array_str += f"{i}, "

    # This line is to placed the string into the HTML
    # under div section with the id called "generate"
    document.getElementById("generate").innerHTML = array_str


# This function is used in Exercise 1.
#		The function is called when the sort button is clicked.

#		You need to do the following:
#		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
#		- create a list of integers from the string of numbers
#		- call your sort function, either bubble sort or insertion sort
#		- create a string of the sorted numbers and store it in array_str

def sortnumber1():
    array_str = document.getElementById("generate").innerHTML
    mylist = []
    for i in array_str:
        if i.isdigit():
            j = int(i)
            mylist.append(j)
    insertion_sort(mylist)


def insertion_sort(array):
    array_str = ""
    for i in range(1, len(array)):
        temporary = array[i]
        while temporary < array[i - 1] and i > 0:
            array[i] = array[i - 1]
            i = i - 1
        array[i] = temporary
    for i in array:
        array_str += f"{i}, "

    document.getElementById("sorted").innerHTML = array_str


def sortnumber2():
    '''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.
		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
    print ('lol')
    digits = document.getElementById("numbers").value

	# Throw alert and stop if nothing in the text input
    if digits == "":
        window.alert("Your textbox is empty")
    for i in digits:
	    if i.isalpha():
		    window.alert("Characters are not accepted, please use numbers")
    array = digits.split(',')
    for i in range(len(array)):
	    temp = int(array[i])
	    array[i] = temp
    insertion_sort(array)
