import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title('Ontario Mental Health Services')
window.geometry('1410x825')

def clearEntry(event=None):
    e1.delete('0', END)

def clearTree():
    for item in tree.get_children():
        tree.delete(item)


def search(event=None):
    clearTree()
    #with open('Book2.csv', mode='r') as file:
    with open('MentalHealthServicesON.csv', mode='r') as file:
        data = csv.reader(file)

        i = e1_value.get().title()

        recordFound = False
        for row in data:
            if row[4] == i:
                tree.insert('', 'end', values=(row[0], row[1], row[2] + ' ' + row[3],
                                               row[13], row[15]))
                recordFound = True

        if not recordFound:
            messagebox.showinfo('Error', 'No city found. Please recheck the city name you entered or try another city.')


def selectItem(event):
    with open('MentalHealthServicesON.csv', mode='r') as file:
        data = csv.reader(file)

        cur_item = tree.item(tree.focus())
        cur_item = cur_item['values'][0]

        for row in data:
            if row[0] == str(cur_item):
                t1.delete('1.0', END)
                t1.insert(END, 'Agency Number: ' + row[0] + '\n\n')
                t1.insert(END, 'Service Name: ' + row[1] + '\n\n')
                t1.insert(END, 'Address: ' + row[2] + ' ' + row[3] + '\n\n')
                t1.insert(END, 'City: ' + row[4] + '\n\n')
                t1.insert(END, 'County: ' + row[5] + '\n\n')
                t1.insert(END, 'Province: ' + row[6] + '\n\n')
                t1.insert(END, 'Postal Code: ' + row[7] + '\n\n')
                t1.insert(END, 'Country: ' + row[8] + '\n\n')
                t1.insert(END, 'Toll Free Phone Number: ' + row[11] + '\n\n')
                t1.insert(END, 'Hotline Phone Number: ' + row[12] + '\n\n')
                t1.insert(END, 'Business Phone Number: ' + row[13] + '\n\n')
                t1.insert(END, 'Email Address: ' + row[14] + '\n\n')
                t1.insert(END, 'Website: ' + row[15] + '\n\n')
                t1.insert(END, 'Mental Health Service Description: ' + row[16] + '\n\n')
                t1.insert(END, 'Eligibility : ' + row[17] + '\n\n')
                t1.insert(END, 'Disability Access: ' + row[18] + '\n\n')
                t1.insert(END, 'Fee Structure: ' + row[19] + '\n\n')
                t1.insert(END, 'Application Process: ' + row[20] + '\n\n')
                t1.insert(END, 'Documents Required: ' + row[21] + '\n\n')
                t1.insert(END, 'Languages Offered: ' + row[22] + '\n\n')
                t1.insert(END, 'Program Agency Name: ' + row[23] + '\n\n')
                t1.insert(END, 'Site Agency Name: ' + row[24] + '\n\n')
                t1.insert(END, 'Hours of Operation: ' + row[25])


frame = Frame(window)
frame.grid(row=0, column=0)

l1 = Label(frame, text='Please Enter A City in Ontario:  ', font=('Times New Roman', 11))
l1.grid(row=0, column=0)

l2 = Label(frame, text='Click on a row to learn more information.', font=('Times New Roman', 11))
l2.grid(row=1, column=1)

e1_value = StringVar()
e1 = Entry(frame, textvariable=e1_value)
e1.grid(row=0, column=1)
e1.bind('<Return>', search)
e1.bind('<Button-1>', clearEntry)
e1.bind('<FocusIn>', clearEntry)

b1 = Button(frame, text='Search', command=search)
b1.grid(row=0, column=2, padx=15)

style = ttk.Style()
style.configure('mystyle.Treeview', highlightthickness=0, bd=0, font=('Times New Roman', 11))
style.configure('mystyle.Treeview.Heading', font=('Times New Roman', 13,'bold'))
style.layout('mystyle.Treeview', [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

tree = ttk.Treeview(window, style='mystyle.Treeview', column=('c1', 'c2', 'c3', 'c4', 'c5'), show='headings', height=15)
tree.column('# 1', width=200, anchor=CENTER)
tree.heading('# 1', text='Facility Number')
tree.column('# 2', width=400, anchor=CENTER)
tree.heading('# 2', text='Name')
tree.column('# 3', width=300, anchor=CENTER)
tree.heading('# 3', text='Address')
tree.column('# 4', width=200, anchor=CENTER)
tree.heading('# 4', text='Business Phone Number')
tree.column('# 5', width=250, anchor=CENTER)
tree.heading('# 5', text='Website')
tree.grid(row=1, column=0, padx=20, pady=15, sticky='w')

tree.bind('<ButtonRelease-1>', selectItem)

scrollBar2 = ttk.Scrollbar(window,command=tree.yview, orient='vertical')
scrollBar2.grid(row=1, column=0, sticky='ens')
tree.configure(yscrollcommand=scrollBar2.set)

t1 = Text(window, width=150, height=21, font=('Times New Roman', 13))
t1.grid(row=2, column=0, padx=20, sticky='w')

scrollBar1 = Scrollbar(window, command=t1.yview, orient='vertical')
scrollBar1.grid(row=2, column=0, sticky='ens')
t1.configure(yscrollcommand=scrollBar1.set)

window.mainloop()
