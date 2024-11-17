import Data.postgresql.auth as auth

def UserExist(id:str):
    def user(con , cur):
        cur.execute(f"SELECT * FROM Users WHERE userID ={id}")
        return cur.fetchone()
    return auth.aut(user)