import marimo

__generated_with = "0.6.11"
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
    number = 23
    guess = int(input('Enter an integer : '))

    if guess == number:
        # 新程序块的开始处
        print('Congratulations, you guessed it.')
        print('(but you do not win any prizes!)')
        # 新程序块的结尾处
    elif guess < number:
        # 另一个程序块
        print('No, it is a little higher than that')
        # 你可以在程序块中“为所欲为”——做任何你想做的事情
    else:
        print('No, it is a little lower than that')
        # 只有当猜测数大于给定数的时候，才会执行此处

    print('Done')
    # 在 if 语句执行结束后，最后的这句语句总是会被执行。
    return guess, number


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


@app.cell(disabled=True)
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
