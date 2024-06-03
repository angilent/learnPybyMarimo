import marimo

__generated_with = "0.6.11"
app = marimo.App(width="medium")


@app.cell
def __():
    return


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md(
        rf"""
        # Beej 的 Python 编程指南

        https://beej.us/guide/bgpython/html/split-wide/what-is-programming-anyway.html#what-is-programming-anyway

        Attitude Prerequisite: be inquisitive, curious, have an eye for puzzles and problem solving, and be willing to take on difficult challenges.
        态度先决条件：好奇、好奇、关注谜题和解决问题，并愿意接受困难的挑战。

        ## 什么是编程？
        You often have that sequence of steps, that recipe, written down on a piece of paper. By itself, it’s definitely not cookies. But when you apply a number of kitchen implements and ingredients and an oven to it, pretty soon you have some cookies.
        您经常将步骤顺序、配方写在一张纸上。就其本身而言，它绝对不是cookie。但是，当您使用一些厨房用具和配料以及烤箱时，很快您就会得到一些饼干。

        Of course, in that case, you have to do the work. With programming, the computer does the work for you. But you have to write down the recipe.
        当然，在这种情况下，你必须做这项工作。通过编程，计算机可以为您完成工作。但你必须写下食谱。

        The recipe is the program. Programming is the act of writing down that recipe so the computer can execute it. And get those cookies baked.
        菜谱就是程序。编程是写下该配方以便计算机可以执行它的行为。然后把饼干烤好。

        When you’re first starting, large programs like that seem impossible. But here’s the secret: each of those large programs is made up of smaller, well-designed building blocks. And each of those building blocks is made up of smaller of the same.
        当你刚开始时，像这样的大型程序似乎是不可能的。但秘密是：每个大型程序都是由更小的、精心设计的构建块组成的。每个构建块都是由较小的相同块组成的。

        And when you start learning to be a programmer, you start with the smallest, most basic blocks, and you build up from there.
        当你开始学习成为一名程序员时，你会从最小、最基本的模块开始，然后从那里开始构建。

        And you keep building! Writing software is a lifelong learning process. There are always new things to learn, new technologies, new languages, new techniques. It’s a craft to be developed and perfected over a lifetime. Sure, at first you won’t have that many tools in your toolkit. But every moment you spend working on software gives you more experience solving problems and gives you more methods to attack them.
        你继续建造！编写软件是一个终生学习的过程。总是有新的东西需要学习、新技术、新语言、新技术。这是一门需要一生去发展和完善的手艺。当然，一开始你的工具箱里不会有那么多工具。但是，您花在软件上的每一刻都会让您获得更多解决问题的经验，并为您提供更多解决问题的方法。
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        rf"""
        ##  这里所说的解决问题是指什么
        In other words, I know what I want to see… how do I get there with the tools I know?
        换句话说，我知道我想看到什么……我如何使用我知道的工具到达那里？

        There’s a great scene in the movie Apollo 133 that I love. The CO2 scrubbers on the command module are spent, and the team wants to use the scrubbers from the lunar module to replace them. But the former are round, and the latter are square and won’t fit. Of course, the spacecraft has limited resources to repair it—just miscellaneous stuff on board that was meant for the mission.
        我喜欢电影《阿波罗 13 号》 3 中的一个很棒的场景。命令舱上的二氧化碳 2 洗涤器已用完，团队希望使用登月舱上的洗涤器来替换它们。但前者是圆的，后者是方的，不合适。当然，航天器的修复资源有限——船上只有用于执行任务的各种杂物。

        You have a limited set of programming techniques at your disposal, and you have the goal that you want to achieve. How can you get to that goal using only those tools? It’s a puzzle!
        您可以使用的编程技术是有限的，并且您有想要实现的目标。仅使用这些工具如何才能实现该目标？这是一个谜题！
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        rf"""
        ## 2.4 那么如何解决呢？

        Fun Programming Fact: Most devs have no idea how to solve a problem when they’re first presented with it. They have to systematically attack it.
        有趣的编程事实：大多数开发人员在第一次遇到问题时不知道如何解决。他们必须系统地攻击它。

        You could have saved a lot of time by actually planning what you were going to do before you started building.
        如果在开始构建之前实际计划好要做什么，您可以节省大量时间。

        Fun Programming Proverb: Hours of debugging can save you minutes of planning.
        有趣的编程谚语：数小时的调试可以节省您数分钟的规划时间。

        我最喜欢的问题解决框架之一是由数学家 George Pólya 于 1945 年在他的《如何解决问题》一书中推广的。它最初是为了解决数学问题而编写的，但它在解决任何问题上都出奇地有效。四个主要步骤是：

        Understanding the Problem. Get clarity on all parts of the problem. Break it down into subproblems, and break those subproblems down. If you don’t understand the problem, any solutions you come up with will be solving the wrong problem! You know you understand the problem when you can explain it to someone completely.
        了解问题。弄清楚问题的各个部分。将其分解为子问题，然后分解这些子问题。如果你不理解问题，你想出的任何解决方案都将解决错误的问题！当你可以向某人完整地解释问题时，你就知道你理解了这个问题。

        Devising a Plan. How are you going to attack this with the tools you have at your disposal and the techniques you know? You know you’re done making a plan when you’re able to easily convert your plan into code.
        制定计划。您将如何利用您拥有的工具和您所知道的技术来解决这个问题？当您能够轻松地将计划转换为代码时，您就知道您已经制定了计划。

        Often when planning you realize there’s something about the problem you don’t fully understand. Just for a bit, pop back to Step 1 until it’s clear, then come back to planning.
        通常，在制定计划时，您会意识到问题中有些内容您并不完全理解。暂时回到第 1 步，直到弄清楚为止，然后再回到计划中。

        Carrying out the plan Convert your plan into code and get it working.
        执行计划 将您的计划转换为代码并使其发挥作用。

        Often in this phase, you find that there was either something you didn’t understand or something the plan didn’t account for. Drop back a step or two until it’s resolved, then come back here.
        通常在这个阶段，你会发现有些东西是你不理解的，或者是计划没有考虑到的。后退一两步直到问题得到解决，然后再回到这里。

        Looking Back. Look back on the code you got working, and consider what went right and what went wrong. What would you do differently next time? What techniques did you learn while writing the code? Was there any place you could have structured things better, or anyplace you could have removed redundant code?
        回头看。回顾一下您正在运行的代码，并考虑哪些是正确的，哪些是错误的。下次你会采取什么不同的做法？您在编写代码时学到了哪些技巧？是否有任何地方可以更好地构建事物，或者可以在任何地方删除冗余代码？
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        rf"""
        ## 第2章 总结
        A programmer is a problem solver. They then write programs that implement a solution to that problem.
        程序员是问题解决者。然后他们编写程序来实现该问题的解决方案。
        A program is a series of instructions that can be carried out by a computer to solve the problem.
        程序是计算机可以执行以解决问题的一系列指令。
        The main problem-solving steps are: Understand the Problem, Devise a Plan, Carry out the Plan, Look Back.
        解决问题的主要步骤是：理解问题、制定计划、执行计划、回顾。
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        rf"""
        ## 如何编写程序？234

        - print("Hello, world!")
        - print("My name's Beej and this is (possibly) my first program!")
        """
    )
    return


@app.cell
def __():
    # 我的第一个程序，也许
    print("Hello, world!")
    print("My name's Beej and this is (possibly) my first program!")
    return


@app.cell
def __(mo):
    mo.md(
        rf"""
        You just wrote some instructions and the computer carried it out!
        你只要写下一些指令，计算机就会执行它！

        Next up: write a Quake III clone!
        下一步：编写一个 Quake III 克隆版本！

        Okay, so maybe there might be a small number of in between things that I skimmed over, but, as Obi-Wan Kenobi once said, “You’ve taken your first step into a larger world.”
        好吧，也许我略过一些中间的事情，但是，正如欧比旺·克诺比曾经说过的那样，“你已经迈出了进入更广阔世界的第一步
        """
    )
    return


@app.cell
def __(mo):
    mo.md(rf"## 回环来一个")
    return


@app.cell
def __():
    # Take whatever `input()` returns and store it in `value`:

    value = input("Enter a value: ")
    print("You entered", value)
    return value,


@app.cell
def __():
    ## 计算个根号2
    return


@app.cell
def __():
    import math

    _x = math.sqrt(2)
    print(_x)
    return math,


@app.cell
def __(mo):
    mo.md(
        rf"""
        This all looks terrifying! Can you feel your brain seizing up over it? Deer in the headlights? That’s OK. This is how developers feel when confronted with a new problem. Really! All of us! But what we know is that we have a problem solving framework we can use to attack this problem regardless of how difficult it seems initially.
        这一切看起来都很可怕！你能感觉到你的大脑在思考它吗？车头灯里有鹿？没关系。这就是开发人员遇到新问题时的感受。真的吗！我们所有人！但我们知道的是，我们有一个问题解决框架，可以用来解决这个问题，无论它最初看起来有多困难。

        Remember: Understand, Plan, then Code It Up.
        请记住：理解、计划，然后编码。
        """
    )
    return


@app.cell
def __():
    return


@app.cell
def __(mo):
    mo.md(
        rf"""
        ## 条件表达式和布尔运算

        George Boole27 was quite an interesting character. From humble beginnings in the early 1800s, he went on to develop the mathematics that became, in many ways, the foundation of modern computation. Pretty awesome.
        乔治·布尔 27 是一个非常有趣的角色。他从 1800 年代初出身卑微，后来发展了数学，在很多方面成为现代计算的基础。太棒了。

        All right! Now one more thing to remember: unless there are parentheses in an expression saying otherwise, AND takes precedence over OR. That is, do the ANDs first, and then do the ORs.
        好的！现在还要记住一件事：除非表达式中有括号另有说明，否则 AND 优先于 OR。即先进行 AND 运算，再进行 OR 运算。

        ## 比较运算

        布尔值
        True
        False

        ## 逻辑运算
        and
        or
        not
        """
    )
    return


@app.cell
def __():
    _x = input("Enter a number: ")
    _x = float(_x)

    if _x >= 50 and _x <= 59:
        print(_x, "is between 50 and 59, inclusive")
        print("Well done!")
    else:
        print(_x, "is not between 50 and 59, inclusive")
    return


@app.cell
def __(mo):
    slider = mo.ui.slider(5,45)
    return slider,


@app.cell(hide_code=True)
def __(mo, slider):
    mo.md(rf"{slider}")
    return


@app.cell
def __(slider):
    x = slider.value
    print(x)
    if x < 10:
        print("x is less than 10")
    elif x < 20:
        print("x is less than 20")
    elif x < 30:
        print("x is less than 30")
    else:
        print("x is greater than or equal to 30")
    return x,


@app.cell
def __(mo):
    mo.md(rf"## while 循环！")
    return


@app.cell
def __():
    _x = 1200

    while _x <= 1210:
        print(_x)
        _x += 1

    print("All done!")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        rf"""
        # 我的笔记

        - 编程就像写文章，可以用做笔记的方式学编程。


        - 点击链接查看和 Kimi 智能助手的对话 https://kimi.moonshot.cn/share/cpcu70ecp7f8oua7rde0
        """
    )
    return


if __name__ == "__main__":
    app.run()
