from classes import Window, Line

def main():
    win = Window(800, 600)
    win.draw_line(Line(0,0,1000000,1000000), "black")
    win.wait_for_close()

main()