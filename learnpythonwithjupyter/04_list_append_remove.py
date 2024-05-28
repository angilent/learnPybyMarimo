import marimo

__generated_with = "0.6.8"
app = marimo.App(width="medium")


@app.cell
def __(mo):
    mo.md(
        r"""
        # 4. Grocery shopping

        ## List methods: .append() and .remove()


        [Learn Python with Jupyter](https://learnpythonwithjupyter.com/) by [Serena Bonaretti](https://sbonaretti.github.io/)   
        Narrative license: [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/2.0/). Code license: [GNU-GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)
        """
    )
    return


@app.cell
def __(mo):
    mo.md(r"- You are going to a grocery store where you have to buy some food:")
    return


@app.cell
def __():
    shopping_list = ["carrots", "chocolate", "olives"]
    print (shopping_list)
    return shopping_list,


@app.cell
def __(mo):
    mo.md(r"- Right before leaving home, you ask yourself if you have to buy something else. If the item is not in the list, you add it:")
    return


@app.cell
def __(shopping_list):
    new_item = input("What else do I have to buy?")

    if new_item in shopping_list:
        print (new_item + " is/are already in the shopping list")
        print (shopping_list) 
    else:
        shopping_list.append(new_item)
        print (shopping_list)
    return new_item,


@app.cell
def __(mo):
    mo.md(r"- Finally, you ask yourself if you have to remove an item. If so, you remove the item from the list:")
    return


@app.cell
def __(shopping_list):
    item_to_remove = input("What do I have to remove?")

    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
        print (shopping_list)
    else:
        print (item_to_remove + " is/are not in the list")
        print (shopping_list)
    return item_to_remove,


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()
