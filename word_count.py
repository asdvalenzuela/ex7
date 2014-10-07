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

    return word_dict
    #this code will sort an alphabetical list of words by frequency
    #sorted_values = sorted(word_dict.items(), key = lambda word: word[1])
    #sorted_keys = sorted(sorted_values, key = lambda word: word[0])
    #for tuple in sorted_keys:
        #print tuple[0], tuple[1]

def sort_freq(argv):

    word_dict = count_words(argv)

    dict_sort = {}
    for key, value in word_dict.iteritems():
        if value not in dict_sort:
            dict_sort.setdefault(value, [key])
        if value in dict_sort:
            dict_sort[value].append(key)

    values_list = dict_sort.values()
    for list_ in values_list:
        for value in item:

    print dict_sort

    #for new_word, frequency in sorted(word_dict.items(), key = lambda word: word[1]):
       # print word, frequency
    # this code will sort and print the keys alphabetically
    #new_words = word_dict.keys()
    #new_words.sort()
    #for word in new_words:
        #print word, word_dict[word]

    #for key,value in word_dict.iteritems():
        #print key,value

def main():

    count_words(argv)
    sort_freq(argv)

if __name__ == "__main__":
    main()
