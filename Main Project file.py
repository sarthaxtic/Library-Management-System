import project_module
import mysql.connector
import sys
choicee=1
password=("admin")
while choicee==1:
    
    print('''                   Welcome to the library database management system
                                                                  Made by:Prateek Vashishth
                                                                                 and
                                                                          Sarthak Chandvaria                  ''')
    print("press 1 if you are a member")
    print("press 2 if you are an administrator")
    ch=int(input("Enter your choice"))
    p=0
    choice=1
    while choice==1:
        if ch==1:
            print("press 1 to select all the records.")
            print("press 2 to search and view details of a particular book_id.")
            print("press 3 to search and view details of books of a particular author.")
            print("press 4 to search and view details of a particular book name.")
            print("press 5 to search and view details of a particular publisher name.")
            print("Press 6 to check whether a book is issued or not and if issued shows its due date.")
            print("Press 7 to issue a book.")
            print("press 8 to return a book.")
            cho=int(input("Enter your choice."))
            if cho==1:
                project_module.selectall()
            elif cho==2:
                project_module.selectid()
            elif cho==3:
                project_module.selectauthor()
            elif cho==4:
                project_module.selectname()
            elif cho==5:
                project_module.selectpublisher()
            elif cho==6:
                project_module.status()
            elif cho==7:
                project_module.issue()
                print("Book issued")
            elif cho==8:
                project_module.unissue()
                print("Book returned")
            else:
                print("Please Enter a valid choice")
            break
        
        
        elif ch==2:
            
            p=input("Enter Administrator password")
            if p==password:
                print("press 1 to select all the records.")
                print("press 2 to search and view details of a particular book_id.")
                print("press 3 to search and view details of books of a particular author.")
                print("press 4 to search and view details of a particular book name.")
                print("press 5 to search and view details of a particular publisher name.")
                print("Press 6 to check whether a book is issued or not and if issued shows its due date.")
                print("Press 7 To insert the record of a new book.")
                print("Press 8 To update the record of an existing book.")
                print("Press 9 To delete a record.")
                print("Press 10 To view the structure of the library table.")
                print("Press 11 to alter the structure of the library table.")
                choi=int(input("Enter your choice"))
                if choi==1:
                    project_module.selectall()
                elif choi==2:
                    project_module.selectid()
                elif choi==3:
                    project_module.selectauthor()
                elif choi==4:
                    project_module.selectname()
                elif choi==5:
                    project_module.selectpublisher()
                elif choi==6:
                    project_module.status()
                elif choi==7:
                    try:
                        project_module.insert()
                        print("Record inserted")
                    except mysql.connector.errors.IntegrityError:
                        print("Can't enter Duplicate Records.Book ID already present")
                        print("press 1 to retry 2 to quit")
                        ci=int(input("Enter your choice"))
                        if ci==1:
                            project_module.insert()
                elif choi==8:
                    project_module.update()
                    print("Record updated")
                elif choi==9:
                    project_module.delete()
                    print("Record deleted")
                elif choi==10:
                    project_module.structure()
                elif choi==11:
                    project_module.alter()
                    print("Table structure changed")
                else:
                    print("Please Enter a valid choice")
                break
         
                    

            elif p!=password:
                print('wrong password')
                choiceee=int(input("Press 1 to retry 2 to quit"))
                if choiceee==1:
                    choice=1
                elif choiceee==2:
                    sys.exit()
        else:
            print("Enter a valid choice")
            break      
        
                
        
    cnm=input("Press y to continue and n to quit")
    if cnm=='y':
        choicee=1
    else:
        choicee=0

                
            
                
