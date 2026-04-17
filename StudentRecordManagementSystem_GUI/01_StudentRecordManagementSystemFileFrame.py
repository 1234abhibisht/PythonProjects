import os

f = open("StudentRecord.txt", "w")

while (True) :
    print("Enter 1 to enter new record")
    print("Enter 2 to delete existing record")
    print("Enter 3 to update existing record")
    print("Enter 4 to display whole record")
    print("Enter 5 to display record of particular student")
    print("Enter 6 to exit program")
    choice = int(input("Enter your response from above options : "))
    match choice :
        case 1 :
            with open("StudentRecord.txt", "a+") as f :
                name = input("Enter name of student : ")
                f.write(name + " ")
                sap_id = input("Enter SAP ID of student : ")
                f.write(sap_id + " ")
                contact = input("Enter contact number of student : ")
                f.write(contact + " ")
                cource = input("Enter cource of student enrolled : ")
                f.write(cource + "\n")
            
            
        case 2 :
            sap_delete = input("Enter SAP Id of student to delete its details : ")
            with open("StudentRecord.txt", "r") as f :
                f.seek(0)
                data_delete = f.readlines()
                data_delete = [i.split() for i in data_delete]
            
                check_delete = False
                check_delete_index = -1
                for i in range(len(data_delete)) :
                    if data_delete[i][1] == sap_delete:
                        check_delete = True
                        check_delete_index = i
            
                if check_delete == False :
                    print("No data of such student found")
                else :
                    data_delete = list(data_delete)  
                    data_delete.pop(check_delete_index)
                
                # now converting above list to file string again
                with open("StudentRecord.txt", "w") as f :
                    for i in data_delete :
                        f.write(" ".join(i))
            
        case 3 :
            sap_update = input("Enter SAP Id of student to update it's details : ")
            with open("StudentRecord.txt", "r") as f :
                f.seek(0)
                data_update = f.readlines()
                data_update = [i.split() for i in data_update]
            
                check_update = False
                check_update_index = -1
                for i in range(len(data_update)) :
                    if data_update[i][1] == sap_update :
                        check_update = True
                        check_update_index = i
                if check_update == False :
                    print("No data of such student found")
                else :
                    print("a to update contact number")
                    print("b to update Cource")
                    choice_update = input("Enter response : ")
                    match choice_update :
                        
                        case 'a' :
                            new_contact = input("Enter new contact number : ")
                            data_update[check_update_index][2] = new_contact
                        
                        case 'b' :
                            new_cource = input("Enter new cource : ")
                            data_update[check_update_index][3] = new_cource
                        
            with open("StudentRecord.txt", "w") as f :
                for i in data_update :
                    lines = " ".join(i) + "\n"
                    f.write(lines)
            
        case 4 :
            # first check whether file is empty or not
            with open("StudentRecord.txt", "r") as f :
                f.seek(0, os.SEEK_END)
                if f.tell() == 0 :
                    print("No data of such student found")
                else :
                    f.seek(0)
                    data = f.readlines()   # after reading whole data, file pointer will come to last
                    data = [i.split() for i in data]
                    print(data)
                
        case 5 :
            sap_record = input("Enter SAP Id student to display its record : ")
            with open("StudentRecord.txt", "r") as f :
                f.seek(0)
                data_record = f.readlines()
                data_record = [i.split() for i in data_record]
                check_record = False
                check_index_record = -1
                for i in range(len(data_record)) :
                    if data_record[i][1] == sap_record :
                        check_record = True
                        check_index_record = i
                if check_record == True :
                    print("Details of",sap_record,"are : ",end = "")
                    print(data_record[check_index_record])
                else :
                    print("No data of this student found")
            
        case 6 :
            break
        
        
