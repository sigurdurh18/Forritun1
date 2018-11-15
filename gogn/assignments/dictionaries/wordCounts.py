import string

def get_word_list(fpointer):
    ''' Returns a list of the words found in the file pointed to by fpointer
        The words are transformed to lower case 
        and punctuation is stripped off the end of the word
    '''
    word_list = []
    for line in fpointer:  
      line_lst = line.strip().split()
      for word in line_lst:
          word = word.lower()
          if word[-1] in string.punctuation:
            word = word[:-1]
          word_list.append(word)
    return word_list

def word_list_to_counts(word_list):
    ''' Makes a dictionary of word counts from the given word list '''
    word_counts = {}

    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def dict_to_tuple(the_dict):
    ''' Returns a list of tuples contains the key-value pairs in the_dict'''
    dictlist = []
    for key, value in the_dict.items():
        temp = (key,value)
        dictlist.append(temp)  
    return dictlist


def main():
    filename = input("Name of file: ")
    # Get a file pointer
    fpointer = open(filename)
    # Get a list of words from the file
    word_list = get_word_list(fpointer) 
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))
    fpointer.close()
    
main()