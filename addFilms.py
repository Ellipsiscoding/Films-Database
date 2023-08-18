from connect import *   
import time             

def insert():
    
    newFilm = []
    filmID = input("Enter Film ID: ")
    filmTitle = input("Enter Film Title: ")
    yearReleased = input("Enter Year Released: ")
    rating = input("Enter Film Rating: ")
    duration = input("Enter Film Duration: ")
    genre = input("Enter Film Genre: ")

    newFilm.append(filmID)
    newFilm.append(filmTitle)
    newFilm.append(yearReleased)
    newFilm.append(rating)
    newFilm.append(duration)
    newFilm.append(genre)

    dbCursor.execute('INSERT INTO tblFilms (filmID, title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?, ?)',(newFilm) )  # Use ? as placeholders
    dbCnx.commit() 

    print(f"{filmTitle} inserted into the films table")

if __name__ =="__main__":
    insert()



