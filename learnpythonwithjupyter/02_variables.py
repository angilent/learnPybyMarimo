import marimo

__generated_with = "0.6.8"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 2. Events and favorites

        ## Variables and string concatenation

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
        ## Organizing an event

        - You are organizing an event, and you have created the following registration form for the participants:

            ```
            Registration form
            first_name = __________________
            last_name  = __________________
            ```
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - The first participant comes in and you fill out the form:
        """
    )
    return


@app.cell
def __():
    first_name = "Fernando"
    last_name  = "Pérez"
    return first_name, last_name


@app.cell
def __(mo):
    mo.md(
        r"""
        -  Then you print out what you entered in the registration form:
        """
    )
    return


@app.cell
def __(first_name, last_name):
    print (first_name)
    print (last_name)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## Favorites
        """
    )
    return


@app.cell
def __():
    name = input("What's your name?")
    return name,


@app.cell
def __():
    favorite_food = input ("What is your favorite food?")
    return favorite_food,


@app.cell
def __(favorite_food, name):
    print ("Hi! My name is " + name)
    print ("My favorite food is " + favorite_food) 
    print (name + "'s favorite food is " + favorite_food)
    return


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

