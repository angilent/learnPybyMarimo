import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # 10. Where are my gloves?

        ## For loop for searching

        [Learn Python with Jupyter](https://learnpythonwithjupyter.com/) by [Serena Bonaretti](https://sbonaretti.github.io/)   
        Narrative license: [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/2.0/). Code license: [GNU-GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)  

        ---
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"## Who doesn’t have a messy drawer? Here is ours! It contains some accessories:")
    return


@app.cell
def __():
    accessories = ["belt", "hat", "gloves", "sunglasses", "ring"]
    print (accessories)
    return accessories,


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"## Print out all accessories one by one, as well as their positions in the list. Use a sentence like *The element x is in position y*:")
    return


@app.cell
def __(accessories):
    # for each position in the list
    for i in range (len(accessories)):
        #print each elements and its position
        print ("The element "  + accessories[i] + " is in position " + str(i))
    return i,


@app.cell
def __(mo):
    mo.md(r"## 1. Print the accessory whose name is **composed of** 6 characters and its position in the list. Use a sentence like *The element x is in position y and it has n characters*:")
    return


@app.cell
def __(accessories):
    # for each position in the list
    for _i in range (len(accessories)):
        # if the length of the element equals 6
        if len(accessories[_i]) == 6:
            # print the element, its position, and its number of characters
            print ("The element " + accessories[_i] + " is in position " + str(_i) + " and it has 6 characters")
    return


@app.cell
def __(mo):
    mo.md(r"## 2. Print the accessories whose names are composed of **less than** 6 characters:")
    return


@app.cell
def __(accessories):
    # for each position in the list
    for _i in range (len(accessories)):
        # if the length of the element is less than 6
        if len(accessories[_i]) < 6:
            # print the element, its position, and its number of characters
            print ("The element " + accessories[_i] + " is in position " + str(_i) + " and it has less than 6 characters")
    return


@app.cell
def __(mo):
    mo.md(r"## 3. Print the accessories whose name is composed of **more than** 6 characters. Also, assign 6 to a variable:")
    return


@app.cell
def __(accessories):
    # defining the threshold
    n_of_characters2 = 6 
    # for each position in the list 
    for i4 in range (len(accessories)):
        # if the length of the element is greater than the threshold
        if len(accessories[i4]) > n_of_characters2:
            # print the element, its position, and its number of characters
            print ("The element " + accessories[i4] + " is in position " + str(i4) + " and it has more than " + str(n_of_characters2) + " characters")
    return i4, n_of_characters2


@app.cell
def __(mo):
    mo.md(r"## 4. Print the accessories whose names are composed of a number of characters **different from** 6:")
    return


@app.cell
def __(accessories):
    # defining the threshold
    n_of_characters3 = 6 
    # for each position in the list 
    for i5 in range (len(accessories)):
        # if the length of the element is not equal to the threshold
        if len(accessories[i5]) != n_of_characters3:
            # print the element, its position, and its number of characters
            print ("The element " + accessories[i5] + " is in position " + str(i5) + " and it has a number of characters different from " + str(n_of_characters3))
    return i5, n_of_characters3


@app.cell
def __(mo):
    mo.md(r"## 5. Print the accessories whose position is **less than or equal to** 2:")
    return


@app.cell
def __(accessories):
    # defining the threshold
    position2 = 2 
    # for each position in the list 
    for i6 in range (len(accessories)):
        # if the position of the element is less then or equal to to the threshold
        if i6 <= position2:
            # print the element, its position, and its position characteristic
            print ("The element " + accessories[i6] + " is in position " + str(i6) + ", which is less than or equal to " + str(position2))
    return i6, position2


@app.cell
def __(mo):
    mo.md(r"## 6. Print the accessories whose position is **at least** 2:")
    return


@app.cell
def __(accessories):
    # defining the threshold
    position3 = 2 
    # for each position in the list 
    for i7 in range (len(accessories)):
        # if the position of the element is greater then or equal to to the threshold
        if i7 >= position3:
            # print the element, its position, and its position characteristic
            print ("The element " + accessories[i7] + " is in position " + str(i7) + ", which is at least " + str(position3))
    return i7, position3


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()
