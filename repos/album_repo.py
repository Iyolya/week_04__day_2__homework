from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist


def save(album):
    def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id,) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

    def delete_all():

        def select(id):