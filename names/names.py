import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
# f_sorted_1 = sorted(names_1)
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
# f_sorted_2 = sorted(names_2)
f.close()

duplicates = []  # Return the list of duplicates in this data structure

#Replace the nested for loops below with your improvements


# middle = len(names_1) // 2  

# print(f_sorted_1[middle] < f_sorted_2[middle])

# for name_1 in f_sorted_1[middle]:
#     if name_1 > names_2[middle]:
#             for name_2 in names_2:
#                 if name_1 == name_2:
#                     duplicates.append(name_1)


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # print(f"created new Tree with value: {self.value}")

    # Insert the given value into the tree
    def insert(self, value):
        # print(value)
        if self.value is None:
            self = BinarySearchTree(value)

        elif value < self.value:
            # print(f"{value} is less than {self.value}")
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        elif value >= self.value:
            # print(f"value is greater than or == {self.value}")
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # print(target,self.value)
        if self.value == target:
            # print("base case:",self.value)
            return True

        elif target < self.value:
            if self.left == None:
                return False
            return self.left.contains(target)

        elif target >= self.value:
            if self.right == None:
                return False
            # else:
            return self.right.contains(target)



# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

#current complexity is O(n^2)
# to turn into O(nlogn), utilize the Binary Search Tree class. 


if __name__ == "__main__":
    bs = BinarySearchTree(names_1[0])
    for name1 in names_1:
        bs.insert(name1)
    for name2 in names_2:
        if bs.contains(name2):
            duplicates.append(name2)
    end_time = time.time()
    print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
    print (f"runtime: {end_time - start_time} seconds")