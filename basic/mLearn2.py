import marimo

__generated_with = "0.6.8"
app = marimo.App()


@app.cell
def __():
    return


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md(
        rf"""
        学习如何使用 marimo 编写python 程序：
        基础：
        """
    )
    return


@app.cell
def __():
    1 + 1
    a = 1
    b = 2
    c = a + b
    print(c)
    return a, b, c


@app.cell
def __():
    'This is a String'
    return


@app.cell
def __():
    "Everything you write between quotes is a string"
    return


@app.cell
def __():
    input("what is you name")
    return


@app.cell
def __():
    print("/\_/\ ")
    print(">^.^< ")
    print(" / \  ")
    print("(__)__")
    return


if __name__ == "__main__":
    app.run()
