import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 18. Animals, unique numbers, and sum

        ## Various kinds of conditions


        [Learn Python with Jupyter](https://learnpythonwithjupyter.com/) by [Serena Bonaretti](https://sbonaretti.github.io/)   
        Narrative license: [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/2.0/). Code license: [GNU-GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)  

        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## 1. Guess the animal!

        - Given the following list:
        """
    )
    return


@app.cell
def __():
    animals = ["giraffe", "dolphin", "penguin"]
    return animals,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Create a game in which the computer randomly picks one of the three animals and the player has to guess the animal picked by the computer. Make sure that the player keeps playing until they guess the animal picked by the computer. At the end of the game, tell the player how many attempts it took to guess the animal
        """
    )
    return


@app.cell
def __(animals):
    import random

    # computer pick
    computer_pick = random.choice (animals)
    # print (computer_pick)

    # player guess
    player_guess = input("Guess the animal! Choices: giraffe, dolphin, penguin: ")

    # initializing the counter
    n_of_attempts = 1

    # as long as the player's guess and the computer's pick are different 
    while player_guess != computer_pick:

        # tell the player that the animal is not right
        print ("That's not the right animal!")

        # print the numbers of attempts so far
        print ("Number of attempts so far: " + str(n_of_attempts))

        # increase the number of attempts
        n_of_attempts += 1 

        # ask the player to guess again
        player_guess = input("Try again! Guess the animal! Choices: giraffe, dolphin, penguin: ")
        
    # tell the player that they guessed the right animal   
    print ("Well done! You guessed " + computer_pick + " at attempt number " + str(n_of_attempts))
    return computer_pick, n_of_attempts, player_guess, random


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## 2. Create a list of 8 unique random numbers!

        - Create a list of 8 random numbers between 0 and 10. Make sure they are unique, meaning each number is present only once in the list. If the number is already in the list, then print the following: *The number x is already in the list*. How many numbers did you generate before finding 8 unique numbers?
        """
    )
    return


@app.cell
def __():
    import random

    # initialize the number list 
    unique_random_numbers = []

    # initialize the counter
    counter = 0

    # as long as the length of the list is not 8
    while len(unique_random_numbers) != 8:
        
        # create a random number between 0 and 10
        number = random.randint(0,10)
        
        # increase the counter by 1
        counter += 1 
        
        # if the number is already in the list
        if number in unique_random_numbers:
            # print that the number is in the list
            print ("The number " + str(number) + " is already in the list")
        # otherwise    
        else:
            # add the new number to the list
            unique_random_numbers.append(number)

    # print the final list and the total amount of generated numbers
    print (unique_random_numbers)
    print ("The total amount of generated numbers is: " + str(counter))
    return counter, number, random, unique_random_numbers


@app.cell
def __(mo):
    mo.md(
        r"""
        --- 
        ## 3. Summing up positive multiples of 3

        - Write code that continues asking a player to enter an integer until they enter a negative number. At the end, print the sum of all entered integers that are multiples of 3
        """
    )
    return


@app.cell
def __():
    # initialize the sum to 0 
    sum_of_numbers = 0

    # ask the user for an interger
    number = int(input("Enter an integer: "))

    # as long as the number positive
    while number >= 0:
        
        # if the number is a multiple of 3
        if number % 3 == 0:
            # add the number to the sum
            sum_of_numbers += number
        
        # ask for the next new integer
        number = int(input("Enter another integer: "))
        
    # print the final sum    
    print ("The sum of the entered multiples of 3 is: " + str(sum_of_numbers))
    return number, sum_of_numbers


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

