'''
This is an auxiliary file for notebook 1 of exercises. Here I'll
define a function that I'm going to import in the notebbok.
'''

# Define a simple function that returns the square value for
# each element on a given iterable array
def squared(a):
    '''
    Params:
        a : array-like object
            Array of int or float numbers.
    Output:
        Returns an array where the squared values
        of each element in array a.
    '''
    # Init empty list for results
    res = []

    # Get values
    for n in a:
        res.append(n**2)
    return res