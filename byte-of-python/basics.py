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
    mo.md(rf"## 基础操作")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(rf"仅仅打印 hello world 还不够，不是吗？我们要做的远不止这些--我们要接收一些输入，对其进行操作并从中得到一些东西。在 Python 中，我们可以使用常量和变量来实现这一点，本章我们还将学习一些其他概念。")
    return


@app.cell
def __(mo):
    mo.md(
        rf"""
        ## 注释

        注释是 # 符号右侧的任何文本，主要用于为程序读者提供注释。
        例如

        `print('hello world') # Note that print is a function`
        """
    )
    return


@app.cell
def __():
    print('hello world') # Note that print is a function
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        rf"""
        在程序中尽可能多地使用有用的注释，以便

        - 解释假设
        - 解释重要决定
        - 解释重要细节
        - 解释您试图解决的问题
        - 解释您试图在程序中克服的问题，等等。
        """
    )
    return


if __name__ == "__main__":
    app.run()
