import marimo

__generated_with = "0.6.11"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # 15. Fortune cookies

        ## The Python module *random*


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
        - You are at a Chinese restaurant, and at the end of the meal, you get a fortune cookie. There are only three fortune cookies left. Each of them contains a message:
        """
    )
    return


@app.cell
def __():
    fortune_cookies = ["The man on the top of the mountain did not fall there",
                       "If winter comes, can spring be far behind?",
                       "Land is always on the mind of a flying bird"]
    return fortune_cookies,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Which fortune cookie will you get? Let the computer decide! To do so, the computer needs a module called random: 
        """
    )
    return


@app.cell
def __():
    import random
    return random,


@app.cell
def __(mo):
    mo.md(
        r"""
        - Here is your message when the computer picks a message index:
        """
    )
    return


@app.cell
def __(fortune_cookies, random):
    # pick a message index
    message_index = random.randint(0,len(fortune_cookies)-1)
    print(message_index)

    # get the message
    message = fortune_cookies[message_index]
    print (message)
    return message, message_index


@app.cell
def __(mo):
    mo.md(
        r"""
        - And here is your message when the computer directly picks a message:
        """
    )
    return


@app.cell
def __(fortune_cookies, random):
    # pick a message
    message = random.choice(fortune_cookies)
    print (message)
    return message,


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

