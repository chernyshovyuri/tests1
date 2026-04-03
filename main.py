from functions import calculate_sum
from viewer import App


def main():

    app = App(callback=calculate_sum)
    app.mainloop()


if __name__ == '__main__':
    main()