# __main__.py
import tkinter as tk
from pacman.game import PacmanGame


def main():
    root = tk.Tk()
    root.title('Pacman')
    PacmanGame(root)
    root.mainloop()


if __name__ == '__main__':
    main()
