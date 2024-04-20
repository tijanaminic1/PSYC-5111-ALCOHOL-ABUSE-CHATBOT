from tkinter import *

# GUI
root = Tk()
root.title("Alcohol Abuse Assistant")

BG_GRAY = "#9DD3D7"
BG_COLOR = "#DCE2F8"
TEXT_COLOR = "#000000"

FONT = ("Comic Sans MS", 16) 
FONT_BOLD = ("Comic Sans MS", 16, "bold") 

# Global variables
questions = [
    "Hi! Welcome to the alcohol abuse questionnaire! \n How old are you? (Enter a number)",
    "How many drinks do you usually have in a \n given week? (Enter a number)",
    "At what age did you first begin drinking? \n (Enter a number or NA)",
    "Does your family have a history of alcohol abuse? (yes/no)",
    "How involved are you in campus activities \n on a scale of 1-10? (Enter a number)",
    "How often do you experience hangovers on a \n scale of 1-10? (Enter a number)",
    "Everyone in college is drinking. Please reply \n how strongly you agree with the statement on a scale from 1-5",
    "I try to limit the amount of drink I have in a day. \n Please reply how strongly you agree with the statement on a scale from 1-5",
    "If I need help I am comfortable reaching out to someone at CAPS. \n Please reply how strongly you agree with the statement on a scale from 1-5",
    "Do you engage in pregaming? (yes/no)",
    "Do you participate in Greek life? (yes/no)",
    "Do you live on campus?(yes/no)",
    "I am comfortable reaching out to my RA for guidance/help. \n Please reply how strongly you agree with the statement on a scale from 1-5",
    "Please reply to the following statement with yes/no:\n When I go to parties that involve drinking, I make sure to bring friends that I trust will take care of me",
    "Please reply to the following statement with yes/no: \nI only go to frat parties that I heard from friends were safe and have a good risk-prevention team",
    "Please reply to the following statement with yes/no:\n When I go to parties that involve drinking, I make sure to have a ride home from a sober friend/person.",
    "Please reply to the following statement with yes/no:\n At parties, I never leave my drink unattended.",
    "Please reply to the following statement with yes/no: \nI usually avoid mixing my drinks"
]
current_question = 0
points = 0
triggers =[]

# Send function
def send():
    global current_question, points

    user_input = e.get().lower()
    send = "You -> " + user_input
    txt.insert(END, "\n" + send)


    if current_question == 0:
        try:
            age = int(user_input)
            if age > 18:
                points += 5  # Add points for being over 18
            else:
                points -= 10  # Deduct points for being under 18
        except ValueError:
            txt.insert(END, "\n" + "Sippy -> Please enter a valid age.")
            current_question -= 1

    elif current_question == 1:
        try:
            drinks_per_week = int(user_input)
            if drinks_per_week == 0:
                points -= 10
            elif drinks_per_week <= 4:
                points += 10
            else:
                points += 20
        except ValueError:
            txt.insert(END, "\n" + "Sippy -> Please enter a valid number.")
            current_question -= 1

    elif current_question == 2:
        if user_input.lower() == "na":
            pass  # No points if NA
        else:
            try:
                drinking_age = int(user_input)
                if drinking_age < 18:
                    points += 10
                else:
                    points += 5
            except ValueError:
                txt.insert(END, "\n" + "Sippy -> Please enter a valid age or NA.")
                current_question -= 1

    elif current_question == 3:
        if user_input.lower() == "yes":
            points += 10
        elif user_input.lower() == "no":
            pass  # No points for no family history
        else:
            txt.insert(END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1

    elif current_question == 4:
        try:
            activities_per_week = int(user_input)
            if activities_per_week == 0:
                points += 20
            elif activities_per_week <= 3:
                points += 10
            elif activities_per_week <= 5:
                points += 5
        except ValueError:
            txt.insert(END, "\n" + "Sippy -> Please enter a valid number.")
            current_question -= 1

    elif current_question == 5:
        try:
            hangovers_per_week = int(user_input)
            if hangovers_per_week == 0:
                points -= 10
            elif hangovers_per_week == 1:
                points += 5
            else:
                points += 10
        except ValueError:
            txt.insert(END, "\n" + "Sippy -> Please enter a valid number.")
            current_question -= 1
            
    elif current_question == 6:
        try:
            everyone_drinking = int(user_input)
            if everyone_drinking == 1:
                points -= 10
            elif everyone_drinking == 2:
                points -= 5
            elif everyone_drinking == 3:
                pass
            elif everyone_drinking == 4:
                points += 5
            elif everyone_drinking == 5:
                points += 10
        except ValueError:
            txt.insert(END, "\n" + "Sippy -> Please enter a valid number.")
            current_question -= 1
            
    elif current_question == 7:
        try:
            limit_drink = int(user_input)
            if limit_drink == 1:
                points += 10
            elif limit_drink == 2:
                points += 5
            elif limit_drink == 3:
                pass
            elif limit_drink == 4:
                points -= 5
            elif limit_drink == 5:
                points -= 10
        except ValueError:
            txt.insert(END, "\n" + "Sippy -> Please enter a valid number.")
            current_question -= 1
            
    elif current_question == 8:
        try:
            caps = int(user_input)
            if caps == 1:
                points += 10
            elif caps == 2:
                points += 5
            elif caps == 3:
                pass
            elif caps == 4:
                points -= 5
            elif caps == 5:
                points -= 10
        except ValueError:
            txt.insert(END, "\n" + "Sippy -> Please enter a valid number.")
            current_question -= 1
            
    elif current_question == 9:
        if user_input.lower() == "yes":
            points += 10
        elif user_input.lower() == "no":
            points -= 10
        else:
            txt.insert(END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1
            
    elif current_question == 10:
        if user_input.lower() == "yes":
            points += 10
        elif user_input.lower() == "no":
            points -= 10
        else:
            txt.insert(END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1
            
    elif current_question == 11:
        if user_input.lower() == "yes":
            pass
        elif user_input.lower() == "no":
            pass
        else:
            txt.insert(END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1
            
    elif current_question == 12:
        if user_input.lower() == "yes":
            points += 5
        elif user_input.lower() == "no":
            points -= 5
        else:
            txt.insert(END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1
            
    elif current_question == 13:
        if user_input.lower() == "yes":
            points += 5
        elif user_input.lower() == "no":
            points -= 5
        else:
            txt.insert(END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1
            
    elif current_question == 14:
        if user_input.lower() == "yes":
            points += 5
        elif user_input.lower() == "no":
            points -= 5
        else:
            txt.insert(END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1
            
    elif current_question == 15:
        if user_input.lower() == "yes":
            points += 5
        elif user_input.lower() == "no":
            points -= 5
        else:
            txt.insert(END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1
            
    elif current_question == 16:
        if user_input.lower() == "yes":
            points += 5
        elif user_input.lower() == "no":
            points -= 5
        else:
            txt.insert(END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1

    current_question += 1
    if current_question < len(questions):
        txt.insert(END, "\n" + "Sippy -> " + questions[current_question])
    else:
        # Provide feedback based on the total score
        if points >= 60:
            txt.insert(END, "\n" + "You might want to consider your drinking habits and seek help if needed.")
        elif points >= 30:
            txt.insert(END, "\n" + "Your drinking habits seem relatively moderate.")
        else:
            txt.insert(END, "\n" + "You appear to have healthy drinking habits.")

    e.delete(0, END)
    txt.yview(END)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(root, command=txt.yview)
scrollbar.grid(row=1, column=2, sticky='nsew')
txt.config(yscrollcommand=scrollbar.set)

e = Entry(root, bg="#FFFFFF", fg=TEXT_COLOR, font=FONT, width=50)
e.grid(row=2, column=0)


send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=send).grid(row=2, column=1)

txt.insert(END, "Sippy -> " + questions[current_question])

# Load the logo image
logo_image = PhotoImage(file="/Users/tijanaminic/Documents/School/Spring 2024/Psych Seminar/Sippy2.png")
logo_label = Label(root, image=logo_image, bg=BG_COLOR)
logo_label.grid(row=0, column=0, columnspan=2)


root.mainloop()
