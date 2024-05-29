import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 16. Rock, paper, scissors 
        ## Introduction to algorithms

        [Learn Python with Jupyter](https://learnpythonwithjupyter.com/) by [Serena Bonaretti](https://sbonaretti.github.io/)   
        Narrative license: [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/2.0/). Code license: [GNU-GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)  

        --- 
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ### 1. Computer pick
        - Make the computer pick among *rock*, *paper*, or *scissors*: 
        """
    )
    return


@app.cell
def __():
    import random

    # list of game possibilities
    possibilities = ["rock", "paper", "scissors"]

    # computer random pick
    computer_pick = random.choice(possibilities)
    print (computer_pick)
    return computer_pick, possibilities, random


@app.cell
def __(mo):
    mo.md(
        r"""
        ### 2. Player choice  
        - Make the player choose among *rock*, *paper*, or *scissors*:
        """
    )
    return


@app.cell
def __():
    # asking the player to make their choice
    player_choice = input("Rock, paper, or scissors?")
    print (player_choice)
    return player_choice,


@app.cell
def __(mo):
    mo.md(
        r"""
        ### 3. Determine who wins
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - If the computer picks *rock*:
        """
    )
    return


@app.cell
def __(computer_pick, player_choice):
    if computer_pick == "rock":
        
        # compare to the player's choice
        if player_choice == "rock":
            print("Tie!")       
        elif player_choice == "paper": 
            print ("You win!")
        else:
            print ("The computer wins!")
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - If computer picks *paper*:
        """
    )
    return


@app.cell
def __(computer_pick, player_choice):
    if computer_pick == "paper":
        
        # compare to the player's choice
        if player_choice == "paper":
            print("Tie!")       
        elif player_choice == "scissors": 
            print ("You win!")
        else: 
            print ("The computer wins!")
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - If computer picks *scissors*:
        """
    )
    return


@app.cell
def __(computer_pick, player_choice):
    if computer_pick == "scissors":
        
        # compare to the player's choice
        if player_choice == "scissors":
            print("Tie!")  
        elif player_choice == "rock":
            print ("You win!")
        else:
            print ("You didn't win")
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ### Merging the code
        - Let's merge the code:
        """
    )
    return


@app.cell
def __():
    import random

    # list of game possibilities
    possibilities = ["rock", "paper", "scissors"]
    # computer random pick
    computer_pick = random.choice(possibilities)

    # player choice
    player_choice = input("Rock, paper, or scissors?")

    # determine who wins
    # if the computer picks rock
    if computer_pick == "rock":
        # compare to the player's choice
        if player_choice == "rock":
            print("Tie!")       
        elif player_choice == "paper": 
            print ("You win!")
        else:
            print ("The computer wins!")

    # if the computer picks paper
    if computer_pick == "paper":
        # compare to the player's choice
        if player_choice == "paper":
            print("Tie!")       
        elif player_choice == "scissors": 
            print ("You win!")
        else: 
            print ("The computer wins!")

    # if the computer picks scissors        
    if computer_pick == "scissors":
        # compare to the player's choice
        if player_choice == "scissors":
            print("Tie!")  
        elif player_choice == "rock":
            print ("You win!")
        else: 
            print ("You didn't win")
    return computer_pick, player_choice, possibilities, random


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

