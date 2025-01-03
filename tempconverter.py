import tkinter as tk

def cels_to_frhnt():
    try:
        celsius = float(user_input.get("1.0",tk.END))
    except ValueError:
        label.config(text="Invalid Input")
    
    frhnt = (celsius*1.8) + 32
    label.config(text=f"Converted Temperature: {frhnt}°F")

def frhnt_to_cels():
    try:
        fahrenheit = float(user_input.get("1.0",tk.END))
    except ValueError:
        label2.config(text="Invalid Input")
        return
    
    celsius = (fahrenheit-32) * (5/9)
    label2.config(text=f"Converted Temperature: {celsius}°C")

def prefilledtext_clear(event):
    if user_input.get("1.0",tk.END).strip() == "Enter Here...":
        user_input.delete("1.0",tk.END)

button_style = {
    "font" : ("Bahnschrift SemiBold",15,"bold"),
    "bg" : "#4CAF50",
    "fg" : "White",
    "relief" : "raised",
    "bd" : 5,
    "width" : 19,
    "height" : 1,
    "cursor" : "hand2"
}

root = tk.Tk()
root.geometry("400x400")
root.title("Temperature Converter")

user_input = tk.Text(root,width=15,height=1,font=("Helvetica",29))

user_input.config(bg="#4CAF50")
user_input.pack(pady=15)

user_input.bind("<FocusIn>",prefilledtext_clear)

user_input.insert("1.0","Enter Here...",)

label0 = tk.Label(root,text="Convert Temperature",font=("Bahnschrift SemiBold",27,),background="Dark green",fg="White")
label0.pack(pady=20)

button = tk.Button(root,text="Celsius to Fahrenheit",command=cels_to_frhnt,**button_style)
button.pack(pady=5)

label = tk.Label(root,text="",font=("Arial",10))
label.pack()

button2 = tk.Button(root,text="Fahrenheit to Celsius",command=frhnt_to_cels,**button_style)
button2.pack(pady=5)

label2 = tk.Label(text="",font=("Arial",10))
label2.pack()

root.mainloop()
