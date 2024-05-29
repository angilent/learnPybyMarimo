import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 21. Overview of lists 

        ## Operations, methods, and tricks

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
        ## 1. Arithmetic operations on list elements
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Sum two lists element‐wise:

        """
    )
    return


@app.cell
def __():
    odd_numbers  = [1,3,5]
    even_numbers = [2,4,6]
    summed  = []

    for i in range (len(odd_numbers)):
        summed.append(odd_numbers[i] + even_numbers[i])

    print(summed)
    return even_numbers, i, odd_numbers, summed


@app.cell
def __(mo):
    mo.md(
        r"""
        - Sum a number to each element of a list:
        """
    )
    return


@app.cell
def __():
    numbers = [1,2,3] 
    number = 3

    for i in range(len(numbers)):
        numbers[i] += number 
        
    print (numbers)
    return i, number, numbers


@app.cell
def __(mo):
    mo.md(
        r"""
        --- 
        ## 2. "Arithmetic" operations among lists
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Concatenate two lists:
        """
    )
    return


@app.cell
def __():
    odd_numbers  = [1,3,5] # two lists
    even_numbers = [2,4,6]
    concatenated = odd_numbers + even_numbers
    print (concatenated)
    return concatenated, even_numbers, odd_numbers


@app.cell
def __(mo):
    mo.md(
        r"""
        - Replicate a list 3 times:
        """
    )
    return


@app.cell
def __():
    numbers = [1,2,3]
    number  = 3
    replicated = numbers * number
    print (replicated)
    return number, numbers, replicated


@app.cell
def __(mo):
    mo.md(
        r"""
        - When is replication useful?
        """
    )
    return


@app.cell
def __():
    short_list = [0]
    number     = 50
    long_list  = short_list * number
    print (long_list)
    return long_list, number, short_list


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## 3. List assignment

        - Given a list containing a few integers:  
        """
    )
    return


@app.cell
def __():
    given_list = [1,2,3]
    print (given_list)
    return given_list,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Assign `given_list` to `new_list`:
        """
    )
    return


@app.cell
def __(given_list):
    new_list = given_list 
    print (new_list)
    return new_list,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Change the first element of `new_list`:
        """
    )
    return


@app.cell
def __(new_list):
    new_list[0] = 10
    print (new_list)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Print `given_list`:
        """
    )
    return


@app.cell
def __(given_list):
    print (given_list)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - How can we create an independent copy of a list?
        """
    )
    return


@app.cell
def __():
    given_list  = [1,2,3]
    new_list    = given_list.copy()
    new_list[0] = 40
    print (given_list)
    print (new_list)
    return given_list, new_list


@app.cell
def __(mo):
    mo.md(
        r"""
        --- 
        ## 4. Adding elements or lists to a list  

        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Add one element at the end of a list:
        """
    )
    return


@app.cell
def __():
    numbers = [1,2,3]
    numbers.append(4)
    print (numbers)
    return numbers,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Insert the number 2 in position 1:
        """
    )
    return


@app.cell
def __():
    numbers = [1,3,4]
    numbers.insert(1,2)
    print (numbers)
    return numbers,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Concatenate two lists:
        """
    )
    return


@app.cell
def __():
    first_list  = [1,2,3]
    second_list = [4,5,6]
    third_list  =  first_list + second_list
    print (third_list)
    return first_list, second_list, third_list


@app.cell
def __(mo):
    mo.md(
        r"""
        - Add one list at the end of another list:
        """
    )
    return


@app.cell
def __():
    first_list  = [1,2,3]
    second_list = [4,5,6]
    first_list.extend(second_list)
    print (first_list)
    return first_list, second_list


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## 5. Removing elements from a list  
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - From the following list, remove all the elements `"ciao"`:
        """
    )
    return


@app.cell
def __():
    greetings = ["ciao", "ciao", "hello"] 
    greetings.remove("ciao")
    print (greetings)
    return greetings,


@app.cell
def __(mo):
    mo.md(
        r"""
        - How do we remove both `"ciao"` from greetings?
        """
    )
    return


@app.cell
def __():
    greetings = ["ciao", "ciao", "hello"] 
    while "ciao" in greetings:
        greetings.remove("ciao")
    print (greetings)
    return greetings,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Remove the string `"hello"` based on its position:
        """
    )
    return


@app.cell
def __():
    greetings = ["ciao", "ciao", "hello"] 
    greetings.pop(2)
    print (greetings)
    return greetings,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Remove all elements in a list:
        """
    )
    return


@app.cell
def __():
    greetings = ["ciao", "ciao", "hello"] 
    greetings.clear()
    print (greetings) 
    return greetings,


@app.cell
def __(mo):
    mo.md(
        r"""
        --- 
        ## 6. Sorting a list  
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Sort the following list of integers:
        """
    )
    return


@app.cell
def __():
    numbers = [5,7,6]
    numbers.sort()
    print (numbers)
    return numbers,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Sort the following list of integers in a descending way:
        """
    )
    return


@app.cell
def __():
    numbers = [5,7,6]
    numbers.sort(reverse=True)
    print (numbers)
    return numbers,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Reverse the following list of integers:
        """
    )
    return


@app.cell
def __():
    numbers = [5,7,6] 
    numbers.reverse()
    print (numbers)
    return numbers,


@app.cell
def __(mo):
    mo.md(
        r"""
        --- 
        ## 7. Searching elements 
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Create a list and search for a specific element:
        """
    )
    return


@app.cell
def __():
    letters = ["a","g","c","g"]
    position = letters.index("g") 
    print (position)
    return letters, position


@app.cell
def __(mo):
    mo.md(
        r"""
        - How do we find all positions?
        """
    )
    return


@app.cell
def __():
    letters = ["a","g","c","g"]
    positions = []
    for i in range (len(letters)):
        if letters [i] == "g":
            positions.append(i)
    print (positions)
    return i, letters, positions


@app.cell
def __(mo):
    mo.md(
        r"""
        - Count how many times an element is present in a list: 
        """
    )
    return


@app.cell
def __():
    letters = ["a","g","c","g"]
    n = letters.count("g") 
    print (n)
    return letters, n


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## In more depth
        """
    )
    return


@app.cell
def __():
    greetings = ["ciao", "ciao", "hello"] # alternative with for
    for i in range (len(greetings)):
        print ("---------------")
        print ("i == " + str(i))
        print ("before the if:")
        print (greetings)
        if greetings[i] == "ciao":
            del greetings[i]   
        print ("after the if:")
        print (greetings)
    return greetings, i


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

