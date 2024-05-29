import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 20. What's behind comparisons and conditions? 

        ## Booleans

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
        ### 1. Single comparison or condition
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Given the following assignment:  
        """
    )
    return


@app.cell
def __():
    number = 5
    return number,


@app.cell
def __(mo):
    mo.md(
        r"""
        - What is the outcome of the following comparison operation?
        """
    )
    return


@app.cell
def __(number):
    print (number > 3)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Assign the above operation to a variable, and print it. What type is it?
        """
    )
    return


@app.cell
def __(number):
    result = number > 3
    print (result)
    type(result)
    return result,


@app.cell
def __(mo):
    mo.md(
        r"""
        - What is the outcome of the following comparison operation?
        """
    )
    return


@app.cell
def __(number):
    print (number < 3)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Assign the above operation to a variable, and print it. What type is it?
        """
    )
    return


@app.cell
def __(number):
    result = number < 3
    print (result)
    type(result)
    return result,


@app.cell
def __(mo):
    mo.md(
        r"""
        ### 2. Combining comparisons or conditions
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - What is the outcome of the following comparison operations? 
        """
    )
    return


@app.cell
def __():
    number = 3
    print (number > 1)           
    print (number < 5)           
    print (number > 1 and number < 5) 
    return number,


@app.cell
def __(mo):
    mo.md(
        r"""
        - What happens if we change the first condition to be false?
        """
    )
    return


@app.cell
def __():
    number = 3
    print (number > 4)           
    print (number < 5)           
    print (number > 4 and number < 5) 
    return number,


@app.cell
def __(mo):
    mo.md(
        r"""
        - What happens if we change the second condition to be false?
        """
    )
    return


@app.cell
def __():
    number = 3
    print (number > 1)           
    print (number < 2)           
    print (number > 1 and number < 2) 
    return number,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Finally, what happens if we change both conditions to be false?
        """
    )
    return


@app.cell
def __():
    number = 3
    print (number > 4)           
    print (number < 2)           
    print (number > 4 and number < 2) 
    return number,


@app.cell
def __(mo):
    mo.md(
        r"""
        --- 

        ### 3. Where else do we use booleans? 
          
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Look at this modified version of the example *Do you want more candies?* from Chapter 17 :
        """
    )
    return


@app.cell
def __():
    # initialize variables 
    number_of_candies = 0 

    # use the boolean as a flag
    flag = True

    # print the initial number of candies
    print ("You have " + str(number_of_candies) + " candies")

    # as long as the flag is True (= a green traffic light): 
    while flag == True:  
        
        # ask if one wants a candy
        answer = input("Do you want a candy? (yes/no)")
        
        # if the answer is yes
        if answer == "yes":
            
            # add a candy
            number_of_candies += 1 
        
            # print the total number of candies
            print ("You have " + str(number_of_candies) + " candies")
        
        # if the answer is no
        else:
        
            # print out the final number of candies
            print ("You have a total of " + str(number_of_candies) + " candies")
            
            # stop the loop by assigning False to the flag (= a red traffic light)
            flag = False
    return answer, flag, number_of_candies


@app.cell
def __(mo):
    mo.md(
        r"""
        - Here is the code from Chapter 17 for comparison:
        """
    )
    return


@app.cell
def __():
    # initialize variables 
    number_of_candies = 0 

    # print the initial number of candies
    print ("You have " + str(number_of_candies) + " candies")

    # ask if one wants a candy
    answer = input("Do you want a candy? (yes/no)")

    # as long as the answer is yes: 
    while answer == "yes":  
        
        # add a candy
        number_of_candies += 1 
        
        # print the current number of candies
        print ("You have " + str(number_of_candies) + " candies")
        
        # ask again if they want more candies 
        answer = input("Do you want more candies? (yes/no)")

    # print the final number of candies
    print ("You have a total of " + str(number_of_candies) + " candies")
    return answer, number_of_candies


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

