# remove all 'WUB' in a string, WUB should be replaced by 1 space,
# multiples WUB should be replaced by only 1 space
# heading or trailing spaces should be removed

'''
def song_decoder(song):  # before refactoring, fckn quick and dirty
    new_song = song.replace('WUB', ' ')
    new_song = new_song.split(' ')
    new_song = filter(None, new_song)
    new_song = list(new_song)
    new_song = ' '.join(new_song)

    return new_song
'''

def song_decoder(song):  # after refactoring
    return ' '.join(filter(None, song.split('WUB')))


print(song_decoder('AWUBBWUBC'))
print(song_decoder('WUBAWUBBWUBCWUB'))
print(song_decoder('WUBWUBWUBWUBWUBWUBWUBAWUBWUBWUBBWUBWUBWUBC'))

