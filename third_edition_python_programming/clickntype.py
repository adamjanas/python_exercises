from graphics import *


def main():
    win = GraphWin("Click and type", 400, 400)
    for i in range(10):
        pt = win.getMouse()
        key = input("type something")

        label = Text(pt, key)
        label.draw(win)


main()



