import string
def fetchData():
    try:
        '''
        Data structure should be:
        a dictonaryes where the key is a word and the value is a set of documents containing set word
        {word:{document_index1,document_index2}}
        
        and a list of string contained in the files
        '''
        with open(input("Document collection: ")) as fil:#gogn/projects/hw8/ap_docs2.txt
            index=-1
            search_queary={}
            document_contents=[]
            for line in fil:
                if line.strip('\n') == "<NEW DOCUMENT>":
                    index+=1
                    document_contents.append("")
                else:
                    document_contents[index]+=line
                    for word in line.split():
                        if word.strip(string.punctuation).lower() in search_queary:
                            search_queary[word.strip(string.punctuation).lower()].add(index)
                        else:
                            search_queary[word.strip(string.punctuation).lower()]={index}
            return search_queary,document_contents

    except Exception as e:
        print('Documents not found.')
        return False,False

def options():
    print("What would you like to do?")
    opt=["Search Documents", "Print Document", "Quit Program"]
    for i in range(len(opt)):
        print('{:d}. {}'.format(i+1, opt[i]))

def search_by_words(query):
    inp=""
    while inp=="":
        inp=input("Enter search words: ")
    try:
        words=inp.split()
        set_join=query[words[0]]
        for word in words[1:]:
            set_join=set_join & query[word]
        print("Documents that fit search:",end=" ")
        for i in set_join:
            print("{}".format(i),end=" ")
        print("\n")
        return set_join
    except:
        print("No match.")
        return

def printDocument(documents):
    while True:
        try:
            val=int(input("Enter document number: "))
            print("Document #{:d}".format(val))
            print(documents[val])
            return
        except:
            print("No match.")

def main():
    queary,documents=fetchData()
    run = True
    while run and documents:
        options()
        val=input("> ")
        if val=="1":
            search_by_words(queary)
        elif val=="2":
            printDocument(documents)
        elif val=="3":
            run=False
            print("Exiting program.")
        else:
            print("error")

main()