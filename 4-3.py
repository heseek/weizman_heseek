import tkinter as tk

root = tk.Tk()
root.geometry('600x600')
root.resizable(True, False)

bt = []
k = 0
for i in range(1):
    for j in range(5):
        bt.append(tk.Button(text='버튼' + str(k + 1)))
        bt[k].place(x=100 * i, y=100 * j)
        k += 1

bt[0].config(bg='red', fg='white')
bt[1].config(bg='orange', fg='white')
bt[2].config(bg='yellow', fg='white')
bt[3].config(bg='green', fg='white')
bt[4].config(bg='blue', fg='white')

root.mainloop()
# # import tkinter as tk
# #
# # root = tk.Tk()
# # root.title("아이콘 연습")
# # root.geometry("640x400+100+100")
# # root.resizable(False, False)
# #
# # image = tk.PhotoImage(file='beetle.gif')
# # label = tk.Label(root, image=image)
# # label.pack()
# #
# # root.mainloop()
# import tkinter
# import tkinter.font
#
# root = tkinter.Tk()
#
# font = tkinter.font.Font(family='MS Serif', size=40, slant="italic")
# print(tkinter.font.families())
# label = tkinter.Label(root, text="파이썬 python", font=font)
# label.pack()
#
# root.mainloop()
