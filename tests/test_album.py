from lib.album import Album

def test_album_attributes():
    album = Album(1,'Doolittle',1984,1)
    assert album.id == 1
    assert album.title == 'Doolittle'
    assert album.release_year == 1984
    assert album.artist_id == 1