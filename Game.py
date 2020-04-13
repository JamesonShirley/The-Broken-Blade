import tkinter as tk 

iterator = 0

TotalYes = 0
TotalNo = 0
Chosen = True
FirstMainChoice = True

fight = 50
reason = 50
Marissa = 50
caution = 50
brash = 50

FirstText = "Welcome to a world of magic and fantasy! \n You are Joshua, a skilled fighter and negotiater from the kingdom of Arania. \n You are on a solo diplomatic mission to a neighboring kingdom, and on the road you are attacked by a vicious bandit. \n \nWould you like to fight him or try to reason with him?"

def choice():
    global fight
    global reason
    global Marissa
    global caution
    global brash
    if iterator == 1:
        GameName.config(text = FirstText)
        firstbutton.config(text = "Fight")
        secondbutton.config(text = "Reason")
    if iterator == 2:
        if Chosen:
            fight +=5
            reason -=5
            secondtext = "You fight the ferocious bandit. \n With a series of skilled swings, you deflect his attacks. \n After a few exchanges you see your opening and swing. \n The bandit has no defense and is killed. Good job. \n"
        else:
            reason +=5
            fight -= 5
            secondtext = "You attempt to reason with the bandit. \n Although he looks like he is contemplating your words, you can tell that his mind is made up. \n It isn't honorable, but you swing your blade ending his life. \n"
        secondtext += "The rest of your journey is uneventful and you arrive at castle in the city of Arnon. \n You are greeted by the Lady Marissa, the oldest princess in the kingdom. \n \"I hope your journey was pleasant.\" She said. \n \"It's a pleasure to finally meet you Joshua.\" \n \n Do you agree that it is a pleasure to meet Marissa?"
        GameName.config(text = secondtext)
        firstbutton.config(text = "Agree")
        secondbutton.config(text = "Disagree")
    if iterator == 3:
        if Chosen:
            Marissa += 5
            thirdstring = "Marissa looks pleased at your response."
        else:
            Marissa -= 10
            thirdstring = "Marissa looks extremely displeased at your response."
        thirdstring += "\n She leads you to where you'll be staying and bids you goodbye. \n Before she leaves, she warns you that some unusual things have been occuring in the southern tower of the castle. \n She asks that you avoid that part of the castle for your safety. \n \n Do you ignore her advice and go explore, or do you stay in the safety of your room?"
        GameName.config(text = thirdstring)
        firstbutton.config(text = "explore")
        secondbutton.config(text = "stay")
    if iterator == 4:
        if Chosen:
            Marissa -= 5
            brash += 5
            caution -= 5
            fourthstring = "You go out and wander around the southern tower for a few hours. \n You are unable to locate anything outside of the ordinary. You then return to your rooms disappointed."
        else:
            Marissa += 5
            caution += 5
            brash -= 5
            reason += 5
            fourthstring = "You stay in your rooms and study a book you brought with you. \n You feel like the principles in the book will help you with negotiating."

        fourthstring += "\n You hear a scratching outside your door. \n You open the door and see what looks like an oversized rat. \n\n Do you try to fight it or do you call for the guards?"
        GameName.config(text = fourthstring)
        firstbutton.config(text = "Fight")
        secondbutton.config(text = "Guards")
    if iterator == 5:    
        if Chosen:
            if fight < 50:
                caution -= 5
                fight -= 5
                reason -= 5
                brash += 10
                fifthstring = "You pull out your sword and swing at the rat. You miss badly, and it leaps on top of you tackling you. \n The rat's claws dig into your chest and you cry out in pain. \n Luckily the guards hear the noise and come running, saving you from the embarrasing death that would have occured."
            else:
                fight += 5
                brash += 5
                caution -= 5
                fifthstring = "You quickly pull out your sword and stab into the rat's eyes. \n It convulses and lets out a shriek of pain before going limp. \n A few guards run up hearing the noise."
        else:
            fifthstring = "You call out for the guards, trying to close the door. \n The rat pushes against the door trying to get in and you enter a frantic contest with the rat. \n You hear swords being drawn and the rat crying out in pain as the resistance of the door disappears. \n You open the door to see a few guards outside with their swords drawn."

        fifthstring += "\n \"Are you okay Milord?\" One of the guards asks. \n \"I'll live,\" you respond, \"Where did that thing come from?\" \n \"I'm not sure. We'll investigate it!\" \n You wonder what is really going on in this castle \n"
        GameName.config(text = fifthstring)
        firstbutton.config(text = "Continue")
        secondbutton.config(text = "Continue")
    if iterator == 6:
        sixthstring = ""
        GameName.config(text = "")
        firstbutton.config(text = "")
        secondbutton.config(text = "")
    if FirstMainChoice:
        if iterator == 6:
            if Chosen:
                string = ""
            else:
                string = ""

        string += ""
        GameName.config(text = "")
        firstbutton.config(text = "")
        secondbutton.config(text = "")
    else:
        if iterator == 6:
            if Chosen:
                string = ""
            else:
                string = ""

        string += ""
        GameName.config(text = "")
        firstbutton.config(text = "")
        secondbutton.config(text = "")


def on_exitbutton_click():
    window.destroy()

def onfirstbutton_click():
    global iterator
    iterator += 1
    global TotalYes 
    TotalYes += 1
    global Chosen
    Chosen = True
    choice()

    
def onsecondbutton_click():
    global iterator 
    iterator += 1
    global TotalNo 
    TotalNo+= 1
    global Chosen
    Chosen = False
    choice()

window = tk.Tk()

GameName = tk.Label(text="The Broken Blade", width = 100, height = 40)
firstbutton = tk.Button(window, text = "Start", command=onfirstbutton_click, height = 10)
exitbutton = tk.Button(window, text = "Exit", command =on_exitbutton_click, height = 3)
secondbutton = tk.Button(window, text = "Start", command=onsecondbutton_click, height = 10)
GameName.pack()
firstbutton.pack(side = tk.LEFT, ipadx = 75)
secondbutton.pack(side = tk.RIGHT, ipadx = 75)
exitbutton.pack(side = tk.BOTTOM, ipadx = 25)



    
window.mainloop()