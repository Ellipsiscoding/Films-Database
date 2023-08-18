from connect import * 
import time

def update():
    idField = input("Enter the FilmID of the film to be updated: ")

    userinput = input("Enter the \n 1. Title or \n 2. Year or \n 3. Rating or \n 4. Duration or \n 5. Genre          ")
    if userinput == "1":
        fieldName = "title"
    elif userinput == "2":
        fieldName = "yearReleased"
    elif userinput == "3":
        fieldName = "rating"
    elif userinput == "4":
        fieldName = "duration"
    else:
        fieldName = "genre"
    
    fieldValue = input(f"Enter the value for {fieldName}: ") 
    print(fieldValue)

    fieldValue = "'"+fieldValue+"'"
    print(fieldValue)

    dbCursor.execute(f"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE filmID = {idField}")
    dbCnx.commit()

    time.sleep(3)
    print(f"Record {idField}  updated successfully in films table.")

if __name__=="__main__":
    update()