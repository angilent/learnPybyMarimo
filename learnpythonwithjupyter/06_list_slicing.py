import marimo

__generated_with = "0.6.8"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 6. Traveling around the world

        ## List slicing

        [Learn Python with Jupyter](https://learnpythonwithjupyter.com/) by [Serena Bonaretti](https://sbonaretti.github.io/)   
        Narrative license: [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/2.0/). Code license: [GNU-GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)  
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Consider the following list:
        """
    )
    return


@app.cell
def __():
    cities = ["San Diego", "Prague", "Cape Town", "Tokyo", "Melbourne"]
    print (cities)
    return cities,


@app.cell
def __(mo):
    mo.md(
        r"""
        1. Slice "Prague":
        """
    )
    return


@app.cell
def __(cities):
    print (cities[1])
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        2. Slice the cities from "Prague" to "Tokyo":
        """
    )
    return


@app.cell
def __(cities):
    print (cities[1:4])
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        3. Slice "Prague" and "Tokyo":
        """
    )
    return


@app.cell
def __(cities):
    print (cities[1:4:2])
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        4. Slice the cities from "San Diego" to "Cape Town" (two ways):
        """
    )
    return


@app.cell
def __(cities):
    print (cities[0:3])
    return


@app.cell
def __(cities):
    print (cities[:3])
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        5. Slice the cities from "Cape Town" to "Melbourne" (two ways):
        """
    )
    return


@app.cell
def __(cities):
    print (cities[2:5])
    return


@app.cell
def __(cities):
    print (cities[2:])
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        6. Slice "San Diego", "Cape Town", and "Melbourne" (two ways):
        """
    )
    return


@app.cell
def __(cities):
    print (cities[0:5:2])
    return


@app.cell
def __(cities):
    print (cities[::2])
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        7. Slice "Melbourne" (two ways):
        """
    )
    return


@app.cell
def __(cities):
    print (cities[4])
    return


@app.cell
def __(cities):
    print (cities[-1])
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        8. Slice the cities from "Prague" to "Tokyo" using negative indices (alternative to example 2):
        """
    )
    return


@app.cell
def __(cities):
    print (cities[-4:-1])
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        9. Slice the cities from "Tokyo" to "Prague" using positive indices (reverse order):
        """
    )
    return


@app.cell
def __(cities):
    cities[3:0:-1]
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        10. Slice the cities from "Tokyo" to "Prague" using negative indices (reverse order) (alternative to example 9):
        """
    )
    return


@app.cell
def __(cities):
    cities[-2:-5:-1]
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        11. Slice all the cities in reverse order:
        """
    )
    return


@app.cell
def __(cities):
    print (cities[::-1])
    return


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

