import marimo

__generated_with = "0.6.10"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 5. Customizing the burger menu

        ## List methods: .index(), .pop(), and .insert()


        [Learn Python with Jupyter](https://learnpythonwithjupyter.com/) by [Serena Bonaretti](https://sbonaretti.github.io/)   
        Narrative license: [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/2.0/). Code license: [GNU-GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)
        """
    )
    return


@app.cell
def __(mo):
    mo.md(r"## You are at a food court, ready to order. Today’s menu includes a burger, a side dish, and a drink:")
    return


@app.cell
def __():
    todays_menu = ["burger", "salad", "coke"]
    print(todays_menu)
    return todays_menu,


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"## You are happy with burger and coke, but you want to change your side dish from *salad* to *fries*. To do so, you:")
    return


@app.cell
def __(mo):
    mo.md(r"1. 1. Look at the position of the side dish in the menu:")
    return


@app.cell
def __(todays_menu):
    side_dish_index = todays_menu.index("salad")
    print (side_dish_index)
    return side_dish_index,


@app.cell
def __(mo):
    mo.md(r"2. Remove *salad* from the side dish position:")
    return


@app.cell
def __(side_dish_index, todays_menu):
    todays_menu.pop(side_dish_index)
    print (todays_menu)
    return


@app.cell
def __(mo):
    mo.md(r"3. Add *fries* to the side dish position:")
    return


@app.cell
def __(side_dish_index, todays_menu):
    todays_menu.insert(side_dish_index, "fries")
    print (todays_menu)
    return


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()
