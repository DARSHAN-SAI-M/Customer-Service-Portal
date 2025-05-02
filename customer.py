import tkinter as tk
import csv as csv
from tkinter import messagebox
import datetime

# Creating Main Window 
window = tk.Tk()
window.geometry('1000x800') 
window.title('custemer information')
window.configure(background='#1a1a1a')  

# Creating Frame 
frame = tk.Frame(
    window,
    background='#d4af37',  
    highlightbackground='#3d3d3d',  
    highlightthickness=5  
)

# add function 
def add():
    name=name_entry.get()
    phone=phone_entry.get()
    brand=brand_entry.get()
    problem=problem_entry.get()
    model=modelno_entry.get()
    date=datetime.date.today()

    if not name or not phone or not problem or not model :
        messagebox.showerror('Error','Please fill all the details')
    else:
        try:
            count=0
            x=open('customer.csv','r',newline='')
            z=csv.reader(x)
            for i in z :
                count+=1
        except:
            count=0
        
        phone = '+91'+phone
        x=open('customer.csv','a',newline='')
        y=csv.writer(x)
        p=[]
        p.append(count)
        p.append(model)
        p.append(name)
        p.append(phone)
        p.append(brand)
        p.append(problem)
        p.append(date)
        y.writerow(p)

        name_entry.delete(0,tk.END)
        phone_entry.delete(0,tk.END)
        brand_entry.delete(0,tk.END)
        problem_entry.delete(0,tk.END)
        modelno_entry.delete(0,tk.END)
        messagebox.showinfo("Success",f'complain has been rised and your complain no is {count}')


custom_font = ('Arial', 18, 'bold')  # New font style

# Name label and entry 
name_label = tk.Label(frame, text='Name', bg='#d4af37', fg='#1a1a1a', font=custom_font)
name_label.grid(column=2, row=0, padx=10, pady=5)

name_entry = tk.Entry(frame, font=custom_font)
name_entry.grid(column=3, row=0, padx=10, pady=5)

# Phone number label and entry 
phone_label = tk.Label(frame, text='Phone Number', bg='#d4af37', fg='#1a1a1a', font=custom_font)
phone_label.grid(column=2, row=1, padx=10, pady=5)

phone_entry = tk.Entry(frame, font=custom_font)
phone_entry.grid(column=3, row=1, padx=10, pady=5)

# Brand Name And Entry 
brand_label = tk.Label(frame, text='Brand Name', bg='#d4af37', fg='#1a1a1a', font=custom_font)
brand_label.grid(column=2, row=2, padx=10, pady=5)

brand_entry = tk.Entry(frame, font=custom_font)
brand_entry.grid(column=3, row=2, padx=10, pady=5)

# Problem Entry 
problem_label = tk.Label(frame, text='Problem', bg='#d4af37', fg='#1a1a1a', font=custom_font)
problem_label.grid(column=2, row=3, padx=10, pady=5)

problem_entry = tk.Entry(frame, font=custom_font)
problem_entry.grid(column=3, row=3, padx=10, pady=5)

# Model Number 
modelno_label = tk.Label(frame, text='Model number', bg='#d4af37', fg='#1a1a1a', font=custom_font)
modelno_label.grid(column=2, row=4, padx=10, pady=5)

modelno_entry = tk.Entry(frame, font=custom_font)
modelno_entry.grid(column=3, row=4, padx=10, pady=5)

# submit button 
submit_button = tk.Button(
    frame,
    text='SUBMIT',
    command=add,
    bg='#b22222',  
    fg='white',
    font=custom_font,
    bd=3,
    relief='ridge'
)
submit_button.grid(column=3, row=5, padx=10, pady=20)

frame.pack(expand=True, padx=20, pady=20)
window.mainloop()