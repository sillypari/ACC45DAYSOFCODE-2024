# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/THREETOPICS

# Take input in the form of a single line
try:
    # Read the input
    A, B, C, X = map(int, input("Enter A, B, C, X: ").split())

    # Check if X is one of the topics Chef prepared
    if X in (A, B, C):
        print("Yes")
    else:
        print("No")
except ValueError:
    print("Please enter exactly four integers separated by spaces.")

