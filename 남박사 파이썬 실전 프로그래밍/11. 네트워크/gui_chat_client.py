import tkinter

IP = ""
PORT = 0

def connect():
    global IP, PORT
    connect_string = input_string.get()
    addr = connect_string.split(":")
    IP = addr[0]
    PORT = addr[1]

w_connect = tkinter.Tk()
w_connect.title("접속대상")
tkinter.Label(w_connect, text="접속대상").grid(row=0, column=0)
input_string = tkinter.StringVar(value="127.0.0.1:13000")
input_addr = tkinter.Entry(w_connect, textvariable=input_string, width=20)
input_addr.grid(row=0, column=1, padx=5, pady=5)
c_button = tkinter.Button(w_connect, text="접속하기", command=connect)
c_button.grid(row=0, column=2, padx=5, pady=5)

width = 300
height = 45

screen_width = w_connect.winfo_screenmmwidth()
screen_height = w_connect.winfo_screenmmheight()

x = int((screen_width / 2) - (width / 2))
y = int((screen_height / 2) - (height / 2))

w_connect.geometry('{}x{}+{}+{}'.format(width, height, x, y))

w_connect.mainloop()