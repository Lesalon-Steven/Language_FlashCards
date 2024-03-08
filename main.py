from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Language Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# with open("data/french_words.csv", "r") as data:
#     words = data.read()
#     print(words)

data = pandas.read_csv("data/french_words.csv")
new_dict = data.to_dict(orient="records")
# print(new_dict)
random_word = new_dict[random.randint(0, len(new_dict)-1)]

def next_word():
    random_word = new_dict[random.randint(0, len(new_dict) - 1)]
    french_word = random_word["French"]
    english_word = random_word["English"]
    canvas.itemconfig(word_to_learn, text=french_word)

    pass
        # print(word_dict)




canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_to_learn = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_word)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_word)
right_button.grid(row=1, column=1)

window.mainloop()
