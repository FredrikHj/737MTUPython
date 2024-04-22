from tkinter import *
from api.ConnectionAPI import APIPhidgets, APIFsuipc

def runConStates(root):
   Label(root, text=APIPhidgets["connectionState"]).grid(row=1, column=2)
   Label(root, text=APIFsuipc["connectionState"]).grid(row=1, column=5)