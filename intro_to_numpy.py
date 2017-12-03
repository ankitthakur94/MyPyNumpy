################################################################
# Objective :
################################################################
# Explore the very basics of data manipulation using numpy.
# Work on arrays and matrices efficiently
################################################################
import numpy as np



def print_array_and_shape (arr, array_name):
    ''' Print the array name / the array / shape of the array. '''
    print ('{} -> '.format(array_name) )
    print (arr)
    print ( '{}.shape = {}'.format(array_name, arr.shape))



print ('-------------------------------------------------')
################################################################
# Populate a numpy array using python list
# array_variable = np.array ( <list> )
################################################################
mylist = list (range(1,6))
print ('mylist : ', mylist)
np_arr_from_list = np.array(mylist)
print_array_and_shape( np_arr_from_list, 'np_arr_from_list'  )
################################################################


print ('-------------------------------------------------')
################################################################
# Creating 2-dim numpy array by passing 2 / multiple python lists
# arr_variable = np.array ( <list of lists> )
# 1-st array is 1st row
#  2-nd array is 2nd row and so on
# Means that the lists are stacked vertically to create a 2-d array
################################################################
list1 = list(range(1,6))
list2 = list(range(11,16))
np_arr_2d = np.array( [ list1, list2] )
print_array_and_shape(np_arr_2d, 'np_arr_2d')

################################################################






print ('-------------------------------------------------')
################################################################
# Using arange
# np.arange(start, end, step_size)
# Creates a 1-d array
################################################################
np_arange = np.arange(0,30,2)
print_array_and_shape(np_arange, 'np_arange')
################################################################






print ('-------------------------------------------------')
################################################################
## arr.reshape()
# returns the reshaped array as a separate copy without effecting the original array
################################################################

np_arange_reshaped = np_arange.reshape(3,5)
print ( id(np_arange), id(np_arange_reshaped))
print_array_and_shape(np_arange_reshaped, 'np_arange_reshaped')
################################################################





print ('-------------------------------------------------')
################################################################
## arr.resize ()
# resizes the array in place
################################################################
np_arange.resize(5,3)
print_array_and_shape(np_arange, 'np_arange')

################################################################





print ('-------------------------------------------------')
################################################################
# Creating arrays of 0s and 1s
################################################################
ones_arr = np.ones((3,2), dtype=int)
print_array_and_shape(ones_arr, 'ones_arr')

zeros_arr = np.zeros((2,3))
print_array_and_shape(zeros_arr, 'zeros_arr')

################################################################





print ('-------------------------------------------------')
################################################################
## Stacking arrays horizontally and vertically
## Make sure dimensions of the arrays to be stacked are in sync
################################################################
x = list(range(1,5))
y = list(range(11,15))

arr1 = np.array([x,y])
arr1.resize(2,4)
arr2 = np.ones((2,4))

np_arr_hstacked = np.hstack((arr1,arr2))
print_array_and_shape(np_arr_hstacked, 'np_arr_hstacked')


np_arr_vstacked = np.vstack((arr1, arr2))
print_array_and_shape(np_arr_vstacked, 'np_arr_vstacked')
################################################################





print ('-------------------------------------------------')
################################################################
# Using dtype and astype
# Since numpy arrays can only hold homogeneous data (i.e of single type)
# arr.dtype can be used to get the data type
# arr.astype can be used to change the data type.
#       Does not effect the original array and returns the modified array
################################################################

print ( np_arr_vstacked.dtype )
np_arr_vstacked_casted = np_arr_vstacked.astype('int64')
print ( np_arr_vstacked_casted.dtype )
################################################################







################################################################
# + / - : perform element by element addition and subtraction of 2 numpy arrays
################################################################



################################################################
# Some other data analysis operations available on numpy arrays
# var.max()       : Find maximum value in numpy array
# var.min()         : Minimum
# var.mean()        : Mean of all values
# var.std()         : Standard deviation of all values

# var.argmax()      : Index of max value
# var.argmin()      : Index of min value
################################################################



print ('-------------------------------------------------')
################################################################
# Indexing and slicing : Available like in python strings
# arr_var[start : end : step_size]  < returns the clipped array
# start : index is included
# end : index is not included ( like in range () function in python )
# default : 0 , -1, 2
# negative indexing also available :  -1 -> last index
################################################################

np_arr = (np.arange(1,15))**2
print_array_and_shape(np_arr, 'np_arr')

# To select a particular element in 1-D array :
print (np_arr[2])                       # < Value at index 2 = 9
print (np_arr[4])                       # < Value at index 4 = 25
np_arr_indexed = np_arr[2:4]

print ((np_arr_indexed))                # [9,16]
print (type(np_arr_indexed))            # numpy.darray

print (id(np_arr))                      # say id1
print (id(np_arr_indexed))              # id2 (different from id1)


# Exploring the same in 2-D arrays
# var [<indexing_for_row> , <indexing_for_col> ]
# and indexing for row and column individually works as shown above [start, stop, step] with -ve indexing supported


np_arr_2d = np.arange(1,16).reshape(3,5)
print_array_and_shape(np_arr_2d, 'np_arr_2d')

print (np_arr_2d[2, 2])                 # Return element in 3rd row and 3rd column

# Get slice of the 3rd row.
print (' 3rd row : ' , np_arr_2d[2,  ])

# Get slice of the 3rd row and columns 2-4
print (' 3rd row and columns 2 ,3, 4 ', np_arr_2d[2, 1:3 ])

# Get slice of the 3rd row and columns 2 and 4
print ('3rd row and columns 2, 4 ', np_arr_2d[2,  1:4:2])
################################################################







print ('-------------------------------------------------')
################################################################
# IMP !!
# Changing the slice array will also change the original array
# Ex :
#  sliced_arr = original_arr [3, ]      # Get 4th column
#  sliced_arr[:] = 1                    # Assign all elements = 1
# In this scenario the original array will also be modified  such that 4th column = 1

# Workaround : use .copy function
# copied_arr = original_arr.copy()
################################################################

print ( ' Original array before modifying sliced variable ')
print (np_arr_2d)

sliced_np_arr_2d = np_arr_2d[2, ]                       # Get 3rd row
sliced_np_arr_2d [:] = 0                                # Assign all elements = 0

print ( ' Original array after modifying sliced variable ')
print (np_arr_2d)

# We can see that the inspite of changing the variable in which slice of original array was stored
# THe original array has also changed.
# So keep this in mind.





print ('-------------------------------------------------')
################################################################
## Conditional Indexing :
#  arr_var [ condition on arr_var ]
# The condition should be such an operating which can be executed element-by-element on the array
# Ex : >
################################################################

# Return all the elements which are > 5
filtered_np_arr = np_arr_2d[np_arr_2d > 5]
# Returns a 1-D numpy array

print_array_and_shape( filtered_np_arr, 'filtered_np_arr' )
print ( 'type(filtered_np_arr) : ', type(filtered_np_arr))

################################################################







print ('-------------------------------------------------')
################################################################
# Iterating on a numpy array
################################################################



arr1 = np.arange(1,16).reshape((5,3))
print_array_and_shape( arr1, 'arr1' )
arr2 = np.arange(11,26).reshape((3,5))
print_array_and_shape( arr2, 'arr2' )


# Iterating over each row
print ( ' Iterating over each row : ')
for row in arr1 :
    print (row)


# Use enumerate to get the row index and row elements
print ('Using enumerate')
for i, row in enumerate(arr1) :
    print ('row {} is = {}'.format(i, row))

# Using zip to iterate over 2 / more arrays
print ('Using zip  ')
for i,j in zip(arr1, arr2):
    print (i, j)

# ideally it should oterate over 3x3 row matrix only.
# Don't know what is happening
################################################################



################################################################
# Conclusion
################################################################
# Operations which do not modify the original numpy array and insted return a copy of the new modified array
#   Ex : **2
#   arr = arr**2
# We might think that since we are multiplying each element of arr by 2 and assigning the result in the same variable, then there must be no copy present.
# But if we print the id(arr) before and after **2 statement, the id's will be different
# Meaning that arr variable now is present in some other location. GIven that to us it looks the same.


# Important :
# If you change a variable which was formed by slicing a numpy array,
# It will also change the original array.
# So keep this in mind. Of you do not  want to change the original,
# make a copy using  copied_arr = original_arr.copy ()
################################################################


