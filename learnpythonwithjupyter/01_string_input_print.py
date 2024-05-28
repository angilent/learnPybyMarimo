import marimo

__generated_with = "0.6.8"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md(
        r"""
        # 1. Text, questions, and art

        ## Strings, input(), and print()

        [Learn Python with Jupyter](https://learnpythonwithjupyter.com/) by [Serena Bonaretti](https://sbonaretti.github.io/)   
        Narrative license: [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/2.0/). Code license: [GNU-GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)
        """
    )
    return


@app.cell
def __(mo):
    mo.md(r"## Strings")
    return


@app.cell
def __(mo):
    mo.md(r"- Look at the following strings and run the cells:")
    return


@app.cell
def __():
    "this is a string"
    return


@app.cell
def __():
    'everything you write in between quotes is a string'
    return


@app.cell
def __(mo):
    mo.md(r"## Asking questions: input()")
    return


@app.cell
def __(mo):
    mo.md(r"- Look at the following examples and run the cells:")
    return


@app.cell
def __():
    input("What's your name?")
    return


@app.cell
def __():
    input("Where are you from?")
    return


@app.cell
def __(mo):
    mo.md(r"## ASCII art: print()")
    return


@app.cell
def __(mo):
    mo.md(r"- Look at the following example and run the cells:")
    return


@app.cell
def __():
    print (" /\_/\   ")
    print (" >^.^<   ")
    print ("  / \    ")
    print (" (___)___")
    print(111)
    return


if __name__ == "__main__":
    app.run()
