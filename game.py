from cards import cards, Card


def create_new_card():
    question = str(input("Type in a new question \n"))
    answer = str(input("Now type in the answer to that question \n"))
    return Card(question, answer)


def play(card: Card):
    print(card.question)
    _next = int(input("Press 1 to reveal the answer \n"))
    if _next == 1:
        print(card.answer)


print("Welcome to your memory cards! \n"
      "You have {index} cards saved in this collection.".format(index=cards.count()))
if cards.count() == 0:
    choice = 1
else:
    choice = int(input("What would you like to do? \n"
                       "1. Create new card \n"
                       "2. Train over existing cards \n"))
if choice == 1:
    while choice == 1:
        print("Creating a new card")
        create_new_card()
        choice = int(input("Would you like to create another card? \n"
                           "1. Yes \n"
                           "2. No, I want to practice! \n"))
if choice == 2:
    while choice == 2:
        play(Card.shuffle())
        choice = int(input("for next card press 2, any other to exit \n"))
