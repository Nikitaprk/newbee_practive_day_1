# A spoonerism is a spoken phrase in which the first letters of two of the words are swapped around, often with
# amusing results. In its most basic form a spoonerism is a two word phrase in which only the first letters of each
# word are swapped: "not picking" --> "pot nicking"


def spoonerize(words):
    list_split = words.split(" ")
    a = list(list_split[0])
    b = list(list_split[1])
    a[0], b[0] = b[0], a[0]
    word = ''.join(a) + ' ' + ''.join(b)
    return word


print(spoonerize("wedding bells"))
print(spoonerize("jelly beans"))
print(spoonerize("flat battery"))
