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
print(keys)
for i in keys:
    print(i, song_genre[i])

s = input('Запрос: ')
if s in song_genre:
    print(song_genre[s])
else:
    print('В словаре нет информации по запросу')

