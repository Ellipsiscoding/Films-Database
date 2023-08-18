from connect import * 


def read():
    dbCursor.execute("SELECT * FROM tblFilms")

    allRecords = dbCursor.fetchall()

    for eachRecord in allRecords:
        
        print(eachRecord)
if __name__=="__main__":
    read()

