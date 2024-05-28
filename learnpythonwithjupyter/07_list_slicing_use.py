import marimo

__generated_with = "0.6.8"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 7. Senses, planets, and a house

        ## Changing, adding, and removing list elements using slicing

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
        ## 1. Senses
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Given the following list: 
        """
    )
    return


@app.cell
def __():
    senses = ["eyes", "nose", "ears", "tongue", "skin"]
    print (senses)
    return senses,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Replace "nose" with "smell":
        """
    )
    return


@app.cell
def __(senses):
    senses[1] = "smell"
    print (senses)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Replace "tongue" and "skin" with "taste" and "touch": 
        """
    )
    return


@app.cell
def __(senses):
    senses[3:5] = ["taste", "touch"]
    print (senses)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Replace "eyes" and "ears" with "sight" and "hearing": 
        """
    )
    return


@app.cell
def __(senses):
    senses[0:3:2] = ["sight", "hearing"]
    print (senses)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        --- 
        ## 2. Planets
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Given the following list: 
        """
    )
    return


@app.cell
def __():
    planets = ["Mercury", "Mars", "Earth", "Neptune"]
    print (planets)
    return planets,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Add "Jupiter" at the end of the list:
        """
    )
    return


@app.cell
def __(planets):
    planets = planets + ["Jupiter"]
    print (planets)
    return planets,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Add "Venus" between "Mars" and "Earth":
        """
    )
    return


@app.cell
def __(planets):
    planets = planets[0:2] + ["Venus"] + planets[2:5]
    print (planets)
    return planets,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Add "Uranus" and "Saturn" between "Neptune" and "Jupiter":
        """
    )
    return


@app.cell
def __(planets):
    planets = planets[:5] + ["Uranus", "Saturn"] + planets[5:]
    print(planets)
    return planets,


@app.cell
def __(mo):
    mo.md(
        r"""
        --- 
        ## 3. A house
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Given the following list: 
        """
    )
    return


@app.cell
def __():
    house = ["kitchen", "dining room", "living room", "bedroom", "bathoom", "garden", "balcony", "terrace"]
    print (house)
    return house,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Delete "dining room":
        """
    )
    return


@app.cell
def __(house):
    del house[1]
    print (house)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Delete "garden" and "balcony":
        """
    )
    return


@app.cell
def __(house):
    del house[4:6]
    print (house)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Delete "kitchen", "bedroom", and "terrace":
        """
    )
    return


@app.cell
def __(house):
    del house[::2]
    print (house)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Delete "house":
        """
    )
    return


@app.cell
def __(house):
    del house
    print (house)
    return


@app.cell
def __():
    return


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

