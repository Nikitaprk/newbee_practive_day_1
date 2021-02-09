# Wolves have been reintroduced to Great Britain.
# You are a sheep farmer, and are now plagued by wolves which pretend to be sheep.
# Fortunately, you are good at spotting them.
# Warn the sheep in front of the wolf that it is about to be eaten.
# Remember that you are standing at the front of the queue which is at the end of the array:


def warn_the_sheep(queue):
    index = queue.index('wolf')
    n = (len(queue)-1) - index
    if n>=1:
        return "Oi! Sheep number " + str(n) + "! You are about to be eaten by a wolf!"
    else:
        return 'Pls go away and stop eating my sheep'


print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']))
print(warn_the_sheep(['sheep', 'sheep', 'wolf']))
print(warn_the_sheep(['sheep', 'wolf', 'sheep']))