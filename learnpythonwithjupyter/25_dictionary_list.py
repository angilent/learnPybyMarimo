import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 25. Trip to Switzerland


        ## Dictionary with lists as values


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
        - Your friend is planning a trip to Switzerland, and he has asked you for some tips. You start with an empty dictionary to fill out:
        """
    )
    return


@app.cell
def __():
    tips = {}
    return tips,


@app.cell
def __(mo):
    mo.md(
        r"""
        - He would like to visit some cities and taste typical food. Therefore, you add some recommendations:
        """
    )
    return


@app.cell
def __(tips):
    tips["cities"] = ["Bern", "Lucern"]
    tips["food"]   = ["chocolate", "raclette"]
    print (tips)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - Because his stay is four days, you add two more cities and two more dishes:
        """
    )
    return


@app.cell
def __(tips):
    tips["cities"].append("Lugano")
    print (tips)
    # using [] and .append() (syntax 1)
    return


@app.cell
def __(tips):
    tips["cities"] += ["Geneva"]
    print (tips)
    # using [] and list concatenation (syntax 2)
    return


@app.cell
def __(tips):
    tips.get("food").append("onion tarte")
    print (tips)
    # using get and .append() (syntax 3)
    return


@app.cell
def __(tips):
    tips["food"] = tips.get("food") + ["fondue"]
    print (tips)
    # using get and list concatenation (syntax 4)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - You want to check that the dictionary is correct, so you print all items one by one:
        """
    )
    return


@app.cell
def __(tips):
    for k,v in tips.items():
        print (k,v)
    return k, v


@app.cell
def __(mo):
    mo.md(
        r"""
        - Finally, you improve the print for improved readability:
        """
    )
    return


@app.cell
def __(tips):
    for k,v in tips.items():
        print ("{:>6}: {}".format(k,v))
    return k, v


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ---

        ## Olympic games
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - You are a sports journalist and you have to collect lists of summer and winter sports at the Olympic games. You start with an empty dictionary:
        """
    )
    return


@app.cell
def __():
    olympic_games = {}
    return olympic_games,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Then you add two summer sports and two winter sports: 
        """
    )
    return


@app.cell
def __(olympic_games):
    olympic_games["summer"] = ["diving", "swimming"]
    olympic_games["winter"] = ["alpine skiing", "figure skeating"]
    print (olympic_games)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - The lists look a bit short, so you want to add two more summer sports and two more winter sports: 
        """
    )
    return


@app.cell
def __(olympic_games):
    # using [] and .append() (syntax 1)
    olympic_games["summer"].append("rowing")
    olympic_games
    return


@app.cell
def __(olympic_games):
    # using [] and list concatenation (syntax 2)
    olympic_games["summer"] += ["sailing"]
    print (olympic_games)
    return


@app.cell
def __(olympic_games):
    # using get and .append() (syntax 3)
    olympic_games.get("winter").append("snowboad")
    print (olympic_games)
    return


@app.cell
def __(olympic_games):
    # using get and list concatenation (syntax 4)
    olympic_games["winter"] = olympic_games.get("winter") + ["bobsleigh"]
    print (olympic_games)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - You print out all items one by one in two different ways:
        """
    )
    return


@app.cell
def __(olympic_games):
    for k,v in olympic_games.items():
        print ("-> ",k,v)
    return k, v


@app.cell
def __(olympic_games):
    for k,v in olympic_games.items(): 
        print ("{:>20}: {}".format(k,v))
    return k, v


@app.cell
def __(mo):
    mo.md(
        r"""
        - And finally you want to print out only the sports lists:
        """
    )
    return


@app.cell
def __(olympic_games):
    for v in olympic_games.values():
        print (v)
    return v,


@app.cell
def __(mo):
    mo.md(
        r"""
        ---

        ## Teaching python
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - You are teaching python to some students and you want to list their names according to the course they are attending. You start by creating a dictionary:
        """
    )
    return


@app.cell
def __():
    students = {}
    return students,


@app.cell
def __(mo):
    mo.md(
        r"""
        - So far you have two students for the basic course and three students for the advanced course. You add their names to the dictionary:
        """
    )
    return


@app.cell
def __(students):
    students["basic"]    = ["Paul", "Laura"]
    students["advanced"] = ["Mohammed", "Geetha", "Maria"]
    print (students)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - You have just got four new registrations, three for the basic course, and one for the advanced course. You add the new students' names to the dictionary:
        """
    )
    return


@app.cell
def __(students):
    # using [] and .append() (syntax 1)
    students["basic"].append("Tom")
    students
    return


@app.cell
def __(students):
    # using [] and list concatenation (syntax 2)
    students["basic"] += ["Juhee"]
    print (students)
    return


@app.cell
def __(students):
    # using get and .append() (syntax 3)
    students.get("advanced").append("Matt")
    print (students)
    return


@app.cell
def __(students):
    # using get and list concatenation (syntax 4)
    students["basic"] = students.get("basic") + ["Marc"]
    print (students)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - After checking the background of one of your basic class students, you realize that she/he does not need the basic course. So you move her/him from the basic to the advanced course:
        """
    )
    return


@app.cell
def __(students):
    students["basic"].remove("Laura")
    students["advanced"].append("Laura")
    print (students)
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        - You print out all items one by one in two different ways:
        """
    )
    return


@app.cell
def __(students):
    for k,v in students.items():
        print ("->",k,v)
    return k, v


@app.cell
def __(students):
    for k,v in students.items():
        print ("{:>8}: {}".format(k,v))
    return k, v


@app.cell
def __(mo):
    mo.md(
        r"""
        - And finally you print out only the course names: 
        """
    )
    return


@app.cell
def __(students):
    for k in students.keys():
        print (k)
    return k,


@app.cell
def __():
    return


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

