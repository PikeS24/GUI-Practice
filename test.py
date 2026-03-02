#Pike Steck
#Stan Stojanovich

import tkinter
from tkinter import *
class lexerGUI:
    def __init__(self, root):
        self.master = root
        self.master.geometry("600x400")
        self.master.title("Lexical Analyzer for TinyPie")

        self.line = 0

        ##Set up and places
        ##top two text
        self.label1 = Label(self.master, text = "Source Code Input:")
        self.label1.grid(row=0, column=0, sticky=W)
        self.label2 = Label(self.master, text = "Lexical Analyzed Result:")
        self.label2.grid(row=0, column=3, sticky=E)
        ##text boxes
        self.codeentry = Text(self.master, height = 10, width = 30)
        self.codeentry.grid(row=1, column = 0, columnspan=2)
        self.outputT = Text(self.master, height=10, width=30)
        self.outputT.grid(row=1, column=3, columnspan=2)
        ##Bottom text
        self.label3 = Label(self.master, text="Current Processing Line:")
        self.label3.grid(row=2, column=0)
        ##Next button
        self.nextButton = Button(self.master, text= "Next Line", command= self.nextline)
        self.nextButton.grid(row= 3, column=0)
        ##counter
        self.label4 = Label(self.master, text = self.line)
        self.label4.grid(row= 2, column=2)
        ##quit button
        self.quitButton = Button(self.master, text= "Quit", command=self.quit)
        self.quitButton.grid(row=3, column=4)

    ##what next button does
    def nextline(self):
        self.codeLine = self.codeentry.get("1.0", "end-1c")
        self.codeList = self.codeLine.splitlines()
        printingline = self.codeList[self.line] + "\n"
        self.outputT.insert(tkinter.END, printingline)
        self.line = self.line +1
        self.label4.config(text = self.line)


    def quit(self):
        self.master.destroy()

if __name__ == '__main__':
    myTkRoot = Tk()
    lexer_gui = lexerGUI(myTkRoot)

    myTkRoot.mainloop()
