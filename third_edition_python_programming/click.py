from graphics import *

def main():
    win = GraphWin("Click Me!")
    while True:
        p = win.getMouse()
        p.setFill("blue")
        p.draw(win)
        print(f"You clicked at: {p.getX()}, {p.getY()}")

main()