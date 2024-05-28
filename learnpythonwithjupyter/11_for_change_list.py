import marimo

__generated_with = "0.6.8"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 11. Cleaning the mailing list

        ## For loop to change list elements

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
        - You are responsible for a newsletter, and you have to send an email to the following addresses:
        """
    )
    return


@app.cell
def __():
    email = ["SARAH.BROWN@GMAIL.com", "Pablo.Hernandez@live.com", "LI.Min@hotmail.com"] 
    return email,


@app.cell
def __(mo):
    mo.md(
        r"""
        - For the sake of consistency, you want all email addresses to be lowercase. So you change them:
        """
    )
    return


@app.cell
def __(email):
    # for each position in the list
    for i in range (0, len(email)):
        
        print ("-> Loop: " + str(i))
        
        # print element before the change
        print ("Before the change, the element in position " + str(i) + " is: " + email[i])
        
        # change element and reassign 
        email[i] = email[i].lower()
        
        # print element after the change 
        print ("After the change, the element in position " + str(i) + " is: " + email[i])
        
    # print the modified list
    print ("Now the list is: " + str(email))
    return i,


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

