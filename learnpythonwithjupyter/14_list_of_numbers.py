import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 14. Playing with numbers

        ## Common operations with lists of numbers

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
        ## 1. Changing numbers based on conditions
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Given the following list of numbers:
        """
    )
    return


@app.cell
def __():
    numbers = [12, 3, 15, 7, 18] 
    return numbers,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Subtract 1 from the numbers greater than or equal to 10, and add 2 to the numbers that are less than 10: 
        """
    )
    return


@app.cell
def __(numbers):
    # for each position in the list
    for i in range (len(numbers)):  
        
        # if the current number is greater than or equal to 10
        if numbers[i] >= 10:
            # subtract 1
            numbers[i] = numbers[i] - 1
        # otherwise
        else:
            # add 2
            numbers[i] = numbers[i] + 2

    # print the final result
    print (numbers) 
    return i,


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## 2. Separating even and odd numbers
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Given the following list of numbers:
        """
    )
    return


@app.cell
def __():
    numbers = [2, 10, 7, 5, 0, 9] 
    return numbers,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Separate them in two different lists, one for odd numbers, and one for even numbers:
        """
    )
    return


@app.cell
def __(numbers):
    # initialize empty lists
    even = []
    odd  = []

    # for each position in the list
    for i in range (len(numbers)): 
        
        # if the current number is even
        if numbers [i] % 2 == 0:
            # add it to the list "even"
            even.append(numbers[i])
        # otherwise
        else:
            # add it to the list "odd"
            odd.append(numbers[i])

    # check the final results
    print (even)
    print (odd)
    return even, i, odd


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## 3. Finding the maximum of a list of numbers
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Given the following list of numbers:
        """
    )
    return


@app.cell
def __():
    numbers = [2, -5, 34, 70, 22] 
    return numbers,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Find the maximum number in the list:
        """
    )
    return


@app.cell
def __(numbers):
    # initialize the maximum with the first element of the list
    maximum = numbers[0]

    # for each position in the list starting from the second
    for i in range (1, len(numbers)):
        
        # if the current number is greater than the current maximum
        if numbers[i] > maximum:
            # assign the number to maximum
            maximum = numbers[i]

    # print the maximum of the list
    print (maximum)
    return i, maximum


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

