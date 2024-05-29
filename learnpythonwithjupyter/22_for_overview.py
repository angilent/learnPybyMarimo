import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 22. More about the for loop

        ## Various ways of repeating commands on lists and beyond

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

        ## 1. Repeating commands

        - Print 3 random numbers between 1 and 10:
        """
    )
    return


@app.cell
def __():
    import random

    for _ in range (3):
        number = random.randint(1,10)
        print (number)
    return number, random


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## 2. For loops with lists
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ### 2.1. For loop through *indices*

        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Capitalize each string using a for loop through *indices*:
        """
    )
    return


@app.cell
def __():
    last_names = ["garcia", "smith", "zhang"]

    for i in range (len(last_names)):
        print ("The element in position " + str(i) + " is: " + last_names[i])
        last_names[i] = last_names[i].title()

    print (last_names)
    return i, last_names


@app.cell
def __(mo):
    mo.md(
        r"""
        ### 2.2 For loop through *elements* 
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Capitalize each string using a for loop through  *elements*:
        """
    )
    return


@app.cell
def __():
    last_names = ["garcia", "smith", "zhang"]
    last_names_upper = [] 
     
    for last_name in last_names:
        print ("The current element is: " + last_name)
        last_names_upper.append(last_name.title())

    print (last_names_upper)
    return last_name, last_names, last_names_upper


@app.cell
def __(mo):
    mo.md(
        r"""
        ### 2.3 For loop through *indeces* and *elements* 


        - Capitalize each string using a for loop through and *indeces and elements*:
        """
    )
    return


@app.cell
def __():
    last_names = ["garcia", "smith", "zhang"]

    for i,last_name in enumerate (last_names):
        print ("The element in position " + str(i) + " is: " + last_name)
        last_names[i] = last_name.title()
        
    print (last_names)                            
    return i, last_name, last_names


@app.cell
def __(mo):
    mo.md(
        r"""
        ### 2.4 List comprehension 

        - Capitalize each string using *list comprehension* containing a for loop through *indices*:
        """
    )
    return


@app.cell
def __():
    last_names = ["garcia", "smith", "zhang"]
    last_names = [last_names[i].title() for i in range(len(last_names))] 
    print (last_names)
    return last_names,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Capitalize each string using *list comprehension* containing a for loop through *elements*:
        """
    )
    return


@app.cell
def __():
    last_names = ["garcia", "smith", "zhang"]
    last_names = [last_name.title() for last_name in last_names]
    print (last_names)
    return last_names,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Keep and capitalize only the elements shorter than 6 characters:
        """
    )
    return


@app.cell
def __():
    last_names = ["garcia", "smith", "zhang"]
    last_names = [last_name.title() for last_name in last_names if len(last_name) < 6]
    print (last_names)
    return last_names,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Delete elements that are composed of 5 characters:
        """
    )
    return


@app.cell
def __():
    last_names = ["garcia", "smith", "zhang"]
    last_names = [last_name for last_name in last_names if len(last_name) != 5] 
    print (last_names)
    return last_names,


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## 3. Nested for loops 

        - Given the following list of vowels: 
        """
    )
    return


@app.cell
def __():
    vowels = ["A", "E", "I", "O", "U"]
    return vowels,


@app.cell
def __(mo):
    mo.md(
        r"""
        - For each vowel, print all the vowels on the right:
        """
    )
    return


@app.cell
def __(vowels):
    for i in range (len(vowels)): 
        print ("-- " + vowels[i])
        for j in range(i+1, len(vowels)):
            print (vowels[j])
    return i, j


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

