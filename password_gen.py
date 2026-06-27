import customtkinter as ctk
import pyperclip
import secrets

def copy_password():
    pyperclip.copy(password_entry.get())

def generate_password():
    
    Uper="QWERTYUIOPASDFGHJKLZXCVBNM"
    Lower=Uper.lower()
    Number="1234567890"
    special="!@#$%^&*"
    chars=""
    password=[]
    if(UC.get()==1):
        password.append(secrets.choice(Uper))
        chars=chars+Uper
    if(LC.get()==1):
        password.append(secrets.choice(Lower))
        chars=chars+Lower
    if(Num.get()==1):
        password.append(secrets.choice(Number))
        chars=chars+Number
    if(Sym.get()==1):
        password.append(secrets.choice(special))
        chars=chars+special

    if (UC.get()==0 and LC.get()==0 and Num.get()==0 and Sym.get()==0):
        chars=Uper+Lower+Number+special
    rem=int(password_len.get())-len(password)
    for _ in range(rem):
        password.append(secrets.choice(chars))

    password="".join(password)
    if int(password_len.get())>12:
        password_entry.configure(font=("Arial Black", 15, "bold"))
    password_entry.configure(state="normal")
    password_entry.delete(0,"end")
    password_entry.insert(0,password)
    password_entry.configure(state="readonly")

root=ctk.CTk()
root.title("Password Generator")
root.geometry("350x400")
root.maxsize(350,400)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
ctk.CTkLabel(root,text="PASSWORD ",text_color="#3773FF",font=("Century", 20, "bold")).place(x=42,y=8)
ctk.CTkLabel(root,text="GENERATOR",font=("Century", 20, "bold")).place(x=170,y=8)

password_entry=ctk.CTkEntry(root,width=270,height=60,fg_color="#3A3939",text_color="#30FB99",font=("Arial Black", 25, "bold"),border_width=2,border_color="#8F3EF2")
password_entry.place(x=15,y=50)
password_entry.insert(0,"password")
password_entry.configure(state="readonly")

copy_bwt=ctk.CTkButton(root,text="⧉",command=copy_password,font=("Century", 20, "bold"),fg_color=root.cget("fg_color"),height=60,width=60,border_color="#A8A8A8",border_width=2)
copy_bwt.place(x=286,y=50)

f1=ctk.CTkFrame(root,height=165,width=320,border_width=2,border_color="#A8A8A8")
f1.place(y=120,x=15)

ctk.CTkLabel(f1,text="Charcter Types",text_color="#3773FF",font=("Century", 15, "bold","underline")).place(x=10,y=2)
UC=ctk.CTkCheckBox(f1,text="Uppercase Letters (A-Z)")
UC.place(x=20,y=40)
LC=ctk.CTkCheckBox(f1,text="Lowercase Letters (a-z)")
LC.place(x=20,y=70)
Num=ctk.CTkCheckBox(f1,text="Numbers (0-9)")
Num.place(x=20,y=100)
Sym=ctk.CTkCheckBox(f1,text="Special Characters (!@#$%^&*)")
Sym.place(x=20,y=130)

password_len=ctk.CTkComboBox(root,
                             values=["8","12","16","20"],
                             width=320,
                             border_width=2,
                             border_color="#A8A8A8"
                             )
password_len.place(x=15,y=300)

button=ctk.CTkButton(root,
                     text="Generate Password",
                     font=("Arial Black", 25, "bold"),
                     command=generate_password,
                     width=320,
                     height=50,
                     border_width=2,
                     border_color="#3773FF")
button.place(x=15,y=340)
root.bind("<Return>",lambda event:button.invoke())

root.mainloop()