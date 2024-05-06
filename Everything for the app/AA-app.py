import tkinter as tk

# GUI
root = tk.Tk()
root.title("Alcohol Abuse Assistant")

BG_GRAY = "#FFFFFF"
BG_COLOR = "#FFE9E1"
TEXT_COLOR = "#000000"
RESULT_COLOR = "#FF0000"  # Red color for final result
TRIGGER_COLOR = "#0000FF"  # Blue color for triggers


font_size = 16  # Initial font size
FONT = ("Comic Sans MS", font_size)
FONT_BOLD = ("Comic Sans MS", 18, "bold")

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
    "I am comfortable reaching out to my RA for guidance/help. (yes/no)",
    "When I go to parties that involve drinking, I make sure to bring friends\n that I trust will take care of me. (yes/no)",
    "I only go to frat parties that I heard from friends were safe and have\n a good risk-prevention team. (yes/no)",
    "When I go to parties that involve drinking, I make sure to have a ride\n home from a sober friend/person. (yes/no)",
    "At parties, I never leave my drink unattended. (yes/no)",
    "I usually avoid mixing my drinks. (yes/no)"
]
current_question = 0
points = 0
triggers = []

BMI = "Brief Motivational Interviewing (BMI) would involve you meeting one-on-one with \n an interventionist whose there to help you by changing your motivates around the \n problem. Additionally, it would involve getting personalized feedback \n from your interventionist whilst learning more about alcohol. \n\n"
AMI = "Adaptations of Motivational Interviewing (AMI) would involve you meeting with a \n counselor to help build the motivation to make changes to your life about a \n specific issue. You would meet them and they would be non-judgmental, empathetic,\n understanding, and supporting you to make the changes you want to make about your\n specific circumstances. AMI would also incorporate a few other elements besides\n the basis of Motivational Interviewing (MI) but ultimately it is to help change\n motivations to make changes when you are having difficulty making the\n changes you want to make.\n\n"
EI = "An Educational Intervention would help you to learn a greater deal about alcohol \n and alcohol within the college environment. They would help you to understand more \n about the challenges provided by alcohol and how to have safe behaviors \nif you do drink.\n\n"
ECS = " Expectancy Challenges would help teach you the actual effects of alcohol on a \n person. The goal is to train you out of current expectations you may have about\n someone's behavior and how they are affected after drinking and learn what those\n behaviors and effects really are. The goal is to challenge current \nexpectations and set in your mind proper expectations for what drinking does.\n\n"
ASTP = "In CAPS, ASTP stands for Alcohol Skills Training Program. This would entail a \n 90-minute session bent on helping students to develop a bettter understanding of\n what addiction is and how it works. Additionally, ASTP would focus on supporting\n students to develop necessary skills in order to decline alcohol and understand\n drinking amounts."
DRT = "Deviance Regulation Theory would help in changing how you view the norms of your\n surrounding environment, especially in terms of healthy or unhealthy \ndrinking behaviors. If you tend to think that unhealthy behaviors \nare more common in your environment, then you will receive\n messages promoting and encouraging healthy behaviors. If you believe \nthat the behaviors around you tend to be healthier, then you will receive \nmessages that discourage unhealthy drinking behaviors. \n\n"
PBS = "Protective Behavioral Strategies would teach you behaviors and actions to take \n while drinking that would reduce negative consequences from drinking. \nOverall, the rate and severity of negative consequences from drinking\n alcohol would be reduced through learning these strategies. \n\n"
PACE = "Pregaming Awareness in College Environments would be a set of modules occurring\n online that would discuss the high-risks of pregaming and its consequences.\n The goal would be to reduce pregaming behaviors and therefore any negative \nconsequences that may occur from it. \n\n"
GLF = "Useful tip: if you're visiting parties hosted by Greek life organizations,\n it would be good to always go with a group of friends you trust to take\n care of you and be responsible.\n\n"
GLR = "Useful tip: try to do your research on different Greek life organizations before\n you visit their parties. Specifically, target the ones known for their good \nrisk prevention team, as they will take good care of you if anything\n bad happens! \n\n"
RA = "Sometimes reaching out to your Residents Assistant (RA) can help finding resources\n if you're dealing with alcohol abuse problems. They are closer to you in \nage than your professors, so they can find a way to help you without \nmaking you feel ashamed or uncomfortable!\n\n"
CAPS = "Seton Hall University's Counseling and Psychological Services (CAPS) is an easily \n accessible intervention that students can utilize. They can schedule a \n meeting with campus by contacting them or coming into the office. CAPS can greatly\n assist students dealing with smaller issues regarding alcohol abuse and you \ncan even have weekly or monthly meetings with them. Those with greater issues can get a referral\n to a professional who would be more tailored to help them. \n\n"
AEFT = "Academic Goal-Relevant Episodic Future Thinking or A-EFT would involve you trying\n to see the future of taking a certain action. A-EFT would work on your \nability to see the results of taking a particular action.\n Additionally, A-EFT would encourage you to view events that had positive\n impacts on your academic goal both in a short-term and in a long-term \nmanner to help you better understand the impacts your actions have in\n the outcomes you create. By helping you to develop a better ability\n to predict the future based on your actions it is trying to\n help with managing impulses, or having better control over yourself.\n\n"
MHH = "This 973-275-4357 is the number you should reach out to if you are having\n a mental health crisis. Someone will be able to give you immediate help\n in whatever situation is troubling you.\n\n"
AUDIT = "Alcohol Use Disorders Identification Test is a screening tool designed to assess you\n for unhealthy alcohol use. It is a simple and effective way to anonymously find out for\n yourself if you may have any issues with alcohol.\n\n"

def print_trigger_text(triggers):
    trigger_texts = {
        "BMI": BMI,
        "AMI": AMI,
        "EI": EI,
        "ECS": ECS,
        "DRT": DRT,
        "PBS": PBS,
        "PACE": PACE,
        "GLF": GLF,
        "GLR": GLR,
        "RA": RA,
        "CAPS": CAPS,
    }

    txt.insert(tk.END, "\n\nAdditional information based on your answers:\n\n")
    for trigger in triggers:
        if trigger in trigger_texts:
            txt.insert(tk.END, trigger_texts[trigger], "trigger_text")
    txt.tag_config("trigger_text", foreground=TRIGGER_COLOR)



# Send function
def send():
    global current_question, points

    user_input = e.get().lower()
    send = "You -> " + user_input
    txt.insert(tk.END, "\n" + send)

    if current_question == 0:
        try:
            age = int(user_input)
            if age > 18:
                points += 5  # Add points for being over 18
            else:
                points -= 10  # Deduct points for being under 18
                triggers.append("AMI")

        except ValueError:
            txt.insert(tk.END, "\n" + "Sippy -> Please enter a valid age.")
            current_question -= 1

    elif current_question == 1:
        try:
            drinks_per_week = int(user_input)
            if drinks_per_week == 0:
                points -= 10
            elif drinks_per_week <= 4:
                points += 10
                triggers.extend(["BMI", "EI", "ECS"])
            else:
                points += 20
                triggers.extend(["AMI", "BMI", "EI", "ECS"])
        except ValueError:
            txt.insert(tk.END, "\n" + "Sippy -> Please enter a valid number.")
            current_question -= 1

    elif current_question == 2:
        if user_input.lower() == "na":
            pass  # No points if NA
        else:
            try:
                drinking_age = int(user_input)
                if drinking_age < 18:
                    points += 10
                    triggers.extend(["AMI", "BMI", "EI"])
                else:
                    points += 5
            except ValueError:
                txt.insert(tk.END, "\n" + "Sippy -> Please enter a valid age or NA.")
                current_question -= 1

    elif current_question == 3:
        if user_input.lower() == "yes":
            points += 10
            triggers.append("AMI")
        elif user_input.lower() == "no":
            pass  # No points for no family history
        else:
            txt.insert(tk.END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
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
            txt.insert(tk.END, "\n" + "Sippy -> Please enter a valid number.")
            current_question -= 1

    elif current_question == 5:
        try:
            hangovers_per_week = int(user_input)
            if hangovers_per_week == 0:
                points -= 10
                triggers.append("DRT")
            elif hangovers_per_week == 1:
                points += 5
                triggers.extend(["PBS", "DRT"])
            else:
                points += 10
                triggers.extend(["PBS", "DRT"])
        except ValueError:
            txt.insert(tk.END, "\n" + "Sippy -> Please enter a valid number.")
            current_question -= 1

    elif current_question == 6:
        try:
            everyone_drinking = int(user_input)
            if everyone_drinking == 1:
                points -= 10
                triggers.extend(["DRT", "EI", "BMI"])
            elif everyone_drinking == 2:
                points -= 5
                triggers.extend(["DRT", "EI", "BMI"])
            elif everyone_drinking == 3:
                triggers.append("EI")
            elif everyone_drinking == 4:
                points += 5
                triggers.append("DRT")
            elif everyone_drinking == 5:
                points += 10
                triggers.append("DRT")
        except ValueError:
            txt.insert(tk.END, "\n" + "Sippy -> Please enter a valid number.")
            current_question -= 1

    elif current_question == 7:
        try:
            limit_drink = int(user_input)
            if limit_drink == 1:
                points += 10
            elif limit_drink == 2:
                points += 5
            elif limit_drink == 3:
                triggers.extend(["EI", "PBS", "BMI"])
            elif limit_drink == 4:
                points -= 5
                triggers.extend(["EI", "PBS", "BMI"])
            elif limit_drink == 5:
                points -= 10
                triggers.extend(["EI", "PBS", "BMI"])
        except ValueError:
            txt.insert(tk.END, "\n" + "Sippy -> Please enter a valid number.")
            current_question -= 1

    elif current_question == 8:
        try:
            caps = int(user_input)
            if caps == 1:
                points += 10
                triggers.append("BMI")
            elif caps == 2:
                points += 5
                triggers.append("BMI")
            elif caps == 3:
                triggers.append("EI")
            elif caps == 4:
                points -= 5
                triggers.append("EI")
            elif caps == 5:
                points -= 10
                triggers.append("EI")
        except ValueError:
            txt.insert(tk.END, "\n" + "Sippy -> Please enter a valid number.")
            current_question -= 1

    elif current_question == 9:
        if user_input.lower() == "yes":
            points += 10
            triggers.extend(["PACE", "EI", "BMI"])
        elif user_input.lower() == "no":
            points -= 10
        else:
            txt.insert(tk.END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1

    elif current_question == 10:
        if user_input.lower() == "yes":
            triggers.extend(["GLR", "GLF"])
        elif user_input.lower() == "no":
            points -= 10
        else:
            txt.insert(tk.END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1

    elif current_question == 11:
        if user_input.lower() == "yes":
            triggers.append("RA")
        elif user_input.lower() == "no":
            pass
        else:
            txt.insert(tk.END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1

    elif current_question == 12:
        if user_input.lower() == "yes":
            points += 5
        elif user_input.lower() == "no":
            points -= 5
        else:
            txt.insert(tk.END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1

    elif current_question == 13:
        if user_input.lower() == "yes":
            points += 5
        elif user_input.lower() == "no":
            points -= 5
        else:
            txt.insert(tk.END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1

    elif current_question == 14:
        if user_input.lower() == "yes":
            points += 5
        elif user_input.lower() == "no":
            points -= 5
        else:
            txt.insert(tk.END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1

    elif current_question == 15:
        if user_input.lower() == "yes":
            points += 5
        elif user_input.lower() == "no":
            points -= 5
        else:
            txt.insert(tk.END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1

    elif current_question == 16:
        if user_input.lower() == "yes":
            points += 5
        elif user_input.lower() == "no":
            points -= 5
        else:
            txt.insert(tk.END, "\n" + "Sippy -> Please enter either 'yes' or 'no'.")
            current_question -= 1

    current_question += 1
    if current_question < len(questions):
        txt.insert(tk.END, "\n" + "Sippy -> " + questions[current_question])
    else:
            # Provide feedback based on the total score
            if points >= 60:
                triggers.extend(["ASTP", "AUDIT", "AEFT", "EI", "CAPS","AMI", "MHH"])
                txt.insert(tk.END, "\n\nYou might want to consider your drinking habits and seek help if needed", "result")
                print_trigger_text(list(set(triggers)))

            elif points >= 30:
                triggers.extend(["AMI", "AEFT", "AUDIT", "CAPS", "MHH"])
                txt.insert(tk.END, "\n\nYour drinking habits seem relatively moderate.", "result")
                print_trigger_text(list(set(triggers)))
            else:
                triggers.extend(["AMI", "AUDIT", "CAPS", "AEFT", "MHH"])
                txt.insert(tk.END, "\n\nYou appear to have healthy drinking habits.\n\n\n", "result")
                print_trigger_text(list(set(triggers)))

                # Configure the font color
    txt.tag_config("result", foreground=RESULT_COLOR)



    e.delete(0, tk.END)
    txt.yview(tk.END)


def increase_font_size():
    global font_size, FONT, FONT_BOLD
    if font_size < 20:
        font_size += 2
        FONT = ("Comic Sans MS", font_size)
        txt.config(font=FONT, width=60, height=20)


def decrease_font_size():
    global font_size, FONT, FONT_BOLD
    if font_size > 10:
        font_size -= 2
        FONT = ("Comic Sans MS", font_size)
        txt.config(font=FONT, width=60, height=20)


txt = tk.Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60, height=20, wrap="none")
txt.grid(row=1, column=0, columnspan=6, sticky="ew")

scrollbar_y = tk.Scrollbar(root, command=txt.yview)
scrollbar_y.grid(row=1, column=7, sticky='ns')
txt.config(yscrollcommand=scrollbar_y.set)

e = tk.Entry(root, bg="#FFFFFF", fg=TEXT_COLOR, font=FONT, width=60)
e.grid(row=3, column=0, columnspan=2)

send_button = tk.Button(root, text="Send", command=send)
send_button.grid(row=3, column=3)

# Button to increase font size
increase_font_button = tk.Button(root, text="+", command=increase_font_size)
increase_font_button.grid(row=3, column=4)

# Button to decrease font size
decrease_font_button = tk.Button(root, text="-", command=decrease_font_size)
decrease_font_button.grid(row=3, column=5)

txt.insert(tk.END, "Sippy -> " + questions[current_question])

# Load the logo image
logo_image = tk.PhotoImage(file="/Users/tijanaminic/Documents/GitHub/PSYC-5111-ALCOHOL-ABUSE-CHATBOT/Everything for the app/Sippy6.png")
logo_label = tk.Label(root, image=logo_image, bg="#FFFFFF")
logo_label.grid(row=0, column=0, columnspan=6)


root.mainloop()




