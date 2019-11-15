#!/usr/bin/env python3

'''
HexadecimalAndBinaryBingo16to31.py

for use with bingo cards




'''

import sys
import random
import pygame
from tkinter import messagebox
from time import sleep

#CONSTANTS
MIN_ASCII_VALUE = 97 
MAX_ASCII_VALUE = 122
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 800

BACKGROUND_COLOR=(90,30,90)
FOREGROUND_COLOR=(0,255,255)

gameDisplay = pygame.display.set_mode((0, 0))
pygame.font.init()               
myfont = pygame.font.SysFont('arial', 36, 'Comic Sans MS', 40)
myfont_big = pygame.font.SysFont('arial', 40, 'Comic Sans', 54)

choicesDone = []
choices = ['0b10000', '0b10001', '0b10010', '0b10011', '0b10100', '0b10101', '0b10110', '0b10111', '0b11000', '0b11001', '0b11010', '0b11011', '0b11100', '0b11101', '0b11110', '0b11111', 'Ox10', 'Ox11', 'Ox12', 'Ox13', 'Ox14', 'Ox15', 'Ox16', 'Ox17', 'Ox18', 'Ox19', 'Ox1a', 'Ox1b', 'Ox1c', 'Ox1d', 'Ox1e', 'Ox1f']

# this worked print("choices are " + str(choices))

line1 = "Type any letter when you are ready"
line2 = 'to get a randomly selected Bingo call.'
line3 = 'press y to start a new game press q to close the game'

def main():
    screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption('Bingo Selector for Hexadecimal and Binary 16 to 31')
    screen.fill(BACKGROUND_COLOR)
    display_message(screen, line1, FOREGROUND_COLOR, (150, 100))
    display_message(screen, line2, FOREGROUND_COLOR, (150, 140))
    display_message(screen, line3, FOREGROUND_COLOR, (150, 180))
    pygame.display.flip()
    how = True
    while how == True:

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
            else:
                letter = ask_letter(screen, 80, 350)
                if letter == "":
                    how = False
                    main()
                # starts new game and resets
                elif letter.lower() == 'y':
                    how = False
                    choicesDone = []
                    choices = ['0b10000', '0b10001', '0b10010', '0b10011', '0b10100', '0b10101', '0b10110', '0b10111', '0b11000', '0b11001', '0b11010', '0b11011', '0b11100', '0b11101', '0b11110', '0b11111', 'Ox10', 'Ox11', 'Ox12', 'Ox13', 'Ox14', 'Ox15', 'Ox16', 'Ox17', 'Ox18', 'Ox19', 'Ox1a', 'Ox1b', 'Ox1c', 'Ox1d', 'Ox1e', 'Ox1f']
                    #print(choices)
                    #print(choicesDone)
                    main()
                elif letter.lower() == 'q':
                    line25 = "Thank you so very much for playing!" 
                    screen.fill(BACKGROUND_COLOR)
                    display_message(screen, line25, FOREGROUND_COLOR, (180, 230))
                    sleep(2)
                    line27 = "Good Bye!" 
                    screen.fill(BACKGROUND_COLOR)
                    display_message(screen, line27, FOREGROUND_COLOR, (180, 230))
                    sleep(1)
                    sys.exit()
                else:
                    wordA = generate_choice()
                    updateChoices(wordA)

            screen.fill(BACKGROUND_COLOR)
            line5 = "The Next Number to call is: " 
            display_message(screen, line5 + str(wordA), FOREGROUND_COLOR, (0, 230))
            line6 = "The Numbers you have already called are: "
            display_message(screen, line6, FOREGROUND_COLOR, (180, 310))
            global choicesDone
            if len(choicesDone) >= 1:
                line7 = str(choicesDone[:4])
                display_message(screen, line7, FOREGROUND_COLOR, (180, 350))
            if len(choicesDone) > 4:
                line9 = str(choicesDone[4:8])
                display_message(screen, line9, FOREGROUND_COLOR, (180, 390))
            if len(choicesDone) > 8:
                line11 = str(choicesDone[8:12])
                display_message(screen, line11, FOREGROUND_COLOR, (180, 430))
            if len(choicesDone) > 12:
                line13 = str(choicesDone[12:16])
                display_message(screen, line13, FOREGROUND_COLOR, (180, 470))
            if len(choicesDone) > 16:
                line15 = str(choicesDone[16:20])
                display_message(screen, line15, FOREGROUND_COLOR, (180, 510))
            if len(choicesDone) > 20:
                line17 = str(choicesDone[20:24])
                display_message(screen, line17, FOREGROUND_COLOR, (180, 550))
            if len(choicesDone) > 24:
                line19 = str(choicesDone[24:28])
                display_message(screen, line19, FOREGROUND_COLOR, (180, 590))
            if len(choicesDone) > 28:
                line21 = str(choicesDone[28:33])
                display_message(screen, line21, FOREGROUND_COLOR, (180, 630))
            if len(choicesDone) == 32:
                line31 = "All choices have been called press y to start over q to close this program!"
                display_message(screen, line31, FOREGROUND_COLOR, (180, 670)) 
            pygame.display.flip()


def updateChoices(word):
    global choicesDone
    choicesDone = sorted(choicesDone)
    
           
def display_message(screen, message, color, pos = (50, 30)):
    text = myfont.render(message, False, color)
    screen.blit(text, pos)
    pygame.display.flip()

def show_message_box(screen, message):
    sleep(2)
    screen.fill((90,30,30))
    text = myfont_big.render(message, False, (95, 255, 55))
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    sleep(3)

def detect_pressed_key(screen, key_pressed_ascii):
    key_pressed = ""
    if key_pressed_ascii >= MIN_ASCII_VALUE and key_pressed_ascii <= MAX_ASCII_VALUE: 
        key_pressed = chr(key_pressed_ascii)
        if key_pressed == "":
            pass
        else:
            return key_pressed
    else:
        
        return key_pressed   

def ask_letter(screen, cord_x = 50, cord_y = 50):
    running = True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                 sys.exit()
            if events.type == pygame.KEYDOWN:
                letter = detect_pressed_key(screen, events.key)
                running = False
    return letter
               
def generate_choice():
    global choices
    global choicesDone
    if len(choices) > 0:
        numberBig = random.randint(0, 12345)
        number = choices[numberBig % len(choices)]
        numberW = numberBig % len(choices)
        choicesDone.append(choices.pop(numberW))
        return number
    else:
        choicesDone = []
        choices = ['0b10000', '0b10001', '0b10010', '0b10011', '0b10100', '0b10101', '0b10110', '0b10111', '0b11000', '0b11001', '0b11010', '0b11011', '0b11100', '0b11101', '0b11110', '0b11111', 'Ox10', 'Ox11', 'Ox12', 'Ox13', 'Ox14', 'Ox15', 'Ox16', 'Ox17', 'Ox18', 'Ox19', 'Ox1a', 'Ox1b', 'Ox1c', 'Ox1d', 'Ox1e', 'Ox1f']
        numberBig = random.randint(0, 12345)
        number = choices[numberBig % len(choices)]
        numberW = numberBig % len(choices)
        choicesDone.append(choices.pop(numberW))
        return number

if __name__=="__main__":
  main()
