import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 13. Implementing a calculator

        ## Integers, floats, and arithmetic operations

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
        ## 1. What are the arithmetic operations in Python?
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        In Python there are 7 arithmetic operators. Try them in the following cells:
        1. Addition: `+`
        """
    )
    return


@app.cell
def __():
    4+3
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        2. Subtraction: `-` 
        """
    )
    return


@app.cell
def __():
    6-2
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        3. Multiplication: `*` 
        """
    )
    return


@app.cell
def __():
    6*5
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        4. Exponentiation: `**` 
        """
    )
    return


@app.cell
def __():
    2**3
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        5. Division: `/` 
        """
    )
    return


@app.cell
def __():
    10/5
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        6. Floor division: `//` 
        """
    )
    return


@app.cell
def __():
    7//4
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        7. Modulo: `%`  
        """
    )
    return


@app.cell
def __():
    7.5%4
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## 2. How do we ask a user to input a number? 
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Ask a user to input a number, assign it to a variable, and print out the variable:
        """
    )
    return


@app.cell
def __():
    number = input("Insert a number")
    print (number)
    return number,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Check the *type* of the variable `number`:
        """
    )
    return


@app.cell
def __(number):
    type(number)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Transform `number` into an integer, print it out, and check its type: 
        """
    )
    return


@app.cell
def __(number):
    number = int(number)
    print (number)
    type(number)
    return number,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Transform `number` into a float, print it out, and check its type: 
        """
    )
    return


@app.cell
def __(number):
    number = float(number)
    print (number)
    type (number)
    return number,


@app.cell
def __(mo):
    mo.md(
        r"""
        - You already know how to transform a number to a string. How do you do that?
        """
    )
    return


@app.cell
def __(number):
    number = str(number)
    print (number)
    type(number)
    return number,


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## 3. Let's create the calculator
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Ask the user the first input: 
        """
    )
    return


@app.cell
def __():
    first_number = input ("Insert the first number: ") 
    first_number = float (first_number)
    type(first_number)
    return first_number,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Ask the user the second input: 
        """
    )
    return


@app.cell
def __():
    operator = input ("Insert an arithmetic operator: ")
    type (operator)
    return operator,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Ask the user the third input:
        """
    )
    return


@app.cell
def __():
    second_number = float(input ("Insert the second number: ")) 
    type(second_number)
    return second_number,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Let's write the core of the calculator:
        """
    )
    return


@app.cell
def __(first_number, operator, second_number):
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "**":
        result = first_number / second_number
    elif operator == "/":
        result = first_number ** second_number
    elif operator == "//":
        result = first_number // second_number 
    elif operator == "%": 
        result = first_number % second_number 
    else: 
        print ("You didn't enter an arithmetic operator") 
    print (result)
    return result,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Finally, let's print out the result:
        """
    )
    return


@app.cell
def __(first_number, operator, result, second_number):
    print (str(first_number) + " " + operator + " " + str(second_number) + " = " + str(result))
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ### Make it a real calculator!

        - Merge the code you wrote above in the cell below:
        """
    )
    return


@app.cell
def __():
    # first input
    first_number = float (input ("Insert the first number: ")) 

    # operator
    operator = input ("Insert an arithmetic operator: ")

    # second input
    second_number = float (input ("Write the second number: ")) 

    # computations
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "**":
        result = first_number / second_number
    elif operator == "/":
        result = first_number ** second_number
    elif operator == "//":
        result = first_number // second_number 
    elif operator == "%": 
        result = first_number % second_number 
    else: 
        print ("You didn't enter an arithmetic operator. Please, run the cell again:")
        
    # print the result
    print (str(first_number) + " " + operator + " " + str(second_number) + " = " + str(result))
    return first_number, operator, result, second_number


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

