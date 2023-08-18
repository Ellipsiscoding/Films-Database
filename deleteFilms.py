from connect import *  
import time

def delete():
    idField = input("Enter the filmID of the film to be deleted: ")

    dbCursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField}")
    dbCnx.commit()

    time.sleep(3)
    print(f"Record {idField}  deleted successfully from films table")
if __name__=="__main__":
        delete()