from time import sleep
import pygame
import pygame_menu
import Main
from pygame_menu import themes

pygame.init()
surface = pygame.display.set_mode((1380,720))



    
def set_difficulty(value,difficulty):
    print(difficulty)
    
def set_song(value,song):
    print(song)
    
def get_difficulty(widget):
    return widget.get_value()

def start_the_game():
    mainmenu.disable()
    Main.Launcher(songSwitch.get_value(),diffSwitch.get_value(),myName.get_value())
    mainmenu.enable()
    




mainmenu = pygame_menu.Menu('Welcome', 1380, 720, theme=themes.THEME_DARK)
myName = mainmenu.add.text_input('Name: ', default='username', maxchar=20)
mainmenu.add.button('Play', start_the_game)

mainmenu.add.button('Quit', pygame_menu.events.EXIT)


diffSwitch = mainmenu.add.selector('Difficulty :', [('Expert',0),('Hard', 1), ('Medium', 2),('Easy',3)], onchange=set_difficulty)


songSwitch = mainmenu.add.selector('Song:', [("Guns N_ Roses - Welcome To The Jungle",0),
                            ("Weezer - My Name Is Jonas", 1),
                            ("Pearl Jam - Even Flow", 2),
                            ("Heart - Barracuda",3),
                            ("Metallica - One",4)], onchange=set_difficulty)


####################driver code##############
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)

    pygame.display.update()