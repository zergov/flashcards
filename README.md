# flashcards
Command line application that focus on creating decks of flashcards quickly and easily.

## What is flashcards
Flascards is a small CLI Study tools. It focuses on creating decks of flashcards easily and quickly.

The reason I developped this application is because I wanted to write flashcards during my classes, so that I didn't have to write them in my spare time.
Unfortunately, writing them on papers is long and on top of taking physical space, costs money.

I used to use the [Quizlet](https://quizlet.com) services, but it requires an internet connection.
Also, using the Quizlet mobile app offline didnt fit for me because I find it annoying to write cards on my phone.

That is why I created flashcards.

Flashcards definition from wikipedia:
>A flashcard or flash card is a set of cards bearing information, as words or numbers, on either or both sides,
>used in classroom drills or in private study.
>
>One writes a question on a card and an answer overleaf.
>Flashcards can bear vocabulary, historical dates, formulas or any subject matter that can be learned via a question-and-answer format.
>Flashcards are widely used as a learning drill to aid memorization by way of spaced repetition.

## Creating a studyset and adding cards to it.

Idealy, flashcards are contained in studysets or also called decks.

For this use case, we will create a basic mathematic studyset.

```
$ flashcards sets new
```

A series of prompt will ask you to enter the title for this set and also a 
description for this set.

Once all the information has been entered, a confirmation message will be shown, 
letting you know that the studyset has been created.

```
$ flashcards sets new

[cli][prompt] Title of the study set: Mathematics
[cli][prompt] Description for the study set: Some math questions.

Study set created ! 
```

At this point, you're ready to create flashcards to add in your studyset.

To add a card run this command:

```
$ flashcards cards add
```

A series of prompt will ask you to enter the question and the answer to that question.

Once all the information has been entered, a confirmation message will be shown, 
letting you know that the flashcard has been added to the studyset.

```
$ flashcards cards add

[cli][prompt] Question: 2 + 2 = ?
[cli][prompt] Answer: 4 (duhh)

Card added to the studyset !
```

Congratulations ! You just created your first studyset ! 

To see the status of this studyset, simply run this command:

```
$ flashcards status

Currently using studyset: Mathematics (1 cards)

Description: Some math questions
```

If you're wondering how the application knows you're asking about the status of 
the "Mathematics" studyset, it's because this is the currently selected 
studyset.

By default, after creating a studyset, the application automaticaly selects it.
This means that the application is currently focused on this studyset. Every new created cards
will be stored in this studyset. Also, the `status` command will show informations on the currently selected
studyset.


To select a different studyset, use the following command:

```
# Let's say we want to select our "French" studyset
$ flashcards sets select French

[cli][info] Selected studyset: French
[cli][info] Any created card will be automatically added to this studyset.
```

When using tabcomplete, autocomplete should propose a list of existing studysets after the `select` keyword.


## Bash autocomplete

When installing with pip, auto completion should work out of the box.


## Storage directory

By default, studysets are stored in the following path:
```
~/.flashcards/studysets
```
