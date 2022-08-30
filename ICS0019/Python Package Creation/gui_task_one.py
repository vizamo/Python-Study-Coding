from sys import version_info
from triangle_area_package import triangle_area

if version_info.major == 2:
    import Tkinter as tkinter
elif version_info.major == 3:
    import tkinter as tkinter


def pizza():
    window = tkinter.Tk()
    window.title("How Big Is Your Pizza")
    window.geometry('500x300')

    # Input of values for pizza area math
    tkinter.Label(window, text='How long is the height of your pizza?', font=("Helvetica", 12)).grid(row=0)
    tkinter.Label(window, text='How long is the base of your pizza?', font=("Helvetica", 12)).grid(row=1)
    tkinter.Label(window, text='How many people with you eat that pizza?', font=("Helvetica", 12)).grid(row=2)

    height_input = tkinter.Entry(window, width=5)
    height_input.grid(column=1, row=0)
    height_input.focus()  # Set focus to entry widget

    base_input = tkinter.Entry(window, width=5)
    base_input.grid(column=1, row=1)

    people_input = tkinter.Entry(window, width=5)
    people_input.grid(column=1, row=2)

    def how_big_is_pizza():
        piece_heigh = int(height_input.get())
        piece_base = int(base_input.get())
        people_count = int(people_input.get())
        piece_area = triangle_area.triangle_area(piece_heigh, piece_base)
        pizza_area = piece_area * people_count
        print("Yours pizza area is " + str(int(pizza_area)))
        tkinter.Label(window, text="Yours pizza area is " + str(int(pizza_area)), font=("Helvetica", 12)).grid(row=7)

    btn = tkinter.Button(window, text="Calculate Pizza Area",
                         command=how_big_is_pizza,
                         font=("Helvetica", 15))
    btn.grid(column=0, row=5)

    window.mainloop()


if __name__ == '__main__':
    pizza()
