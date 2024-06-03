import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        rf"""
        # 欢迎来到 marimo 入门
        - 今天介绍基础的 cell 和 页面显示信息
        - 看看应该如何使用cell 的输出
        """
    )
    return


@app.cell
def __():
    1+1 
    print(1+1)
    1+3
    "hello"
    return


@app.cell
def __(ss):
    ss
    return


@app.cell
def __(mo):
    mo.md(rf"markdonw 的方式是为了轻松的输入文本").callout()
    return


@app.cell
def __():
    ss = "Hello World"
    print(ss)

    ss
    return ss,


@app.cell
def __(mo, name):
    mo.md(rf"my name is {name}")
    return


@app.cell
def __(mo):
    text_input_name = mo.ui.text(placeholder="你的名字")
    text_input_name
    return text_input_name,


@app.cell
def __(text_input_name):
    name = text_input_name.value
    print("my name is " + name)
    text_input_name.value
    return name,


if __name__ == "__main__":
    app.run()
