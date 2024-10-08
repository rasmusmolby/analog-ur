import pygame
import math
import datetime
import time
import random

# Initializes pygame and mixer
pygame.init()
pygame.mixer.init()

# Set up the screen dimensions (Large letters because fixed values)
WIDTH, HEIGHT = 680,680


# Initiate the display as "screen"
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# Sounds for the watch and their intensity
fart1 = pygame.mixer.Sound(r'Fart1.mp3')
fart2 = pygame.mixer.Sound(r'Fart2.mp3')
fart3 = pygame.mixer.Sound(r'Fart3.mp3')
fart4 = pygame.mixer.Sound(r'Fart4.mp3')
fart5 = pygame.mixer.Sound(r'Fart5.mp3')
fart6 = pygame.mixer.Sound(r'Fart6.mp3')
fart7 = pygame.mixer.Sound(r'Fart7.mp3')
fart8 = pygame.mixer.Sound(r'Fart8.mp3')
fart9 = pygame.mixer.Sound(r'Fart9.mp3')
fart_minute = pygame.mixer.Sound(r'fart_minute.mp3')
fart_hour = pygame.mixer.Sound(r'Farthour.mp3')
intro_fart = pygame.mixer.Sound(r'der_pruttes.mp3')


#Initiate the time
now = datetime.datetime.now()
hour = now.hour
minute = now.minute
second = now.second
day = now.day
local_minute = minute
local_hour = hour

# Date for watch
font = pygame.font.Font(None, 60)

# Background image :)
background = pygame.image.load('rolex.jpg')

# Random fart selecter for the watch.
# Only for the second hand
def fart_second():
    random_pick = random.randint(1,10)
    if random_pick == 1:
        fart1.play()
    elif random_pick == 2:
        fart2.play()
    elif random_pick == 3:
        fart3.play()
    elif random_pick == 4:
        fart4.play()
    elif random_pick == 5:
        fart5.play()
    elif random_pick == 6:
        fart6.play()
    elif random_pick == 7:
        fart7.play()
    elif random_pick == 8:
        fart8.play()
    else:
        fart9.play()





#Function to draw the actual face of the watch
def draw_watch_face(screen):

    # Background initilisation
    screen.blit(background,(-60,-56))
    

    # Define the center of the watch
    center = (HEIGHT // 2, WIDTH // 2)
    
    # Draws the circle for the watch
    pygame.draw.circle(screen, (0,0,0), center,WIDTH // 2 , 5)

    # Draw the hour and minute marks
    draw_hour_marks(screen, center)
    draw_minute_marks(screen, center)
    
    # Draw the different hands
    draw_hour_line(screen, center)
    draw_minute_line(screen,center)
    draw_second_line(screen,center)

    # Date for watch 
    dato = font.render(str(day), True, (0,0,0))
    screen.blit(dato, [550, 322])


    # Draw the center circle for the watch
    pygame.draw.circle(screen, (212,175,55),center, 30)
    pygame.draw.circle(screen, (0,0,0),center, 20)
    pygame.draw.circle(screen, (212,175,55),center, 10)
    pygame.draw.circle(screen, (0,0,0),center, 1)


# Draws the hour marks for the watch
# Made by calculating the different x and y points
# and drawing a line between them.
# Center is defined by x and y values. Set as a list so
# if the screen is edited, it syncs
def draw_hour_marks(screen, center):
    for i in range(12):
        # Using radians to calculate the lines
        angle = i * (2 * math.pi / 12) # Angel calculations for the hour marks
        x_start = center[0] + math.cos(angle) * (WIDTH // 2 - 50) # Start closer to the center???
        y_start = center[1] + math.sin(angle) * (HEIGHT // 2 - 50)
        x_end = center[0] + math.cos(angle) * (WIDTH // 2 - 20)
        y_end = center[1] + math.sin(angle) * (HEIGHT // 2 - 20)
        pygame.draw.line(screen,(0,0,0),(x_start,y_start),(x_end,y_end),5)
    
# Draws the minute marks for the watch
def draw_minute_marks(screen, center):
    # Using radians to calculate the lines
    for i in range(60):
        angle = i * (2* math.pi / 60) 
        x_start = center[0] + math.cos(angle) * (WIDTH // 2-40)
        y_start = center[1] + math.sin(angle) * (HEIGHT // 2 - 40)
        x_end = center[0] + math.cos(angle) * (WIDTH // 2 - 20)
        y_end = center[1] + math.sin(angle) * (HEIGHT // 2 - 20)

        # Draw the lines for minutes
        pygame.draw.aaline(screen,(0,0,0),(x_start,y_start),(x_end,y_end),100)

# Draws the hour hand for the hour and plays the sound
def draw_hour_line(screen, center):
    global local_hour
    # Using radians to calculate the lines
    angle = (hour % 12 + minute / 60) * (2 * math.pi / 12) - math.pi / 2
    x_start = center[0]
    y_start = center[1]
    x_end = center[0] + math.cos(angle) * (WIDTH // 2- 130)
    y_end = center[1] + math.sin(angle) * (HEIGHT // 2 - 130)
    pygame.draw.line(screen,(255,0,0),(x_start,y_start),(x_end,y_end),10)
    if hour != local_hour:
        local_hour = hour
        fart_hour.play()

# Draws the second hand for the watch and plays the sound
def draw_second_line(screen, center):
    # Using radians to calculate the lines
    angle = second * (2 * math.pi / 60) - math.pi / 2
    x_start = center[0]
    y_start = center[1]
    x_end = center[0] + math.cos(angle) * (WIDTH // 2 - 80)
    y_end = center[1] + math.sin(angle) * (HEIGHT // 2 - 80)
    pygame.draw.line(screen,(0,255,0),(x_start,y_start),(x_end,y_end),6)
    fart_second()

# Draws the minute hand for the watch and plays the sound
def draw_minute_line(screen, center):
    global local_minute
    # Using radians to calculate the lines
    angle = minute * (2 * math.pi / 60) - math.pi / 2
    x_start = center[0]
    y_start = center[1]
    x_end = center[0] + math.cos(angle) * (WIDTH // 2 - 80)
    y_end = center[1] + math.sin(angle) * (HEIGHT // 2 - 80)
    pygame.draw.line(screen,(255,255,0),(x_start,y_start),(x_end,y_end),10)
    if minute != local_minute:
        local_minute = minute
        fart_minute.play()



# Plays the intro sound for the watch
intro_fart.play()

# Loop for the game to run
running = True # Flag for the game to run
while running: # While running == True, this loop will happen
    for event in pygame.event.get(): # Loops through all events that pygame has stored (clicks, movement, window closing etc)
        if event.type == pygame.QUIT: # Checks if the event is "pygame.QUIT", it sets running to false and stops the loop.
            running = False

    # Time to make the sounds sync with the watch
    time.sleep(1)
    draw_watch_face(screen) 

    # Initiate time for clock
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second


    # Updates the display
    pygame.display.flip()