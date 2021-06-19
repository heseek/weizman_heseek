# # # # import tkinter as tk
# # # #
# # # # root = tk.Tk()
# # # #
# # # # labell = tk.Label(root, text="안녕하세요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# # # # labell.pack()
# # # #
# # # # root.mainloop()
# # # import tkinter as tk
# # #
# # # root = tk.Tk()
# # # a = tk.Label(text="안녕")
# # # a.pack()
# # # a = tk.Label(text="+_+")
# # # a.pack()
# # # a = tk.Label(text="ㄴㅇㄱ")
# # # a.pack()
# # # a = tk.Label(text="ㅇ0ㅇ")
# # # a.pack()
# # # a = tk.Label(text="@_@")
# # # a.pack()
# # # a = tk.Label(text=";[")
# # # a.pack()
# # # a = tk.Label(text=":]")
# # # a.pack()
# # # a = tk.Label(text=";]")
# # # a.pack()
# # # a = tk.Label(text=":[")
# # # a.pack()
# # #
# # # b = tk.Entry()
# # # b.pack()
# # #
# # # root.mainloop()
# # import tkinter as tk
# #
# #
# # def okClick():
# #     name = b.get()
# #     print(name)
# #     a.config(text=name)
# #
# #
# # root = tk.Tk()
# #
# # a = tk.Label(text="*")
# # a.pack()
# #
# # b = tk.Entry()
# # b.pack()
# #
# # btn = tk.Button(root, text="1", command=okClick)
# # btn.pack()
# #
# # root.mainloop()
#
# import tkinter as tk
#
#
# def okClick():
#     name = b.get()
#     print(name)
#     a.config(text=name)
#
# def ret(event):
#     a.config(text='*')
#
# root = tk.Tk()
#
# a = tk.Label(text="*")
# a.pack()
#
# b = tk.Entry()
# b.pack()
#
# btn = tk.Button(root, text="1", command=okClick)
# btn.pack()
#
# a.bind('<Button-1>', ret)
# root.mainloop()
#
#
# import tkinter as tk
#
# root = tk.Tk()
#
# root.title("윤해식")
# root.geometry("640x400+100+100")
# root.resizable(True, True)
#
# a = tk.Label(text="1")
# a.pack()
#
# b = tk.Entry()
# b.pack()
#
# root.mainloop()
