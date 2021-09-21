import os
import threading
from tkinter import *
from http.server import HTTPServer, CGIHTTPRequestHandler

def launchserver():
    os.chdir('.')
    server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
    server_object.serve_forever()

def callback():
    serverthread = threading.Thread(target=launchserver)
    serverthread.start()

mainWindow = Tk()
mainWindow.title("HTTPServerLauncher")
mainWindow.geometry("200x100")

headLabel = Label(mainWindow, text="Launch server").pack()
launchButton = Button(mainWindow, text="Launch", command=callback).pack()

mainWindow.mainloop()
