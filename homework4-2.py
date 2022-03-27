"""SELECT запросы. 2 часть домашнего задания"""

from audioop import add
import sqlalchemy
import pandas as pd
if __name__ == "__main__":
    with open("requirements.txt") as f:
        file = f.readlines()
        password_psql = file[0]
    db = f"postgresql://postgres:{password_psql}@localhost:5432/postgres"
    engine = sqlalchemy.create_engine(db)
    connection = engine.connect()

    def select_db():    
        '''Год выпуска альбома 2018 '''
        print(connection.execute(
            """SELECT album_name, year_ FROM albums 
            WHERE year_ = 2018;"""
            ).fetchall())

        '''Название и продолжительность самого длительного трека'''
        print(connection.execute(
            """SELECT id, track_name, track_time FROM track
            ORDER BY track_time DESC;"""
            ).fetchone())

        '''Треки длительностью более 3.5 мин'''
        print(connection.execute(
            """SELECT track_name, track_time FROM track
            WHERE track_time >= 3.5;"""
            ).fetchall())

        '''Сборники выпущенные между 2018 и 2020'''
        print(connection.execute(
            """SELECT name_ FROM collection 
            WHERE year_ BETWEEN 2018 and  2020;"""
            ).fetchall())

        '''Название группы/артиста состоящее из одного слова'''
        res = connection.execute(
            """SELECT artist_name FROM artists;"""
            ).fetchall()       
        for name in res:
            list_name = str(*name)
            list_name = list_name.split(' ')
            if len(list_name) == 1:
                print(*list_name)
            
        '''Треки содержащие "my" '''
        print(connection.execute(
            """SELECT track_name FROM track 
            WHERE track_name ILIKE '%%my%%';"""
            ).fetchall())        
    select_db()