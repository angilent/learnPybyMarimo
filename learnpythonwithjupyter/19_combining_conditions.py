import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        ---


        # 19. And, or, not, not in

        ## Combining and reversing conditions


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
        ## and 

        - Given the following list of integers:
        """
    )
    return


@app.cell
def __():
    numbers = [1, 5, 7, 2, 8, 19]
    return numbers,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Print out the numbers that are between 5 **and** 10:
        """
    )
    return


@app.cell
def __(numbers):
    # for each position in the list
    for i in range (0, len(numbers)):
        
        # if the current number is between 5 and 10
        if numbers[i] >= 5 and numbers[i] <=10 :
        
            # print the current number
            print ("The number " + str(numbers[i]) + " is between 5 and 10")   
    return i,


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## or  

        - Given the following string: 
        """
    )
    return


@app.cell
def __():
    message = "Have a nice day!!!"
    return message,


@app.cell
def __(mo):
    mo.md(
        r"""
        - And given all punctuation:
        """
    )
    return


@app.cell
def __():
    punctuation = "\"\/'()[]{}<>.,;:?!^@∼#$%&*_-"
    return punctuation,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Print and count the number of characters that are punctuation **or** vowels:
        """
    )
    return


@app.cell
def __(message, punctuation):
    # string of vowels
    vowels = "aeiou"

    # initialize counter
    counter = 0

    # for each position in the message
    for i in range (len(message)):
        
        # if the current element is punctuation or vowel
        if message[i] in punctuation or message[i] in vowels:
            
            # print a message
            print (message [i] + " is a vowel or a punctuation")
            
            # increase the counter
            counter += 1
            
    # print the final amount
    print ("The total amount of punctuation or vowels is " + str(counter))
    return counter, i, vowels


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## not
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Given the following list of integers:
        """
    )
    return


@app.cell
def __():
    numbers = [4, 6, 7, 9]
    return numbers,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Print out the numbers that are **not** divisible by 2:
        """
    )
    return


@app.cell
def __(numbers):
    # for each position in the list
    for i in range (len(numbers)):
        
        # if the current number is not even
        if not numbers[i] % 2 == 0:
            
            # print the current numeber
            print (numbers[i])
    return i,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Alternative solution:
        """
    )
    return


@app.cell
def __(numbers):
    # for each position in the list
    for i in range (len(numbers)):
        
        # if the current number is odd
        if numbers[i] % 2 != 0:
            
            # print the current numeber
            print (numbers[i])
    return i,


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## not in
        - Generate 5 random numbers between 0 and 10. If the random numbers are **not** already **in** the following list, add them:
        """
    )
    return


@app.cell
def __():
    numbers = [1,4,7]
    return numbers,


@app.cell
def __(numbers):
    import random

    # for five times
    for _ in range (5):
        
        # generate a random number between 0 and 10 
        number = random.randint(0,10)
        # print the number as a check
        print (number)
            
        # if the new number is not in numbers
        if number not in numbers:
            # add the number to numbers
            numbers.append(number)

    # print the final list
    print (numbers)
    return number, random


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

