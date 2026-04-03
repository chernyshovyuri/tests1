import customtkinter as CTk
from PIL import Image
import os

from functions import calculate_sum


class ImageLabel:

    @staticmethod
    def get(file_name: str, width: int, height: int)-> CTk.CTkImage:
        path = os.path.dirname(__file__)
        full_path = os.path.join(path, file_name)

        image = Image.open(full_path)

        return CTk.CTkImage(light_image=image, dark_image=image, size=(width, height))


class App(CTk.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("600x500")
        self.title("СуперОкно")
        self.logo = ImageLabel.get('d.rak.jpg', 180, 180)
        self.resizable(width=True, height=True)



        self.image_label = CTk.CTkLabel(self, image = self.logo, text='Я MR Дмитрий-Чак Норрис-Рак',font=("Arial", 16, "bold"), compound='bottom')
        self.image_label.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        self.thoughts = CTk.CTkLabel(self, text = '◀ Покажи мне свой лучший код...\nВот ......\nИ это твой лучший код ха ха ха\n'
                                                  'Вот мой лучший код ....\nТы его видишь?\nНет .....\nВот а он есть, это самый чистый код который ты даже не видишь...\n'
                                                  'Ха ха ха, хе хе хе , ху ху ху (смех из фильма Майор Пэйн)', text_color= 'red', corner_radius= 15,
                                     width= 250, height= 80, font=("Comic Sans MS", 13, "italic"), justify='center')

        self.thoughts.grid(row = 0, column=1, padx=(5, 20), pady=60, sticky="nw")


        self.button = CTk.CTkButton(master=self, text='Calculate Summ', width= 150, command= self.set_funktion)
        self.button.grid(row=1, column=0, padx=20, pady=20, sticky="w")

    def set_funktion(self):
        print(calculate_sum(10))






if __name__ == '__main__':

    app = App()
    app.mainloop()




 