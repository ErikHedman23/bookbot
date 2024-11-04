def count_characters(text):
    
    diction = {}
    lowered = text.lower()
    for char in lowered: 
        if char in diction: 
            diction[char] += 1
        else: 
            diction[char] = 1    
    print(diction) 

def count_words(text):
    words = text.split()
    # print(words)
    count_of_words = len(words)
    return count_of_words
def main():
    with open('books/genesis.txt', 'r') as f:
        text = f.read()
    # print(text)
    print(count_words(text))
    count_characters(text)


main()