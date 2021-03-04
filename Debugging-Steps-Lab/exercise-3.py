"""
Exercise 3

PART 1: Gather Information
Gather information about the source of the error and paste your findings here. E.g.:
- What is the expected vs. the actual output?
- What error message (if any) is there?
- What line number is causing the error?
- What can you deduce about the cause of the error?


PART 2: State Assumptions
State your assumptions here or say them out loud to your partner ...
Make sure to be SPECIFIC about what each of your assumptions is!
HINT: It may help to draw a picture to clarify what your assumptions are.

Answer:
Expected - [1, 2, 3, 5, 6]
Actual- IndexError: list index out of range
Line causing error- 7
We need to add while j>= 0 to the statement so that it knows 
the position its on ~ one ahead of its current position. 
"""

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i]

        j = i-1
        while j>= 0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)