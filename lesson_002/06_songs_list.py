#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean'

duration_song_4 = violator_songs_list[3][1]
duration_song_6 = violator_songs_list[5][1]
duration_song_9 = violator_songs_list[-1][1]
total_duration_songs_1 = duration_song_4 + duration_song_6 + duration_song_9
print(round(total_duration_songs_1, 2))

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'

duration_song_2 = violator_songs_dict['Sweetest Perfection']
duration_song_7 = violator_songs_dict['Policy of Truth']
duration_song_8 = violator_songs_dict['Blue Dress']
total_duration_songs_2 = duration_song_2 + duration_song_7 + duration_song_8
print(round(total_duration_songs_2))

# зачет!
