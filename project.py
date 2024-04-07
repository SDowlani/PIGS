from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from random import randint
from module import Player
from pygame import mixer
from time import sleep


OUTPUT_PATH = Path(__file__).parent
ASSET_PATH = Path(OUTPUT_PATH / "assets")
SOUNDTRACK_PATH = Path(OUTPUT_PATH / "soundtracks")

window = Tk()
mixer.init()

def main():
    window.title("PIGS")
    photo = PhotoImage(file = OUTPUT_PATH / "pig.png")
    window.iconphoto(False, photo)
    home_screen()
def home_screen():
    mixer.music.load(SOUNDTRACK_PATH / "Super Mario 64 Soundtrack - Cool, Cool Mountain.mp3")
    mixer.music.play(loops=1)
    
    FRAME_PATH = Path(ASSET_PATH / "home_screen")
    window.geometry("338x535")
    window.configure(bg = "#19191E")


    canvas = Canvas(
        window,
        bg = "#19191E",
        height = 535,
        width = 338,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        63.0,
        28.0,
        anchor="nw",
        text="PIGS!\nGood 'ol\nPIG Game!\n",
        fill="#1F4B8B",
        font=("Inter SemiBold", 35 * -1)
    )

    button_image_1 = PhotoImage(
        file=(FRAME_PATH / "button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=player_screen,
        relief="flat"
    )
    button_1.place(
        x=23.0,
        y=417.0,
        width=280.0,
        height=40.0
    )

    image_image_1 = PhotoImage(
        file=FRAME_PATH / "image_1.png")
    image_1 = canvas.create_image(
        154.0,
        267.0,
        image=image_image_1
    )
    window.resizable(False, False)
    window.mainloop()
def player_screen():
    FRAME_PATH = Path(ASSET_PATH / "player_screen")
    
    window.geometry("376x550")  
    window.configure(bg="#19191E")

    canvas = Canvas(
        window,
        bg="#19191E",
        height=500,
        width=376,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=FRAME_PATH / "image_1.png")
    image_1 = canvas.create_image(
        135.0,
        132.0,
        image=image_image_1
    )

    canvas.create_text(
        48.0,
        233.0,
        anchor="nw",
        text="SET NAMES!",
        fill="#1F4B8B",
        font=("Inter SemiBold", 35 * -1)
    )

    canvas.create_text(
        48.0,
        288.0,
        anchor="nw",
        text="PLAYER 1",
        fill="#9393D5",
        font=("Inter Light", 15 * -1)
    )

    entry_image_1 = PhotoImage(
        file=FRAME_PATH / "entry_1.png")
    entry_bg_1 = canvas.create_image(
        188.0,
        339.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#B6B6F9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=63.0,
        y=319.0,
        width=250.0,
        height=38.0
    )

    # Create entry for Player 2
    canvas.create_text(
        48.0,
        403.0,
        anchor="nw",
        text="PLAYER 2",
        fill="#9393D5",
        font=("Inter Light", 15 * -1)
    )
    entry_image_2 = PhotoImage(
        file=FRAME_PATH / "entry_2.png")
    entry_bg_2 = canvas.create_image(
        188.0,
        454.0,  #
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#B6B6F9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=63.0,
        y=434.0,
        width=250.0,
        height=38.0
    )

    # Create "Play" button
    button_image_play = PhotoImage(
        file=FRAME_PATH / "play.png")
    button_play = Button(
        image=button_image_play,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: empty(entry_1, entry_2), 
        relief="flat"
    )
    button_play.place(
        x=48.0,
        y=487.0, 
        width=280.0,
        height=40.0
    )

    window.resizable(False, False)
    window.mainloop()    
def empty(entry1, entry2):
    if not entry1.get() or not entry2.get():
        messagebox.showwarning(title="Warning", message="Something's empty here!")
    else:
        winning_points_screen(entry1.get(), entry2.get())
def winning_points_screen(player1_nickname, player2_nickname):
    FRAME_PATH = Path(ASSET_PATH / "points_screen")
    window.geometry("338x535")
    window.configure(bg = "#19191E")


    canvas = Canvas(
        window,
        bg = "#19191E",
        height = 535,
        width = 338,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        32.0,
        23.0,
        anchor="nw",
        text="SET\nWIN\nPOINTS",
        fill="#1F4B8B",
        font=("Inter SemiBold", 35 * -1)
    )

    button_image_1 = PhotoImage(
        file=FRAME_PATH / "35.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: rules_screen(player1_nickname, player2_nickname, 35),
        relief="flat"
    )
    button_1.place(
        x=16.0,
        y=211.0,
        width=280.0,
        height=40.0
    )

    button_image_2 = PhotoImage(
        file=FRAME_PATH / "75.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: rules_screen(player1_nickname, player2_nickname, 75),
        relief="flat"
    )
    button_2.place(
        x=16.0,
        y=281.0,
        width=280.0,
        height=40.0
    )

    button_image_3 = PhotoImage(
        file=FRAME_PATH / "115.png")
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: rules_screen(player1_nickname, player2_nickname, 115),
        relief="flat"
    )
    button_3.place(
        x=16.0,
        y=351.0,
        width=280.0,
        height=40.0
    )

    button_image_4 = PhotoImage(
        file=FRAME_PATH / "150.png")
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: rules_screen(player1_nickname, player2_nickname, 150),
        relief="flat"
    )
    button_4.place(
        x=16.0,
        y=421.0,
        width=280.0,
        height=40.0
    )

    image_image_1 = PhotoImage(
        file=FRAME_PATH /  "medal.png")
    image_1 = canvas.create_image(
        257.0,
        93.0,
        image=image_image_1
    )
    window.resizable(False, False)
    window.mainloop()
def rules_screen(player1_nickname, player2_nickname, winning_points):
    FRAME_PATH = Path(ASSET_PATH / "rules_screen")
    window.geometry("340x635")
    window.configure(bg = "#19191E")

    canvas = Canvas(
        window,
        bg = "#19191E",
        height = 535,
        width = 338,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        25.0,
        45.0,
        anchor="nw",
        text="PIG\nRULES",
        fill="#1F4B8B",
        font=("Inter SemiBold", 35 * -1)
    )

    image_image_1 = PhotoImage(
        file=FRAME_PATH / "rules.png")
    image_1 = canvas.create_image(
        232.0,
        90.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=FRAME_PATH / "ready.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: game_screen(player1_nickname, player2_nickname, winning_points),
        relief="flat"
    )
    button_1.place(
        x=66.0,
        y=562.0,
        width=184.0,
        height=33.0
    )

    canvas.create_text(
        18.0,
        174.0,
        anchor="nw",
        text="Accumulate Points by \n   ->  Rolling \n\n Rolling a One will\n     -> Reset Your Score \n     -> Lose your Turn\n\n Hit HOLD to\n      -> Keep Score \n      -> Pass \n\n Reaching Max Points \n     -> Win",
        fill="#E9CFFE",
        font=("Inter SemiBold", 22 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
def game_screen(player1_nickname, player2_nickname, winning_points):
    FRAME_PATH = Path(ASSET_PATH / "game_screen")
    mixer.music.load(SOUNDTRACK_PATH / "Mario Kart Soundfx.mp3")
    mixer.music.play(loops=0)
    sleep(5)
    mixer.music.load(SOUNDTRACK_PATH / "Super Mario 64 Soundtrack - Title Theme.mp3")
    mixer.music.play(loops=1)
    
    
    player_1 = Player(player1_nickname, 1)
    player_2 = Player(player2_nickname, 2)
    
    window.geometry("1074x582")
    window.configure(bg = "#19191E")

    def update_image(image_id, new_image_path):
        new_image = PhotoImage(file = new_image_path)
        canvas.itemconfig(image_id, image=new_image)
        canvas.image = new_image
        
    def switch_turn(active_player: Player):
        if active_player.id == 1:
            button_1.config(state='disabled')
            button_2.config(state='disabled')
            canvas.after(600, lambda: button_3.config(state='normal'))
            canvas.after(600, lambda: button_4.config(state='normal'))
            update_image (image_1, FRAME_PATH / "blocked.png")
            canvas.after(600, update_image, image_2, FRAME_PATH / "0_dots.png")
            canvas.after(400, lambda : canvas.itemconfigure(turn_belongs_to, text="   " + player_2.name))
        else:
            button_3.config(state='disabled')
            button_4.config(state='disabled')
            canvas.after(600, lambda: button_1.config(state='normal'))
            canvas.after(600, lambda: button_2.config(state='normal'))
            update_image (image_2, FRAME_PATH / "blocked.png")
            canvas.after(600, update_image, image_1, FRAME_PATH / "0_dots.png")
            canvas.after(400, lambda : canvas.itemconfigure(turn_belongs_to, text="   " + player_1.name))
            
        player_won(active_player)
  
    def roll(player : Player, current_image):
        rolled = randint(1,6)
        update_image(current_image, FRAME_PATH / (str(rolled)+"_dots.png"))
        if rolled != 1:
            player.points += rolled
        else:
            player.points = 0
            canvas.after(600, switch_turn, player)
            
        if (player.id == 1):
            canvas.itemconfigure(p1_score, text = "Score: "+ str(player.points))
        else:
            canvas.itemconfigure(p2_score, text = "Score: "+ str(player.points))
            
        player_won(player)
            
    def player_won(player):
        if player.points >= winning_points:
            button_1.config(state='disabled')
            button_2.config(state='disabled')
            button_3.config(state='disabled')
            button_4.config(state='disabled')
            canvas.after(1000, winner_screen, player)
            
    canvas = Canvas(
        window,
        bg = "#19191E",
        height = 582,
        width = 1074,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        48.0,
        45.0,
        anchor="nw",
        text=player_1.name,
        fill="#1F4B8B",
        font=("Inter SemiBold", 35 * -1)
    )

    canvas.create_text(
        768.0,
        45.0,
        anchor="nw",
        text=player_2.name,
        fill="#1F4B8B",
        font=("Inter SemiBold", 35 * -1)
    )

    canvas.create_text(
        437.0,
        49.0,
        anchor="nw",
        text="TURN:\n",
        fill="#1F4B8B",
        font=("Inter SemiBold", 35 * -1)
    )

    turn_belongs_to = canvas.create_text(
        425.0,
        125.0,
        anchor="nw",
        text="   "+ player1_nickname,
        fill="#E9CFFE",
        font=("Inter SemiBold", 35 * -1)
    )

    image_image_1 = PhotoImage(
        file=FRAME_PATH / "0_dots.png")
    image_1 = canvas.create_image(
        121.0,
        205.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=FRAME_PATH / "0_dots.png")
    image_2 = canvas.create_image(
        818.0,
        212.0,
        image=image_image_2
    )

    p1_score = canvas.create_text(
        48.0,
        321.0,
        anchor="nw",
        text="Score: " + str(player_1.points),
        fill="#FFFFFF",
        font=("Inter SemiBold", 25 * -1)
    )

    p2_score = canvas.create_text(
        742.0,
        321.0,
        anchor="nw",
        text="Score: " + str(player_2.points),
        fill="#FFFFFF",
        font=("Inter SemiBold", 25 * -1)
    )

    button_image_1 = PhotoImage(
        file=FRAME_PATH / "roll_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: roll(player_1, image_1),
        relief="flat"
    )
    button_1.place(
        x=29.0,
        y=380.0,
        width=280.0,
        height=40.0
    )

    button_image_2 = PhotoImage(
        file=FRAME_PATH / "hold_1.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_turn(player_1),
        relief="flat"
    )
    button_2.place(
        x=29.0,
        y=449.0,
        width=280.0,
        height=40.0
    )

    button_image_3 = PhotoImage(
        file=FRAME_PATH / "hold_2.png")
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        state='disabled',
        command=lambda: switch_turn(player_2),
        relief="flat"
    )
    button_3.place(
        x=679.0,
        y=440.0,
        width=280.0,
        height=40.0
    )

    button_image_4 = PhotoImage(
        file=FRAME_PATH / "roll_2.png")
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        state = 'disabled',
        command=lambda:roll(player_2, image_2),
        relief="flat"
    )
    button_4.place(
        x=679.0,
        y=375.0,
        width=280.0,
        height=40.0
    )
    window.resizable(False, False)
    window.mainloop()
def winner_screen(winner : Player):
    FRAME_PATH = Path(ASSET_PATH / "winner_screen")
    mixer.music.load(SOUNDTRACK_PATH / "Super Mario World Music_ Level Complete.mp3")
    mixer.music.play(loops=0)
    
    
    window.geometry("354x551")
    window.configure(bg = "#19191E")


    canvas = Canvas(
        window,
        bg = "#19191E",
        height = 551,
        width = 354,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        87.0,
        11.0,
        anchor="nw",
        text="We Have \na Winner!",
        fill="#E9CFFE",
        font=("Inter SemiBold", 34 * -1)
    )

    canvas.create_text(
        83.0,
        326.0,
        anchor="nw",
        text="Congrats!",
        fill="#E9CFFE",
        font=("Inter SemiBold", 34 * -1)
    )

    canvas.create_text(
        105.0,
        111.0,
        anchor="nw",
        text=winner.name,
        fill="#E9CFFE",
        font=("Inter SemiBold", 34 * -1)
    )

    button_image_1 = PhotoImage(
        file=FRAME_PATH / "play_again.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: home_screen(),
        relief="flat"
    )
    button_1.place(
        x=75.0,
        y=451.0,
        width=184.0,
        height=33.0
    )

    button_image_2 = PhotoImage(
        file=FRAME_PATH / "quit.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: window.destroy(),
        relief="flat"
    )
    button_2.place(
        x=75.0,
        y=403.0,
        width=184.0,
        height=33.0
    )

    image_image_1 = PhotoImage(
        file=FRAME_PATH / "trophy.png")
    image_1 = canvas.create_image(
        158.0,
        238.0,
        image=image_image_1
    )
    window.resizable(False, False)
    window.mainloop()



    return True
if __name__ == "__main__":
    main()