# import tkinter as tk
#
# root = tk.Tk()
# root.geometry("320x240")
# root.title("Frame Test")
#
# frame = tk.Frame(root, bd=5, bg='light blue', relief='groove')
# frame.pack()
#
# l_frame = tk.Frame(root, bd=40, bg='white')
# l_frame.pack(side=tk.LEFT)
#
# l_frame1 = tk.Frame(l_frame, bd=40, bg='white')
# l_frame1.pack(side=tk.LEFT)
#
# l_frame2 = tk.Frame(l_frame, bd=40, bg='white')
# l_frame2.pack(side=tk.RIGHT)
#
# r_frame = tk.Frame(root)
# r_frame.pack(side=tk.RIGHT)
#
# label = tk.Label(frame, text='Hello Tkinter!')
# label.pack()
#
# button1 = tk.Button(l_frame1, text='Button 1')
# button1.pack(padx=10, pady=10)
#
# button11 = tk.Button(l_frame1, text='Button 11')
# button11.pack(padx=10, pady=10)
#
# button12 = tk.Button(l_frame1, text='Button 12')
# button12.pack(padx=10, pady=10)
#
# button2 = tk.Button(r_frame, text='Button 2', bd=5, bg='blue')
# button2.pack(padx=10, pady=10)
#
# button3 = tk.Button(l_frame2, text='Button 3', bd=5, bg='light blue')
# button3.pack(padx=10, pady=10)
#
# button4 = tk.Button(r_frame, text='Button 4')
# button4.pack(padx=10, pady=10)
#
# root.mainloop()
import tkinter as tk
import tkinter.filedialog as tkf


def domenu():
    pass


def save():
    f = tkf.asksaveasfile(mode="w", defaultextension=".txt")
    if f is None:
        return
    ts = str(text.get(1.0, END))
    f.write(ts)
    f.close()

root = tk.Tk()
mb = tk.Menu(root)
fmb = tk.Menu(mb, tearoff=0)

mb.add_cascade(label='파일', menu=fmb)
fmb.add_command(label='불러오기', command=domenu)
fmb.add_command(label='저장', command=save)
fmb.add_command(label='새파일', command=domenu)
fmb.add_command(label='다른이름으로 저장', command=domenu)
fmb.add_command(label='5', command=domenu)

emb = tk.Menu(mb, tearoff=0)
mb.add_cascade(label='애디트', menu=emb)
emb.add_command(label='복사', command=domenu)
emb.add_command(label='붙여놓기', command=domenu)
emb.add_command(label='반복', command=domenu)
emb.add_command(label='되돌리기', command=domenu)
emb.add_command(label='＊', command=domenu)

text = tk.Text(root, height=30, width=80)
text.pack()
root.config(menu=mb)
root.mainloop()
