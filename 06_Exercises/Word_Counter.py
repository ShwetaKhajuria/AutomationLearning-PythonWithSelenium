My_Sentence = "python is fun and python is easy"
words= My_Sentence.split()
counter={}
print(type(counter))
for word in words:
    if word in counter:
        counter[word]+=1
    else:
        counter[word]=1

My_list = counter.items()
print(max(My_list))