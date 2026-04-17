from tkinter import *
from tkinter import ttk
root = Tk()
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
    updateButton_add_new_record_window = Button(add_new_record_window, text = "Add Record", font = ("Aerial", 25, "bold"), bg = "green", fg = "white")
    updateButton_add_new_record_window.place(x = 240, y = 380)
    
    # message dialog box inside add_new_record_window
    messageBox_add_new_record_window = LabelFrame(add_new_record_window, text = "Message: ", font = ("Aerial", 25, "bold"), labelanchor = NW)
    messageBox_add_new_record_window.place(x = 800, y = 10, height = 400, width = 370)
    
    # seperator_add_new_record_window = ttk.Separator(add_new_record_window, orient = "vertical")
    # seperator_add_new_record_window.place(x = 400)
    
    # Text box inside message box
    textBox_add_new_record_window = Text(add_new_record_window, font = ("Aerial", 25), bd = 8)
    textBox_add_new_record_window.place(x = 820, y = 60, height = 330, width = 320)
    
    
def open_update_record_window() :
    update_record_window = Toplevel(root)
    update_record_window.title("Update Record")
    update_record_window.geometry("990x450+100+600")
    
    # label frame update_record
    labelframe_update_record = LabelFrame(update_record_window, text = "Update Record: ", font = ("Aerial", 25, "bold"), labelanchor = N)
    labelframe_update_record.place(x = 40, y = 10, height = 190, width = 925)

    # label inside labelframe_update_record
    labelframe_update_record_lab1 = Label(update_record_window, text = "New Contact: ", font = ("Aerial", 25))
    labelframe_update_record_lab1.place(x = 70, y = 60)

    label_frame2_lab2 = Label(update_record_window, text = "New Cource: ", font = ("Aerial", 25))
    label_frame2_lab2.place(x = 70, y = 130)

    # entry box inside labelframe_update_record
    entry_labelframe_update_record_1 = Entry(update_record_window, font =("Aerial", 25), bd = 5)
    entry_labelframe_update_record_1.place(x = 310, y = 60, width = 400)

    entry_labelframe_update_record_2 = Entry(update_record_window, font =("Aerial", 25), bd = 5)
    entry_labelframe_update_record_2.place(x = 310, y = 135, width = 400)

    # update button inside labelframe_update_record
    button_labelframe_update_record = Button(update_record_window, text = "Update", font = ("Aerial", 25, "bold"), bg = "green", fg = "white")
    button_labelframe_update_record.place(x = 760, y = 85)
    
    # message dialog box inside update_record_window
    messageBox_add_new_record_window = LabelFrame(update_record_window, text = "Message: ", font = ("Aerial", 25, "bold"), labelanchor = NW)
    messageBox_add_new_record_window.place(x = 40, y = 220, height = 220, width = 600)
    
    # Text box inside message box
    textBox_add_new_record_window = Text(update_record_window, font = ("Aerial", 25), bd = 8)
    textBox_add_new_record_window.place(x = 60, y = 270, height = 155, width = 560)
    
    
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
    entry_labelframe_search_record_1 = Entry(delete_record_window, font = ("Aerial", 25), bd = 5)
    entry_labelframe_search_record_1.place(x = 310, y = 60, height = 40, width = 400)

    entry_labelframe_search_record_2 = Entry(delete_record_window, font = ("Aerial", 25), bd = 5)
    entry_labelframe_search_record_2.place(x = 310, y = 135, height = 40, width = 400)

    entry_labelframe_search_record_3 = Entry(delete_record_window, font = ("Aerial", 25), bd = 5)
    entry_labelframe_search_record_3.place(x = 310, y = 210, height = 40, width = 400)

    entry_labelframe_search_record_4 = Entry(delete_record_window, font = ("Aerial", 25), bd = 5)
    entry_labelframe_search_record_4.place(x = 310, y = 285, height = 40, width = 400)
    
    # update button inside delete_record_window
    button_labelframe_update_record = Button(delete_record_window, text = "Delete Record: ", font = ("Aerial", 25, "bold"), bg = "green", fg = "white")
    button_labelframe_update_record.place(x = 240, y = 380)
    
    # message dialog box inside delete_record_window
    messageBox_add_new_record_window = LabelFrame(delete_record_window, text = "Message: ", font = ("Aerial", 25, "bold"), labelanchor = NW)
    messageBox_add_new_record_window.place(x = 800, y = 10, height = 400, width = 370)
    
    # Text box inside message box
    textBox_add_new_record_window = Text(delete_record_window, font = ("Aerial", 25), bd = 8)
    textBox_add_new_record_window.place(x = 820, y = 60, height = 330, width = 320)

def open_search_record_window() :
    search_record_window = Toplevel(root)
    search_record_window.title("Search Record Window")
    search_record_window.geometry("1200x450+1000+600")
    
    # label frame (search record)
    labelframe_search_record = LabelFrame(search_record_window, text = "Input Details: ", font = ("Aerial", 25, "bold"), labelanchor = NW)
    labelframe_search_record.place(x = 40, y = 10, height = 350, width = 700)

    # Labels inside labelframe_search_record
    labelframe_search_record_lab1 = Label(search_record_window, text = "Name : ", font = ("Aerial", 25))
    labelframe_search_record_lab1.place(x = 90, y = 60)

    labelframe_search_record_lab2 = Label(search_record_window, text = "SAP ID : ", font = ("Aerial", 25))
    labelframe_search_record_lab2.place(x = 90, y = 135)

    labelframe_search_record_lab3 = Label(search_record_window, text = "Contact : ", font = ("Aerial", 25))
    labelframe_search_record_lab3.place(x = 90, y = 210)

    labelframe_search_record_lab4 = Label(search_record_window, text = "Cource : ", font = ("Aerial", 25))
    labelframe_search_record_lab4.place(x = 90, y = 285)

    # entrybox widget inside labelframe_search_record
    entry_labelframe_search_record_1 = Entry(search_record_window, font = ("Aerial", 25), bd = 5)
    entry_labelframe_search_record_1.place(x = 310, y = 60, height = 40, width = 400)

    entry_labelframe_search_record_2 = Entry(search_record_window, font = ("Aerial", 25), bd = 5)
    entry_labelframe_search_record_2.place(x = 310, y = 135, height = 40, width = 400)

    entry_labelframe_search_record_3 = Entry(search_record_window, font = ("Aerial", 25), bd = 5)
    entry_labelframe_search_record_3.place(x = 310, y = 210, height = 40, width = 400)

    entry_labelframe_search_record_4 = Entry(search_record_window, font = ("Aerial", 25), bd = 5)
    entry_labelframe_search_record_4.place(x = 310, y = 285, height = 40, width = 400)
    
    # update button inside search_record_window
    button_labelframe_update_record = Button(search_record_window, text = "Search Record: ", font = ("Aerial", 25, "bold"), bg = "green", fg = "white")
    button_labelframe_update_record.place(x = 240, y = 380)
    
    # message dialog box inside search_record_window
    messageBox_add_new_record_window = LabelFrame(search_record_window, text = "Message: ", font = ("Aerial", 25, "bold"), labelanchor = NW)
    messageBox_add_new_record_window.place(x = 800, y = 10, height = 400, width = 370)
    
    # Text box inside message box
    textBox_add_new_record_window = Text(search_record_window, font = ("Aerial", 25), bd = 8)
    textBox_add_new_record_window.place(x = 820, y = 60, height = 330, width = 320)
    
def open_view_all_records_window() :
    view_all_records_window = Toplevel(root)
    view_all_records_window.title("View All Records")
    view_all_records_window.geometry("1300x440")
    
    # label frame output_record
    labelframe_view_all_records = LabelFrame(view_all_records_window, text = "Student Records",font = ("Aerial", 25, "bold"), labelanchor = N)
    labelframe_view_all_records.place(x = 40, y = 10, height = 370, width = 800)

    # textbox widget in label frame 3
    textbox_labelframe_output_record_1 = Text(view_all_records_window, font = ("Aerial", 25), bd = 5)
    textbox_labelframe_output_record_1.place(x = 60, y = 60, height = 300, width = 760)
    
    # message dialog box inside view_all_records_window
    messageBox_add_new_record_window = LabelFrame(view_all_records_window, text = "Message: ", font = ("Aerial", 25, "bold"), labelanchor = NW)
    messageBox_add_new_record_window.place(x = 890, y = 10, height = 400, width = 370)
    
    # Text box inside message box
    textBox_add_new_record_window = Text(view_all_records_window, font = ("Aerial", 25), bd = 8)
    textBox_add_new_record_window.place(x = 915, y = 60, height = 330, width = 320)
    
    
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