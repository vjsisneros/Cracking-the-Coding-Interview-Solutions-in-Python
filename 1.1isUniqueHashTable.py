


## 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
## What if you cannot use additional data structures?


##This is how I break down a problem when I am initially given it. It main seem uncessary for most but it helps for me to clarify
##what exactly the problem is, what is given, and what is the expected format of the output. 

##Problem: Determine if a string has all unique characters. Thats is no characters are the same.
##Input:
##Output:

##Clarifying Questions:
##      Does case matter? For example, is Dad considered a unique world because D and d are not the same ASCII or Unicode value?
##      Should I just return a boolean indicating if a word is unique or not? If not, then what value should be output?



def hasAllUnique(inStr):
    letMap =  {}
    inStr = inStr.lower()
    
    for char in inStr:

        if(char in letMap):
            return False

        else:
            letMap[char] = char

    return True


def main():
    print(hasAllUnique("Dad"))
    
main()
