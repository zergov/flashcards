# flashcards
CLI application that focus on quickly creating study flash cards. 

# What is flashcards
Flascards is a small CLI Study tools. It focuses on creating study flashcards easily and quickly.
The study flow of the flashcards method works like this:

The user decides on a subject he wants to learn.
The user then creates study flashcards on the subject. A flashcards is a card with a question written on one of its side, and the answer on the other.
Once the user has a good set of cards, he can starts studying it. To study, the user just take a card, read the question then attempt to answer the question in his
head. When the user thinks he got the right answer, he flips the card to see if got the right answer.
The process keeps going until all the cards has been answered.

This method should be repeated until the user can answer most of the cards without failling to find the right answer.

## Commands

### set
set new: Create a new set
    -t: title
    -d: description

set delete [TITLE] : Delete the given set.
set edit [TITLE] : Edit the given set.
set select [TITLE] : Focus on given set. ( Any created card will be stored in this set )

### card
card new: Create a new card
    -q: question of the card
    -a: answer of the card

### study
study [TITLE] : Study the given set, or the currently focused one if no set is given.
    --mode, -m : The study mode 
