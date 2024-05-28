import marimo

__generated_with = "0.6.8"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 9. At the zoo
        ## For loop with if... == ... / else

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
        - You are at the zoo and you write down a list of some animals you see:
        """
    )
    return


@app.cell
def __():
    animals = ["giraffe", "penguin", "dolphin"]
    print (animals)
    return animals,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Then you print out the animals one by one:
        """
    )
    return


@app.cell
def __(animals):
    # for each position in the list
    for i in range (0, len(animals)):
        print ("-- Beginning of loop --")
        # print each element and its position
        print ("The element in position " + str(i) + " is " + animals[i])
    return i,


@app.cell
def __(mo):
    mo.md(
        r"""
        - You really wanted to see a penguin: 
        """
    )
    return


@app.cell
def __():
    wanted_to_see = "penguin"
    return wanted_to_see,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Once home, you tell your friend the animals you saw, specifying which one you really wanted to see:
        """
    )
    return


@app.cell
def __(animals, wanted_to_see):
    # for each position in the list
    for i in range (0, len(animals)):
        # if the current animal is what you really wanted to see
        if animals[i] == wanted_to_see:
            # print out that that's the animal you really wanted to see
            print ("I saw a " + animals[i] + " and I really wanted to see it!")
        # if the current animal is not what you really wanted to see
        else:
            # just print out that you saw it
            print ("I saw a " + animals[i])
        
    return i,


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

