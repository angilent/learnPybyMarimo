import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 26. Counting, compressing, and sorting


        ## What are dictionaries for?


        [Learn Python with Jupyter](https://learnpythonwithjupyter.com/) by [Serena Bonaretti](https://sbonaretti.github.io/)   
        Narrative license: [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/2.0/)   
        Code license: [GNU-GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)  
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        --- 
        ## 1. Counting elements
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Given the following string:
        """
    )
    return


@app.cell
def __():
    greetings = "hello! how are you?"
    return greetings,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Create a dictionary where the keys are the letters of the alphabet found in the string, and the corresponding values are the number of times each letter is present. Write the code in two ways: (1) using `if`/`else`, and (2) using `.get()` 

        1. Using `if`/`else`:
        """
    )
    return


@app.cell
def __(greetings):
    letter_counter = {}

    for letter in greetings:
        if letter not in letter_counter.keys():
            letter_counter[letter] = 1
        else:
            letter_counter[letter] += 1   

    for k, v in letter_counter.items():
        print (k, v)
    return k, letter, letter_counter, v


@app.cell
def __(mo):
    mo.md(
        r"""
        2. Using `.get()`:
        """
    )
    return


@app.cell
def __(greetings):
    letter_counter = {}

    for letter in greetings:
        letter_counter[letter] = letter_counter.get(letter, 0) + 1

    for k, v in letter_counter.items():
        print (k, v)  
    return k, letter, letter_counter, v


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## 2. Compressing information
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Given the following list:
        """
    )
    return


@app.cell
def __():
    sparse_vector = [0,0,0,1,0,7,0,0,4,0,0,0,8,0,0,0,6,0,0,0,0,0,0,0,9,0,0]
    return sparse_vector,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Convert it into a dictionary:
        """
    )
    return


@app.cell
def __(sparse_vector):
    # create the dictionary
    sparse_dict = {}
    for i in range(len(sparse_vector)):
        if sparse_vector[i] != 0:
            sparse_dict[i] = sparse_vector[i]

    # save the list length 
    sparse_dict["length"] = len(sparse_vector) 
            
    # print
    for k,v in sparse_dict.items():
        print (k,v) 
    return i, k, sparse_dict, v


@app.cell
def __(mo):
    mo.md(
        r"""
        - How do we get back to the sparse vector? 
        """
    )
    return


@app.cell
def __(sparse_dict):
    # create a list of zeros
    sparse_vector_back = [0] * sparse_dict["length"]

    # add nonzero values
    for k,v in sparse_dict.items():
        if k != "length":
            sparse_vector_back[k] = v 

    # print
    print (sparse_vector_back)
    return k, sparse_vector_back, v


@app.cell
def __(mo):
    mo.md(
        r"""
        ---
        ## 3. Sorting dictionary
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Given the following dictionary:
        """
    )
    return


@app.cell
def __():
    registry = {"Shaili":4, "Chris":90, "Maria":70}
    return registry,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Sort the dictionary items according to their *keys*:
        """
    )
    return


@app.cell
def __(registry):
    # create a new dictionary
    sorted_registry= {}

    # sort the keys
    sorted_keys = list(registry.keys())
    sorted_keys.sort()

    # fill out the new dictionary
    for k in sorted_keys:
        sorted_registry[k] = registry[k]
        
    print (sorted_registry)
    return k, sorted_keys, sorted_registry


@app.cell
def __(mo):
    mo.md(
        r"""
        -  Sort the dictionary items according to their *values*:
        """
    )
    return


@app.cell
def __(registry):
    # create a new dictionary
    sorted_registry = {}

    # sort keys according to values 
    sorted_keys = sorted(registry, key=registry.get) 

    # fill out the new dictionary
    for k in sorted_keys:
        sorted_registry[k] = registry[k]
        
    print (sorted_registry)
    return k, sorted_keys, sorted_registry


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

