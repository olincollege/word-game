# Letter Bubbles
#### by Kathy Yang, Shruti, and Sanjana

Although we did not pull the game's concept from any existing titles, we hoped to create a game that was vary to understand and that all people can enjoy. We settled on a game that we believe has an addicting yet relaxing game loop.

## How to Use:

Clone the Repo and or download the required files, word_game.py, word_controller.py., word_view.py, and main.py,

## The Process:
When you boot up the game, the program will select a random word from the word list as your target word. With that target word, the program will add each of its letters into a list, and then it will add additional letters which are incorrect. The letters are shuffled, so the order that they appear to the player is random.

Each time the player clicks, the game checks if the click is the intended letter. If this is true, then the player is awarded one point. For each word that they complete, they gain an additional point. However, if the player hits an incorrect letter, three seconds is deducted from their time remaining. Once the player completes spelling a word, a new word is generated, and the cycle repeats

For the word list, we found a list of words as a text file that user Xethron on GitHub created for his Hangman project. There is a line on the game over screen that credits Xethron.

Originally, the letters were meant to appear randomly at timed intervals rather than appearing all at once. However, we soon realized that this concept would have many complications: players may have to wait long periods of time to see a correct letter appear, and that would be extremely unfair in a timed-based game. Therefore, we decided to change the design to a game that rewards speedy players, while also providing the relaxing aspect for players that I want to take their time. The game may seem simple, but I will definitely be playing it in my random fits of boredom!

Surprisingly, implementing a restart function was difficult. There was a lot to consider than I initially thought. For example, the bubble letter list would not proplerly reset, or the previous target word would always appear first. These issues were fixed by scrutinizing the game_over and restart functions.

## Results
![How the game looks when you run it!]letter_bubbles_screenshot.png

## Future
If provided more time, the game can be much more user-friendly. The game lacks input feedback-- for example, when the player clicks in incorrect letter, there should be an indicationthat the player misclicked and they lost time. A marker that underlines or bolds the player's current letter can also help clarify the game's mechanics. There are glaring shortcomings to its visuals, such as its simplest look and the misalignment of texts. Additionally, there lacks features like a start menu and high scores. Despite these limitations, this project is complete and I have learned so much about using pygame.