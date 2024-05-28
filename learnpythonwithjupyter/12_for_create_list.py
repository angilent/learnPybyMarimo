import marimo

__generated_with = "0.6.8"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 12. What a mess at the bookstore!

        ## For loop to create new lists

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
        - There were many customers in the shop today, and they mixed up the books whose authors’ last names start with A and S:
        """
    )
    return


@app.cell
def __():
    authors = ["Alcott", "Saint-Exupery", "Arendt", "Sepulveda", "Shakespeare"]
    return authors,


@app.cell
def __(mo):
    mo.md(
        r"""
        - So you have to put the books whose authors’ last name starts with A on one shelf, and the books whose authors’ last name starts with S on another shelf:
        """
    )
    return


@app.cell
def __(authors):
    # initialize the variables as empty lists
    shelf_a = []
    shelf_s = []

    # for each position in the list
    for i in range (len(authors)):
        
        # print out the current element
        print ("The current author is: " + authors[i])
        
        # get the initial of the current author
        author_initial = authors[i][0] 
        print ("The author's initial is: " + author_initial)
        
        # if the author's initial is A
        if author_initial == "A": 
            # add the author to the shelf a
            shelf_a.append(authors[i])
            print ("The shelf A now contains: " + str(shelf_a) + "\n")
        
        # otherwise (author's initial is not A)
        else:
            # add the author to the shelf s
            shelf_s = shelf_s + [authors[i]]
            print ("The shelf S now contains: " + str(shelf_s) + "\n")

    # print out the final shelves
    print ("The authors on the shelf A are: " + str(shelf_a))
    print ("The authors on the shelf S are: " + str(shelf_s))      
    return author_initial, i, shelf_a, shelf_s


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

