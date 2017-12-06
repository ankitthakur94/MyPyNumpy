################################################################
# Objective :
################################################################
# Explore the very basics of data manipulation using numpy.
# Work on arrays and matrices efficiently
################################################################
import numpy as np

# Numpy arrays can be 1-D / 2-D / 3-D
# in 2-D (most commonly used)  axis 0 -> row and axis 1 -> column

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


print ('----------------------- Create numpy array from 2-/ multiple lists --------------------------')
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






print ('---------------------- argange ---------------------------')
################################################################
# Using arange
# np.arange(start, end, step_size)
# Creates a 1-d array
# Working of arange is similar to range() function in python
################################################################
np_arange = np.arange(0,30,2)
print_array_and_shape(np_arange, 'np_arange')
################################################################






print ('------------------ reshape -------------------------------')
################################################################
## arr.reshape(x,y)
# returns the reshaped array as a separate copy without effecting the original array
################################################################

np_arange_reshaped = np_arange.reshape(3,5)
print ( id(np_arange), id(np_arange_reshaped))
print_array_and_shape(np_arange_reshaped, 'np_arange_reshaped')
################################################################





print ('----------------------resize ---------------------------')
################################################################
## arr.resize ()
# resizes the array in place
################################################################
np_arange.resize(5,3)
print_array_and_shape(np_arange, 'np_arange')

################################################################





print ('----------------------np.ones / np.zeroes ---------------------------')
################################################################
# Creating arrays of 0s and 1s
################################################################
ones_arr = np.ones((3,2), dtype=int)
print_array_and_shape(ones_arr, 'ones_arr')

zeros_arr = np.zeros((2,3))
print_array_and_shape(zeros_arr, 'zeros_arr')

################################################################





print ('----------------------hstack / vstack---------------------------')
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





print ('---------------------- np.dtype / np.astype(int64)  ---------------------------')
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



print ('---------------------- Indexing -1 ---------------------------')
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
# Syntax : var [<indexing_for_row> , <indexing_for_col> ]
# and indexing for row and column individually works as shown above [start, stop, step] with -ve indexing supported


np_arr_2d = np.arange(1,16).reshape(3,5)
print_array_and_shape(np_arr_2d, 'np_arr_2d')

print (np_arr_2d[2, 2])                 # Return element in 3rd row and 3rd column

# Get slice of the 3rd row.
print (' 3rd row : ' , np_arr_2d[2,  ])

# Get slice of the 3rd row and columns 2-4
print (' 3rd row and columns 2 ,3,  ', np_arr_2d[2, 1:3 ])

# Get slice of the 3rd row and columns 2 and 4
print ('3rd row and columns 2, 4 ', np_arr_2d[2,  1:4:2])
################################################################







print ('---------------------- Making changes to sliced array ---------------------------')
################################################################
# IMP !!
# Changing the sliced array will also change the original array
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

print ( ' Original array after modifying sliced variable ( Assigned 3rd row = 0')
print (np_arr_2d)

# We can see that the inspite of changing the variable in which slice of original array was stored
# THe original array has also changed.
# So keep this in mind.





print ('-------------------- Conditional indexing -----------------------------')
################################################################
## Conditional Indexing :
#  arr_var [ condition on arr_var ]
# The condition should be such an operating which can be executed element-by-element on the array
# Ex : >
################################################################

print_array_and_shape( np_arr_2d, 'np_arr_2d' )
print ( ' After conditional indexing og filtered_np_arr > 3 ')
# Return all the elements which are > 5
filtered_np_arr = np_arr_2d[np_arr_2d > 3]
# Returns a 1-D numpy array

print_array_and_shape( filtered_np_arr, 'filtered_np_arr' )
print ( 'type(filtered_np_arr) : ', type(filtered_np_arr))

print ( ' Printing a boolean mask for np_arr_2d > 3 : ')
print ( np_arr_2d > 3 )

print ( ' -- Getting all values > 3 but < 10 ')
filtered_np_arr = np_arr_2d[ (np_arr_2d > 3) & (np_arr_2d < 10) ]
print_array_and_shape( filtered_np_arr, 'filtered_np_arr' )
print ( 'type(filtered_np_arr) : ', type(filtered_np_arr))
################################################################







print ('---------------------- Iterating a numpy array ---------------------------')
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

# ideally it should iterate over 3x3 row matrix only.
# Don't know what is happening
################################################################




################################################################
# Conclusion
################################################################
 # Cheat-sheet for numpy commands :
# https: // s3.amazonaws.com / assets.datacamp.com / blog_assets / Numpy_Python_Cheat_Sheet.pdf

# 1) Numpy array can be created using :

        # 1.A) Single list (np.array(<list>)
                # Creates a 1-D array with each element of the list represeting a row in numpy array.
                # If the list has 'n' elements, numpy array will have (n,1) dimensions.

        # 1.B) List of lists (np.array ( [<list1> , <list2> .. and so on ] , dtype = float) )
                # Creates a 2-D array
                # Each list is added as a new row now.
                # Each element of a  single list is a new column in np.array ( This is different from 1.A) where each element of the list was a new row.
                #   <list1>  --> row1
                #   <list2>  --> row2

        # 1.C) np.arange (start : stop : step )
            # Creates a 1-D array of numbers
            # arange works similar to range() in python

        # 1.D) np.ones ((x,y), dtype = int)  / np.zeroes ( (x,y) , dtype = int )
            # Creates numpy array of the given dimensions with all values as 1 or 0

        # 1.E) np.random.random ( (2,2) )
            # Create a 2x2 random array.

        # 1.F) np.empty((x,y))
            # Create an empty array


# 2.) np.dtype() / arr.dtype.name
# returns the datatype / name of the data type of values stores in numpy array
# A nunmpy array can only store homogenous values


# 3.) np.astype ('int32')
# Changes the datatype.
# Returns a copy, does not mdify the original array.


# 4.) Datatypes in numpy array :
    # int64 / float32 / complex / bool / object / string_ / unicode_

# 5.) np.reshape (x,y)
        # returns a new array with the given shape and original array untouched.

# 6.) np.resize (x,y)
        # Changes the dimensions of the array in place.

# 7.) Inspecting array :
        # 5.A) arr.shape
                # Get array dimensions

        # 5.B) arr.size
                # Num of elements in array

        # 5.C) arr.ndim
                # Number of dimensions of array (1/2/3)


# 8.) np.hstack ( (arr1, arr2, arr3 .. )  / np.vstack ((arr1, arr2, arr3 .. ))
        # stacks the given arrays horizontally / vertically

# 9.) Array mathematics

        # 9.A) Arithematic operations
                # s = a + b / a -b / a/b  / a*b  -> element-by-element operations
                # np.add(b,a) / np.subtract (a,b) / np.divide (a,b) / np.multiply (a,b)  -> Equivalent to above operations

                # np.exp(arr) / np.log(arr)  -> element-by-element  exponent / /log of all values

                # np.sin(arr) / np.cos(arr)  ->  -- intuitive

                # np.sqrt(arr)

                # arr1.dot(arr2)            -> dot product of 2 arrays.

        # 9.B) Comparison
                # a == b        -> element wise comparison, returns a boolean mask. (a,b must be of the same shape)
                # a < 2         -> element wise comparison, returns a boolean mask of same dim as a.
                    # When a boolean mask is applied to an array of any type, a 1-D array (list-type) is returned containing the elements which satisfy have corresponsing boolean mask entry = True

        # 9.C ) Aggregation functions (Return a single value)
                # arr.sum ()
                # arr.min ()
                # arr.max (axis = 0)
                # arr.mean ()
                # arr.median ()
                # np.std(arr)

        # 9.D ) Sorting
                # arr.sort (axis =0 )

# 10.) Indexing 1-D array
        # arr[start : stop : step] -> retunrs another 1-D array of given index.
        # This indexing works similar to indexing of strings in python. (negative indexing supported)
        # Also instead of giving :: notation, we can also provide a list
            # Ex : arr [[1,2,3]]  -> gives row  numbers 2,3,4  ( Eq to : arr [1:4] )

# 11.) Indexing 2-D array
        # arr [ <row_indexing> , <column_indexing> ]
        # Here each of the row / column indexing independently works similar to 9.)
        # Ex : sliced_arr = orig_arr [0:2 , 1:3] -> returns 1st and 2nd row with ony 2nd and 3rd col.


# 12.) Assigning values to a part of the array
        # arr [:] = 1 -> Sets all values to 1
        # arr [slice_index]  = 1 -> can be used to set a slice of the array = 1

# 13.) Conditional indexing
        # arr [arr > 5 ] -> Iterates over all elements of arr and returns a 1-D array for which the condition is satisfied.
                # since ( arr > 5 ) retunrs a boolean mask and as discussed previously, applying a boolean mask on a numpy array (using [] indexing)
                    # will return a 1-D array of values satisfying that condition.
        # Conditions can be chained.
            # Ex : arr_2 = arr [ ( arr > 2) & (arr < 10) ]


# 14.) Iterating a numpy array
        # 14.A)  Simple for
            # for row in arr :
                # print (row)
            # A simple for loop iterates over every row.
            # If its a 1-D Array, every single  element is returned in 1 iteration.
            # If its a 2-D array, 1 row as a whole is returned in 1 iteration.

        # 14.B) Using enumerate
            # for index, row in arr :
                 #..
            # Again iterates row wise, giving the index of loop iteration also.

        # 14.C ) Using zip
            # Iterate on 2 / more arrays at the same time.

# Some more imp. points :
# Operations which do not modify the original numpy array and instead return a copy of the new modified array
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


