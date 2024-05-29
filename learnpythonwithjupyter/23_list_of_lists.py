import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 23. List of lists


        ## Slicing, nested for loops, and flattening


        [Learn Python with Jupyter](https://learnpythonwithjupyter.com/) by [Serena Bonaretti](https://sbonaretti.github.io/)   
        Narrative license: [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/2.0/). Code license: [GNU-GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)  

        ---
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## 1. Slicing
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Given the following list of lists: 
        """
    )
    return


@app.cell
def __():
    animals = [["dog", "cat"], ["cow", "sheep", "horse", "chicken", "rabbit"], ["panda", "elephant", "giraffe", "penguin"]]
    return animals,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Print the sub-lists containing pets, farm animals, and wild animals:  
        """
    )
    return


@app.cell
def __(animals):
    print (animals[0])
    print (animals[1])
    print (animals[2])
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Print the sub-elements "cat", "rabbit", and from "panda" to "giraffe":
        """
    )
    return


@app.cell
def __(animals):
    print (animals[0][1])
    print (animals[1][-1])
    print (animals[2][:3])
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        --- 
        ## 2. Nested for loops
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Given the following list of lists: 
        """
    )
    return


@app.cell
def __():
    sports = [["skiing", "skating", "curling"], ["canoeing", "cycling", "swimming", "surfing"]]
    return sports,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Print the sub-list elements one-by-one using a nested for loops through *indices*:
        """
    )
    return


@app.cell
def __(sports):
    for i in range (len(sports)):  
        for j in range (len(sports[i])):
            print (sports[i][j])
    return i, j


@app.cell
def __(mo):
    mo.md(
        r"""
        - Print the sub-list elements one-by-one using a nested for loops through *values*:
        """
    )
    return


@app.cell
def __(sports):
    for seasonal_sports in sports:
        for sport in seasonal_sports:
            print (sport)
    return seasonal_sports, sport


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## Flattening
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Given the following list of lists:
        """
    )
    return


@app.cell
def __():
    instruments = [["contrabass", "cello", "clarinet"],["gong", "guitar"],["tambourine", "trumpet", "trombone", "triangle"]]
    return instruments,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Flatten the list using a nested for loop through *indices*:
        """
    )
    return


@app.cell
def __(instruments):
    flat_instruments = []
    for i in range(len(instruments)):
        for j in range (len(instruments[i])):
            flat_instruments.append(instruments[i][j])
    print (flat_instruments)
    return flat_instruments, i, j


@app.cell
def __(mo):
    mo.md(
        r"""
        - Flatten the list using a nested for loop through  *elements*:
        """
    )
    return


@app.cell
def __(instruments):
    flat_instruments = []
    for group in instruments:
        for instrument in group:
            flat_instruments.append(instrument)
    print (flat_instruments)
    return flat_instruments, group, instrument


@app.cell
def __(mo):
    mo.md(
        r"""
        - Flatten the list using a for loop and list concatenation:
        """
    )
    return


@app.cell
def __(instruments):
    flat_instruments = []
    for group in instruments:
        flat_instruments += group
    print (flat_instruments)
    return flat_instruments, group


@app.cell
def __(mo):
    mo.md(
        r"""
        - Flatten the list using list comprehension:
        """
    )
    return


@app.cell
def __():
    instruments = [instrument for group in instruments for instrument in group]
    print (instruments)
    return instruments,


@app.cell
def __():
    return


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

