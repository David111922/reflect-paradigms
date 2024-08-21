# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

# Remember, when writing in a functional style:
# Keep variables immutable
# Write only pure functions
# Remember, functions may be higher order

def flatten_and_sort(arr):
    flattened = []

    # Helper function to flatten the array
    def flatten(items):
        for item in items:
            if isinstance(item, list):
                flatten(item)  # Recursively flatten the list
            else:
                flattened.append(item)  # Add the item to the flattened list

    # Flatten the array
    flatten(arr)

    # Sort the flattened list
    return sorted(flattened)

# Example usage
array = [3, [2, 1], [5, 4, [6]], 0]
result = flatten_and_sort(array)
print(result) 

# 1 How does this solution ensure data immutability?

# The function does not change anything in the given array ie numbers list. It simply uses a built in feature in Python that sorts the numbers and the flatten part relies on the input array but does not change it.

# 2 Is this solution a pure function? Why or why not?

# Pure . Any given input will always give the same output without side effects.

# 3 Is this solution a higher order function? Why or why not?

# It is not. It does not return a function ortake a function as an arguement.

# 4 Would it have been easier to solve this problem using a different programming style?

# Not sure. Could have been done with a for loop but that would have been more coding I think. Not sure.

# 5 Why in particular is functional programming a helpful paradigm when solving this problem?

# Even though it is using a for loop and other functions it is immutable and can be reused for different applications without changing the input.

# OOP
# Object Oriented Prompt
# Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.


class Podracer:
    def __init__(self, max_speed, condition, price):
     self.max_speed = max_speed
     self.condition = condition
     self.price = price
#  Define a repair() method that will update the condition of the podracer to "repaired".    
    def repair(self):
        self.condition("repaired")
#  Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.       
     
class AnakinsPod(Podracer): 
   def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
 
    def boost (self):
       self.max_speed *=2

class  SebulbasPod(Podracer):   
    def __init__(self, max_speed, condition, price):
     super.init(max_speed, condition, price)

    def flame_jet (self, other):  
     other.condition = "trashed"
