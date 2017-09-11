import csv
from collections import Counter

keyword = ['Amazon']
counter = Counter()

def find_collocations(corpus):
    for line in corpus:
        line = line.lower()
        words_list = line.split(' ')
        for i in range(len(words_list)-1):
            if words_list[i] in keyword:
                counter[(word_list[i], word_list[i+1])] += 1
    return counter

def main():
    file = open('C:\\Users\\student\\Desktop\\rus-wikipedia-sample-companies.txt', 'r', encoding = 'utf-8')
    corpus = file.readlines()
    find_collocations(corpus)
    print(find_collocations(corpus))

if __name__ == "__main__":
    main()
    
