#Вариант10
song_genre = {
    'SeparateWays.mp3' : 'рок',
    'Колыбельная.mp3' : 'тяжёлый метал',
    'ALittleLessConversation.mp3' : 'поп',
    'Болталка.mp3' : 'подкаст',
    'AllStar.mp3' : 'альтернативный рок',
    'Bangarang.mp3' : 'дабстеп',
    'ГолубаяСтрела.mp3' : 'авторская песня'
    }

keys = list(song_genre.keys())
d = dict()
for i in keys:
    d[song_genre[i]] = i

print(d)
