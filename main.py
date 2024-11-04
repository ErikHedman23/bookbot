import time

def count_characters(text):
    diction = {}
    lowered = text.lower()
    for char in lowered: 
        if char in diction: 
            diction[char] += 1
        else: 
            diction[char] = 1    
    # print(diction)
     
    for key in diction:
        print(f"The {key} character was found {diction[key]} times...")
        time.sleep(0.1)
     
def count_words(text):
    words = text.split()
    # print(words)
    count_of_words = len(words)
    return count_of_words

def main():
    with open('books/genesis.txt', 'r') as f:
        text = f.read()
    # print(text)
    print(f"The book of Genesis in English has {count_words(text)} words in it...")
    time.sleep(.5)
    count_characters(text)

main()