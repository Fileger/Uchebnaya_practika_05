from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title('Русская рулетка')
root.geometry ('1200x800')
root.resizable(width=False, height=False)
canvas = Canvas(root, height=1200, width=800)
canvas.pack()
frame = Frame(root)
frame.place(relwidth=1, relheight=1)
canvas = Canvas(frame, bg="white")
canvas.pack(fill="both", expand=True)


def clear_window():
    for widget in frame.winfo_children():
        if widget != canvas:
            widget.destroy()
    canvas.delete("all")



def rule():
    clear_window()
    title = Label(frame, text='ПРАВИЛА ИГРЫ',  bg='white', font=("Arial", 20))
    title.place(relx=0.5, rely=0.27, relwidth=0.2, relheight=0.03, anchor="center")
    rules=Label(frame, text= "Цель – отнять все жизни противника.\n"
            "Револьвер: 1 жизнь, до 4 патронов, 1 заряжен по умолчанию.\n"
            "Дробовик: 3 жизни, 5 патронов, 3 холостых в первой партии.\n"
            "Выстрел в себя: без выстрела — доп. ход, иначе — минус жизнь.\n"
            "Победа: у противника 0 жизней.\n"
            "Рейтинг увеличивается за каждую победу.", bg='white', font=("Arial", 14), justify=LEFT)
    image = Image.open("pngwing.com (11).png")
    image = image.resize((50, 50))
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo, bg='white')
    label.image = photo
    btn = Button(frame, image=photo, activebackground='white', borderwidth=0, bg='white', command=main_menu)
    btn.place(x=305, y=535)
    rules.place(relx=0.25, rely=0.35, relwidth=0.5)
    canvas.create_line(290, 180, 290, 600, fill="black", width=1)
    canvas.create_line(290, 600, 910, 600, fill="black", width=1)
    canvas.create_line(910, 180, 910, 600, fill="black", width=1)
    canvas.create_line(290, 180, 910, 180, fill="black", width=1)


class modes:
    def modes_1():
        clear_window()
        global mode_players, mode_firearm
        mode_firearm = 0
        mode_players = 0
        title = Label(frame, text='КОЛИЧЕСТВО ИГРОКОВ', bg='white', font=("Arial", 20))
        title.place(relx=0.5, rely=0.075, relwidth=0.3, relheight=0.03, anchor="center")
        img1 = Image.open("1.png").resize((75, 90))
        photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open("111.png").resize((75, 90))
        photo2 = ImageTk.PhotoImage(img2)
        current_state = {"image": 1}
        btn = Button(frame, image=photo1, borderwidth=0, activebackground='white', bg='white', command=lambda: modes.toggle_image(current_state, current_state2, btn, photo2, btn2, photo1_a))
        btn.image = photo1
        btn.place(x=400, y=130)
        img2_a = Image.open("2.png").resize((75, 90))
        photo1_a = ImageTk.PhotoImage(img2_a)
        img2_b = Image.open("22.png").resize((75, 90))
        photo2_b = ImageTk.PhotoImage(img2_b)
        current_state2 = {"current": 1}
        btn2 = Button(frame, image=photo1_a, activebackground='white',  command=lambda: modes.toggle_image2(current_state2,current_state, btn2, photo2_b, btn, photo1), borderwidth=0, bg='white')
        btn2.image = photo1_a
        btn2.place(x=725, y=130)
        image3 = Image.open("pngwing.com (11).png")
        image3 = image3.resize((60, 60))
        photo3 = ImageTk.PhotoImage(image3)
        label3 = Label(root, image=photo3, bg='white')
        label3.image = photo3
        btn3 = Button(frame, image=photo3,activebackground='white',  borderwidth=0, bg='white', command=main_menu)
        btn3.place(x=20, y=725)


        title1 = Label(frame, text='ВЫБОР ОРУЖИЯ', bg='white', font=("Arial", 20))
        title1.place(relx=0.5, rely=0.4, relwidth=0.3, relheight=0.03, anchor="center")
        img11 = Image.open("pngwing.com (5).png").resize((90, 120))
        photo11 = ImageTk.PhotoImage(img11)
        img21 = Image.open("pngwing.com (5)_1.png").resize((90, 120))
        photo21 = ImageTk.PhotoImage(img21)
        current_state1 = {"image": 1}
        img2_a1 = Image.open("pngwing.com (6).png").resize((240, 80))
        photo1_a1 = ImageTk.PhotoImage(img2_a1)
        img2_b1 = Image.open("pngwing.com (6)_1.png").resize((240, 80))
        photo2_b1 = ImageTk.PhotoImage(img2_b1)
        current_state21 = {"current": 1}
        btn1 = Button(frame, image=photo11, borderwidth=0, activebackground='white', bg='white', command=lambda: modes.toggle_image1(current_state1, current_state21, btn1, photo21, btn21, photo1_a1))
        btn1.image = photo1
        btn1.place(x=400, y=440)
        btn21 = Button(frame, image=photo1_a1, activebackground='white', command=lambda: modes.toggle_image21(current_state21, current_state1, btn21, photo2_b1, btn1, photo11), borderwidth=0, bg='white')
        btn21.image = photo1_a1
        btn21.place(x=725, y=440)

        image4 = Image.open("pngwing.png")
        image4 = image4.resize((110, 110))
        photo4 = ImageTk.PhotoImage(image4)
        label4 = Label(root, image=photo4, bg='white')
        label4.image = photo4
        btn4 = Button(frame, image=photo4, activebackground='white', borderwidth=0, bg='white', command=lambda: modes.modes_2(mode_firearm, mode_players))
        btn4.place(x=1050, y=690)

    def toggle_image(s, sq, q, photo2, qq, photo1_a):
        global mode_players
        global current_state
        global current_state2
        global btn
        global btn2
        btn2 = qq
        current_state2 = sq
        current_state = s
        btn = q
        if s["image"] == 1:
            btn.config(image=photo2)
            btn.image = photo2
            current_state["image"] = 2
            btn2.config(image=photo1_a)
            btn2.image = photo1_a
            current_state2["current"] = 1
            mode_players=1
    def toggle_image2(s, sq, q, photo2_b, qq, photo1):
        global current_state2
        global btn2
        global btn
        global mode_players
        btn = qq
        current_state = sq
        current_state2 = s
        btn2 = q
        if s["current"] == 1:
            btn2.config(image=photo2_b)
            btn2.image = photo2_b
            current_state2["current"] = 2
            btn.config(image=photo1)
            btn.image = photo1
            current_state["image"] = 1
            mode_players = 2
    def toggle_image1(s,sq, q, photo21, qq, photo1_a1):
        global current_state1
        global current_state21
        global btn1
        global btn21
        global mode_firearm
        btn21 = qq
        current_state21=sq
        current_state1=sq
        btn1=q
        if s["image"] == 1:
            btn1.config(image=photo21)
            btn1.image = photo21
            current_state1["image"] = 2
            btn21.config(image=photo1_a1)
            btn21.image = photo1_a1
            current_state21["current"] = 1
            mode_firearm=1
    def toggle_image21(s,sq, q, photo2_b1, qq, photo11):
        global current_state21
        global btn21
        global btn1
        global mode_firearm
        btn1 = qq
        current_state1 = sq
        current_state21=s
        btn21=q
        if s["current"] == 1:
            btn21.config(image=photo2_b1)
            btn21.image = photo2_b1
            current_state21["current"] = 2
            btn1.config(image=photo11)
            btn1.image = photo11
            current_state1["image"] = 1
        mode_firearm = 2
    def modes_2(q,qq):
        if (q!=0) and (qq!=0):
            if q==1:
                modes.modes_roulette()
            else:
                modes.modes_shotgun()

    def modes_roulette():
        clear_window()
    def modes_shotgun():
        clear_window()

class Settings:
    def settings():
        clear_window()
        img1 = Image.open("3039404.png").resize((170, 170))
        photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open("ff.png").resize((220, 200))
        photo2 = ImageTk.PhotoImage(img2)
        current_state = {"image": 1}
        btn = Button(frame, image=photo1, borderwidth=0, activebackground='white', bg='white', command=lambda: Settings.toggle_image(current_state, btn, photo2, photo1))
        btn.image = photo1
        btn.place(x=300, y=320)
        img2_a = Image.open("pngwing.com.png").resize((195, 195))
        photo1_a = ImageTk.PhotoImage(img2_a)
        img2_b = Image.open("gg.png").resize((253, 230))
        photo2_b = ImageTk.PhotoImage(img2_b)
        current_state2 = {"current": 1}
        btn2 = Button(frame, image=photo1_a, activebackground='white', command=lambda: Settings.toggle_image2(current_state2, btn2, photo1_a, photo2_b), borderwidth=0, bg='white')
        btn2.image = photo1_a
        btn2.place(x=725, y=302.5)
        image3 = Image.open("pngwing.com (11).png")
        image3 = image3.resize((60, 60))
        photo3 = ImageTk.PhotoImage(image3)
        label3 = Label(root, image=photo3, bg='white')
        label3.image = photo3
        btn3 = Button(frame, image=photo3, borderwidth=0, activebackground='white', bg='white', command=main_menu)
        btn3.place(x=20, y=725)
    def toggle_image(s, q, photo2, photo1):
        global current_state
        global btn
        current_state=s
        btn=q
        if s["image"] == 1:
            btn.config(image=photo2)
            btn.image = photo2
            btn.place(x=282, y=297)
            current_state["image"] = 2
        else:
            btn.config(image=photo1)
            btn.image = photo1
            btn.place(x=300, y=320)
            current_state["image"] = 1
    def toggle_image2(s, q, photo1_a, photo2_b):
        global current_state2
        global btn
        current_state2=s
        btn2=q
        if s["current"] == 1:
            btn2.config(image=photo2_b)
            btn2.image = photo2_b
            btn2.place(x=690, y=280)
            current_state2["current"] = 2
        else:
            btn2.config(image=photo1_a)
            btn2.image = photo1_a
            btn2.place(x=725, y=302.5)
            current_state2["current"] = 1



def main_menu():
    clear_window()
    title = Label(frame, text='РУССКАЯ  РУЛЕТКА', bg='white', font=("Arial", 20))
    title.place(relx=0.15, rely=0.27, relwidth=0.7)
    btn1 = Button(frame, text='ИГРАТЬ', font=("Arial", 15), command=modes.modes_1)
    btn1.place(relx=0.38, rely=0.35, relwidth=0.24)
    btn2 = Button(frame, text='ПРАВИЛА', font=("Arial", 15), command=rule)
    btn2.place(relx=0.38, rely=0.43, relwidth=0.24)
    btn3 = Button(frame, text='НАСТРОЙКИ', font=("Arial", 15),command=Settings.settings)
    btn3.place(relx=0.38, rely=0.5, relwidth=0.24)
    btn4 = Button(frame, text='ВЫХОД', font=("Arial", 15), command=exit)
    btn4.place(relx=0.38, rely=0.57, relwidth=0.24)
main_menu()


root.mainloop()