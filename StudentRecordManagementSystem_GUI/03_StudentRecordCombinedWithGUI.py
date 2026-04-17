from tkinter import *
from tkinter import ttk
import os
root = Tk()

def add_new_record(var_add_new_record_name, var_add_new_record_sap, var_add_new_record_contact, var_add_new_record_cource, textbox) :
    with open("StudentRecord.txt", "a") as f :
       f.write(var_add_new_record_name + " ")
       f.write(var_add_new_record_sap + " ")
       f.write(var_add_new_record_contact + " ")
       f.write(var_add_new_record_cource + "\n")
       
    # to display message output in textbox, we passed textbox argument to this function and insert the message
    # remember to first delete the previous message from textbox so that it can't overlapp with current message
    
    textbox.delete("1.0", END)
    textbox.insert(END, "Record added successfully")
    
def update_record(var_find_name, var_find_sap, var_update_record_contact, var_update_record_cource, textbox) :
    with open("StudentRecord.txt", "r") as f:
        # check for empty file
        f.seek(0, os.SEEK_END)
        if f.tell() == 0 :
            print("")
        else :
            f.seek(0)
            data_update_record = f.readlines()
            data_update_record = [i.split() for i in data_update_record]
        
        check = False
        update_index = -1
        for i in range(len(data_update_record)) :
            if data_update_record[i][0] == var_find_name and data_update_record[i][1] == var_find_sap :
                update_index = i
                check = True
        if check == True :
            data_update_record[update_index][2] = var_update_record_contact
            data_update_record[update_index][3] = var_update_record_cource
            textbox.delete("1.0",END)
            textbox.insert(END, "Record updated successfully")
        else :
            textbox.delete("1.0", END)
            textbox.insert(END, "Record not found")
            
    # reflecting update in file
    with open("StudentRecord.txt", "w") as f:
        for i in data_update_record :
            lines = " ".join(i) + "\n"
            f.write(lines)
    
def delete_record(var_delete_record_name, var_delete_record_sap, var_delete_record_contact, var_delete_record_cource, textbox) :
    with open("StudentRecord.txt", "r") as f :
        f.seek(0, os.SEEK_END)
        if f.tell() == 0 :
            textbox.delete("1.0", END)
            textbox.insert(END, "Empty file")
        else :
            f.seek(0)
            data_delete_record = f.readlines()
            data_delete_record = [i.split() for i in data_delete_record]
        
        check = False
        delete_index = -1
        for i in range(len(data_delete_record)) :
            if data_delete_record[i][0] == var_delete_record_name and data_delete_record[i][1] == var_delete_record_sap :
                delete_index = i
                check = True
        if check == True :
            data_delete_record = list(data_delete_record)
            data_delete_record.pop(delete_index)
            textbox.delete("1.0",END)
            textbox.insert(END, "Record deleted successfully")
        else :
            textbox.delete("1.0",END)
            textbox.insert(END, "Record not found")

    # reflecting updates in file
    with open("StudentRecord.txt", "w") as f:
        for i in data_delete_record :
            f.write(" ".join(i) + "\n")
    
def search_record(var_search_record_name, var_search_record_sap, textbox) :
    with open("StudentRecord.txt", "r") as f:
        f.seek(0, os.SEEK_END)
        if f.tell() == 0 :
            textbox.delete("1.0", END)
            textbox.insert(END, "Empty file")
        else :
            f.seek(0)
            data_search_record = f.readlines()
            data_search_record = [i.split() for i in data_search_record]
        
        check = False
        search_index = -1
        for i in range(len(data_search_record)) :
            if data_search_record[i][0] == var_search_record_name and data_search_record[i][1] == var_search_record_sap :
                search_index = i
                check = True
        if check == True :
            textbox.delete("1.0",END)
            textbox.insert(END, data_search_record[search_index])
        else :
            textbox.delete("1.0",END)
            textbox.insert(END, "Record not found")

def view_all_records(textboxLabelframe, textboxMessage) :
    with open("StudentRecord.txt", "r") as f:
        f.seek(0, os.SEEK_END)
        if f.tell() == 0 :
            textboxMessage.delete("1.0", END)
            textboxMessage.insert(END, "Empty file")
        else :
            f.seek(0)
            data_view_all_records = f.readlines()
            data_view_all_records = [i.split() for i in data_view_all_records]
            
            # convert upper list as a string
            textboxLabelframe.delete("1.0", END)
            for i in data_view_all_records :
                textboxLabelframe.insert(END, " ".join(i) + "\n")
        
root.title("Student Record System")

root.geometry("800x700+600+200")
root.resizable(False, False)

def open_add_new_record_window() :
    add_new_record_window = Toplevel(root)
    add_new_record_window.title("Add New Record")
    add_new_record_window.geometry("1200x450")
    # label frame (input details)
    labelframe_input_details = LabelFrame(add_new_record_window, text = "Input Details: ", font = ("Aerial", 25, "bold"), labelanchor = NW)
    labelframe_input_details.place(x = 40, y = 10, height = 350, width = 700)

    # label inside add_new_record_window
    labelframe_input_details_lab1 = Label(add_new_record_window, text = "Name : ", font = ("Aerial", 25))
    labelframe_input_details_lab1.place(x = 45, y = 65)

    labelframe_input_details_lab2 = Label(add_new_record_window, text = "SAP ID : ", font = ("Aerial", 25))
    labelframe_input_details_lab2.place(x = 45, y = 140)

    labelframe_input_details_lab3 = Label(add_new_record_window, text = "Contact : ", font = ("Aerial", 25))
    labelframe_input_details_lab3.place(x = 45, y = 215)

    labelframe_input_details_lab4 = Label(add_new_record_window, text = "Cource : ", font = ("Aerial", 25))
    labelframe_input_details_lab4.place(x = 45, y = 290)

    # entry box inside add_new_record_window
    var_add_new_record_name = StringVar()
    entry_box_labelframe_input_detials_1 = Entry(add_new_record_window, font = ("Aerial", 25), bd = 5, textvariable = var_add_new_record_name)
    entry_box_labelframe_input_detials_1.place(x = 290, y = 65, height = 40, width = 400)

    var_add_new_record_sap = StringVar()
    entry_box_labelframe_input_detials_2 = Entry(add_new_record_window, font = ("Aerial", 25), bd = 5, textvariable = var_add_new_record_sap)
    entry_box_labelframe_input_detials_2.place(x = 290, y = 140, height = 40, width = 400)

    var_add_new_record_contact = StringVar()
    entry_box_labelframe_input_detials_3 = Entry(add_new_record_window, font = ("Aerial", 25), bd = 5, textvariable = var_add_new_record_contact)
    entry_box_labelframe_input_detials_3.place(x = 290, y = 215, height = 40, width = 400)

    var_add_new_record_cource = StringVar()
    entry_box_labelframe_input_detials_4 = Entry(add_new_record_window, font = ("Aerial", 25), bd = 5, textvariable = var_add_new_record_cource)
    entry_box_labelframe_input_detials_4.place(x = 290, y = 290, height = 40, width = 400)

    # update button inside add_new_record_window
    updateButton_add_new_record_window = Button(add_new_record_window, text = "Add Record", font = ("Aerial", 25, "bold"), bg = "green", fg = "white", command = lambda: add_new_record(var_add_new_record_name.get(), var_add_new_record_sap.get(), var_add_new_record_contact.get(), var_add_new_record_cource.get(), textBox_add_new_record_window))
    updateButton_add_new_record_window.place(x = 240, y = 380)
    
    # message dialog box inside add_new_record_window
    messageBox_add_new_record_window = LabelFrame(add_new_record_window, text = "Message: ", font = ("Aerial", 25, "bold"), labelanchor = NW)
    messageBox_add_new_record_window.place(x = 800, y = 10, height = 400, width = 370)
    
    # Text box inside message box
    textBox_add_new_record_window = Text(add_new_record_window, font = ("Aerial", 25), bd = 8)
    textBox_add_new_record_window.place(x = 820, y = 60, height = 330, width = 320)
    
def open_update_record_window() :
    update_record_window = Toplevel(root)
    update_record_window.title("Update Record")
    update_record_window.geometry("990x900+100+600")
    
    # search details label frame
    labelframe_searchdetails_update_record = LabelFrame(update_record_window, text = ("Search Details: "), font = ("Aerial", 25, "bold"), labelanchor = NW)
    labelframe_searchdetails_update_record.place(x = 40, y = 10, height = 350, width = 700)
    
    # label inside search details label frame
    labelframe_input_details_lab1 = Label(update_record_window, text = "Name : ", font = ("Aerial", 25))
    labelframe_input_details_lab1.place(x = 45, y = 120)

    labelframe_input_details_lab2 = Label(update_record_window, text = "SAP ID : ", font = ("Aerial", 25))
    labelframe_input_details_lab2.place(x = 45, y = 220)

    # entry box inside search details label frame
    var_find_name = StringVar()
    entry_box_labelframe_input_detials_1 = Entry(update_record_window, font = ("Aerial", 25), bd = 5, textvariable = var_find_name)
    entry_box_labelframe_input_detials_1.place(x = 290, y = 120, height = 40, width = 400)

    var_find_sap = StringVar()
    entry_box_labelframe_input_detials_2 = Entry(update_record_window, font = ("Aerial", 25), bd = 5, textvariable = var_find_sap)
    entry_box_labelframe_input_detials_2.place(x = 290, y = 220, height = 40, width = 400)
    
    # label frame update_record
    labelframe_update_record = LabelFrame(update_record_window, text = "Update Record: ", font = ("Aerial", 25, "bold"), labelanchor = NW)
    labelframe_update_record.place(x = 40, y = 400, height = 190, width = 925)

    # label inside labelframe_update_record
    labelframe_update_record_lab1 = Label(update_record_window, text = "New Contact: ", font = ("Aerial", 25))
    labelframe_update_record_lab1.place(x = 70, y = 455)

    label_frame2_lab2 = Label(update_record_window, text = "New Cource: ", font = ("Aerial", 25))
    label_frame2_lab2.place(x = 70, y = 530)

    # entry box inside labelframe_update_record
    var_update_record_contact = StringVar()
    entry_labelframe_update_record_1 = Entry(update_record_window, font =("Aerial", 25), bd = 5, textvariable = var_update_record_contact)
    entry_labelframe_update_record_1.place(x = 310, y = 455, width = 400)

    var_update_record_cource = StringVar()
    entry_labelframe_update_record_2 = Entry(update_record_window, font =("Aerial", 25), bd = 5, textvariable = var_update_record_cource)
    entry_labelframe_update_record_2.place(x = 310, y = 530, width = 400)

    # update button inside labelframe_update_record
    button_labelframe_update_record = Button(update_record_window, text = "Update", font = ("Aerial", 25, "bold"), bg = "green", fg = "white", 
                                             command = lambda: update_record(var_find_name.get(), var_find_sap.get(), var_update_record_contact.get(), var_update_record_cource.get(), textBox_update_record_window))
    button_labelframe_update_record.place(x = 760, y = 493)
    
    # message dialog box inside update_record_window
    messageBox_update_record_window = LabelFrame(update_record_window, text = "Message: ", font = ("Aerial", 25, "bold"), labelanchor = NW)
    messageBox_update_record_window.place(x = 40, y = 620, height = 220, width = 600)
    
    # Text box inside message box
    textBox_update_record_window = Text(update_record_window, font = ("Aerial", 25), bd = 8)
    textBox_update_record_window.place(x = 60, y = 670, height = 155, width = 560)
    
    
def open_delete_record_window() :
    delete_record_window = Toplevel(root)
    delete_record_window.title("Delete Record Window")
    delete_record_window.geometry("1200x450+1000+100")

    # label frame delete record
    labelframe_delete_record = LabelFrame(delete_record_window, text = "Input Details:", font = ("Aerial", 25, "bold"), labelanchor = NW)
    labelframe_delete_record.place(x = 40, y = 10, height = 350, width = 700)

    # Labels inside delete record
    labelframe_search_record_lab1 = Label(delete_record_window, text = "Name : ", font = ("Aerial", 25))
    labelframe_search_record_lab1.place(x = 90, y = 60)

    labelframe_search_record_lab2 = Label(delete_record_window, text = "SAP ID : ", font = ("Aerial", 25))
    labelframe_search_record_lab2.place(x = 90, y = 135)

    labelframe_search_record_lab3 = Label(delete_record_window, text = "Contact : ", font = ("Aerial", 25))
    labelframe_search_record_lab3.place(x = 90, y = 210)

    labelframe_search_record_lab4 = Label(delete_record_window, text = "Cource : ", font = ("Aerial", 25))
    labelframe_search_record_lab4.place(x = 90, y = 285)

    # entrybox widget inside labelframe_search_record
    var_delete_record_name = StringVar()
    entry_labelframe_search_record_1 = Entry(delete_record_window, font = ("Aerial", 25), bd = 5, textvariable = var_delete_record_name)
    entry_labelframe_search_record_1.place(x = 310, y = 60, height = 40, width = 400)

    var_delete_record_sap = StringVar()
    entry_labelframe_search_record_2 = Entry(delete_record_window, font = ("Aerial", 25), bd = 5, textvariable = var_delete_record_sap)
    entry_labelframe_search_record_2.place(x = 310, y = 135, height = 40, width = 400)

    var_delete_record_contact = StringVar()
    entry_labelframe_search_record_3 = Entry(delete_record_window, font = ("Aerial", 25), bd = 5, textvariable = var_delete_record_contact)
    entry_labelframe_search_record_3.place(x = 310, y = 210, height = 40, width = 400)

    var_delete_record_cource = StringVar()
    entry_labelframe_search_record_4 = Entry(delete_record_window, font = ("Aerial", 25), bd = 5, textvariable = var_delete_record_cource)
    entry_labelframe_search_record_4.place(x = 310, y = 285, height = 40, width = 400)
    
    # update button inside delete_record_window
    button_labelframe_update_record = Button(delete_record_window, text = "Delete Record: ", font = ("Aerial", 25, "bold"), bg = "green", fg = "white",
                                             command = lambda: delete_record(var_delete_record_name.get(), var_delete_record_sap.get(), var_delete_record_contact.get(), var_delete_record_cource.get(), textBox_delete_record_window))
    button_labelframe_update_record.place(x = 240, y = 380)
    
    # message dialog box inside delete_record_window
    messageBox_delete_record_window = LabelFrame(delete_record_window, text = "Message: ", font = ("Aerial", 25, "bold"), labelanchor = NW)
    messageBox_delete_record_window.place(x = 800, y = 10, height = 400, width = 370)
    
    # Text box inside message box
    textBox_delete_record_window = Text(delete_record_window, font = ("Aerial", 25), bd = 8)
    textBox_delete_record_window.place(x = 820, y = 60, height = 330, width = 320)

def open_search_record_window() :
    search_record_window = Toplevel(root)
    search_record_window.title("Search Record Window")
    search_record_window.geometry("1200x450+1000+600")
    
    # label frame (search record)
    labelframe_search_record = LabelFrame(search_record_window, text = "Input Details: ", font = ("Aerial", 25, "bold"), labelanchor = NW)
    labelframe_search_record.place(x = 40, y = 10, height = 350, width = 700)

    # Labels inside labelframe_search_record
    labelframe_search_record_lab1 = Label(search_record_window, text = "Name : ", font = ("Aerial", 25))
    labelframe_search_record_lab1.place(x = 90, y = 110)

    labelframe_search_record_lab2 = Label(search_record_window, text = "SAP ID : ", font = ("Aerial", 25))
    labelframe_search_record_lab2.place(x = 90, y = 200)

    # entrybox widget inside labelframe_search_record
    var_search_record_name = StringVar()
    entry_labelframe_search_record_1 = Entry(search_record_window, font = ("Aerial", 25), bd = 5, textvariable = var_search_record_name)
    entry_labelframe_search_record_1.place(x = 310, y = 110, height = 40, width = 400)

    var_search_record_sap = StringVar()
    entry_labelframe_search_record_2 = Entry(search_record_window, font = ("Aerial", 25), bd = 5, textvariable = var_search_record_sap)
    entry_labelframe_search_record_2.place(x = 310, y = 200, height = 40, width = 400)
    
    # update button inside search_record_window
    button_labelframe_search_record = Button(search_record_window, text = "Search Record: ", font = ("Aerial", 25, "bold"), bg = "green", fg = "white", 
                                             command = lambda: search_record(var_search_record_name.get(), var_search_record_sap.get(), textBox_search_record_window))
    button_labelframe_search_record.place(x = 240, y = 380)
    
    # message dialog box inside search_record_window
    messageBox_search_record_window = LabelFrame(search_record_window, text = "Message: ", font = ("Aerial", 25, "bold"), labelanchor = NW)
    messageBox_search_record_window.place(x = 800, y = 10, height = 400, width = 370)
    
    # Text box inside message box
    textBox_search_record_window = Text(search_record_window, font = ("Aerial", 25), bd = 8)
    textBox_search_record_window.place(x = 820, y = 60, height = 330, width = 320)
    
def open_view_all_records_window() :
    view_all_records_window = Toplevel(root)
    view_all_records_window.title("View All Records")
    view_all_records_window.geometry("1300x440")
    
    # label frame output_record
    labelframe_view_all_records = LabelFrame(view_all_records_window, text = "Student Records",font = ("Aerial", 25, "bold"), labelanchor = N)
    labelframe_view_all_records.place(x = 40, y = 10, height = 370, width = 800)

    # textbox widget in label frame 3
    textbox_labelframe_viewall_record_1 = Text(view_all_records_window, font = ("Aerial", 25), bd = 5)
    textbox_labelframe_viewall_record_1.place(x = 60, y = 60, height = 300, width = 760)
    
    # message dialog box inside view_all_records_window
    messageBox_viewall_record_window = LabelFrame(view_all_records_window, text = "Message: ", font = ("Aerial", 25, "bold"), labelanchor = NW)
    messageBox_viewall_record_window.place(x = 890, y = 10, height = 400, width = 370)
    
    # Text box inside message box
    textBox_viewall_record_window = Text(view_all_records_window, font = ("Aerial", 25), bd = 8)
    textBox_viewall_record_window.place(x = 915, y = 60, height = 330, width = 320)
    
    view_all_records(textbox_labelframe_viewall_record_1, textBox_viewall_record_window)
    
lab1 = Label(root, text = "Student Record Menu", font = ("Aerial", 25, "bold"), bg = "blue", fg = "white")
lab1.place(x = 200, y = 50, height = 60, width = 450)

button_new_record = Button(text = "Add New Record", font = ("Aerial", 25), cursor = "hand2", command = open_add_new_record_window)
button_new_record.place(x = 255, y = 150, width = 300)

button_update_record = Button(text = "UpdateRecord", font = ("Aerial", 25), cursor = "hand2", command = open_update_record_window)
button_update_record.place(x = 255, y = 225, width = 300)

button_delete_record = Button(text = "Delete Record", font = ("Aerial", 25), cursor = "hand2", command = open_delete_record_window)
button_delete_record.place(x = 255, y = 300, width = 300)

button_search_record= Button(text = "Search Record", font = ("Aerial", 25), cursor = "hand2", command = open_search_record_window)
button_search_record.place(x = 255, y = 375, width = 300)

button_view_all_record = Button(text = "View All Records", font = ("Aerial", 25), cursor = "hand2", command = open_view_all_records_window)
button_view_all_record.place(x = 255, y = 450, width = 300)

button_exit = Button(text = "Exit", font = ("Aerial", 25), cursor = "hand2")
button_exit.place(x = 255, y = 525, width = 300)


root.mainloop()