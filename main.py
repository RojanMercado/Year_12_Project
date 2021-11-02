 ###Random Math Test###

import tkinter as tk
from tkinter import font as tkfont
import random
# ***************************************************************************#

random_text = "sEkc beASt"

"""creating a list of positive integers greater than 1 and less than 10"""
integer_list = []
for i in range(10):
    if i > 1:
        integer_list.append(i)

# ***************************************************************************#


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=10, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


# ***************************************************************************#


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create the intro label
        intro_label = tk.Label(self, text="Rojan's Math Test")
        intro_label.pack(side="top", fill="x", pady=10)

        # Intro Label to introduce the student
        message_text = "Welcome! This is my maths test. Try it out for yourself!"
        message_label = tk.Label(self, text=message_text)
        message_label.pack(padx=10, pady=5, side="top")

        # Button to
        button1 = tk.Button(self, text="Play", command=lambda: controller.show_frame("PageOne"))
        button1.pack()


# ***************************************************************************#

### Pythagorean Theorem ##
pythagorean_triple_1 = [3,4,5]
new_list = []
n = random.randint(1,4)
for i in pythagorean_triple_1:
    new_list.append(i*n)
print(new_list)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        number = 1
        question_one_label = tk.Label(self, text="Question {}".format(number), font=controller.title_font) #Question One
        question_one_label.pack(side="top", fill="x", pady=10)
        
        question_one_text = tk.Label(self, text = "A triangle has a hypotenuse side length of {}, and another side length of {}".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        question_one_label = tk.Label(self, text = "What is the length of the other side?", padx = 10, pady = 5)
        users_input = tk.Entry(self)
        
        def Submit():
            data = users_input.get()
            print(data)
            users_input.destroy()
            user_answer = tk.Label(self, text=data, font=controller.title_font)
            user_answer.pack()
            submit.destroy()
            submit22 = tk.Button(self, text="submit", state='disabled')
            submit22.pack()
            button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageTwo"))
            button.pack()

            
        submit = tk.Button(self, text="submit", command =lambda: Submit())
        #button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageTwo"))
        #question_one = tk.Label(self, text = "A triangle has a hypotenuse side length of {}, and another side length of {}".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        
        
        question_one_text.pack()
        question_one_label.pack()
        users_input.pack()
        submit.pack()



# ***************************************************************************#

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        number = 2
        question_two_label = tk.Label(self, text = "Question {}".format(number), font = controller.title_font)
        question_two_label.pack(side="top", fill="x", pady=10)
        
        question_one_text = tk.Label(self, text = "blah blah blah blah".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        question_one_label = tk.Label(self, text = "What is 69 divided by len(blah)?", padx = 10, pady = 5)
        users_input = tk.Entry(self)

        def Submit():
            data = users_input.get()
            print(data)
            users_input.destroy()
            user_answer = tk.Label(self, text=data, font=controller.title_font)
            user_answer.pack()
            submit.destroy()
            submit22 = tk.Button(self, text="submit", state='disabled')
            submit22.pack()           
            button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageThree"))
            button.pack()
        
        submit = tk.Button(self, text="submit", command =lambda: Submit())
        #button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageTwo"))
        #question_one = tk.Label(self, text = "A triangle has a hypotenuse side length of {}, and another side length of {}".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        
        
        question_one_text.pack()
        question_one_label.pack()
        users_input.pack()
        submit.pack()


# ***************************************************************************#

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        number = 3
        label = tk.Label(self, text="Question Three", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        question_one_text = tk.Label(self, text = "blah blah blah blah".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        question_one_label = tk.Label(self, text = "What is 69 divided by len(blah)?", padx = 10, pady = 5)
        users_input = tk.Entry(self)

        def Submit():
            data = users_input.get()
            print(data)
            users_input.destroy()
            user_answer = tk.Label(self, text=data, font=controller.title_font)
            user_answer.pack()
            submit.destroy()
            submit22 = tk.Button(self, text="submit", state='disabled')
            submit22.pack()             
            button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageFour"))
            button.pack()
        
        submit = tk.Button(self, text="submit", command =lambda: Submit())
        #button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageTwo"))
        #question_one = tk.Label(self, text = "A triangle has a hypotenuse side length of {}, and another side length of {}".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        
        
        question_one_text.pack()
        question_one_label.pack()
        users_input.pack()
        submit.pack()


# ***************************************************************************#

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Question Four", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        question_one_text = tk.Label(self, text = "blah blah blah blah".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        question_one_label = tk.Label(self, text = "What is 69 divided by len(blah)?", padx = 10, pady = 5)
        users_input = tk.Entry(self)

        def Submit():
            data = users_input.get()
            print(data)
            users_input.destroy()
            user_answer = tk.Label(self, text=data, font=controller.title_font)
            user_answer.pack()
            submit.destroy()
            submit22 = tk.Button(self, text="submit", state='disabled')
            submit22.pack()            
            button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageFive"))
            button.pack()
        
        submit = tk.Button(self, text="submit", command =lambda: Submit())
        #button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageTwo"))
        #question_one = tk.Label(self, text = "A triangle has a hypotenuse side length of {}, and another side length of {}".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        
        
        question_one_text.pack()
        question_one_label.pack()
        users_input.pack()
        submit.pack()


# ***************************************************************************#

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Question Five", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        question_one_text = tk.Label(self, text = "blah blah blah blah".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        question_one_label = tk.Label(self, text = "What is 69 divided by len(blah)?", padx = 10, pady = 5)
        users_input = tk.Entry(self)

        def Submit():
            data = users_input.get()
            print(data)
            users_input.destroy()
            user_answer = tk.Label(self, text=data, font=controller.title_font)
            user_answer.pack()
            submit.destroy()
            submit22 = tk.Button(self, text="submit", state='disabled')
            submit22.pack()             
            button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageSix"))
            button.pack()
        
        submit = tk.Button(self, text="submit", command =lambda: Submit())
        #button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageTwo"))
        #question_one = tk.Label(self, text = "A triangle has a hypotenuse side length of {}, and another side length of {}".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        
        
        question_one_text.pack()
        question_one_label.pack()
        users_input.pack()
        submit.pack()


# ***************************************************************************#

class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Question Six", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        question_one_text = tk.Label(self, text = "blah blah blah blah".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        question_one_label = tk.Label(self, text = "What is 69 divided by len(blah)?", padx = 10, pady = 5)
        users_input = tk.Entry(self)

        def Submit():
            data = users_input.get()
            print(data)
            users_input.destroy()
            user_answer = tk.Label(self, text=data, font=controller.title_font)
            user_answer.pack()
            submit.destroy()
            submit22 = tk.Button(self, text="submit", state='disabled')
            submit22.pack()             
            button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageSeven"))
            button.pack()
        
        submit = tk.Button(self, text="submit", command =lambda: Submit())
        #button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageTwo"))
        #question_one = tk.Label(self, text = "A triangle has a hypotenuse side length of {}, and another side length of {}".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        
        
        question_one_text.pack()
        question_one_label.pack()
        users_input.pack()
        submit.pack()


# ***************************************************************************#

class PageSeven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Question Seven", font=controller.title_font)


        question_one_text = tk.Label(self, text = "Answers:".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        question_one_label = tk.Label(self, text = "69,420", padx = 10, pady = 5)

        
        question_one_text.pack()
        question_one_label.pack()

# ***************************************************************************#


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
print("hello")

# ***************************************************************************#

