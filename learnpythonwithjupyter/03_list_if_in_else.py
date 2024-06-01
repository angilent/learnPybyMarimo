import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # 3. In a bookstore

        ## Lists and if... in... / else...

        [Learn Python with Jupyter](https://learnpythonwithjupyter.com/) by [Serena Bonaretti](https://sbonaretti.github.io/)   
        Narrative license: [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/2.0/). Code license: [GNU-GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)
        """
    )
    return


@app.cell
def __(mo):
    mo.md(r"- You are the owner of a bookstore. n the programming shelf there are:")
    return


@app.cell
def __():
    programming_books = ["Learn python", "Python for all",  "Intro to python", "Learn python with marimo"]
    print (programming_books)
    return programming_books,


@app.cell
def __(mo):
    mo.md(r"## A new customer comes in, and you ask what book she wants:")
    return


@app.cell
def __():
    wanted_book = input("Hi! What book would you like to buy?")
    print (wanted_book)
    return wanted_book,


@app.cell
def __(mo):
    mo.md(r"## You check if you have the book, and you reply accordingly:")
    return


@app.cell
def __(programming_books, wanted_book):
    if wanted_book in programming_books:
        print ("Yes, you are so lucy, we sell it!")
    else:
        print ("Sorry, we don't sell that book")
    return


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()
