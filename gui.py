from tkinter import *
from questions import questions, choices, answer





class Quiz:
    def __init__(self, master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        self.button2 = Button(master, text="Back", command=self.back_btn)
        self.button2.pack(side=BOTTOM, pady=10)
        self.button = Button(master, text="Next", command=self.next_btn)
        self.button.pack(side=BOTTOM)
        
        

    def create_q(self, master, qn):
        b = Label(master, text="Geography Quiz")
        labelfont = ('times', 20, 'bold')
        b.config(font=labelfont)
        b.pack(side=TOP, pady=10)

        w = Label(master, text=questions[qn])
        w.pack(side=TOP, pady=10)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="", variable=self.opt_selected, value=b_val+1)
            b.append(btn)
            btn.pack(side=TOP, padx=10, pady=2)
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = questions[qn]
        for op in choices[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == answer[qn]:
            return True
        return False

    def print_results(self):
        print("Score: ", self.correct, "/", len(questions))
        Button(root, text="Quit", command=root.destroy).pack(side=BOTTOM, padx=10, pady=10)


    def back_btn(self):
        print("go back")
        

    def next_btn(self):
        if self.check_q(self.qn):
            print("Correct")
            self.correct += 1
        else:
            print("Wrong")
        self.qn = self.qn + 1
        if self.qn >= len(questions):
            self.print_results()
            self.button.pack_forget()
            self.button2.pack_forget()
        else:
            self.display_q(self.qn)


            
root = Tk()
root.title('Geography Quiz')
root.geometry("500x300")
app = Quiz(root)
