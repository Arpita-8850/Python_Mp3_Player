from tkinter import *
import tkinter
import pygame
from tkinter import filedialog


#------------ CREATING A WINDOW ---------------
root = Tk()  # creating an object named 'root'
root.title('Music Player')  #assigning the title of the window
root.geometry("600x470")  #defining the dimensions of the window
root.configure(bg='#fffafa', 
               highlightbackground="#f5d300",  
               highlightcolor="#f5d300",  
               highlightthickness=5)  
pygame.mixer.init()  # Initializing PyGame mixer


# ---------------- ADD SONGS -----------------
def add_songs():
    # Giving path fo the music folder
    songs = filedialog.askopenfilenames(initialdir="C:\\Users\\karpi\\OneDrive\\Desktop\\Music", title="Choose Songs", filetypes=(("mp3 Files", "*.mp3"),))

    #for loop to insert songs in the queue
    for song in songs:
        song = song.replace("C:/Users/karpi/OneDrive/Desktop/Music/", "")
        song = song.replace(".mp3", "")
        #Insert into playlist
        song_box.insert(END, song)


# ----------Create Global Play Flag Variable-------------
global playFlag, firstTimePlay
playFlag = False
firstTimePlay = True


#--------------PLAY FUNCTION--------------
def play():
    global playFlag, firstTimePlay  #definig two global variabeles 'playFlag' and 'firstTimePlay'
    
    if firstTimePlay == True:
        # to play a song for first time
        new_song = song_box.get(ACTIVE)  #geeting the current/active song from the playlist
        new_song = f'C:/Users/karpi/OneDrive/Desktop/Music/{new_song}.mp3'  #definig the path for the song 
        pygame.mixer.music.load(new_song)  #playing the active/current song
        pygame.mixer.music.play(loops=0)   # not keeping the song in loop
        var.set(song_box.get(tkinter.ACTIVE))  #setting the 'var' to display the title of the cureent song on top
        play_pause_btn.configure(image=pause_btn_img)  #showing the the pause icon
        firstTimePlay = False 
        playFlag = True
    
    else:
        if playFlag == True:
            # we have to Pause
            pygame.mixer.music.pause()
            play_pause_btn.configure(image=play_btn_img)
            playFlag = False
        else:
            # we have to Unpause i.e. play
            pygame.mixer.music.unpause()
            play_pause_btn.configure(image=pause_btn_img)
            playFlag = True
    
    
#--------------STOP FUNCTION--------------
def stop():
    pygame.mixer.music.stop()
    play_pause_btn.configure(image=play_btn_img)
    song_box.selection_clear(ACTIVE)


#--------------PLAY NEXT FUNCTION--------------
def next_song():

    next_one = song_box.curselection() # Get the current song tuple number
    next_one = next_one[0]+1 # Add one to the current song number
    song = song_box.get(next_one) # Grab song title from playlist
    song = f'C:/Users/karpi/OneDrive/Desktop/Music/{song}.mp3' #add directory structure and mp3 to song title
    pygame.mixer.music.load(song)  #load and play song
    pygame.mixer.music.play(loops=0)   # not keeping the song in loop
    song_box.selection_clear(0, END)  # Clear active bar in playlist box
    song_box.activate(next_one) #Activate new song bar
    song_box.selection_set(next_one, last=None) # Set Activate bar to next song
    var.set(song_box.get(tkinter.ACTIVE))  #setting the 'var' to display the title of the cureent song on top


#--------------PLAY PREVIOUS FUNCTION--------------
def previous_song():
   
    previous_one = song_box.curselection()  # Get the current song tuple number  
    previous_one = previous_one[0] - 1  # Add one to the current song number
    song = song_box.get(previous_one)  # Grab song title from playlist
    song = f'C:/Users/karpi/OneDrive/Desktop/Music/{song}.mp3'   # add directory structure and mp3 to song title
    pygame.mixer.music.load(song)  # load and play song
    pygame.mixer.music.play(loops=0)   # not keeping the song in loop
    song_box.selection_clear(0, END)  # Clear active bar in playlist box
    song_box.activate(previous_one) # Activate new song bar    
    song_box.selection_set(previous_one, last=None) # Set Activate bar to next song
    var.set(song_box.get(tkinter.ACTIVE))


#--------------DELETE SINGLE FUNCTION--------------
def delete_song():
    song_box.delete(ANCHOR)  #delete the current/active song
    pygame.mixer.music.stop()  #stop the curent played song


#--------------DELETE ALL FUNCTION--------------
def delete_all_songs():
    song_box.delete(0, END)  #Delete all songs
    pygame.mixer.stop()    #Stop Music if its playing


# --------------PLAY SELECTED SONG FUNCTION--------------
def playClickedSong(event):
    global playFlag, firstTimePlay
    firstTimePlay = True
    playFlag = False


# -----------------SHWOWING THE TITLE OF THE CURRENT PLAYED SONG-------------------
var = tkinter.StringVar() 
song_title = tkinter.Label(root, font=("calibri 20 underline"), fg = "black", textvariable = var, bg="#fffafa")
song_title.pack()


#------------------CREATING A PLAYLIST BOX---------------
song_box = Listbox(root, 
                   bg="#241571", 
                   width=67, 
                   height=15, 
                   highlightcolor="black", 
                   highlightbackground="black",
                   highlightthickness=2, 
                   font="calibri 12",
                   fg="#fffafa", 
                   selectbackground = "#2832c2", 
                   borderwidth=0, )
song_box.bind('<<ListboxSelect>>', playClickedSong) #when a song is selected on the playlist then go to 'playClickedSong' function
song_box.pack(pady=1)  #giving padding on y-axis = 1


# ------------------GIVING PATH FOR THE BUTTONS ICONS---------------
back_btn_img = PhotoImage(file="C:\\Users\\karpi\\OneDrive\\Desktop\\Python\\mp3 player\\icon3\\back.png")
forward_btn_img= PhotoImage(file="C:\\Users\\karpi\\OneDrive\\Desktop\\Python\\mp3 player\\icon3\\next.png")
play_btn_img = PhotoImage(file="C:\\Users\\karpi\\OneDrive\\Desktop\\Python\\mp3 player\\icon3\\play.png")
pause_btn_img = PhotoImage(file="C:\\Users\\karpi\\OneDrive\\Desktop\\Python\\mp3 player\\icon3\\pause.png")
stop_btn_img = PhotoImage(file="C:\\Users\\karpi\\OneDrive\\Desktop\\Python\\mp3 player\\icon3\\stop.png")


#------------------CREATING A FRAME FOR THE BUTTONS---------------
# creating a frame for the button so that all the buttons are in one line
controls_frame = Frame(root, bg = '#fffafa')  
controls_frame.pack()


#------------------CREATING BUTTONS AND DEFINING ALL PARAMETERS FOR THE BUTTONS---------------
# defining all the parameters for buttons like background color, image path and commands for each button
back_btn = Button(controls_frame, image = back_btn_img, borderwidth=0, command=previous_song, bg="#fffafa", activebackground="#fffafa")
forward_btn = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song, bg="#fffafa", activebackground="#fffafa")
play_pause_btn = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play, bg="#fffafa", activebackground="#fffafa")
stop_btn = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop, bg="#fffafa", activebackground="#fffafa")


#------------------PUTTNING THE BUTTONS IN A GRID---------------
# putting all the buttons in a tabul3 format. there is only 1 row (row=0) and 4 columns (columns range = 0 to 4)
back_btn.grid(row=0,column=0, pady=15, padx=15)
play_pause_btn.grid(row=0,column=1, pady=15, padx=15)
forward_btn.grid(row=0,column=2, pady=15, padx=15)
stop_btn.grid(row=0,column=4, pady=15, padx=15)


#------------------CREATING A MENU BAR---------------
my_menu = Menu(root)
root.config(menu=my_menu)


#------------------CREATING 'ADD SONGS' DROPDOWN IN MENU BAR ---------------
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", command=add_songs)


#------------------CREATING 'DELETE A SONG' & 'DELETE ALL SONGS' DROPDOWNS IN MENU BAR ---------------
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Delete Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song from playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs from playlist", command=delete_all_songs)


# ------------------STARTING MAIN LOOP ---------------
root.mainloop()