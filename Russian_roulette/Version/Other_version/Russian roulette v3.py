from tkinter import *
from PIL import Image, ImageTk
import random
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
        img2_a1 = Image.open("pngwing.com (6).png").resize((240, 130))
        photo1_a1 = ImageTk.PhotoImage(img2_a1)
        img2_b1 = Image.open("pngwing.com (6)_1.png").resize((240, 130))
        photo2_b1 = ImageTk.PhotoImage(img2_b1)
        current_state21 = {"current": 1}
        btn1 = Button(frame, image=photo11, borderwidth=0, activebackground='white', bg='white', command=lambda: modes.toggle_image1(current_state1, current_state21, btn1, photo21, btn21, photo1_a1))
        btn1.image = photo1
        btn1.place(x=400, y=440)
        btn21 = Button(frame, image=photo1_a1, activebackground='white', command=lambda: modes.toggle_image21(current_state21, current_state1, btn21, photo2_b1, btn1, photo11), borderwidth=0, bg='white')
        btn21.image = photo1_a1
        btn21.place(x=625, y=440)

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
                modes.mode_roulette()
            else:
                if qq==1:
                    game.shotgun_1()
                else:
                    game.shotgun_2()

    def mode_roulette():
        clear_window()
        image5 = Image.open("pngwing.com (11).png")
        image5 = image5.resize((60, 60))
        photo5 = ImageTk.PhotoImage(image5)
        label5 = Label(root, image=photo5, bg='white')
        label5.image = photo5
        btn5 = Button(frame, image=photo5, activebackground='white', borderwidth=0, bg='white', command=main_menu)
        btn5.place(x=20, y=725)
        image6 = Image.open("pngwing.png")
        image6 = image6.resize((110, 110))
        photo6 = ImageTk.PhotoImage(image6)
        label6 = Label(root, image=photo6, bg='white')
        label6.image = photo6
        btn6 = Button(frame, image=photo6, activebackground='white', borderwidth=0, bg='white', command= modes.modes3_roulette)
        btn6.place(x=1050, y=690)
        title = Label(frame, text='КОЛИЧЕСТВО ПАТРОНОВ', bg='white', font=("Arial", 20))
        title.place(relx=0.5, rely=0.075, relwidth=0.6, relheight=0.04, anchor="center")
        patron_img = ImageTk.PhotoImage(Image.open("pngwing.com (8).png").resize((120, 120)))
        drum_imgs = [ImageTk.PhotoImage(Image.open("pngwing.com-_7_1.bmp").resize((200, 200))),
            ImageTk.PhotoImage(Image.open("pngwing.com-_7_2.bmp").resize((200, 200))),
            ImageTk.PhotoImage(Image.open("pngwing.com-_7_3.bmp").resize((200, 200))),
            ImageTk.PhotoImage(Image.open("pngwing.com-_7_4.bmp").resize((200, 200))),
            ImageTk.PhotoImage(Image.open("pngwing.com-_7_5.bmp").resize((200, 200)))]
        drum = canvas.create_image(400, 300, image=drum_imgs[0])
        canvas.drum_imgs = drum_imgs
        canvas.drum_state = 0
        patrons = []
        start_positions = [(50, 50), (150, 50), (50, 150), (150, 150)]
        for i, pos in enumerate(start_positions):
            p = canvas.create_image(pos[0], pos[1], image=patron_img)
            patrons.append(p)
        canvas.patron_img = patron_img
        canvas.deleted = []
        dragging_patron = [None]
        dragging_returning = [False]
        def start_drag(event):
            item = canvas.find_withtag("current")
            if not item:
                return
            item = item[0]
            if item == drum:
                if canvas.deleted:
                    patron_id, _ = canvas.deleted.pop()
                    patrons.append(patron_id)
                    canvas.itemconfig(patron_id, state="normal")
                    if canvas.drum_state > 0:
                        canvas.drum_state -= 1
                        canvas.itemconfig(drum, image=drum_imgs[canvas.drum_state])
                    canvas.coords(patron_id, event.x, event.y)
                    dragging_patron[0] = patron_id
                    dragging_returning[0] = True
                else:
                    dragging_patron[0] = None
                    dragging_returning[0] = False
            elif item in patrons:
                dragging_patron[0] = item
                dragging_returning[0] = False
        def do_drag(event):
            if dragging_patron[0] is not None:
                canvas.coords(dragging_patron[0], event.x, event.y)
                if not dragging_returning[0]:
                    check_collision(dragging_patron[0])
        def stop_drag(event):
            dragging_patron[0] = None
            dragging_returning[0] = False
        canvas.bind("<Button-1>", start_drag)
        canvas.bind("<B1-Motion>", do_drag)
        canvas.bind("<ButtonRelease-1>", stop_drag)
        def check_collision(patron_id):
            global drum_state
            if patron_id not in patrons:
                return
            p = canvas.bbox(patron_id)
            t = canvas.bbox(drum)
            if p and t:
                if (p[2] > t[0] and p[0] < t[2] and p[3] > t[1] and p[1] < t[3]):
                    patrons.remove(patron_id)
                    canvas.deleted.append((patron_id, canvas.coords(patron_id)))
                    canvas.itemconfig(patron_id, state="hidden")
                    if canvas.drum_state + 1 < len(canvas.drum_imgs):
                        canvas.drum_state += 1
                        canvas.itemconfig(drum, image=drum_imgs[canvas.drum_state])



    def modes3_roulette():
        global mode_players
        if mode_players == 1:
            game.roulette_1()
        else:
            game.roulette_2()


class game:
    def roulette_1():
        global a, title3, rating_1
        a = random.randint(1, 6)
        clear_window()
        rating_1=0
        title3 = Label(frame, text=rating_1, bg='white', font=("Arial", 25))
        title3.place(x=62, y=53, relwidth=0.03, relheight=0.05, anchor="center")

        canvas.create_line(150, 800, 270, 350, fill="black", width=2)
        canvas.create_line(1050, 800, 930, 350, fill="black", width=2)
        canvas.create_line(930, 350, 270, 350, fill="black", width=2)

        opp = ImageTk.PhotoImage(Image.open("pngwing.com (111).png").resize((350, 300)))
        canvas.create_image(570, 239, image=opp)

        roulette = ImageTk.PhotoImage(Image.open("pngwing.com (5).png").resize((90, 120)))
        canvas.create_image(600, 550, image=roulette)
        canvas.image = opp,roulette

        img1 = Image.open("3039404.png").resize((35, 35))
        photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open("ff.png").resize((46, 41))
        photo2 = ImageTk.PhotoImage(img2)
        current_state = {"image": 1}
        btn = Button(frame, image=photo1, borderwidth=0, activebackground='white', bg='white', command=lambda: game.toggle_image(current_state, btn, photo2, photo1))
        btn.image = photo1
        btn.place(x=110, y=33)
        img2_a = Image.open("pngwing.com.png").resize((40, 40))
        photo1_a = ImageTk.PhotoImage(img2_a)
        img2_b = Image.open("gg.png").resize((53, 48))
        photo2_b = ImageTk.PhotoImage(img2_b)
        current_state2 = {"current": 1}
        btn2 = Button(frame, image=photo1_a, activebackground='white', command=lambda: game.toggle_image2(current_state2, btn2, photo1_a, photo2_b), borderwidth=0,bg='white')
        btn2.image = photo1_a
        btn2.place(x=170, y=30)

        image3 = Image.open("pngwing.com (11).png")
        image3 = image3.resize((50, 50))
        photo3 = ImageTk.PhotoImage(image3)
        label3 = Label(root, image=photo3, bg='white')
        label3.image = photo3
        btn3 = Button(frame, image=photo3, borderwidth=0, activebackground='white', bg='white', command=main_menu)
        btn3.place(x=230, y=25)


        canvas.create_line(30, 25, 30, 85, fill="black", width=1)
        canvas.create_line(30, 25, 95, 25, fill="black", width=1)
        canvas.create_line(95, 25, 95, 85, fill="black", width=1)
        canvas.create_line(30, 85, 95, 85, fill="black", width=1)
        title1 = Label(frame, text='1 ИГРОК', bg='white', font=("Arial", 13))
        title1.place(x=61, y=16, relwidth=0.3, relheight=0.02, anchor="center")


        def opp_shot():
            global a, rating_1
            if a>(canvas.drum_state+1):
                a = random.randint(1, 6)
                b = random.randint(1, 2)
                if a <= (canvas.drum_state + 1):
                    if b==1:
                        print('Вы проиграли')
                    else:
                        print('Вы победили')
                        if rating_1 != 98:
                            rating_1 += 1
                        else:
                            rating_1 = 0
                        title3.config(text=rating_1)
            else:
                print('Вы победили')
                if rating_1 != 98:
                    rating_1 += 1
                else:
                    rating_1 = 0
                title3.config(text=rating_1)
            a = random.randint(1, 6)
        def shot():
            global a
            if a <= (canvas.drum_state + 1):
                print('Вы проиграли')
            a = random.randint(1, 6)

        btn5 = Button(frame, text='ВЫСТРЕЛИТЬ В ПРОТИВНИКА', font=("Arial", 15), command=opp_shot)
        btn5.place(relx=0.18, rely=0.85, relwidth=0.27, relheight=0.13)
        btn4 = Button(frame, text='ВЫСТРЕЛИТЬ В СЕБЯ', font=("Arial", 15), command=shot)
        btn4.place(relx=0.55, rely=0.85, relwidth=0.27, relheight=0.13)



    def toggle_image(s, q, photo2, photo1):
        global current_state
        global btn
        current_state = s
        btn = q
        if s["image"] == 1:
            btn.config(image=photo2)
            btn.image = photo2
            btn.place(x=105.6, y=28)
            current_state["image"] = 2
        else:
            btn.config(image=photo1)
            btn.image = photo1
            btn.place(x=110, y=33)
            current_state["image"] = 1

    def toggle_image2(s, q, photo1_a, photo2_b):
        global current_state2
        global btn
        current_state2 = s
        btn2 = q
        if s["current"] == 1:
            btn2.config(image=photo2_b)
            btn2.image = photo2_b
            btn2.place(x=163, y=25)
            current_state2["current"] = 2
        else:
            btn2.config(image=photo1_a)
            btn2.image = photo1_a
            btn2.place(x=170, y=30)
            current_state2["current"] = 1


    def roulette_2():
        clear_window()
        global player, a, rating_1, rating_2, title3, title4
        rating_1=0
        rating_2=0
        player=1
        a = random.randint(1, 6)

        title3 = Label(frame, text=rating_1, bg='white', font=("Arial", 25))
        title3.place(x=62, y=53, relwidth=0.03, relheight=0.05, anchor="center")
        title4 = Label(frame, text=rating_2, bg='white', font=("Arial", 25))
        title4.place(x=152.5, y=54, relwidth=0.04, relheight=0.05, anchor="center")

        canvas.create_line(150, 800, 270, 350, fill="black", width=2)
        canvas.create_line(1050, 800, 930, 350, fill="black", width=2)
        canvas.create_line(930, 350, 270, 350, fill="black", width=2)

        opp = ImageTk.PhotoImage(Image.open("pngwing.com (112).png").resize((250, 340)))
        opp_label = Label(frame, image=opp, bg='white')
        opp_label.image = opp
        opp_label.place(x=475, y=9, height=340)

        roulette = ImageTk.PhotoImage(Image.open("pngwing.com (5).png").resize((90, 120)))
        canvas.create_image(600, 550, image=roulette)
        canvas.image = opp, roulette

        img1 = Image.open("3039404.png").resize((35, 35))
        photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open("ff.png").resize((46, 41))
        photo2 = ImageTk.PhotoImage(img2)
        current_state = {"image": 1}
        btn = Button(frame, image=photo1, borderwidth=0, activebackground='white', bg='white',
                     command=lambda: game.toggle_image1(current_state, btn, photo2, photo1))
        btn.image = photo1
        btn.place(x=200, y=33)
        img2_a = Image.open("pngwing.com.png").resize((40, 40))
        photo1_a = ImageTk.PhotoImage(img2_a)
        img2_b = Image.open("gg.png").resize((53, 48))
        photo2_b = ImageTk.PhotoImage(img2_b)
        current_state2 = {"current": 1}
        btn2 = Button(frame, image=photo1_a, activebackground='white',
                      command=lambda: game.toggle_image21(current_state2, btn2, photo1_a, photo2_b), borderwidth=0,
                      bg='white')
        btn2.image = photo1_a
        btn2.place(x=260, y=30)

        image3 = Image.open("pngwing.com (11).png")
        image3 = image3.resize((50, 50))
        photo3 = ImageTk.PhotoImage(image3)
        label3 = Label(root, image=photo3, bg='white')
        label3.image = photo3
        btn3 = Button(frame, image=photo3, borderwidth=0, activebackground='white', bg='white', command=main_menu)
        btn3.place(x=320, y=25)

        canvas.create_line(30, 25, 30, 85, fill="black", width=1)
        canvas.create_line(30, 25, 95, 25, fill="black", width=1)
        canvas.create_line(95, 25, 95, 85, fill="black", width=1)
        canvas.create_line(30, 85, 95, 85, fill="black", width=1)
        title1 = Label(frame, text='1 ИГРОК', bg='white', font=("Arial", 13))
        title1.place(x=61, y=16, relwidth=0.07, relheight=0.02, anchor="center")

        canvas.create_line(120, 25, 120, 85, fill="black", width=1)
        canvas.create_line(120, 25, 185, 25, fill="black", width=1)
        canvas.create_line(185, 25, 185, 85, fill="black", width=1)
        canvas.create_line(120, 85, 185, 85, fill="black", width=1)
        title2 = Label(frame, text='2 ИГРОК', bg='white', font=("Arial", 13))
        title2.place(x=153, y=16, relwidth=0.07, relheight=0.02, anchor="center")

        def opp_shot():
            global player, a, rating_1, rating_2
            if player == 1:
                if a <= (canvas.drum_state + 1):
                    print('1 Игрок победил, 2 Игрок проиграл')
                    if rating_1!=98:
                        rating_1+=1
                    else:
                        rating_1=0
                    title3.config(text=rating_1)
                else:
                    opp_img2 = ImageTk.PhotoImage(Image.open("pngwing.com (113).png").resize((250, 340)))
                    opp_label.config(image=opp_img2)
                    opp_label.image = opp_img2
                    player = 2
            else:
                if a <= (canvas.drum_state + 1):
                    print('1 Игрок проиграл, 2 Игрок выиграл')
                    if rating_2!=98:
                        rating_2+=1
                    else:
                        rating_2=0
                    title4.config(text=rating_2)
                else:
                    opp_img1 = ImageTk.PhotoImage(Image.open("pngwing.com (112).png").resize((250, 340)))
                    opp_label.config(image=opp_img1)
                    opp_label.image = opp_img1
                    player = 1
            a = random.randint(1, 6)

        def shot():
            global a, rating_1, rating_2
            if a <= (canvas.drum_state + 1):
                if player == 1:
                    print('1 Игрок проиграл, 2 Игрок выиграл')
                    if rating_2!=98:
                        rating_2+=1
                    else: rating_2=0
                    title4.config(text=rating_2)
                else:
                    print('1 Игрок выиграл, 2 Игрок проиграл')
                    if rating_1!=99:
                        rating_1+=1
                    else: rating_1=0
                    title3.config(text=rating_1)
            a = random.randint(1, 6)


        btn5 = Button(frame, text='ВЫСТРЕЛИТЬ В ПРОТИВНИКА', font=("Arial", 15), command=opp_shot)
        btn5.place(relx=0.18, rely=0.85, relwidth=0.27, relheight=0.13)
        btn4 = Button(frame, text='ВЫСТРЕЛИТЬ В СЕБЯ', font=("Arial", 15), command=shot)
        btn4.place(relx=0.55, rely=0.85, relwidth=0.27, relheight=0.13)

    def toggle_image1(s, q, photo2, photo1):
        global current_state
        global btn
        current_state = s
        btn = q
        if s["image"] == 1:
            btn.config(image=photo2)
            btn.image = photo2
            btn.place(x=195.6, y=28)
            current_state["image"] = 2
        else:
            btn.config(image=photo1)
            btn.image = photo1
            btn.place(x=200, y=33)
            current_state["image"] = 1

    def toggle_image21(s, q, photo1_a, photo2_b):
        global current_state2
        global btn
        current_state2 = s
        btn2 = q
        if s["current"] == 1:
            btn2.config(image=photo2_b)
            btn2.image = photo2_b
            btn2.place(x=253, y=25)
            current_state2["current"] = 2
        else:
            btn2.config(image=photo1_a)
            btn2.image = photo1_a
            btn2.place(x=260, y=30)
            current_state2["current"] = 1

    def shotgun_1():
        clear_window()
        global blank_patron, n, life_1, life_2, a, rating_1
        life_1=3
        rating_1=0
        life_2=3
        blank_patron = 3
        n=5
        a = random.randint(1, n)
        title3 = Label(frame, text=rating_1, bg='white', font=("Arial", 25))
        title3.place(x=62, y=53, relwidth=0.03, relheight=0.05, anchor="center")

        canvas.create_line(150, 800, 270, 350, fill="black", width=2)
        canvas.create_line(1050, 800, 930, 350, fill="black", width=2)
        canvas.create_line(930, 350, 270, 350, fill="black", width=2)
        heart = ImageTk.PhotoImage(Image.open("pngwing.com (1).png").resize((50, 50)))
        canvas.create_image(1150, 40, image=heart)
        canvas.create_image(1090, 40, image=heart)
        canvas.create_image(1030, 40, image=heart)

        opp = ImageTk.PhotoImage(Image.open("pngwing.com (111).png").resize((350, 300)))
        canvas.create_image(570, 239, image=opp)

        shotgun = ImageTk.PhotoImage(Image.open("pngwing.com (6).png").resize((240, 130)))
        canvas.create_image(600, 550, image=shotgun)
        canvas.image = opp, shotgun,heart

        img1 = Image.open("3039404.png").resize((35, 35))
        photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open("ff.png").resize((46, 41))
        photo2 = ImageTk.PhotoImage(img2)
        current_state = {"image": 1}
        btn = Button(frame, image=photo1, borderwidth=0, activebackground='white', bg='white',
                     command=lambda: game.toggle_image(current_state, btn, photo2, photo1))
        btn.image = photo1
        btn.place(x=110, y=33)
        img2_a = Image.open("pngwing.com.png").resize((40, 40))
        photo1_a = ImageTk.PhotoImage(img2_a)
        img2_b = Image.open("gg.png").resize((53, 48))
        photo2_b = ImageTk.PhotoImage(img2_b)
        current_state2 = {"current": 1}
        btn2 = Button(frame, image=photo1_a, activebackground='white',
                      command=lambda: game.toggle_image2(current_state2, btn2, photo1_a, photo2_b), borderwidth=0,
                      bg='white')
        btn2.image = photo1_a
        btn2.place(x=170, y=30)

        image3 = Image.open("pngwing.com (11).png")
        image3 = image3.resize((50, 50))
        photo3 = ImageTk.PhotoImage(image3)
        label3 = Label(root, image=photo3, bg='white')
        label3.image = photo3
        btn3 = Button(frame, image=photo3, borderwidth=0, activebackground='white', bg='white', command=main_menu)
        btn3.place(x=230, y=25)

        canvas.create_line(30, 25, 30, 85, fill="black", width=1)
        canvas.create_line(30, 25, 95, 25, fill="black", width=1)
        canvas.create_line(95, 25, 95, 85, fill="black", width=1)
        canvas.create_line(30, 85, 95, 85, fill="black", width=1)
        title1 = Label(frame, text='1 ИГРОК', bg='white', font=("Arial", 13))
        title1.place(x=61, y=16, relwidth=0.3, relheight=0.02, anchor="center")

        def opp_shot():
            global n, a, rating_1, blank_patron, life_1, life_2
            if a > blank_patron:
                print('Противник потерял 1 жизнь')
                n -= 1
                life_2 -= 1
                if n == 0:
                    blank_patron = random.randint(1, 5)
                    print('В дробовике', blank_patron, 'холостых патронов')
                    n = 5

                a = random.randint(1, n)
                b = random.randint(1, 2)
                if (a > blank_patron) and (life_2!=0):
                    if b==1:
                        print('Вы потеряли 1 жизнь')
                        life_1-=1
                        n-=1
                    else:
                        print('Противник потерял 1 жизнь')
                        life_2 -= 1
                        n-=1
                else:
                    if life_2==0:
                        print('Противник проиграл')
                        life_1 = 3
                        life_2 = 3
                        n=5
                        blank_patron=3
                        if rating_1 != 98:
                            rating_1 += 1
                        else:
                            rating_1 = 0
                        title3.config(text=rating_1)
                    else:
                        print('холостой')
                        blank_patron -= 1
                        n-=1
                        print(blank_patron)
            else:
                print('холостой')
                blank_patron -= 1
                n -= 1
                print(blank_patron)

            if (n==0) and (life_2!=0) and (life_1!=0):
                blank_patron = random.randint(1,5)
                print('В дробовике', blank_patron, 'холостых патронов')
                n = 5
            if life_2 == 0:
                if rating_1 != 98:
                    rating_1 += 1
                else:
                    rating_1 = 0
                title3.config(text=rating_1)
                print('Противник проиграл')
                life_1 = 3
                life_2 = 3
                n = 5
                blank_patron = 3

            if life_1 == 0:
                print('Вы проиграли')
                life_1 = 3
                life_2 = 3
                n = 5
                blank_patron = 3

            a = random.randint(1, n)

        def shot():
            global a, blank_patron, life_1, life_2, n
            if a > blank_patron:
                print('Вы потеряли 1 жизнь')
                life_1 -= 1
                n -= 1
                if life_1 == 0:
                    print('Вы проиграли')
                    life_1 = 3
                    life_2 = 3
                    n = 5
                    blank_patron = 3
                    a = random.randint(1, n)
                    return
                if n == 0:
                    blank_patron = random.randint(1, 5)
                    print('В дробовике', blank_patron, 'холостых патронов')
                    n = 5
                a = random.randint(1, n)
                b = random.randint(1, 2)
                if a > blank_patron:
                    if b == 1:
                        print('Вы потеряли 1 жизнь')
                        life_1 -= 1
                        n -= 1
                        if life_1 == 0:
                            print('Вы проиграли')
                            life_1 = 3
                            life_2 = 3
                            n = 5
                            blank_patron = 3
                    else:
                        print('Противник потерял 1 жизнь')
                        n -= 1
                        life_2 -= 1
                        if life_2 == 0:
                            print('Вы проиграли')
                            life_1 = 3
                            life_2 = 3
                            n = 5
                            blank_patron = 3
                            if rating_1 != 98:
                                rating_1 += 1
                            else:
                                rating_1 = 0
                            title3.config(text=rating_1)
            else:
                print('холостой')
                blank_patron -= 1
                n -= 1
                print(blank_patron)
            if (n==0) and (life_1!=0) and (life_2 != 0):
                blank_patron = random.randint(1, 5)
                print('В дробовике', blank_patron, 'холостых патронов')
                n = 5
            a = random.randint(1, n)

        btn5 = Button(frame, text='ВЫСТРЕЛИТЬ В ПРОТИВНИКА', font=("Arial", 15), command=opp_shot)
        btn5.place(relx=0.18, rely=0.85, relwidth=0.27, relheight=0.13)
        btn4 = Button(frame, text='ВЫСТРЕЛИТЬ В СЕБЯ', font=("Arial", 15), command=shot)
        btn4.place(relx=0.55, rely=0.85, relwidth=0.27, relheight=0.13)


    def shotgun_2():
        clear_window()
        global player, n, a, rating_1, rating_2, blank_patron, life_1, life_2
        life_1 = 3
        rating_1 = 0
        rating_2=0
        life_2 = 3
        blank_patron = 3
        n = 5
        player=1
        a = random.randint(1, n)
        title3 = Label(frame, text=rating_1, bg='white', font=("Arial", 25))
        title3.place(x=62, y=53, relwidth=0.03, relheight=0.05, anchor="center")
        title4 = Label(frame, text=rating_2, bg='white', font=("Arial", 25))
        title4.place(x=152.5, y=54, relwidth=0.04, relheight=0.05, anchor="center")

        canvas.create_line(150, 800, 270, 350, fill="black", width=2)
        canvas.create_line(1050, 800, 930, 350, fill="black", width=2)
        canvas.create_line(930, 350, 270, 350, fill="black", width=2)
        heart = ImageTk.PhotoImage(Image.open("pngwing.com (1).png").resize((50, 50)))
        canvas.create_image(1150, 40, image=heart)
        canvas.create_image(1090, 40, image=heart)
        canvas.create_image(1030, 40, image=heart)

        opp = ImageTk.PhotoImage(Image.open("pngwing.com (112).png").resize((250, 340)))
        opp_label = Label(frame, image=opp, bg='white')
        opp_label.image = opp
        opp_label.place(x=475, y=9, height=340)

        shotgun = ImageTk.PhotoImage(Image.open("pngwing.com (6).png").resize((240, 130)))
        canvas.create_image(600, 550, image=shotgun)
        canvas.image = opp, shotgun, heart

        img1 = Image.open("3039404.png").resize((35, 35))
        photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open("ff.png").resize((46, 41))
        photo2 = ImageTk.PhotoImage(img2)
        current_state = {"image": 1}
        btn = Button(frame, image=photo1, borderwidth=0, activebackground='white', bg='white',
                     command=lambda: game.toggle_image1(current_state, btn, photo2, photo1))
        btn.image = photo1
        btn.place(x=200, y=33)
        img2_a = Image.open("pngwing.com.png").resize((40, 40))
        photo1_a = ImageTk.PhotoImage(img2_a)
        img2_b = Image.open("gg.png").resize((53, 48))
        photo2_b = ImageTk.PhotoImage(img2_b)
        current_state2 = {"current": 1}
        btn2 = Button(frame, image=photo1_a, activebackground='white',
                      command=lambda: game.toggle_image21(current_state2, btn2, photo1_a, photo2_b), borderwidth=0,
                      bg='white')
        btn2.image = photo1_a
        btn2.place(x=260, y=30)

        image3 = Image.open("pngwing.com (11).png")
        image3 = image3.resize((50, 50))
        photo3 = ImageTk.PhotoImage(image3)
        label3 = Label(root, image=photo3, bg='white')
        label3.image = photo3
        btn3 = Button(frame, image=photo3, borderwidth=0, activebackground='white', bg='white', command=main_menu)
        btn3.place(x=320, y=25)

        canvas.create_line(30, 25, 30, 85, fill="black", width=1)
        canvas.create_line(30, 25, 95, 25, fill="black", width=1)
        canvas.create_line(95, 25, 95, 85, fill="black", width=1)
        canvas.create_line(30, 85, 95, 85, fill="black", width=1)
        title1 = Label(frame, text='1 ИГРОК', bg='white', font=("Arial", 13))
        title1.place(x=61, y=16, relwidth=0.07, relheight=0.02, anchor="center")

        canvas.create_line(120, 25, 120, 85, fill="black", width=1)
        canvas.create_line(120, 25, 185, 25, fill="black", width=1)
        canvas.create_line(185, 25, 185, 85, fill="black", width=1)
        canvas.create_line(120, 85, 185, 85, fill="black", width=1)
        title2 = Label(frame, text='2 ИГРОК', bg='white', font=("Arial", 13))
        title2.place(x=153, y=16, relwidth=0.07, relheight=0.02, anchor="center")


        def opp_shot():
            global n, a, rating_1, blank_patron, life_1, life_2, player, rating_2
            if player==1:
                if a > blank_patron:
                    print('Игрок 2 потерял 1 жизнь')
                    print()
                    n -= 1
                    life_2 -= 1
                else:
                    print('холостой')
                    blank_patron -= 1
                    n -= 1
                    print(blank_patron)
                opp_img2 = ImageTk.PhotoImage(Image.open("pngwing.com (113).png").resize((250, 340)))
                opp_label.config(image=opp_img2)
                opp_label.image = opp_img2
                player=2
            else:
                if a > blank_patron:
                    print('Игрок 1 потерял 1 жизнь')
                    print()
                    n -= 1
                    life_1 -= 1
                    if n == 0:
                        blank_patron = random.randint(1, 5)
                        print('В дробовике', blank_patron, 'холостых патронов')
                        n = 5
                else:
                    print('холостой')
                    blank_patron -= 1
                    n -= 1
                    print(blank_patron)
                opp_img2 = ImageTk.PhotoImage(Image.open("pngwing.com (112).png").resize((250, 340)))
                opp_label.config(image=opp_img2)
                opp_label.image = opp_img2
                player=1

            if (n == 0) and (life_2 != 0) and (life_1 != 0):
                blank_patron = random.randint(1, 5)
                print('В дробовике', blank_patron, 'холостых патронов')
                n = 5
            if life_2 == 0:
                if rating_1 != 98:
                    rating_1 += 1
                else:
                    rating_1 = 0
                title3.config(text=rating_1)
                print('Игрок 1 выиграл, игрок 2 проиграл')
                life_1 = 3
                life_2 = 3
                n = 5
                blank_patron = 3

            if life_1 == 0:
                print('Игрок 1 проиграл, 2 игрок выиграл')
                life_1 = 3
                life_2 = 3
                n = 5
                blank_patron = 3
                if rating_2 != 98:
                    rating_2 += 1
                else:
                    rating_2 = 0
                title4.config(text=rating_2)

            a = random.randint(1, n)

        def shot():
            global a, blank_patron, life_1, life_2, n, rating_1, rating_2, player
            if player==1:
                if a > blank_patron:
                    print('Игрок 1 потерял 1 жизнь')
                    life_1 -= 1
                    n -= 1
                    opp_img2 = ImageTk.PhotoImage(Image.open("pngwing.com (113).png").resize((250, 340)))
                    opp_label.config(image=opp_img2)
                    opp_label.image = opp_img2
                    player=2
                else:
                    print('холостой')
                    blank_patron -= 1
                    n -= 1
                    print(blank_patron)
            else:
                if a > blank_patron:
                    print('Игрок 2 потерял 1 жизнь')
                    life_2 -= 1
                    n -= 1
                    opp_img2 = ImageTk.PhotoImage(Image.open("pngwing.com (112).png").resize((250, 340)))
                    opp_label.config(image=opp_img2)
                    opp_label.image = opp_img2
                    player=1
                else:
                    print('холостой')
                    blank_patron -= 1
                    n -= 1
                    print(blank_patron)

            if (n==0) and (life_1!=0) and (life_2 != 0):
                blank_patron = random.randint(1, 5)
                print('В дробовике', blank_patron, 'холостых патронов')
                n = 5
            if life_2 == 0:
                if rating_1 != 98:
                    rating_1 += 1
                else:
                    rating_1 = 0
                title3.config(text=rating_1)
                print('Игрок 1 выиграл, игрок 2 проиграл')
                life_1 = 3
                life_2 = 3
                n = 5
                blank_patron = 3

            if life_1 == 0:
                print('Игрок 1 проиграл, 2 игрок выиграл')
                life_1 = 3
                life_2 = 3
                n = 5
                blank_patron = 3
                if rating_2 != 98:
                    rating_2 += 1
                else:
                    rating_2 = 0
                title4.config(text=rating_2)
            a = random.randint(1, n)


        btn5 = Button(frame, text='ВЫСТРЕЛИТЬ В ПРОТИВНИКА', font=("Arial", 15), command=opp_shot)
        btn5.place(relx=0.18, rely=0.85, relwidth=0.27, relheight=0.13)
        btn4 = Button(frame, text='ВЫСТРЕЛИТЬ В СЕБЯ', font=("Arial", 15), command=shot)
        btn4.place(relx=0.55, rely=0.85, relwidth=0.27, relheight=0.13)




class settings:
    def settings():
        clear_window()
        img1 = Image.open("3039404.png").resize((170, 170))
        photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open("ff.png").resize((220, 200))
        photo2 = ImageTk.PhotoImage(img2)
        current_state = {"image": 1}
        btn = Button(frame, image=photo1, borderwidth=0, activebackground='white', bg='white', command=lambda: settings.toggle_image(current_state, btn, photo2, photo1))
        btn.image = photo1
        btn.place(x=300, y=320)
        img2_a = Image.open("pngwing.com.png").resize((195, 195))
        photo1_a = ImageTk.PhotoImage(img2_a)
        img2_b = Image.open("gg.png").resize((253, 230))
        photo2_b = ImageTk.PhotoImage(img2_b)
        current_state2 = {"current": 1}
        btn2 = Button(frame, image=photo1_a, activebackground='white', command=lambda: settings.toggle_image2(current_state2, btn2, photo1_a, photo2_b), borderwidth=0, bg='white')
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
    btn3 = Button(frame, text='НАСТРОЙКИ', font=("Arial", 15),command=settings.settings)
    btn3.place(relx=0.38, rely=0.5, relwidth=0.24)
    btn4 = Button(frame, text='ВЫХОД', font=("Arial", 15), command=exit)
    btn4.place(relx=0.38, rely=0.57, relwidth=0.24)
main_menu()

root.mainloop()