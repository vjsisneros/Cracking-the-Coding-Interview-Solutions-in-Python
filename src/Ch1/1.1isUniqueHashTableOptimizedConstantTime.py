## 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
## What if you cannot use additional data structures??

##Problem: Determine if a string has all unique characters. Thats is no characters are the same.
##Input: A sting s
##Output: Indicate if the string s given contains only unique characters.

##Optimizing Question I would ask myself or in an interview be thinking out loud:

##Can I use a different data structure?
##Is this problem similar to one I have seen before?
##Are there any details in the problem discreption that I have not captialized on?
##Is that any inherent structure of the input that I could use to optimize my algorithm?

##The answer to the first three are:
##    Yes, but it would be less efficient.
##    Yes, I could sort the string and then traverse the string linearly while comparaing the two adjacent letters for duplicates
##    Yes. See below.
##    Yes. By the pigeonhole principle if we have a string who's length is greater than 26 letters then this world will certainly contain duplicated
##        Also, by a similar reasoning. If the string has a length of 0 or 1 then this string will not contain any duplicated

##Thus, these cases can be immediately checked before any further processing on the string is computed and shorted-circuited if any are True

##  With this optimization added we can see that our solution is O(1) constant time. The reason that it is constant time is that the solution's worse
## case is when the 26 unique letters. If any string is over that length the algorithm will short-ciruit itself and return false because of the pigeonhole priniciple.

def hasAllUnique(inStr):

    #check for "edge" cases
    if(len(inStr) <= 1 or len(inStr) > 26):
        return False

    #otherwise, process string
    letMap =  {}
    inStr = inStr.lower()
    
    for char in inStr:

        if(char in letMap):
            return False

        else:
            letMap[char] = char

    return True


def main():
    print(hasAllUnique("D"))
    
main()
