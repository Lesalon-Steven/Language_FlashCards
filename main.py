from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}

data = pandas.read_csv("data/french_words.csv")
new_dict = data.to_dict(orient="records")


def next_word():
    global random_word, timer
    window.after_cancel(timer)
    random_word = random.choice(new_dict)
    canvas.itemconfig(word_title, text="French", fill="black")
    canvas.itemconfig(word_to_learn, text=random_word["French"], fill="black")
    canvas.itemconfig(card_background, image=front_card)
    timer = window.after(3000, func=card_flip)


def card_flip():
    canvas.itemconfig(word_title, text="English", fill="white")
    canvas.itemconfig(word_to_learn, text=random_word["English"], fill="white")
    canvas.itemconfig(card_background, image=back_card)


def is_known():
    new_dict.remove(random_word)
    print(len(new_dict))
    data = pandas.DataFrame(new_dict)
    data.to_csv("Words.csv")


window = Tk()
window.title("Language Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=card_flip)

canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_card)
word_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_to_learn = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_word)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_word()

window.mainloop()
