# DESCRIPTION:
# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also
# known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing
# every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, 
# but they are not capitalized in the same way he originally typed them.

# Example:

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def to_jaden_case(string):         
    return " ".join(i.capitalize() for i in string.split())
  
def to_jaden_case(string):
    word_list = string.split()
    capital_word_list = []
    for i in word_list:
        word = i.capitalize()
        capital_word_list.append(word)
        final_string = " ".join(capital_word_list)
    return final_string
