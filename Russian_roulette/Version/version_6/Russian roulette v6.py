from tkinter import *
import time
import sys
import pyaudio
import wave
import threading
import tkinter as tk
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
current_state = 1
current_state2 = 1
m=1

def clear_window():
    for widget in frame.winfo_children():
        if widget != canvas:
            widget.destroy()
    canvas.delete("all")



def rule():
    play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
    clear_window()
    title = Label(frame, text='ПРАВИЛА ИГРЫ',  bg='white', font=("Arial", 20))
    title.place(relx=0.5, rely=0.22, relwidth=0.2, relheight=0.03, anchor="center")
    rules = Label(
        frame,
        text=(
            "Цель – отнять все жизни противника.\n"
            "Перед игрой вам предлагается выбрать режимы: выбор количества игроков\n(«1 игрок» или «2 игрока») "
            "и выбор оружия («Револьвер» или «Дробовик»).\n"
            "При выборе револьвера у каждого по 1 жизни.\nПри выборе дробовика у каждого по 3 жизни.\n"
            "В зависимости от количества патронов в барабане револьвера будет меняться шанс выстрела. Он заполняется перестаскиванием патронов.\n"
            "Чтобы достать патрон, нужно перетащить патрон из барабана.\n"
            "Дробовик имеет 5 патронов, в первой зарядке 3 холостых. После перезарядки показывается окно с числом холостых патронов.\n\n"
            "«ВЫСТРЕЛИТЬ В СЕБЯ»: если выстрела нет, то игрок получает дополнительный ход. Иначе — игрок теряет жизнь, и ход переходит противнику.\n"
            "«ВЫСТРЕЛИТЬ В ПРОТИВНИКА»: если срабатывает выстрел, противник теряет жизнь. Ход переходит к противнику.\n"
            "Победа — у противника 0 жизней.\n"
            "Поражение — у игрока 0 жизней.\n"
            "Рейтинг увеличивается за каждую победу. Максимум — 99. При следующем увеличении или при выходе в меню рейтинг сбрасывается до 0."
        ),
        bg='white',
        font=("Arial", 13),
        justify=LEFT,
        wraplength=635
    )
    image = Image.open("Images\\pngwing.com (11).png")
    image = image.resize((50, 50))
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo, bg='white')
    label.image = photo
    btn = Button(frame, image=photo, activebackground='white', borderwidth=0, bg='white', command=main_menu)
    btn.place(x=284, y=585)
    rules.place(relx=0.225, rely=0.25, relwidth=0.55, relheight=0.47)
    canvas.create_line(259, 138, 259, 650, fill="black", width=1)
    canvas.create_line(259, 650, 941, 650, fill="black", width=1)
    canvas.create_line(941, 138, 941, 650, fill="black", width=1)
    canvas.create_line(259, 138, 941, 138, fill="black", width=1)


class modes:
    def modes_1():
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
        clear_window()
        global mode_players, mode_firearm
        mode_firearm = 0
        mode_players = 0
        title = Label(frame, text='КОЛИЧЕСТВО ИГРОКОВ', bg='white', font=("Arial", 20))
        title.place(relx=0.5, rely=0.075, relwidth=0.3, relheight=0.03, anchor="center")
        img1 = Image.open("Images\\1.png").resize((75, 90))
        photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open("Images\\111.png").resize((75, 90))
        photo2 = ImageTk.PhotoImage(img2)
        current_state3 = 1
        btn = Button(frame, image=photo1, borderwidth=0, activebackground='white', bg='white', command=lambda: modes.toggle_image(current_state3, current_state4, btn, photo2, btn2, photo1_a))
        btn.image = photo1
        btn.place(x=400, y=130)
        img2_a = Image.open("Images\\2.png").resize((75, 90))
        photo1_a = ImageTk.PhotoImage(img2_a)
        img2_b = Image.open("Images\\22.png").resize((75, 90))
        photo2_b = ImageTk.PhotoImage(img2_b)
        current_state4 = 1
        btn2 = Button(frame, image=photo1_a, activebackground='white',  command=lambda: modes.toggle_image2(current_state4,current_state3, btn2, photo2_b, btn, photo1), borderwidth=0, bg='white')
        btn2.image = photo1_a
        btn2.place(x=725, y=130)
        image3 = Image.open("Images\\pngwing.com (11).png")
        image3 = image3.resize((60, 60))
        photo3 = ImageTk.PhotoImage(image3)
        label3 = Label(root, image=photo3, bg='white')
        label3.image = photo3
        btn3 = Button(frame, image=photo3,activebackground='white',  borderwidth=0, bg='white', command=main_menu)
        btn3.place(x=20, y=725)

        title1 = Label(frame, text='ВЫБОР ОРУЖИЯ', bg='white', font=("Arial", 20))
        title1.place(relx=0.5, rely=0.4, relwidth=0.3, relheight=0.03, anchor="center")
        img11 = Image.open("Images\\pngwing.com (5).png").resize((90, 120))
        photo11 = ImageTk.PhotoImage(img11)
        img21 = Image.open("Images\\pngwing.com (5)_1.png").resize((90, 120))
        photo21 = ImageTk.PhotoImage(img21)
        current_state1 = 1
        img2_a1 = Image.open("Images\\pngwing.com (6).png").resize((240, 130))
        photo1_a1 = ImageTk.PhotoImage(img2_a1)
        img2_b1 = Image.open("Images\\pngwing.com (6)_1.png").resize((240, 130))
        photo2_b1 = ImageTk.PhotoImage(img2_b1)
        current_state21 = 1
        btn1 = Button(frame, image=photo11, borderwidth=0, activebackground='white', bg='white', command=lambda: modes.toggle_image1(current_state1, current_state21, btn1, photo21, btn21, photo1_a1))
        btn1.image = photo1
        btn1.place(x=380, y=400)
        btn21 = Button(frame, image=photo1_a1, activebackground='white', command=lambda: modes.toggle_image21(current_state21, current_state1, btn21, photo2_b1, btn1, photo11), borderwidth=0, bg='white')
        btn21.image = photo1_a1
        btn21.place(x=665, y=400)

        image4 = Image.open("Images\\pngwing.png")
        image4 = image4.resize((110, 110))
        photo4 = ImageTk.PhotoImage(image4)
        label4 = Label(root, image=photo4, bg='white')
        label4.image = photo4
        btn4 = Button(frame, image=photo4, activebackground='white', borderwidth=0, bg='white', command=lambda: modes.modes_2(mode_firearm, mode_players))
        btn4.place(x=1050, y=690)

    def toggle_image(s, sq, q, photo2, qq, photo1_a):
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
        global mode_players
        global current_state3
        global current_state4
        global btn
        global btn2
        btn2 = qq
        current_state4 = sq
        current_state3 = s
        btn = q
        if s == 1:
            btn.config(image=photo2)
            btn.image = photo2
            current_state3 = 2
            btn2.config(image=photo1_a)
            btn2.image = photo1_a
            current_state4 = 1
            mode_players=1
    def toggle_image2(s, sq, q, photo2_b, qq, photo1):
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
        global current_state4, current_state3
        global btn2
        global btn
        global mode_players
        btn = qq
        current_state3 = sq
        current_state4 = s
        btn2 = q
        if s == 1:
            btn2.config(image=photo2_b)
            btn2.image = photo2_b
            current_state4 = 2
            btn.config(image=photo1)
            btn.image = photo1
            current_state3 = 1
            mode_players = 2

    def toggle_image1(s, sq, q, photo21, qq, photo1_a1):
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
        global current_state1
        global current_state21
        global btn1
        global btn21
        global mode_firearm
        btn21 = qq
        current_state21 = sq
        current_state1 = sq
        btn1 = q
        if s == 1:
            btn1.config(image=photo21)
            btn1.image = photo21
            current_state1 = 2
            btn21.config(image=photo1_a1)
            btn21.image = photo1_a1
            current_state21 = 1
            mode_firearm = 1

    def toggle_image21(s, sq, q, photo2_b1, qq, photo11):
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
        global current_state21, current_state1
        global btn21
        global btn1
        global mode_firearm
        btn1 = qq
        current_state1 = sq
        current_state21 = s
        btn21 = q
        if s == 1:
            btn21.config(image=photo2_b1)
            btn21.image = photo2_b1
            current_state21 = 2
            btn1.config(image=photo11)
            btn1.image = photo11
            current_state1 = 1
        mode_firearm = 2
    def modes_2(q,qq):
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
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
        image5 = Image.open("Images\\pngwing.com (11).png")
        image5 = image5.resize((60, 60))
        photo5 = ImageTk.PhotoImage(image5)
        label5 = Label(root, image=photo5, bg='white')
        label5.image = photo5
        btn5 = Button(frame, image=photo5, activebackground='white', borderwidth=0, bg='white', command=main_menu)
        btn5.place(x=20, y=725)
        image6 = Image.open("Images\\pngwing.png")
        image6 = image6.resize((110, 110))
        photo6 = ImageTk.PhotoImage(image6)
        label6 = Label(root, image=photo6, bg='white')
        label6.image = photo6
        btn6 = Button(frame, image=photo6, activebackground='white', borderwidth=0, bg='white', command= modes.modes3_roulette)
        btn6.place(x=1050, y=690)
        title = Label(frame, text='КОЛИЧЕСТВО ПАТРОНОВ', bg='white', font=("Arial", 25))
        title.place(relx=0.5, rely=0.05, relwidth=0.6, relheight=0.04, anchor="center")
        patron_img = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (8).png").resize((180, 180)))
        drum_imgs = [ImageTk.PhotoImage(Image.open("Images\\pngwing.com-_7_1.bmp").resize((310, 310))),
            ImageTk.PhotoImage(Image.open("Images\\pngwing.com-_7_2.bmp").resize((310, 310))),
            ImageTk.PhotoImage(Image.open("Images\\pngwing.com-_7_3.bmp").resize((310, 310))),
            ImageTk.PhotoImage(Image.open("Images\\pngwing.com-_7_4.bmp").resize((310, 310))),
            ImageTk.PhotoImage(Image.open("Images\\pngwing.com-_7_5.bmp").resize((310, 310)))]
        drum = canvas.create_image(250, 390, image=drum_imgs[0])
        canvas.drum_imgs = drum_imgs
        canvas.drum_state = 0
        patrons = []
        start_positions = [(700, 400), (800, 400), (900, 400), (1000, 400)]
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
                    play_once("Sounds\\korotkiy-grubyiy-nizkiy-zvuk.wav")
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
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
        clear_window()
        global a, title3, rating_1, life_2
        a = random.randint(1, 6)
        life_2 = 1
        rating_1=0
        title3 = Label(frame, text=rating_1, bg='white', font=("Arial", 25))
        title3.place(x=62, y=53, relwidth=0.03, relheight=0.05, anchor="center")

        canvas.create_line(150, 800, 270, 350, fill="black", width=2)
        canvas.create_line(1050, 800, 930, 350, fill="black", width=2)
        canvas.create_line(930, 350, 270, 350, fill="black", width=2)

        opp = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (111).png").resize((350, 300)))
        canvas.create_image(570, 239, image=opp)

        roulette = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (5).png").resize((90, 120)))
        canvas.create_image(600, 550, image=roulette)
        canvas.image = opp,roulette

        img1 = Image.open("Images\\3039404.png").resize((35, 35))
        photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open("Images\\ff.png").resize((46, 41))
        photo2 = ImageTk.PhotoImage(img2)
        if current_state == 1:
            btn = Button(frame, image=photo1, borderwidth=0, activebackground='white', bg='white', command=lambda: game.toggle_image(current_state, btn, photo2, photo1))
            btn.image = photo1
            btn.place(x=110, y=33)
        else:
            btn = Button(frame, image=photo2, borderwidth=0, activebackground='white', bg='white',
                         command=lambda: game.toggle_image(current_state, btn, photo2, photo1))
            btn.image = photo2
            btn.place(x=105.6, y=28)
        img2_a = Image.open("Images\\pngwing.com.png").resize((40, 40))
        photo1_a = ImageTk.PhotoImage(img2_a)
        img2_b = Image.open("Images\\gg.png").resize((53, 48))
        photo2_b = ImageTk.PhotoImage(img2_b)
        if current_state2 == 1:
            btn2 = Button(frame, image=photo1_a, activebackground='white', command=lambda: game.toggle_image2(current_state2, btn2, photo1_a, photo2_b), borderwidth=0,bg='white')
            btn2.image = photo1_a
            btn2.place(x=170, y=30)
        else:
            btn2 = Button(frame, image=photo2_b, activebackground='white',
                          command=lambda: game.toggle_image2(current_state2, btn2, photo1_a, photo2_b), borderwidth=0,
                          bg='white')
            btn2.image = photo2_b
            btn2.place(x=163, y=25)
        image3 = Image.open("Images\\pngwing.com (11).png")
        image3 = image3.resize((50, 50))
        photo3 = ImageTk.PhotoImage(image3)
        label3 = Label(root, image=photo3, bg='white')
        label3.image = photo3
        btn3 = Button(frame, image=photo3, borderwidth=0, activebackground='white', bg='white', command=main_menu)
        btn3.place(x=230, y=25)

        image4 = Image.open("Images\\pngwing.com (11).png")
        image4 = image4.resize((200, 200))
        photo4 = ImageTk.PhotoImage(image4)
        label4 = Label(root, image=photo4, bg='white')
        label4.image = photo4

        image5 = Image.open("Images\\pngwing.com (2).png")
        image5 = image5.resize((200, 200))
        photo5 = ImageTk.PhotoImage(image5)
        label5 = Label(root, image=photo5, bg='white')
        label5.image = photo5

        canvas.create_line(30, 25, 30, 85, fill="black", width=1)
        canvas.create_line(30, 25, 95, 25, fill="black", width=1)
        canvas.create_line(95, 25, 95, 85, fill="black", width=1)
        canvas.create_line(30, 85, 95, 85, fill="black", width=1)
        title1 = Label(frame, text='1 ИГРОК', bg='white', font=("Arial", 13))
        title1.place(x=61, y=16, relwidth=0.3, relheight=0.02, anchor="center")



        def result():
            global life_2
            dimmer = tk.Frame(root, bg="white")
            dimmer.place(relx=0, rely=0, relwidth=1, relheight=1)
            window = tk.Frame(dimmer, bg="white", bd=1, relief="solid")
            window.place(relx=0.12, rely=0.14, relwidth=0.76, relheight=0.7)


            if life_2 == 0:
                play_once("Sounds\\game-won.wav")
                tk.Label(window, text="ВЫ ВЫИГРАЛИ!", font=("Arial", 30), bg="white").place(relx=0.12, rely=0.12, relwidth=0.76, relheight=0.09)
                life_2 += 1
            else:
                play_once("Sounds\\02c25f2abdd7bbb.wav")
                tk.Label(window, text="ВЫ ПРОИГРАЛИ!", font=("Arial", 30), bg="white").place(relx=0.12, rely=0.12, relwidth=0.76, relheight=0.09)

            btn8 = Button(window, image=photo5, activebackground='white', borderwidth=0, bg='white',
                          command=dimmer.destroy)
            btn8.place(x=140, y=300)
            btn10 = Button(window, image=photo4, activebackground='white', borderwidth=0, bg='white',
                           command=lambda: [dimmer.destroy(), main_menu()])
            btn10.place(x=600, y=300)

        def shoot():
            play_once("Sounds\\b05e1ac8be34248.wav")
            global overlay
            overlay = tk.Canvas(root, bg="white", highlightthickness=0)
            overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
            root.after(800, overlay.place_forget)
            root.after(800, lambda: result())

        def opp_shot():
            play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
            global a, rating_1, life_2
            if a>(canvas.drum_state+1):
                a = random.randint(1, 6)
                b = random.randint(1, 2)
                if a <= (canvas.drum_state + 1):
                    if b==1:
                        shoot()
                    else:
                        life_2 -= 1
                        shoot()
                        if rating_1 != 99:
                            rating_1 += 1
                        else:
                            rating_1 = 0
                        title3.config(text=rating_1)
            else:
                life_2 -= 1
                shoot()
                if rating_1 != 99:
                    rating_1 += 1
                else:
                    rating_1 = 0
                title3.config(text=rating_1)
            a = random.randint(1, 6)
        def shot():
            play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
            global a, life_2
            if a <= (canvas.drum_state + 1):
                shoot()
            a = random.randint(1, 6)

        btn5 = Button(frame, text='ВЫСТРЕЛИТЬ В ПРОТИВНИКА', font=("Arial", 15), command=opp_shot)
        btn5.place(relx=0.18, rely=0.85, relwidth=0.27, relheight=0.13)
        btn4 = Button(frame, text='ВЫСТРЕЛИТЬ В СЕБЯ', font=("Arial", 15), command=shot)
        btn4.place(relx=0.55, rely=0.85, relwidth=0.27, relheight=0.13)

    def toggle_image(s, q, photo2, photo1):
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
        global current_state, stop_flag, loop_thread, btn
        current_state = s
        btn = q
        if s == 1:
            stop_flag = True
            btn.config(image=photo2)
            btn.image = photo2
            btn.place(x=105.6, y=28)
            current_state = 2
        else:
            stop_flag = False
            loop_thread = threading.Thread(target=loop_sound, args=("Sounds\\pixelated-love-20240608-171951.wav",), daemon=True)
            loop_thread.start()
            btn.config(image=photo1)
            btn.image = photo1
            btn.place(x=110, y=33)
            current_state = 1

    def toggle_image2(s, q, photo1_a, photo2_b):
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
        global current_state2, play_sound, btn
        current_state2 = s
        btn2 = q
        if s == 1:
            play_sound = False
            btn2.config(image=photo2_b)
            btn2.image = photo2_b
            btn2.place(x=163, y=25)
            current_state2 = 2
        else:
            play_sound = True
            btn2.config(image=photo1_a)
            btn2.image = photo1_a
            btn2.place(x=170, y=30)
            current_state2 = 1


    def roulette_2():
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
        clear_window()
        global player, a, rating_1, rating_2, title3, title4, life_1, life_2
        life_1=1
        life_2=1
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

        opp = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (112).png").resize((250, 340)))
        opp_label = Label(frame, image=opp, bg='white')
        opp_label.image = opp
        opp_label.place(x=475, y=9, height=340)

        roulette = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (5).png").resize((90, 120)))
        canvas.create_image(600, 550, image=roulette)
        canvas.image = opp, roulette

        img1 = Image.open("Images\\3039404.png").resize((35, 35))
        photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open("Images\\ff.png").resize((46, 41))
        photo2 = ImageTk.PhotoImage(img2)
        if current_state == 1:
            btn = Button(frame, image=photo1, borderwidth=0, activebackground='white', bg='white',
                         command=lambda: game.toggle_image1(current_state, btn, photo2, photo1))
            btn.image = photo1
            btn.place(x=200, y=33)
        else:
            btn = Button(frame, image=photo2, borderwidth=0, activebackground='white', bg='white',
                         command=lambda: game.toggle_image1(current_state, btn, photo2, photo1))
            btn.image = photo2
            btn.place(x=195.6, y=28)
        img2_a = Image.open("Images\\pngwing.com.png").resize((40, 40))
        photo1_a = ImageTk.PhotoImage(img2_a)
        img2_b = Image.open("Images\\gg.png").resize((53, 48))
        photo2_b = ImageTk.PhotoImage(img2_b)
        if current_state2 == 1:
            btn2 = Button(frame, image=photo1_a, activebackground='white',
                          command=lambda: game.toggle_image21(current_state2, btn2, photo1_a, photo2_b), borderwidth=0,
                          bg='white')
            btn2.image = photo1_a
            btn2.place(x=260, y=30)
        else:
            btn2 = Button(frame, image=photo2_b, activebackground='white',
                          command=lambda: game.toggle_image21(current_state2, btn2, photo1_a, photo2_b), borderwidth=0,
                          bg='white')
            btn2.image = photo2_b
            btn2.place(x=253, y=25)

        image3 = Image.open("Images\\pngwing.com (11).png")
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


        image4 = Image.open("Images\\pngwing.com (11).png")
        image4 = image4.resize((200, 200))
        photo4 = ImageTk.PhotoImage(image4)
        label4 = Label(root, image=photo4, bg='white')
        label4.image = photo4

        image5 = Image.open("Images\\pngwing.com (2).png")
        image5 = image5.resize((200, 200))
        photo5 = ImageTk.PhotoImage(image5)
        label5 = Label(root, image=photo5, bg='white')
        label5.image = photo5


        canvas.create_line(120, 25, 120, 85, fill="black", width=1)
        canvas.create_line(120, 25, 185, 25, fill="black", width=1)
        canvas.create_line(185, 25, 185, 85, fill="black", width=1)
        canvas.create_line(120, 85, 185, 85, fill="black", width=1)
        title2 = Label(frame, text='2 ИГРОК', bg='white', font=("Arial", 13))
        title2.place(x=153, y=16, relwidth=0.07, relheight=0.02, anchor="center")


        def result():
            global life_2
            dimmer = tk.Frame(root, bg="white")
            dimmer.place(relx=0, rely=0, relwidth=1, relheight=1)
            window = tk.Frame(dimmer, bg="white", bd=1, relief="solid")
            window.place(relx=0.12, rely=0.14, relwidth=0.76, relheight=0.7)

            if life_2 == 0:
                tk.Label(window, text="1 игрок выиграл", font=("Arial", 30), bg="white").place(relx=0.12, rely=0.12, relwidth=0.76, relheight=0.09)
                tk.Label(window, text="2 игрок проиграл", font=("Arial", 30), bg="white").place(relx=0.12, rely=0.22, relwidth=0.76, relheight=0.09)
                life_2 += 1
            else:
                tk.Label(window, text="1 игрок проиграл", font=("Arial", 30), bg="white").place(relx=0.12, rely=0.12, relwidth=0.76, relheight=0.09)
                tk.Label(window, text="2 игрок выиграл", font=("Arial", 30), bg="white").place(relx=0.12, rely=0.22, relwidth=0.76, relheight=0.09)

            btn8 = Button(window, image=photo5, activebackground='white', borderwidth=0, bg='white', command=dimmer.destroy)
            btn8.place(x=140, y=300)
            btn10 = Button(window, image=photo4, activebackground='white', borderwidth=0, bg='white', command=lambda: [dimmer.destroy(), main_menu()])
            btn10.place(x=600, y=300)

        def shoot():
            play_once("Sounds\\b05e1ac8be34248.wav")
            global overlay
            overlay = tk.Canvas(root, bg="white", highlightthickness=0)
            overlay.place(relx=0, rely=0, relwidth=1, relheight=1)

            root.after(800, overlay.place_forget)

            root.after(800, lambda: result())

        def opp_shot():
            play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
            global player, a, rating_1, rating_2, life_2
            if player == 1:
                if a <= (canvas.drum_state + 1):
                    life_2 -= 1
                    shoot()
                    if rating_1!=99:
                        rating_1+=1
                    else:
                        rating_1=0
                    title3.config(text=rating_1)
                else:
                    opp_img2 = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (113).png").resize((250, 340)))
                    opp_label.config(image=opp_img2)
                    opp_label.image = opp_img2
                    player = 2
            else:
                if a <= (canvas.drum_state + 1):
                    shoot()
                    if rating_2!=99:
                        rating_2+=1
                    else:
                        rating_2=0
                    title4.config(text=rating_2)
                else:
                    opp_img1 = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (112).png").resize((250, 340)))
                    opp_label.config(image=opp_img1)
                    opp_label.image = opp_img1
                    player = 1
            a = random.randint(1, 6)

        def shot():
            play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
            global a, rating_1, rating_2, life_2
            if a <= (canvas.drum_state + 1):
                if player == 1:
                    shoot()
                    if rating_2!=99:
                        rating_2+=1
                    else: rating_2=0
                    title4.config(text=rating_2)
                else:
                    life_2 -= 1
                    shoot()
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
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
        global current_state, stop_flag, loop_thread
        global btn
        current_state = s
        btn = q
        if s == 1:
            stop_flag = True
            btn.config(image=photo2)
            btn.image = photo2
            btn.place(x=195.6, y=28)
            current_state = 2
        else:
            stop_flag = False
            loop_thread = threading.Thread(target=loop_sound, args=("Sounds\\pixelated-love-20240608-171951.wav",), daemon=True)
            loop_thread.start()
            btn.config(image=photo1)
            btn.image = photo1
            btn.place(x=200, y=33)
            current_state = 1

    def toggle_image21(s, q, photo1_a, photo2_b):
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
        global current_state2, play_sound
        global btn
        current_state2 = s
        btn2 = q
        if s == 1:
            play_sound = False
            btn2.config(image=photo2_b)
            btn2.image = photo2_b
            btn2.place(x=253, y=25)
            current_state2 = 2
        else:
            play_sound = True
            btn2.config(image=photo1_a)
            btn2.image = photo1_a
            btn2.place(x=260, y=30)
            current_state2 = 1


    def shotgun_1():
        clear_window()
        global blank_patron, n, life_1, life_2, a, rating_1, btn33
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

        heart_img = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (1).png").resize((50, 50)))

        heart_1 = canvas.create_image(1030, 40, image=heart_img)
        heart_2 = canvas.create_image(1090, 40, image=heart_img)
        heart_3 = canvas.create_image(1150, 40, image=heart_img)

        hearts = [heart_1, heart_2, heart_3]

        opp = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (111).png").resize((350, 300)))
        canvas.create_image(570, 239, image=opp)

        shotgun = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (6).png").resize((240, 130)))
        canvas.create_image(600, 550, image=shotgun)
        canvas.image = opp, shotgun,heart_img

        img1 = Image.open("Images\\3039404.png").resize((35, 35))
        photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open("Images\\ff.png").resize((46, 41))
        photo2 = ImageTk.PhotoImage(img2)
        if current_state == 1:
            btn = Button(frame, image=photo1, borderwidth=0, activebackground='white', bg='white',
                         command=lambda: game.toggle_image(current_state, btn, photo2, photo1))
            btn.image = photo1
            btn.place(x=110, y=33)
        else:
            btn = Button(frame, image=photo2, borderwidth=0, activebackground='white', bg='white',
                         command=lambda: game.toggle_image(current_state, btn, photo2, photo1))
            btn.image = photo2
            btn.place(x=105.6, y=28)
        img2_a = Image.open("Images\\pngwing.com.png").resize((40, 40))
        photo1_a = ImageTk.PhotoImage(img2_a)
        img2_b = Image.open("Images\\gg.png").resize((53, 48))
        photo2_b = ImageTk.PhotoImage(img2_b)
        if current_state2 == 1:
            btn2 = Button(frame, image=photo1_a, activebackground='white',
                          command=lambda: game.toggle_image2(current_state2, btn2, photo1_a, photo2_b), borderwidth=0,
                          bg='white')
            btn2.image = photo1_a
            btn2.place(x=170, y=30)
        else:
            btn2 = Button(frame, image=photo2_b, activebackground='white',
                          command=lambda: game.toggle_image2(current_state2, btn2, photo1_a, photo2_b), borderwidth=0,
                          bg='white')
            btn2.image = photo2_b
            btn2.place(x=163, y=25)

        image3 = Image.open("Images\\pngwing.com (11).png")
        image3 = image3.resize((50, 50))
        photo3 = ImageTk.PhotoImage(image3)
        label3 = Label(root, image=photo3, bg='white')
        label3.image = photo3
        btn33 = Button(frame, image=photo3, borderwidth=0, activebackground='white', bg='white', command=main_menu)
        btn33.place(x=230, y=25)

        image4 = Image.open("Images\\pngwing.com (11).png")
        image4 = image4.resize((200, 200))
        photo4 = ImageTk.PhotoImage(image4)
        label4 = Label(root, image=photo4, bg='white')
        label4.image = photo4

        image5 = Image.open("Images\\pngwing.com (2).png")
        image5 = image5.resize((200, 200))
        photo5 = ImageTk.PhotoImage(image5)
        label5 = Label(root, image=photo5, bg='white')
        label5.image = photo5

        canvas.create_line(30, 25, 30, 85, fill="black", width=1)
        canvas.create_line(30, 25, 95, 25, fill="black", width=1)
        canvas.create_line(95, 25, 95, 85, fill="black", width=1)
        canvas.create_line(30, 85, 95, 85, fill="black", width=1)
        title1 = Label(frame, text='1 ИГРОК', bg='white', font=("Arial", 13))
        title1.place(x=61, y=16, relwidth=0.3, relheight=0.02, anchor="center")

        def update_hearts(life_1):
            for i in range(3):
                if i < life_1:
                    canvas.itemconfigure(hearts[i], state='normal')
                else:
                    canvas.itemconfigure(hearts[i], state='hidden')

        def result():
            global life_2, rating_1, rating_2, life_1, n, blank_patron, a
            dimmer = tk.Frame(root, bg="white")
            dimmer.place(relx=0, rely=0, relwidth=1, relheight=1)
            window = tk.Frame(dimmer, bg="white", bd=1, relief="solid")
            window.place(relx=0.12, rely=0.14, relwidth=0.76, relheight=0.7)

            if life_2==0:
                play_once("Sounds\\game-won.wav")
                tk.Label(window, text="ВЫ ВЫИГРАЛИ!", font=("Arial", 30), bg="white").place(relx=0.12, rely=0.12, relwidth=0.76, relheight=0.09)
                if rating_1 != 99:
                    rating_1 += 1
                else:
                    rating_1 = 0
                title3.config(text=rating_1)
                life_1 = 3
                life_2 = 3
                update_hearts(life_1)
                n = 5
                blank_patron = 3

            else:
                play_once("Sounds\\02c25f2abdd7bbb.wav")
                tk.Label(window, text="ВЫ ПРОИГРАЛИ!", font=("Arial", 30), bg="white").place(relx=0.12, rely=0.12, relwidth=0.76, relheight=0.09)
                life_1 = 3
                life_2 = 3
                update_hearts(life_1)
                n = 5

            btn8 = Button(window, image = photo5, activebackground = 'white', borderwidth = 0, bg = 'white', command=dimmer.destroy)
            btn8.place (x=140, y=300)
            btn10 = Button(window, image = photo4, activebackground = 'white', borderwidth = 0, bg = 'white', command=lambda: [dimmer.destroy(), main_menu()])
            btn10.place(x=600, y=300)


        def shoot():
            global overlay, k
            play_once("Sounds\\horoshiy-blizkiy-odinochnyiy-vyistrel.wav")
            overlay = tk.Canvas(root, bg="white", highlightthickness=0)
            overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
            root.after(800, overlay.place_forget)
            if life_2==0 or life_1==0:
                root.after(800, lambda: result())
                k = 2

        def show_blank_info():
            global label_info, x, l
            if (x == 1) or (l == 2):
                return
            label_info = tk.Label(frame, text=f"В ДРОБОВИКЕ {blank_patron} ХОЛОСТЫХ ПАТРОНОВ", font=("Arial", 15), bg='white', bd=1, relief='solid')
            label_info.place(relx=0.5, rely=0.65, relwidth=0.35, relheight=0.3, anchor='center')
            frame.after(3000, hide_blank_info)
        def hide_blank_info():
            global q,n, blank_patron, a, life_1, life_2
            if label_info:
                label_info.destroy()
                if q==1:
                    a = random.randint(1, n)
                    b = random.randint(1, 2)
                    if a > blank_patron:
                        if b == 1:
                            life_1 -= 1
                            shoot()
                            update_hearts(life_1)
                            n -= 1
                        else:
                            life_2 -= 1
                            shoot()
                            n -= 1
                    else:
                        blank_patron -= 1
                        n -= 1
                    a = random.randint(1, n)
                btn4.config(state=tk.NORMAL)
                btn5.config(state=tk.NORMAL)


        def yyy():
            global a, n, x
            x=2
            root.after(1000, show_blank_info)
            n = 5
            a = random.randint(1, n)


        def move_opp():
            global n, a, rating_1, blank_patron, life_1, life_2, k, q, l, recharge
            a = random.randint(1, n)
            b = random.randint(1, 2)
            if a > blank_patron:
                if b == 1:
                    life_1 -= 1
                    shoot()
                    update_hearts(life_1)
                    n -= 1
                else:
                    life_2 -= 1
                    shoot()
                    n -= 1
            else:
                blank_patron -= 1
                n -= 1
            if (n == 0) and (life_2 != 0) and (life_1 != 0) and (k != 2):
                recharge = 2
                play_once("Sounds\\avtomaticheskaya-byistraya-perezaryadka (1).wav")
                if l == 2:
                    l = 1
                    blank_patron = random.randint(1, 5)
                    btn4.config(state=tk.DISABLED)
                    btn5.config(state=tk.DISABLED)
                    root.after(2000, yyy)
                    return
                blank_patron = random.randint(1, 5)
                btn4.config(state=tk.DISABLED)
                btn5.config(state=tk.DISABLED)
                root.after(3000, show_blank_info)
                n = 5
            btn33.config(state=tk.NORMAL)
            if recharge == 1:
                btn4.config(state=tk.NORMAL)
                btn5.config(state=tk.NORMAL)


        def opp_shot():
            play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
            global n, a, rating_1, blank_patron, life_1, life_2, k, q, l, recharge
            recharge = 1
            q=2
            k=1
            if a > blank_patron:
                life_2 -= 1
                shoot()
                n -= 1
                if (life_2 == 0) or (k == 2):
                    n=5
                    a = random.randint(1, n)
                    return
                if n == 0:
                    recharge = 2
                    play_once("Sounds\\avtomaticheskaya-byistraya-perezaryadka (1).wav")
                    if l == 2:
                        btn4.config(state=tk.DISABLED)
                        btn5.config(state=tk.DISABLED)
                        q = 1
                        l=1
                        blank_patron = random.randint(1, 5)
                        root.after(2000, yyy)
                        return
                    q=1
                    btn4.config(state=tk.DISABLED)
                    btn5.config(state=tk.DISABLED)
                    blank_patron = random.randint(1, 5)
                    root.after(3000, show_blank_info)
                    n = 5
                    a = random.randint(1, n)
                    return
                root.after(2000, move_opp)
                btn33.config(state=tk.DISABLED)
                btn4.config(state=tk.DISABLED)
                btn5.config(state=tk.DISABLED)
                return
            else:
                blank_patron -= 1
                n -= 1
                if n == 0:
                    recharge = 2
                    play_once("Sounds\\avtomaticheskaya-byistraya-perezaryadka (1).wav")
                    if l == 2:
                        q = 1
                        l = 1
                        blank_patron = random.randint(1, 5)
                        btn4.config(state=tk.DISABLED)
                        btn5.config(state=tk.DISABLED)
                        root.after(2000, yyy)
                        return
                    q=1
                    blank_patron = random.randint(1, 5)
                    btn4.config(state=tk.DISABLED)
                    btn5.config(state=tk.DISABLED)
                    root.after(3000, show_blank_info)
                    n = 5
                    a = random.randint(1, n)
                    return
                root.after(2000, move_opp)
                btn33.config(state=tk.DISABLED)
                btn4.config(state=tk.DISABLED)
                btn5.config(state=tk.DISABLED)
                return

        def shot():
            play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
            global a, blank_patron, life_1, life_2, n, rating_1, k, q, l, recharge
            recharge = 1
            k =1
            q=2

            if a > blank_patron:
                life_1 -= 1
                shoot()
                update_hearts(life_1)
                n -= 1
                if (life_1 == 0) or (k==2):
                    n = 5
                    a = random.randint(1, n)
                    return
                if n == 0:
                    recharge = 2
                    play_once("Sounds\\avtomaticheskaya-byistraya-perezaryadka (1).wav")
                    if l == 2:
                        q = 1
                        l = 1
                        blank_patron = random.randint(1, 5)
                        btn4.config(state=tk.DISABLED)
                        btn5.config(state=tk.DISABLED)
                        root.after(2000, yyy)
                        return
                    q=1
                    blank_patron = random.randint(1, 5)
                    btn4.config(state=tk.DISABLED)
                    btn5.config(state=tk.DISABLED)
                    root.after(3000, show_blank_info)
                    n = 5
                    a = random.randint(1, n)
                    return
                root.after(2000, move_opp)
                btn33.config(state=tk.DISABLED)
                btn4.config(state=tk.DISABLED)
                btn5.config(state=tk.DISABLED)
                return

            else:
                blank_patron -= 1
                n -= 1

            if (n==0) and (life_1!=0) and (life_2 != 0) and (k!=2):
                recharge = 2
                play_once("Sounds\\avtomaticheskaya-byistraya-perezaryadka (1).wav")
                if l == 2:
                    l = 1
                    blank_patron = random.randint(1, 5)
                    btn4.config(state=tk.DISABLED)
                    btn5.config(state=tk.DISABLED)
                    root.after(2000, yyy)
                    return
                blank_patron = random.randint(1, 5)
                btn4.config(state=tk.DISABLED)
                btn5.config(state=tk.DISABLED)
                root.after(3000, show_blank_info)
                n = 5

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
        heart_img = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (1).png").resize((50, 50)))
        heart_1 = canvas.create_image(1030, 40, image=heart_img)
        heart_2 = canvas.create_image(1090, 40, image=heart_img)
        heart_3 = canvas.create_image(1150, 40, image=heart_img)
        heart_4 = canvas.create_image(1030, 40, image=heart_img)
        heart_5 = canvas.create_image(1090, 40, image=heart_img)
        heart_6 = canvas.create_image(1150, 40, image=heart_img)

        hearts_player1 = [heart_1, heart_2, heart_3]
        hearts_player2 = [heart_4, heart_5, heart_6]

        heart_visibility_p1 = [True, True, True]
        heart_visibility_p2 = [True, True, True]

        hearts_hidden_globally = False

        opp = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (112).png").resize((250, 340)))
        opp_label = Label(frame, image=opp, bg='white')
        opp_label.image = opp
        opp_label.place(x=475, y=9, height=340)

        shotgun = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (6).png").resize((240, 130)))
        canvas.create_image(600, 550, image=shotgun)
        canvas.image = opp, shotgun, heart_img

        img1 = Image.open("Images\\3039404.png").resize((35, 35))
        photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open("Images\\ff.png").resize((46, 41))
        photo2 = ImageTk.PhotoImage(img2)
        if current_state == 1:
            btn = Button(frame, image=photo1, borderwidth=0, activebackground='white', bg='white',
                         command=lambda: game.toggle_image1(current_state, btn, photo2, photo1))
            btn.image = photo1
            btn.place(x=200, y=33)
        else:
            btn = Button(frame, image=photo2, borderwidth=0, activebackground='white', bg='white',
                         command=lambda: game.toggle_image1(current_state, btn, photo2, photo1))
            btn.image = photo2
            btn.place(x=195.6, y=28)
        img2_a = Image.open("Images\\pngwing.com.png").resize((40, 40))
        photo1_a = ImageTk.PhotoImage(img2_a)
        img2_b = Image.open("Images\\gg.png").resize((53, 48))
        photo2_b = ImageTk.PhotoImage(img2_b)
        if current_state2 == 1:
            btn2 = Button(frame, image=photo1_a, activebackground='white',
                          command=lambda: game.toggle_image21(current_state2, btn2, photo1_a, photo2_b), borderwidth=0,
                          bg='white')
            btn2.image = photo1_a
            btn2.place(x=260, y=30)
        else:
            btn2 = Button(frame, image=photo2_b, activebackground='white',
                          command=lambda: game.toggle_image21(current_state2, btn2, photo1_a, photo2_b), borderwidth=0,
                          bg='white')
            btn2.image = photo2_b
            btn2.place(x=253, y=25)

        image3 = Image.open("Images\\pngwing.com (11).png")
        image3 = image3.resize((50, 50))
        photo3 = ImageTk.PhotoImage(image3)
        label3 = Label(root, image=photo3, bg='white')
        label3.image = photo3

        image4 = Image.open("Images\\pngwing.com (11).png")
        image4 = image4.resize((200, 200))
        photo4 = ImageTk.PhotoImage(image4)
        label4 = Label(root, image=photo4, bg='white')
        label4.image = photo4

        image5 = Image.open("Images\\pngwing.com (2).png")
        image5 = image5.resize((200, 200))
        photo5 = ImageTk.PhotoImage(image5)
        label5 = Label(root, image=photo5, bg='white')
        label5.image = photo5


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

        def hide_hearts_player1():
            global hearts_hidden_p1, hearts_hidden_p2
            hearts_hidden_p1 = True
            for heart in hearts_player1:
                canvas.itemconfigure(heart, state='hidden')
            hearts_hidden_p2 = False
            for i in range(3):
                state = 'normal' if heart_visibility_p2[i] else 'hidden'
                canvas.itemconfigure(hearts_player2[i], state=state)

        def hide_hearts_player2():
            global hearts_hidden_p2, hearts_hidden_p1
            hearts_hidden_p2 = True
            for heart in hearts_player2:
                canvas.itemconfigure(heart, state='hidden')
            hearts_hidden_p1 = False
            for i in range(3):
                state = 'normal' if heart_visibility_p1[i] else 'hidden'
                canvas.itemconfigure(hearts_player1[i], state=state)


        def result():
            global life_2, rating_1, rating_2, life_1, n, blank_patron, a
            dimmer = tk.Frame(root, bg="white")
            dimmer.place(relx=0, rely=0, relwidth=1, relheight=1)
            window = tk.Frame(dimmer, bg="white", bd=1, relief="solid")
            window.place(relx=0.12, rely=0.14, relwidth=0.76, relheight=0.7)

            if life_2==0:
                tk.Label(window, text="1 игрок выиграл", font=("Arial", 30), bg="white").place(relx=0.12, rely=0.12,
                                                        relwidth=0.76, relheight=0.09)
                tk.Label(window, text="2 игрок проиграл", font=("Arial", 30), bg="white").place(relx=0.12, rely=0.22,
                                                        relwidth=0.76, relheight=0.09)
                if rating_1 != 99:
                    rating_1 += 1
                else:
                    rating_1 = 0
                title3.config(text=rating_1)
                life_1 = 3
                life_2 = 3
                update_hearts(life_1, life_2)
                n = 5
                blank_patron = 3

            else:
                tk.Label(window, text="1 игрок проиграл", font=("Arial", 30), bg="white").place(relx=0.12, rely=0.12,
                                                        relwidth=0.76, relheight=0.09)
                tk.Label(window, text="2 игрок выиграл", font=("Arial", 30), bg="white").place(relx=0.12, rely=0.22,
                                                        relwidth=0.76, relheight=0.09)
                life_1 = 3
                life_2 = 3
                update_hearts(life_1, life_2)
                n = 5
                blank_patron = 3
                if rating_2 != 99:
                    rating_2 += 1
                else:
                    rating_2 = 0
                title4.config(text=rating_2)

            btn8 = Button(window, image = photo5, activebackground = 'white', borderwidth = 0, bg = 'white', command=dimmer.destroy)
            btn8.place (x=140, y=300)
            btn10 = Button(window, image = photo4, activebackground = 'white', borderwidth = 0, bg = 'white', command=lambda: [dimmer.destroy(), main_menu()])
            btn10.place(x=600, y=300)

        def update_hearts(life1, life2):
            for i in range(3):
                heart_visibility_p1[i] = i < life1
                heart_visibility_p2[i] = i < life2
                if not hearts_hidden_globally:
                    canvas.itemconfigure(hearts_player1[i], state='normal' if i < life1 else 'hidden')
                    canvas.itemconfigure(hearts_player2[i], state='normal' if i < life2 else 'hidden')

        def shoot():
            play_once("Sounds\\horoshiy-blizkiy-odinochnyiy-vyistrel.wav")
            global overlay, k
            overlay = tk.Canvas(root, bg="white", highlightthickness=0)
            overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
            root.after(800, overlay.place_forget)
            if life_2==0 or life_1==0:
                root.after(800, lambda: result())
                k=2


        def show_blank_info():
            global label_info, m, l
            if (x == 1) or (l == 2):
                return
            label_info = tk.Label(frame, text=f"В ДРОБОВИКЕ {blank_patron} ХОЛОСТЫХ ПАТРОНОВ", font=("Arial", 15), bg='white', bd=1, relief='solid')
            label_info.place(relx=0.5, rely=0.65, relwidth=0.35, relheight=0.3, anchor='center')
            frame.after(3000, hide_blank_info)
        def hide_blank_info():
            if label_info:
                label_info.destroy()
                btn4.config(state=tk.NORMAL)
                btn5.config(state=tk.NORMAL)


        def yyy():
            global a, n, x
            x=2
            root.after(1000, show_blank_info)
            n = 5
            a = random.randint(1, n)


        def opp_shot():
            play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
            global n, a, rating_1, blank_patron, life_1, life_2, player, rating_2, k, l
            k=1
            if player==1:
                if a > blank_patron:
                    life_2 -= 1
                    shoot()
                    n -= 1
                    update_hearts(life_1, life_2)
                else:
                    blank_patron -= 1
                    n -= 1
                opp_img2 = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (113).png").resize((250, 340)))
                opp_label.config(image=opp_img2)
                opp_label.image = opp_img2
                player=2
                hide_hearts_player1()
            else:
                if a > blank_patron:
                    life_1 -= 1
                    shoot()
                    n -= 1
                    update_hearts(life_1, life_2)
                    if n == 0:
                        play_once("Sounds\\avtomaticheskaya-byistraya-perezaryadka (1).wav")
                        if l == 2:
                            l = 1
                            blank_patron = random.randint(1, 5)
                            btn4.config(state=tk.DISABLED)
                            btn5.config(state=tk.DISABLED)
                            root.after(2000, yyy)
                            return
                        blank_patron = random.randint(1, 5)
                        btn4.config(state=tk.DISABLED)
                        btn5.config(state=tk.DISABLED)
                        root.after(3000, show_blank_info)
                        n = 5
                else:
                    blank_patron -= 1
                    n -= 1
                opp_img2 = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (112).png").resize((250, 340)))
                opp_label.config(image=opp_img2)
                opp_label.image = opp_img2
                player=1
                hide_hearts_player2()

            if (n == 0) and (life_2 != 0) and (life_1 != 0) and (k!=2):
                play_once("Sounds\\avtomaticheskaya-byistraya-perezaryadka (1).wav")
                if l == 2:
                    l = 1
                    blank_patron = random.randint(1, 5)
                    btn4.config(state=tk.DISABLED)
                    btn5.config(state=tk.DISABLED)
                    root.after(2000, yyy)
                    return
                blank_patron = random.randint(1, 5)
                btn4.config(state=tk.DISABLED)
                btn5.config(state=tk.DISABLED)
                root.after(3000, show_blank_info)
                n = 5
            else:
                if n==0:
                    n=5
            a = random.randint(1, n)


        def shot():
            play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
            global a, blank_patron, life_1, life_2, n, rating_1, rating_2, player, k, l
            k=1
            if player==1:
                if a > blank_patron:
                    life_1 -= 1
                    shoot()
                    update_hearts(life_1, life_2)
                    n -= 1
                    opp_img2 = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (113).png").resize((250, 340)))
                    opp_label.config(image=opp_img2)
                    opp_label.image = opp_img2
                    player=2
                    hide_hearts_player1()
                else:
                    blank_patron -= 1
                    n -= 1
            else:
                if a > blank_patron:
                    life_2 -= 1
                    shoot()
                    update_hearts(life_1, life_2)
                    n -= 1
                    opp_img2 = ImageTk.PhotoImage(Image.open("Images\\pngwing.com (112).png").resize((250, 340)))
                    opp_label.config(image=opp_img2)
                    opp_label.image = opp_img2
                    player=1
                    hide_hearts_player2()
                else:
                    blank_patron -= 1
                    n -= 1

            if (n==0) and (life_1!=0) and (life_2 != 0) and (k!=2):
                play_once("Sounds\\avtomaticheskaya-byistraya-perezaryadka (1).wav")
                if l == 2:
                    l = 1
                    blank_patron = random.randint(1, 5)
                    btn4.config(state=tk.DISABLED)
                    btn5.config(state=tk.DISABLED)
                    root.after(2000, yyy)
                    return
                blank_patron = random.randint(1, 5)
                btn4.config(state=tk.DISABLED)
                btn5.config(state=tk.DISABLED)
                root.after(3000, show_blank_info)
                n = 5
            else:
                if n==0:
                    n=5
            a = random.randint(1, n)


        btn5 = Button(frame, text='ВЫСТРЕЛИТЬ В ПРОТИВНИКА', font=("Arial", 15), command=opp_shot)
        btn5.place(relx=0.18, rely=0.85, relwidth=0.27, relheight=0.13)
        btn4 = Button(frame, text='ВЫСТРЕЛИТЬ В СЕБЯ', font=("Arial", 15), command=shot)
        btn4.place(relx=0.55, rely=0.85, relwidth=0.27, relheight=0.13)


class settings:
    def settings():
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
        clear_window()
        global tog, current_state, current_state2
        img1 = Image.open("Images\\3039404.png").resize((210, 210))
        photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open("Images\\ff.png").resize((269, 244))
        photo2 = ImageTk.PhotoImage(img2)
        if current_state == 1:
            btn = Button(frame, image=photo1, borderwidth=0, activebackground='white', bg='white', command=lambda: settings.toggle_image(current_state, btn, photo2, photo1))
            btn.image = photo1
            btn.place(x=230, y=290)
        else:
            btn = Button(frame, image=photo2, borderwidth=0, activebackground='white', bg='white',
                         command=lambda: settings.toggle_image(current_state, btn, photo2, photo1))
            btn.image = photo2
            btn.place(x=210, y=262)
        img2_a = Image.open("Images\\pngwing.com.png").resize((240, 240))
        photo1_a = ImageTk.PhotoImage(img2_a)
        img2_b = Image.open("Images\\gg.png").resize((310, 280))
        photo2_b = ImageTk.PhotoImage(img2_b)
        if current_state2 == 1:
            btn2 = Button(frame, image=photo1_a, activebackground='white', command=lambda: settings.toggle_image2(current_state2, btn2, photo1_a, photo2_b), borderwidth=0, bg='white')
            btn2.image = photo1_a
            btn2.place(x=740, y=275)
        else:
            btn2 = Button(frame, image=photo2_b, activebackground='white',
                          command=lambda: settings.toggle_image2(current_state2, btn2, photo1_a, photo2_b),
                          borderwidth=0, bg='white')
            btn2.image = photo2_b
            btn2.place(x=695, y=245.5)
        image3 = Image.open("Images\\pngwing.com (11).png")
        image3 = image3.resize((60, 60))
        photo3 = ImageTk.PhotoImage(image3)
        label3 = Label(root, image=photo3, bg='white')
        label3.image = photo3
        btn3 = Button(frame, image=photo3, borderwidth=0, activebackground='white', bg='white', command=main_menu)
        btn3.place(x=20, y=725)
    def toggle_image(s, q, photo2, photo1):
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
        global current_state, stop_flag, loop_thread
        current_state=s
        btn=q
        if s == 1:
            stop_flag = True
            btn.config(image=photo2)
            btn.image = photo2
            btn.place(x=210, y=262)
            current_state = 2
        else:
            stop_flag = False
            loop_thread = threading.Thread(target=loop_sound, args=("Sounds\\pixelated-love-20240608-171951.wav",), daemon=True)
            loop_thread.start()
            btn.config(image=photo1)
            btn.image = photo1
            btn.place(x=230, y=290)
            current_state = 1
    def toggle_image2(s, q, photo1_a, photo2_b):
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
        global current_state2, play_sound
        current_state2=s
        btn2=q
        if s == 1:
            play_sound = False
            btn2.config(image=photo2_b)
            btn2.image = photo2_b
            btn2.place(x=695, y=245.5)
            current_state2 = 2
        else:
            play_sound = True
            btn2.config(image=photo1_a)
            btn2.image = photo1_a
            btn2.place(x=740, y=275)
            current_state2 = 1


stop_flag = False
def loop_sound(filename):
    global stop_flag
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    while not stop_flag:
        wf.rewind()
        data = wf.readframes(1024)
        while data and not stop_flag:
            stream.write(data)
            data = wf.readframes(1024)
    stream.stop_stream()
    stream.close()
    #p.terminate()
    wf.close()
loop_thread = threading.Thread(target=loop_sound, args=("Sounds\\pixelated-love-20240608-171951.wav",), daemon=True)
loop_thread.start()



play_sound=True

def play_once(filename):
    global play_sound
    if play_sound == True:
        def _sound():
            wf = wave.open(filename, 'rb')
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
            data = wf.readframes(1024)
            while data:
                stream.write(data)
                data = wf.readframes(1024)
            stream.stop_stream()
            stream.close()
            p.terminate()
            wf.close()
        threading.Thread(target=_sound, daemon=True).start()

def exit_game():
    sys.exit()

def sound_exit():
    play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
    root.after(400, exit_game)

def main_menu():
    clear_window()
    global l, x, m, q
    if m==2:
        play_once("Sounds\\knopka-vyiklyucheniya-na-nastolnoy-lampe1.wav")
    l=2
    m=2
    q=2
    x=1
    title = Label(frame, text='РУССКАЯ  РУЛЕТКА', bg='white', font=("Arial", 20))
    title.place(relx=0.15, rely=0.27, relwidth=0.7)
    btn1 = Button(frame, text='ИГРАТЬ', font=("Arial", 15), command=modes.modes_1)
    btn1.place(relx=0.38, rely=0.35, relwidth=0.24)
    btn2 = Button(frame, text='ПРАВИЛА', font=("Arial", 15), command=rule)
    btn2.place(relx=0.38, rely=0.43, relwidth=0.24)
    btn3 = Button(frame, text='НАСТРОЙКИ', font=("Arial", 15),command=settings.settings)
    btn3.place(relx=0.38, rely=0.5, relwidth=0.24)
    btn4 = Button(frame, text='ВЫХОД', font=("Arial", 15), command=sound_exit)
    btn4.place(relx=0.38, rely=0.57, relwidth=0.24)
main_menu()

root.mainloop()