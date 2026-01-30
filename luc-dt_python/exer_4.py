# let's use a standard library to get the current date in YYYY-mm-dd format
from datetime import datetime 
print(datetime.now().strftime('%Y-%m-%d'))


# When we try to access an element that is not part of a list we get an out of index error, 
# with the try block, the error will be
# caught by the except block
# finally will be executed irrespective of if there was an error or not
l = [1, 2, 3, 4, 5] 

index = 10
try:
    element = l[index]
    print(f"Element at index {index} is {element}")
except IndexError:
    print(f"Error: Index {index} is out of range for the list.")
finally:
    print("Execution completed.")
print("----------------------------------------------------------")
index = 2
try:
    element = l[index]
    print(f"Element at index {index} is {element}")
except IndexError:
    print(f"Error: Index {index} is out of range for the list.")
finally:
    print("Execution completed.")

