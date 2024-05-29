import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 24. Inventory at the English bookstore  


        ## Dictionary


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
        - You are the owner of an English bookstore, and these are some classics you sell:
        """
    )
    return


@app.cell
def __():
    classics = {"Austen":"Pride and Prejudice", 
                "Shelley":"Frankenstein", 
                "Joyce":"Ulyssessss"}
    print (classics)
    return classics,


@app.cell
def __(mo):
    mo.md(
        r"""
        - You are conducting an inventory, and you need to print authors and titles: 
        """
    )
    return


@app.cell
def __(classics):
    # as dict_items
    print (classics.items())
    # as a list of tuples
    print (list(classics.items()))
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Then, you need to print authors and titles separately:
        """
    )
    return


@app.cell
def __(classics):
    # authors as dict_items
    print (classics.keys())
    # authors as a list 
    print (list(classics.keys()))

    # titles as dict_values
    print (classics.values())
    # titles as a list
    print (list(classics.values()))
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - You notice that the title of the last book is wrong, so you correct it:
        """
    )
    return


@app.cell
def __(classics):
    print ("Wrong title: " + classics["Joyce"])
    classics["Joyce"] = "Ulysses"
    print ("Corrected title: " + classics["Joyce"])
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Then you add two new books that have just arrived: *Gulliver's travels* by Swift and *Jane Eyre* by Bronte:
        """
    )
    return


@app.cell
def __(classics):
    # adding the first book (syntax 1)
    classics["Swift"] = "Gulliver's travels"
    print (classics)

    # adding the second book (syntax 2)
    classics.update({"Bronte":"Jane Eyre"})
    print (classics)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Finally you remove the books by Austen and Joyce because you have just sold them: 
        """
    )
    return


@app.cell
def __(classics):
    # deleting the first book (syntax 1)
    del classics["Austen"]
    print (classics)

    # deleting the second book (syntax 2)
    classics.pop("Joyce")
    print (classics)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## List of dictionaries (*In more depth* section)

        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Given the following list of dictionaries:
        """
    )
    return


@app.cell
def __():
    countries = [{"name": "China", "capital": "Bejing"},
                 {"name": "France", "capital": "Paris"},]
    print (countries)
    return countries,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Add a list element:
        """
    )
    return


@app.cell
def __(countries):
    countries.append({"name": "Brazil", "capital": "Brasilia"})
    print (countries)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Slice the second element:
        """
    )
    return


@app.cell
def __(countries):
    print (countries [1])
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Print list elements using a for loop through elements and a for loop through indices:
        """
    )
    return


@app.cell
def __(countries):
    # for loop though elements
    print ("-> for loop though elements")
    for country in countries:
        print (country)

    # for loop though indices
    print ("-> for loop though indices")
    for i in range (len(countries)):
        print (countries[i])
    return country, i


@app.cell
def __(mo):
    mo.md(
        r"""
        - Print the country names using a for loop through elements and a for loop through indices:
        """
    )
    return


@app.cell
def __(countries):
    # for loop though elements
    print ("-> for loop though elements")     
    for country in countries:
        print (country["name"])
        
    # for loop though indices
    print ("-> for loop though indices")
    for i in range (len(countries)):
        print (countries[i]["name"])
    return country, i


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

