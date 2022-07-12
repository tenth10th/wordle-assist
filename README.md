### Wordle Assist

Wordle is a popular word-guessing game, inspired by the classic "Bulls and Cows", but using five letter english words as the secret codes.

## Initial Setup

Setup should occur automatically if you open this repo in GitPod!

This script has no dependencies aside from Python 3.8, but the included Pipfile / requirements.txt will install `flake8` for linting and `pytest` for testing, though these are not specifically required. (Using Pipfile, `pipenv install`, or in plain Python, `pip install -r requirements.txt`)

## Cheating at Wordle

Cheating at Wordle is... not very fun.

Since Wordle is designed as a self-contained, client-side JavaScript application, it is possible to extract the list of possible answers, and even to determine which answer is correct for a given day...

This is sort of an interesting reverse-engineering challenge, but completely defeats the point - You don't need to play the game, or even think about the problem space to win every time.

## Assisting with Wordle

A better goal is to help someone playing Wordle to get "un-stuck", especially if they can't come up with more words that fit the available clues. It ideally should not pick the next guess, or tell you the correct answer (unless the feedback accumulated so far has eliminated all other possible options, Sherlock Holmes style.)

It's more interesting to attack Wordle the same way we approached Bulls and Cows - But since all Wordle "codes" are five letter english words, we can't simply generate them and analyze them the way we do with numeric codes.

To help us get started, I've provided `five-letter-english-words.txt`, to act as our starting set of possible options. (Since I started with a list of the 84,000 most common English words, we're probably casting kind of a wide net, but we've further reduced it to 5,787 five-letter words. Some "rude" and "adult" words have also been removed as per Wordle guidelines.)

## Wordle Feedback:

Each Guess consists of a five-letter word, and if it does not match the Secret Word exactly, each letter in a guess will be given specific feedback:

* Green (correct letter, in a correct location)

* Yellow (a correct letter, in an incorrect location)

* Black (a letter which does not appear in the word)

(Note that letters may appear multiple times in the same word: It's possible that a Green letter may appear again later. So Yellow can mean "has an additional location" for a letter that is already Green, and Black can mean "has no additional appearances" for a letter that is already Green or Yellow.)

## Guess Feedback and Data Structures

Your job is to create some sort of data structure(s) that we can use to represent a Wordle game in progress - Either accepting guesses and their scores as input (or simply include a data structure that the "guess feedback" can be entered into), so that the script can display the remaining possible words, and tell you how far you've managed to "reduce" the list of possible words.

* Green letters are fairly straightforward: They indicate that a letter must appear in a specific position.

* Black Letters are also pretty clear: They indicate that a letter must not appear in the secret word at all.

* Yellow letters effectively tell us two things: 1> The yellow letter must appear somewhere in the secret word, and 2> The yellow letter must NOT appear in the position it currently has in the guess...

## Initial Implementation

The `wordle-assist.py` file can load the initial list of 5,787 five-letter words, and has a spot indicated (on line 18) where you could apply filtering based on feedback from a game of Wordle. (You could hardcode that data, or define it in a constant in the file, or even write a parser to accept it on the command line!)

Running `python wordle-assist.py` will initially load the words, count them, and print them, followed by a summary.

I recommend sites like [Wordle History](https://lookleft.github.io/wordle-history/?challenge=23) as a source of additional (past) Wordle games to test your code against, though be prepared to find a new one in the event that they are taken down by lawsuits...
