import os
import string

"""

Notes:

Look into array .extend() method

    append:

    x = [1, 2, 3]
    x.append([4, 5])
    print (x)
    gives you: [1, 2, 3, [4, 5]]

    extend:

    x = [1, 2, 3]
    x.extend([4, 5])
    print (x)
    gives you: [1, 2, 3, 4, 5]


Look into string module , and .punctuation

    https://docs.python.org/2/library/string.html

    string.punctuation
        String of ASCII characters which are considered punctuation characters in the C locale.

Look into the set() builtin data type

    https://docs.python.org/2/library/stdtypes.html#set

"""

# global variables
current_path = "."
stop_words = ['a','an','and','i']
file_list = []
index = {}
search_terms = []

search = raw_input("What the fuck do you want to search for? ")

for word in search.split():
    search_terms.append(word)


#upgrade your recursive find to return a list of files 

def recursive_find(current_path):
    """recursive find all files and return a list of file names"""

    for name in os.listdir(current_path):
        path = os.path.join(current_path, name)
            
        if os.path.isdir(path):
            file_list.extend(recursive_find(path))
        else:
            file_list.append(path)

    return file_list

#print recursive_find(current_path)

def read_data(filename):
    with open(filename,"r") as f:
        return f.read()

def strip_punctuation(token):
    """strip out punctuation from a token"""
    token = "".join(l for l in token if l not in string.punctuation)
    return token

def index_file(filename):
    clean_words = strip_punctuation(read_data(filename))
    word_array = []
    for word in clean_words.split():
        word_array.append(word)
    return word_array
   
    """Index one file return a cleaned array of words"""

#print add index_file("./folder-1/a.txt/a.txt"),file.{}

#index = {"surfing" : ["filename1", "filename2"]}


def add_to_index(words,filename,index):
    """takes a set of words for a filename and adds it to the index"""

    for word in words:
        if word not in index:
            index[word] = [filename]
        else:
            index[word].append(filename)
    return index 


#print add_to_index(index_file("./folder-1/a.txt/a.txt"),"./folder-1/a.txt/a.txt",{})


def index_all_files(file_list,index):
    all_files_index = {}

    for a_file in file_list:
        add_to_index(index_file(a_file),a_file, all_files_index)

    return all_files_index

#print index_all_files(recursive_find(current_path),index)


def find_files_with(index,keywords):
    """takes a list of keywords, and return a list of files with those keywords"""
    #print index
    #print keywords
    file_list = []

    for word in keywords:
        found_it = {k:v for (k,v) in index.iteritems() if word in k}
        for k,v in found_it.iteritems():
            if v not in file_list:
                file_list.extend(v)

    file_list = set(file_list)

    print "Here are your fucking files: "

    for afile in file_list:
        print afile


find_files_with(index_all_files(recursive_find(current_path),index),search_terms)

            

        

