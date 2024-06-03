import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"- The first participant comes in and you fill out the form:")
    return


@app.cell
def __():
    first_name = "Fernando Jerry"
    last_name  = "Pérez"
    return first_name, last_name


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"-  Then you print out what you entered in the registration form:")
    return


@app.cell
def __(first_name, last_name):
    print ("first name is:" + first_name)
    print (last_name)
    (first_name,last_name)
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
def __(mo):
    text_input_name = mo.ui.text()
    mo.md(f"What's your name? {text_input_name}")
    return text_input_name,


@app.cell
def __(text_input_name):
    name = text_input_name.value
    return name,


@app.cell
def __(mo):
    text_input_food = mo.ui.text()
    mo.md(f"What's your favorite food? {text_input_food}")
    return text_input_food,


@app.cell
def __(text_input_food):
    favorite_food = text_input_food.value
    return favorite_food,


@app.cell
def __(favorite_food, name):
    print ("Hi! My name is " + name)
    print ("My favorite food is " + favorite_food) 
    print (name + "'s favorite food is " + favorite_food)
    return


@app.cell
def __(favorite_food, mo, name):
    mo.md(
        f"""
        Hi! My name is {name} \n
        My favorite food is {favorite_food} \n
        """  
    ).callout()
    return


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()
