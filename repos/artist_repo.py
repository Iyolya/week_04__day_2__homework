# from db.run_sql import run_sql
# from models.artist import Artist


# def save(artist):
#     sql = "INSERT INTO artists name VALUES (%s, %s) RETURNING *"
#     values = [name]
#     result = run_sql(sql, values)
#     id = results[0]['id']
#     artist.id = id
#     return artist


