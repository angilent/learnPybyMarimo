import marimo

__generated_with = "0.6.10"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # 8. My friends' favorite dishes 

        ## for ... in range() 

        [Learn Python with Jupyter](https://learnpythonwithjupyter.com/) by [Serena Bonaretti](https://sbonaretti.github.io/)   
        Narrative license: [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/2.0/). Code license: [GNU-GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)  

        ---
        """
    )
    return


@app.cell
def __(mo):
    mo.md(r"- Here are a list of my friends and a list of their favorite dishes:")
    return


@app.cell
def __():
    friends = ["Geetha", "Luca", "Daisy", "Juhan"]
    dishes  = ["sushi", "burgers", "tacos", "pizza"]
    return dishes, friends


@app.cell
def __(mo):
    mo.md(r"- These are all my friends:")
    return


@app.cell
def __(friends):
    print ("My friends' names are:")
    print (friends)
    return


@app.cell
def __(mo):
    mo.md(r"- These are my friends one by one:")
    return


@app.cell
def __(friends):
    for index2 in range (0,4):
        print ("index:  " + str(index2))
        print ("friend: " + friends[index2])
    return index2,


@app.cell
def __(mo):
    mo.md(r"- These are all their favorite dishes:")
    return


@app.cell
def __(dishes):
    print ("Their favorite dishes are:")
    print (dishes)
    return


@app.cell
def __(mo):
    mo.md(r"- These are their favorite dishes one by one:")
    return


@app.cell
def __(dishes):
    for index3 in range (0,4):
        print ("index:  " + str(index3))
        print ("dish: " + dishes[index3])
    return index3,


@app.cell
def __(mo):
    mo.md(r"- These are my friends, with their favorite dishes one by one:")
    return


@app.cell
def __(dishes, friends):
    for index in range (0,4):
        print ("My friend " + friends[index] + "'s favorite dish is " + dishes[index])
    return index,


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()
