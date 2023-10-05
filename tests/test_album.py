from lib.album import Album

def test_album_attributes():
    album = Album(title,release_year,artist_id)
    assert album.title == title
    assert album.release_year == release_year
    assert album.artist_id == artist_id