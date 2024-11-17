import  psycopg2

def aut(callback):
    con = psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password="1324qewr"
    )
    with con:
        with con.cursor() as cur:
            return callback(con,cur)
            



# @aut
# def func(CON,cur):
#     cur.execute("""
#             CREATE TABLE IF NOT EXISTS Users (
#                 userID VARCHAR(20)  NOT NULL ,
#                 gotShared BOOLEAN ,
#                 PRIMARY KEY (userID)
#             );
#             """
#             )