# entry point (`python -m pacman`)
# this kind of command line based entry maybe too hard for students..
import tkinter as tk
from pacman_game.pacman.game import PacmanGame


def main():
    root = tk.Tk()
    root.title("Pacman")
    PacmanGame(root)
    root.mainloop()


if __name__ == '__main__':
    main()
