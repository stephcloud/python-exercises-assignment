#8-6
def city_country(city, country):
    return f"{city}, {country}"


first = city_country("Tokyo", "Japan")
print(first)

second = city_country("Lagos", "Nigeria")
print(second)

third = city_country("Santiago", "Chile")
print(third)

#8-6
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album
firstAlbum = make_album("Adele", "25")
print(firstAlbum)

secondAlbum = make_album("Burna Boy", "Twice as Tall")
print(secondAlbum)

thirdAlbum = make_album("Beyonce", "Renaissance", 16)
print(thirdAlbum)


#8-7
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album


while True:
    print("\nEnter 'q' at any time to quit.")
    artist = input("Artist's name: ")
    if artist == "q":
        break

    title = input("Album title: ")
    if title == "q":
        break

    album = make_album(artist, title)
    print(album)