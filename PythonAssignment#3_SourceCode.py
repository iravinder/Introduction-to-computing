# defining the fuction
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

#asking user for the input string
string = input("Enter the string: ")

#printing the required output
print("The number of words or elements are:\n",word_count(string))