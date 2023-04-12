def getSongNames(text):
    song_names = list()
    for line in text.split('\n'):
        song_names.append(line.split('"')[1])
    return song_names


text = '"City Lights" by The White Stripes\n"Water Fountain" by Tune-Yards\n"Statue of a Fool" by David Ruffin\n"Skyline Pigeon" by Elton John\n"The Water" by Johnny Flynn'

print(getSongNames(text))
