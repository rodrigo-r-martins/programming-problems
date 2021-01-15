"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.
Return the number of different transformations among all words we have.

=> Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations, "--...-." and "--...--.".

=== Note ===
The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
"""

def numberOfTransformationsInMorseCode(words):
    if len(words) == 0:
        return 0
    if len(words) == 1:
        return 1

    morse_code = {
                    'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 
                    'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---",
                    'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 
                    'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-",
                    'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.."
                }
    words_in_morse = []
    word_in_morse = ""

    for word in words:
        for w in word:
            word_in_morse += morse_code[w]
        words_in_morse.append(word_in_morse)
        word_in_morse = ""

    return len(set(words_in_morse))


if __name__ == "__main__":
    words = ["rwjje","aittjje","auyyn","lqtktn","lmjwn"]
    print(numberOfTransformationsInMorseCode(words))
    
    