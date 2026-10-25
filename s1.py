# activity 1
emty_list = []
print(emty_list)

no = [1,2,3,4,5]
print(no)

triples = [1,2,3]*3
print(triples)

a = [100,200,300,400,500]
a = a[::-1]
print(a,"\n")
# activity 2
def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len (word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List of words with first and last character same\n", lst)
    return ctr

count = match_words(['abc', 'cfc','xyz', 'aba', '1221'])
print("Number of words having first and last character same:", count) 
# activity 3