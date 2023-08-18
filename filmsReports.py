from connect import * 

def reportsAll():
    dbCursor.execute("SELECT * FROM tblFilms")

    allRecords = dbCursor.fetchall()

    for eachRecord in allRecords:
        print(eachRecord)


def tableReport():
    
        yearReleased = int(input("What year do you wish to see films from?: "))     
        if yearReleased <2014:
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = {yearReleased}")
        elif yearReleased == 2014:
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = {yearReleased}")
        elif yearReleased == 2015:
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = {yearReleased}")
        elif yearReleased == 2016:
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = {yearReleased}")
        elif yearReleased == 2017:
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = {yearReleased}")
        elif yearReleased == 2018:
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = {yearReleased}")
        elif yearReleased == 2019:
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = {yearReleased}")
        elif yearReleased == 2020:
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = {yearReleased}")
        elif yearReleased == 2021:
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = {yearReleased}")
        elif yearReleased == 2022:
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = {yearReleased}")
        else:
            input("No Film Year Valid")
        records = dbCursor.fetchall()
        for record in records: 
            print(record)


def tableReport2():
        genre = input("What genre category do you wish to see?: ")
        if genre == "Comedy":
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{genre}' ")
        elif genre == "Action":
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{genre}' ")
        elif genre == "Fantasy":
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{genre}' ")
        elif genre == "Crime":
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{genre}' ")
        elif genre == "Animation":
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{genre}' ")
        else:
            input("Invalid genre entered")
        records = dbCursor.fetchall()
        for record in records: 
            print(record)

def tableReport3():
        rating = input("What film rating category do you wish to see?: ").upper()
        if rating == "G":
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{rating}' ")
        elif rating == "PG":
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{rating}' ")
        elif rating == "PG-13":
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{rating}' ")
        elif rating == "R":
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{rating}' ")
        else:
            input("Invalid rating entered")
        records = dbCursor.fetchall()
        for record in records: 
            print(record)

if __name__=="__main__":

    reportsAll()
    tableReport()
    tableReport2()
    tableReport3()


 