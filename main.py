from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Language Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400,263, text="Word", font=("Ariel", 60, "bold"))


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button =Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1,column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)


window.mainloop()
