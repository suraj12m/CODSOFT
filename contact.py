import customtkinter as ctk
import json
import os
from tkinter import messagebox
file_path = "contact.json"

def read_json():
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def write_json(new_data):
    with open(file_path, "w") as f:
        json.dump(new_data, f, indent=4)


def add_contact(func="add",contact=None):
    
    for widget in f3.winfo_children():
        widget.destroy()

    def check():
        data1=read_json()
        name=l1_n.get()
        ph=l2_p.get()
        em=l3_em.get()
        add=l4_add.get("1.0","end").strip('\n')
        l=[name,ph,em,add]
        ph_check=False
        ph1=False
        name_check=False
        names=[x[0] for x in data1["contact"]]
        phon=[x[1] for x in data1["contact"]]
        if name and ph and em and add:
            if(len(ph)==10 and ph.isnumeric()):
                ph_check=True
            if(l[0] not in names) :
                name_check=True
            if(l[1] not in phon):
                ph1=True
        if(func=="add"):
            if(ph_check and name_check and ph1):
                save_new()
            elif(not ph_check):
                messagebox.showerror("Error","Please enter 10 digit phone number")
            elif(not name_check):
                messagebox.showerror("Error","Name Already exist")
            elif(not ph1):
                messagebox.showerror("Error","Phone number Already exist")
        elif(func=="edit"):
            prev_name=contact[0]
            prev_ph=contact[1]
            if(name!=prev_name and name in names):
                messagebox.showerror("Error","Name Already exist")
            elif(ph!=prev_ph and ph in phon):
                messagebox.showerror("Error","Phone number Already exist")
            elif(name==prev_name and ph==prev_ph):
                    save_new()
            elif(name!=prev_name and ph!=prev_ph and name in names and ph in phon):
                messagebox.showerror("Error","Name and Phone number Already exist")
            else:
                if(ph_check):
                    save_new()
                elif(not ph_check):
                    messagebox.showerror("Error","Please enter 10 digit phone number")


    def save_new():
        data=read_json()
        name=l1_n.get()
        ph=l2_p.get()
        em=l3_em.get()
        add=l4_add.get("1.0","end").strip('\n')
        new=[name,ph,em,add]
        n=data["contact"]
        if func=="edit":
            if contact in n:
                n.remove(contact)
        n.append(new)
        new_data={"contact": n}
        write_json(new_data)
        if func=="edit":
            messagebox.showinfo("success",f"Updated {name} Successfully")
        else:
            messagebox.showinfo("success",f"Added {name} Successfully")
            
        data1=read_json()
        for widget in display1.winfo_children():
            widget.destroy()
        display(data1["contact"])
        show_contact(new)

    # Name
    l1_n.configure(state="normal")
    # Phone
    l2_p.configure(state="normal")
    # Email
    l3_em.configure(state="normal")
    # Address
    l4_add.configure(state="normal")
    
    if func=="add":
        l1_n.delete(0, "end")
        l2_p.delete(0, "end")
        l3_em.delete(0, "end")
        l4_add.delete("1.0", "end")

    save=ctk.CTkButton(f3,text="Save",height=45,command=check)
    save.place(x=265,y=15)


def search_contact(event=None):
    s=search.get()
    if s:
        for widget in display1.winfo_children():
            widget.destroy()
        data=read_json()
        l=[]
        for i in data["contact"]:
            if s in i[0] or s in i[1]:
                l.append(i)
        display(l)

def edit_contant(contact):
    add_contact("edit",contact)

def delete_contant(contact):
    confirm=messagebox.askyesno("Delete Confirmation",f"Are You Sure you Want to delete {contact[0]}")
    data=read_json()
    n=data["contact"]
    if confirm:
        n.remove(contact)
        new_data={"contact": n}
        write_json(new_data)
        messagebox.showinfo("deleted",f"Contact {contact[0]} deleted")
    for widget in display1.winfo_children():
        widget.destroy()
    for widget in f3.winfo_children():
        widget.destroy()
    display(n)

    l1_n.configure(state="normal")
    l2_p.configure(state="normal")
    l3_em.configure(state="normal")
    l4_add.configure(state="normal")
    
    l1_n.delete(0, "end")
    l2_p.delete(0, "end")
    l3_em.delete(0, "end")
    l4_add.delete("1.0", "end")

    l1_n.configure(state="disabled")
    l2_p.configure(state="disabled")
    l3_em.configure(state="disabled")
    l4_add.configure(state="disabled")


def show_contact(contact):
    name, phone, email, address = contact
    for widget in f3.winfo_children():
        widget.destroy()

    edit=ctk.CTkButton(f3,text="Edit",height=45,command=lambda: edit_contant(contact))
    edit.place(x=110,y=15)

    delete=ctk.CTkButton(f3,text="Delete",height=45,command=lambda: delete_contant(contact),fg_color="#D92727",hover_color="red")
    delete.place(x=265,y=15)

    # Name
    l1_n.configure(state="normal")
    l1_n.delete(0, "end")
    l1_n.insert(0, name)
    l1_n.configure(state="disabled")

    # Phone
    l2_p.configure(state="normal")
    l2_p.delete(0, "end")
    l2_p.insert(0, phone)
    l2_p.configure(state="disabled")

    # Email
    l3_em.configure(state="normal")
    l3_em.delete(0, "end")
    l3_em.insert(0, email)
    l3_em.configure(state="disabled")

    # Address
    l4_add.configure(state="normal")
    l4_add.delete("1.0", "end")
    l4_add.insert("1.0", address)
    l4_add.configure(state="disabled")

def display(data):
    data=sorted(data,key=lambda x: x[0].lower())
    # print(data)
    
    for i in data:
        row=ctk.CTkFrame(display1,fg_color="#3CB1F5",corner_radius=10,height=37)
        row.pack(fill="x",padx=5,pady=5)
        row.bind("<Button-1>", lambda e, c=i: show_contact(c))
        name_text=ctk.CTkLabel(row,text=f"👤 {i[0]}",text_color="black",font=("Arial",15))
        name_text.place(x=10,y=3)
        name_text.bind("<Button-1>", lambda e, c=i: show_contact(c))
        ph_text=ctk.CTkLabel(row,text=f"📞 {i[1]}",text_color="black",font=("Arial",15))
        ph_text.place(x=220,y=3)
        ph_text.bind("<Button-1>", lambda e, c=i: show_contact(c))



if __name__=="__main__":

    if not os.path.exists(file_path):
     with open(file_path,"w",encoding="utf-8") as f:
          json.dump({"contact":[]},f,indent=4)


    root=ctk.CTk()
    root.geometry("900x570")
    root.resizable(False,False)
    root.title("Contact")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    ctk.CTkLabel(root,text="Contact Book",font=("Imprint MT Shadow",35,"bold")).place(x=25,y=5)
    ctk.CTkLabel(root,text="Manage your contacts easily",font=("Candara Light",15)).place(x=80,y=38)
    new_contact=ctk.CTkButton(root,text="+ Add Contact",height=50,command=add_contact)
    new_contact.place(x=735,y=15)
    frame_color="#272626"
    f1=ctk.CTkFrame(root,fg_color=frame_color,height=475,width=400,border_color="#18181B",border_width=2)
    f1.place(x=15,y=80)
    f2=ctk.CTkFrame(root,fg_color=frame_color,height=475,width=450,border_color="#18181B",border_width=2)
    f2.place(x=430,y=80)
    f3=ctk.CTkFrame(f2,fg_color=frame_color,height=70,width=430)
    f3.place(x=10,y=390)

    #f1
    ctk.CTkLabel(f1,text="Contact List",font=("Arial Black",25),text_color="#83FF4A").place(x=10,y=5)
    search=ctk.CTkEntry(f1,width=376,height=35,placeholder_text="Enter name or number to search")
    search.place(x=10,y=45)
    search.bind("<Return>",search_contact)
    display1=ctk.CTkScrollableFrame(f1,width=352,height=360)
    display1.place(x=10,y=88)

    #f2
    ctk.CTkLabel(f2,text="Contact Details",font=("Arial Black",25),text_color="#83FF4A").place(x=10,y=5)
    l1=ctk.CTkLabel(f2,text="Name : ",font=("Bookman Old Style",20,"bold"))
    l1.place(x=15,y=55)

    l1_n=ctk.CTkEntry(f2,height=35,width=260,placeholder_text="NAME",border_color="grey",border_width=2,fg_color="#26272A")
    l1_n.configure(state="disabled")
    l1_n.place(x=115,y=55)

    l2=ctk.CTkLabel(f2,text="Phone : ",font=("Bookman Old Style",20,"bold"))
    l2.place(x=15,y=100)

    l2_p=ctk.CTkEntry(f2,height=35,width=260,placeholder_text="1234567890",border_color="grey",border_width=2,fg_color="#26272A")
    l2_p.configure(state="disabled")
    l2_p.place(x=115,y=100)

    l3=ctk.CTkLabel(f2,text="Email : ",font=("Bookman Old Style",20,"bold"))
    l3.place(x=15,y=150)

    l3_em=ctk.CTkEntry(f2,height=35,width=260,placeholder_text="abcd@gmail.com",border_color="grey",border_width=2,fg_color="#26272A")
    l3_em.configure(state="disabled")
    l3_em.place(x=115,y=150)

    l4=ctk.CTkLabel(f2,text="Address : ",font=("Bookman Old Style",20,"bold"))
    l4.place(x=15,y=200)

    l4_add=ctk.CTkTextbox(f2,height=155,width=260,border_color="grey",border_width=2,fg_color="#26272A")
    l4_add.configure(state="disabled")
    l4_add.place(x=115,y=200)



    data=read_json()
    display(data["contact"])
   
    root.mainloop()