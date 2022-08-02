"""
Code challenge 23/06/2022

Task
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands 
where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation 
on your list.

"""

if __name__ == '__main__':
    N = int(input())
    output = []
    for i in range(0,N):
        index = input().split()
        if index[0] == "insert":
            output.insert(int(index[1]), int(index[2]))
        elif index[0] == "print":
            print(output)
        elif index[0] == "remove":
            output.remove(int(index[1]))
        elif index[0] == "append":
            output.append(int(index[1]))
        elif index[0] == "sort":
            output.sort()
        elif index[0] == "pop":
            output.pop(-1)
        elif index[0] == "reverse":
            output.reverse()
        else:
            print("enter valid input")
    