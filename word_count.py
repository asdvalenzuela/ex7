from sys import argv
import string

script, filename = argv

def count_words(argv):

    word_dict = {}

    wordcount = open(filename)
    for line in wordcount:
        line = line.strip()
        words = line.split()
        for word in words:
            new_word= ''
            for letter in word:
                if letter not in string.punctuation:
                    new_word += letter 

            new_word = new_word.lower()

            if new_word in word_dict:
                word_dict[new_word] += 1
            else: 
                word_dict[new_word] = 1

    new_words = word_dict.keys()
    new_words.sort()
    for word in new_words:
        print word, word_dict[word]

    #for key,value in word_dict.iteritems():
        #print key,value

def main():

    count_words(argv)

if __name__ == "__main__":
    main()
