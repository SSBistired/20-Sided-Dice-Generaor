from flask import Flask , render_template, request
from tkinter import *
import random


app = Flask(__name__)
root = Tk()
root.geometry('300x300')


l = Label(root, text="Chose your action")
l.pack()

def buttonFunction():
    dice = random.randint(1,20)
    print("You rolled a " + str(dice))
    myLabel = Label(root, text=" You rolled a " + str(dice))
    myLabel.pack()

    b = Button(root, text="Roll dice!", command=buttonFunction)
    b.pack()

    root.mainloop()


@app.route("/")
def hello_world():
    return 'Hello, Dungeon Master!'



if __name__ == "__main__":
    app.run(debug=True)
