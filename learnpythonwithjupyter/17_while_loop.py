import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 17. Do you want more candies?  

        ## The while loop

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

