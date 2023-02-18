#Python packages
#Tkinter - GUI
from tkinter import *
#Pillow for Imagery
from PIL import Image, ImageTk
#Regular Expression for String checker
import re
# Secrets for random alphanumeric string
import secrets
# String for string processes
import string

#Tkinter GUI
root = Tk()
root.title("GoGoChecKEY")

# Adjust size of the Window
root.geometry("900x550")
root.iconbitmap("images/image2.ico")


# Create Canvas
canvas1 = Canvas(root, width=800,
                 height=550)
canvas1.config(bg='#171717')
canvas1.pack(fill="both", expand=True)


#Add Logo
GoGoImage = Image.open("images/image3.png")
resize_logo = GoGoImage.resize((100,100))
Logo = ImageTk.PhotoImage(resize_logo)

# Display Logo
canvas1.create_image(450,100,image=Logo)

#rectangle
c1 = canvas1.create_rectangle(150,150,520,300, outline= "white", width=4, fill="#303030")
canvas1.move(c1, -100, 90)
c2 = canvas1.create_rectangle(150,150,520,300, outline= "white", width=4, fill="#303030")
canvas1.move(c2, 327, 90)

#Password Validator Entry box
entry = Entry(root, show='*')
txtbox = canvas1.create_window(200, 140, window=entry)

canvas1.move(txtbox,33, 150)


#Password Validator Label
ValidatorLabel = Label(root,
                           text="Password Validator: ",
                           fg="white",
                           bg="#303030").place(relx=.26,rely=.48,anchor=CENTER)


#Random Password Generator Label
RPGLabel = Label(root,
                           text="Random Password Generator: ",
                           fg="white",
                           bg="#303030").place(relx=.74,rely=.48,anchor=CENTER)

#=========================================================

#Password Validator Function
def Validator():

    #Adding Text Box
    text_box = Text(root, width=25, height=1)
    text_box.place(relx=.147,rely=.612)

    #List of output for Strength score
    strength = ['Password can not be Blank', 'Very Weak', 'Weak', 'Quite Ok', 'Ok', 'Strong', 'Very Strong']
    score = 1

    #Getting input from entry1
    entry1 = entry.get()

    #entry1 output to Run on the console for checking
    len(entry1), print(entry1)

    print
    entry1, len(entry1)

    #if no input entered
    if len(entry1) == 0:
        text_box.delete(1.0, "end-1c")
        text_box.insert("end-1c", strength[0])
        return

    #if the entered input is less than 7
    if len(entry1) < 7:
        text_box.delete(1.0, "end-1c")
        text_box.insert("end-1c", strength[1])
        return

    #if the entered input is more than or equal to 8
    if len(entry1) >= 8:
        score += 1

        #if entry 1 contains digits
        if re.search("[0-9]", entry1):
            score += 1

        #if entry1 contains uppercase and lowercase letters
        if re.search("[a-z]", entry1):
            score += 1
        if re.search("[A-Z]", entry1):
            score += 1
        #if entry1 contains '!'
        if re.search("!", entry1):
            score += 1

    #Displaying the Strength score
    text_box.delete(1.0, "end-1c")
    text_box.insert("end-1c", strength[score])

#===============================================================

#Random Password Generator
def RandomPasswordGenerator():

    # Adding Text Box
    text_box = Text(root, width=16, height=1)
    text_box.place(relx=.67, rely=.5125)

    #Geting ascii letters and digits
    letters = string.ascii_letters
    digits = string.digits

    #Password Variable
    password = ''
    #Password Length
    pass_length = 16

    #Combining letters and digits
    alphabets = letters + digits

    #To generate random password
    for i in range(pass_length):
        password += ''.join(secrets.choice(alphabets))

    #Displaying Random-generated password
    text_box.delete(1.0, "end-1c")
    text_box.insert("end-1c", password)

#================================================================


#Password Validator Button
checkStrBtn = Button(root, text="Check Strength", command=Validator, height=1, width=15)
btn1 = canvas1.create_window(200, 180, window=checkStrBtn)
canvas1.move(btn1, 32.5, 140)

#Random Generated Password Button
RPGBtn = Button(root, text="Generate Password", command=RandomPasswordGenerator, height=1, width=15)
btn2 = canvas1.create_window(200, 180, window=RPGBtn)
canvas1.move(btn2, 466.5, 160)


#Making the window unresizable
#Note: if window is unresizable, the widgets will be out of place
root.resizable(False,False)

# Execute tkinter window
root.mainloop()