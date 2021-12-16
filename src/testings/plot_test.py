import tkinter as tk
from matplotlib import pyplot as plt
root=tk.Tk()
root.geometry("200x100")

def Submit():
    value=value_entry.get()
    types=type_entry.get()
    tags=tags_entry.get()
    conn = sqlite3.connect("Balance.db")
    c = conn.cursor()
    c.execute("INSERT INTO Log VALUES (:value, :type, :tag)",
            {
                'value': value,
                'type': types,
                'tag': tags
            })
    conn.commit()
    conn.close()
    
    label=["value","type","tag"]
    data=[value,types,tags]
    fig = plt.figure(figsize =(5, 5)) 
    plt.pie(data, labels = label,autopct='%1.2f%%')
    plt.show()
    #clear the text boxes to allow for new input
    values.set("")
    typess.set("")
    tagss.set("")

values=tk.IntVar() 
typess=tk.IntVar()
tagss=tk.IntVar()

value_label = tk.Label(root, text = 'Value')
value_entry = tk.Entry(root, textvariable = values)
type_label = tk.Label(root, text = 'Type')
type_entry = tk.Entry(root, textvariable = typess)
tags_label = tk.Label(root, text = 'Tags')
tags_entry = tk.Entry(root, textvariable = tagss) 
Submit_Button = tk.Button(root, text = "Add to Logs", command = Submit)

value_label.grid(row=0,column=0) 
value_entry.grid(row=0,column=1) 
type_label.grid(row=1,column=0) 
type_entry.grid(row=1,column=1)
tags_label.grid(row=2,column=0) 
tags_entry.grid(row=2,column=1) 
Submit_Button.grid(row=3, column = 1)
   
root.mainloop() 