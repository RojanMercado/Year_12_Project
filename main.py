  ###Random Math Test###

import tkinter as tk
from tkinter import font as tkfont
import random
import math

# ***************************************************************************#

random_text = "sEkc beASt"

"""creating a list of positive integers greater than 1 and less than 10"""
integer_list = []
for i in range(10):
    if i > 1:
        integer_list.append(i)
def two():
    two = 2
def one():
    one = 1
def gap():
    gap = "gap"
# ***************************************************************************#
def negative(b,c):
    global ne_po
    negative = random.randint(0,c)
    if negative >= 0 and negative < 1:
        b = b-(b+b)
    if negative >= 1:
        b = b
    ne_po = b

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
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix):
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
            data1 = users_input.get()
            print(data1)
            users_input.destroy()
            user_answer = tk.Label(self, text=data1, font=controller.title_font)
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

        x = random.randint(-3,7)
        while True:
            random_number1 = random.randint(-8,12)
            if random_number1 != 1:
                if random_number1 != -1:
                    break
        random_number2 = random.randint(-5,6)
        
        random_chancer = random.randint(0,1)
        random_chancer2 = random.randint(0,1)

        if random_number2 > 0:
            question_two_text = ("{}{}+{} = {}".format(random_number1, "x", random_number2, (random_number1*x+random_number2)))
        if random_number2 < 0:
            question_two_text = ("{}{}{} = {}".format(random_number1, "x", random_number2, (random_number1*x+random_number2)))
        """if random_number2 > 0:
            if random_chancer2 == 1:
                question_two_text = ("{}{}+{} = {}".format(random_number1, x, random_number2, (random_number1*x+random_number2)))
                
            if random_chancer2 == 0:
                if random_number1 > 0:
                    question_two_text = ("{} = {}+{}{}".format((random_number1*x+random_number2), random_number2, random_number1, x))
                if random_number1 < 0:
                    question_two_text = ("{} = {}{}{}{}".format((random_number1*x+random_number2), random_number2, "",random_number1, x)"""

        
        question_two_text = tk.Label(self, text = question_two_text, padx = 10, pady = 5)
        question_two_label = tk.Label(self, text = "What is 'x'?", padx = 10, pady = 5)
        users_input = tk.Entry(self)
        print(x)
        
        def Submit():
            data2 = users_input.get()
            print(data2)
            users_input.destroy()
            user_answer = tk.Label(self, text=data2, font=controller.title_font)
            user_answer.pack()
            submit.destroy()
            submit22 = tk.Button(self, text="submit", state='disabled')
            submit22.pack()           
            button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageThree"))
            button.pack()
        
        submit = tk.Button(self, text="submit", command =lambda: Submit())
        #button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageTwo"))
        #question_one = tk.Label(self, text = "A triangle has a hypotenuse side length of {}, and another side length of {}".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        
        
        question_two_text.pack()
        question_two_label.pack()
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
        
        THREE_list = []
        for i in range(1000):
            r = random.randint(5,12)
            if r not in THREE_list:
                THREE_list.append(r)
        """DRAWING 'LOTS' FOR NON REPEATING RANDOM NUMBERS"""
        THREE_first_index = random.randint(0,3)
        THREE_second_index = random.randint(4,7)

        """User's first quadratic question"""
        THREE_first_number = THREE_list[THREE_first_index]
        THREE_second_number = THREE_list[THREE_second_index]

        """random negative or positive for first number"""
        negative(THREE_first_number,2)
        THREE_first_number = ne_po
        #securing first correct number
        THREE_CORRECT_FIRST = THREE_first_number

        """random negative or positive for second number"""
        negative(THREE_second_number,2)
        THREE_second_number = ne_po
        #securing second correct number
        THREE_CORRECT_SECOND = THREE_second_number


        THREE_first_number *= -1
        THREE_second_number *= -1


        """The 'b' and 'c' in a generic quadratic equation"""
        THREE_number_sum = THREE_second_number+THREE_first_number
        THREE_number_product = THREE_second_number*THREE_first_number

        #Choosing whether the 'plus' is necessary
        if THREE_number_sum >= 1 and THREE_number_product >= 1:
            question_three_text = ("x^2 + {}x + {} = 0".format(THREE_number_sum, THREE_number_product))
            
        """special case where the number is the same but one is negative"""
        if THREE_first_number == THREE_second_number-(THREE_second_number*2) or THREE_second_number == THREE_first_number-(THREE_first_number*2):
            question_three_text = ("x^2{} = 0".format(THREE_number_product))
            
        if THREE_number_sum < 0 and THREE_number_product >= 1:
            question_three_text = ("x^2{}x + {} = 0".format(THREE_number_sum, THREE_number_product))
            
        if THREE_number_sum >= 1 and THREE_number_product < 0:
            question_three_text = ("x^2 + {}x {} = 0".format(THREE_number_sum, THREE_number_product))

        """Both numbers are negative"""
        if THREE_number_sum < 1 and THREE_number_product < 0:
            question_three_text = ("x^2{}x{} = 0".format(THREE_number_sum, THREE_number_product))

    
        question_one_text = tk.Label(self, text = question_three_text, padx = 10, pady = 5)
        question_one_label = tk.Label(self, text = "Solve for x (only one root)", padx = 10, pady = 5)
        users_input = tk.Entry(self)

        def Submit():
            data3 = users_input.get()
            print(data3)
            users_input.destroy()
            user_answer = tk.Label(self, text=data3, font=controller.title_font)
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
        global introductory_text
        global second_introductory_text
        global question_five_text
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Question Four", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        FIVE_name_list = ["Garrett", "Connor", "David", "Matthew", "Cody", "Dustin", "Luke", "Jack", "Scott", "Logan", "Barry", "Lucas"]

        FIVE_name_index = random.randint(0,5)
        FIVE_name_index2 = random.randint(6,11)
        FIVE_RANDOM_dad_name = FIVE_name_list[FIVE_name_index]
        FIVE_RANDOM_son_name = FIVE_name_list[FIVE_name_index2]

        """setting up a random year setting"""
        FIVE_random_year = random.randint(1900,2020)
        
        #Completely randomizing the son's age
        FIVE_SON_age_list = [8,10,12,14,16,18]

        """son_age factor list"""
        FIVE_SON_AGE_factor_list = []

        
        #setting up son's age
        son_age_randint = random.randint(0,5)
        FIVE_SON_AGE = int(FIVE_SON_age_list[son_age_randint])
        x = FIVE_SON_AGE
        
        def find_factors(d):
            for i in range(1, (d + 1)):
                if d % i == 0:
                   FIVE_SON_AGE_factor_list.append(i)
                   
        find_factors(FIVE_SON_AGE)

        FIVE_SON_AGE_factor_len = len(FIVE_SON_AGE_factor_list)
        another_rando = random.randint(2,FIVE_SON_AGE_factor_len-2)

        c = FIVE_SON_AGE_factor_list[another_rando]
        
        #AFTER REARRANGING THE FORMULA, b = (x+c)/c
        
        b = (x+c)/c

        #USING 3RD SIMULTANEOUS EQUATION, a = b+1

        a = b+1

        #USING 1ST SIMULTANEOUS EQUATION, ax = y

        y = a*x
        FIVE_DAD_AGE = y
        #creating a realistic 'relationship'

        FIVE_AGE_betweener = y-x
        
        if FIVE_AGE_betweener > 60:
            FIVE_relationship = "grandfather"
        if FIVE_AGE_betweener <= 60 and FIVE_AGE_betweener >= 45:
            FIVE_relationship = "uncle"
        if FIVE_AGE_betweener < 45:
            FIVE_relationship = "dad"
        """writing out full simultaneous word equation"""

        if y >= 110:
            ancestor = 1
            introductory_text = ("In {}, {}'s great ancestor, {}, would be {} times older than {}".format(FIVE_random_year, FIVE_RANDOM_son_name, FIVE_RANDOM_dad_name, int(a), FIVE_RANDOM_son_name))
            two()
            one()
            second_introductory_text = ("In {} years time, {} would then be {} times older than {}".format(int(c), FIVE_RANDOM_dad_name, int(b), FIVE_RANDOM_son_name))
            two()
        if y < 110:
            ancestor = 0
            introductory_text = ("In {}, {}'s {}, {}, is {} times older than {}".format(FIVE_random_year, FIVE_RANDOM_son_name, FIVE_relationship, FIVE_RANDOM_dad_name, int(a), FIVE_RANDOM_son_name))
            two()
            one()
            second_introductory_text = ("{} years later, {} is now {} times older than {}".format(int(c), FIVE_RANDOM_dad_name, int(b), FIVE_RANDOM_son_name))
            two()
        
        if ancestor == 0 or ancestor == 1:
            gap()
            question_four_text = ("1) How old is {} in {}?".format(FIVE_RANDOM_son_name, FIVE_random_year))
            
        FIVE_COUNTER = 0
        FIVE_DAD_COUNTER = 0
        
        if ancestor == 0:
            question_five_text = ("2) How old is {} in {}?".format(FIVE_RANDOM_dad_name, FIVE_random_year))
        if ancestor == 1:
            question_five_text = ("2) How old would {} be in {} (if he was somehow still alive)?".format(FIVE_RANDOM_dad_name, FIVE_random_year))
    
        
        question_four_label = tk.Label(self, text = introductory_text, padx = 10, pady = 5)
        second_question_four_text = tk.Label(self, text = second_introductory_text, padx = 10, pady = 5)
        
        question_four_label_question = tk.Label(self, text = question_four_text, padx = 10, pady = 5)
        users_input = tk.Entry(self)

        def Submit():
            data4 = users_input.get()
            print(data4)
            users_input.destroy()
            user_answer = tk.Label(self, text=data4, font=controller.title_font)
            user_answer.pack()
            submit.destroy()
            submit22 = tk.Button(self, text="submit", state='disabled')
            submit22.pack()            
            button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageFive"))
            button.pack()
        
        submit = tk.Button(self, text="submit", command =lambda: Submit())
        #button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageTwo"))
        #question_one = tk.Label(self, text = "A triangle has a hypotenuse side length of {}, and another side length of {}".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        
        
        question_four_label.pack()
        second_question_four_text.pack()
        
        question_four_label_question.pack()
        users_input.pack()
        submit.pack()


# ***************************************************************************#

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Question Five", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        
        question_five_text = tk.Label(self, text = introductory_text, padx = 10, pady = 5)
        second_question_five_text = tk.Label(self, text = second_introductory_text, padx = 10, pady = 5)
        
        question_five_label = tk.Label(self, text = question_five_text, padx = 10, pady = 5)
        users_input = tk.Entry(self)
        
        def Submit():
            data5 = users_input.get()
            print(data5)
            users_input.destroy()
            user_answer = tk.Label(self, text=data5, font=controller.title_font)
            user_answer.pack()
            submit.destroy()
            submit22 = tk.Button(self, text="submit", state='disabled')
            submit22.pack()             
            button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageSix"))
            button.pack()
        
        submit = tk.Button(self, text="submit", command =lambda: Submit())
        #button = tk.Button(self, text="Next Question", command=lambda: controller.show_frame("PageTwo"))
        #question_one = tk.Label(self, text = "A triangle has a hypotenuse side length of {}, and another side length of {}".format(new_list[2], new_list[0]), padx = 10, pady = 5)
        
        
        question_five_text.pack()
        second_question_five_text.pack()
        question_five_label.pack()
        
        users_input.pack()
        submit.pack()

# ***************************************************************************#

class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Answers", font=controller.title_font)


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


