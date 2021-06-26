# import tkinter as tk
# from tkinter.filedialog import *
# import os
#
#
# def savef():
#     f = asksaveasfile(mode="w", defaultextension=".txt")
#     if f is None:
#         return
#     ts = str(tx.get(1.0, END))
#     f.write(ts)
#     f.close()
#
#
# def openf():
#     file = askopenfile(title="파일 선택", filetypes=(("텍스트 파일", "*.txt"), ("모든 파일", "*.*")))
#     root.title(os.path.basename(file) + " - 메모장")
#     tx.delete(1.0, END)
#     f = open(file, "r")
#     tx.insert(1.0, f.read())
#     f.close()
#
#
# root = tk.Tk()
#
# root.title('메모장')
# root.geometry('640x640')
#
# mb = tk.Menu(root)
# fm = tk.Menu(mb, tearoff=0)
# mb.add_cascade(label="파일", menu=fm)
# fm.add_command(label='저장', command=savef)
# fm.add_command(label='블러오기', command=openf)
# root.config(menu=mb)
#
# tx = tk.Text()
# tx.pack()
#
# root.mainloop()
