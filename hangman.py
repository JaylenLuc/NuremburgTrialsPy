#!/usr/bin/env python3
from ctypes import sizeof
from inspect import _void
from multiprocessing.sharedctypes import Value
import random
import requests
import time
import math
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
import os
os.system("")


# Return a single random word
#print("fhejakhdlj5".isnumeric)
#print(r.get_random_word())
class text_fucker:

    red = '\033[91m'
    cyan = '\033[96m'
    yellow = "\x1b[33;20m"
    green = '\033[92m'
    blue = '\033[94m'
    bright_mag = '\u001b[35;1m'

    color_list = [red,cyan,green,blue,bright_mag]
    #--------------------
    bold = '\033[1m'
    italics = '\033[3m'
    underline = '\033[4m'
    end = '\033[0m'



class Player :
    _count = 0

    def __init__(self, name : str):
        self.color = ""
        Player._count+= 1

        self.player_count = Player._count

        self.name = name

        if len(name) == 0: self.name = "Player " + str(Player._count)
        

        
    
    @staticmethod
    def _clear_count() -> _void:
        Player._count = 0
    
    @staticmethod
    def get_count() -> int :
        return Player._count

    def get_name(self) -> str:
        return self.name
    
    def get_count_instance(self) -> int :
        return self.player_count

    def set_color(self, color):
        self.color = color

class Game_runner:
    gallow="                _____________________ \n"+\
       "                |                    |\n"+\
       "                |                    |\n"+\
       "                |                    |\n"+\
       "                |                    |\n"+\
       "                |                    |"
    gallow2=["                                     |",
       "                                     |",
       "                                     |",
       "                                     |",
       "                                     |",
       "                                     |",
       "                                     |",
       "                                     |",
       "                                     |",
       "                                     |"]
#in order ot fix the formatting issue, i think i shoudl format the hangman node strings  into the gallow strings
#this prolly means that before even printing the gallow i would need to check the hang man nodes first and if
#there are any to print, format it into the gallow string and then only aafter the checks are done do we print them
#monolothically, if there are no nodes in a particular string inthe gallows then they should be empty spaces
    hangman_nodes= {
    .1:"             ( ͡° ͜ʖ ͡°)                |",
    .2:"               /|\\                   |",
    .3:"              / | \\                  |",
    .4:"             /  |  \\                 |",
    .5:"            m   8=D  m               |",
    .6:"              /     \                |",
    .7:"          |===|      |===|           |",
    .8:"          |   |      |   |           |",
    .9:"          /  &|      |&  \\           |",
    1:"       .-'`  , )*   *( ,  `'-.       |\n"+\
    '      ` """""`"`      `"`"""""`      |'
    }
    #EASY: ceiling of length of word * 2.5 = the max num of tries  
    #ratio of wrong answers / max num of tries = hangman_node progress
    #hangman_nodes_hard = {}
    def __init__(self, players : list[Player], word :str, diff :str):
        self.players = players
        self.word = word
        self.word_list = []
        self.wrong_count = 0
        self.ratio = 0
        self.difficulty = diff
        if self.difficulty == 'e': self.tries = math.ceil(len(self.word) *2.5)
        else: self.tries = math.ceil(len(self.word) *1.5)
    


    def runner(self):
        #5 -3 = 2
        #len(self.word) - len(word_list) =
        pointer = 0
        #print("self.word = ", self.word)
        while True:
            time.sleep(.5)
            print(chr(27) + "[2J")
            
            if pointer > len(self.players)-1:
                pointer = 0
            print()
            curr_color = self.players[pointer].color
            #print(curr_color + "*"*69 + text_fucker.end)
            print(curr_color + f"{self.players[pointer].get_name()}"+text_fucker.end+"'s TURN !!!" )
            wrong = False
            print(curr_color + Game_runner.gallow + text_fucker.end)
            curr_index = ""
            self.ratio = self.wrong_count / self.tries
            for k,v in Game_runner.hangman_nodes.items():
                if self.ratio >= k: print(curr_color + v +text_fucker.end)
                else: print(curr_color + "                                     |"+ text_fucker.end)

            
            [print(curr_color + "                                     |" + text_fucker.end) for i in range(3)]
            print()

            for i in range(len(self.word)):
                try: 
                    curr_index = self.word_list.index(self.word[i])
                    print(curr_color + text_fucker.underline + self.word_list[curr_index] + text_fucker.end + " ", end = '' )

                except ValueError:
                    print(curr_color +"_ " +text_fucker.end, end= '')
            print()
            inp = input((curr_color+ "Enter an alphabetical character: "+ text_fucker.end))
            print()
            print()
            if inp.isnumeric() or inp not in self.word or inp == "" or inp in self.word_list:
                self.wrong_count += 1
                self.ratio = self.wrong_count / self.tries
                wrong = True
            else:
                self.word_list.append(inp)
            #print(chr(27) + "[2J")
            
            print(curr_color +"Progress: |--------------------------------------------------| 0.0% Complete"+ text_fucker.end, end= "\r")
            #print(chr(27) + "[2J")
            #print()
            time.sleep(.15)
            print(curr_color +"Progress: |██████--------------------------------------------| 15.0% Complete"+ text_fucker.end, end= "\r")
            time.sleep(.15)
            print(curr_color +"Progress: |█████████████-------------------------------------| 30.0% Complete"+ text_fucker.end,end= "\r")
            #print()
            #print(chr(27) + "[2J")
            time.sleep(.15)
            print(curr_color +"Progress: |██████████████████--------------------------------| 40.0% Complete"+ text_fucker.end,end= "\r")
            time.sleep(.15)
            print(curr_color +"Progress: |███████████████████████---------------------------| 50.0% Complete"+ text_fucker.end,end= "\r")
            time.sleep(.15)
            print(curr_color +"Progress: |████████████████████████████████------------------| 60.0% Complete"+ text_fucker.end,end= "\r")
            time.sleep(.15)
            print(curr_color +"Progress: |███████████████████████████████████████-----------| 70.0% Complete"+ text_fucker.end,end= "\r")
            #print()
            #print(chr(27) + "[2J")
            time.sleep(.15)
            print(curr_color +"Progress: |████████████████████████████████████████████------| 85.0% Complete"+ text_fucker.end,end= "\r")
            time.sleep(.15)
            #print(chr(27) + "[2J")
            print(curr_color +"Progress: |██████████████████████████████████████████████████| 100.0% Complete"+ text_fucker.end,end= "\r")
            print()
            print()
            if wrong : 
                cprint(figlet_format(f'  " {inp} "  is wrong!!', font='big',width=190), 'red', attrs=['bold'])
                time.sleep(1)
                
            else:
                cprint(figlet_format(f'  " {inp} "  is correct!!',  font='big',width=190), 'green', attrs=['bold'])
                time.sleep(1)
            if self.ratio >= 1:
                print(curr_color + Game_runner.gallow + text_fucker.end)
                for k,v in Game_runner.hangman_nodes.items():
                    if self.ratio >= k:
                        print(curr_color +v +text_fucker.end)
                [print(curr_color + "                                     |" + text_fucker.end) for i in range(3)]
                print()
                print()
                time.sleep(.2)
                cprint(figlet_format("U    HAVE    LOST,    :((   !  !  ! ",  font='big',width=190), 'yellow', attrs=['bold'])
                time.sleep(.2)
                print()
                print(text_fucker.bold + text_fucker.blue+ "The word you have failed to guess is" + text_fucker.end, end = '')
                time.sleep(.9)
                print(text_fucker.bold + text_fucker.blue + "s" + text_fucker.end, end='')
                time.sleep(.9)
                print(text_fucker.bold + text_fucker.blue + "s" + text_fucker.end, end='')
                time.sleep(.9)
                print(text_fucker.bold + text_fucker.blue + "s:" + text_fucker.end)

                cprint(figlet_format(f"{self.word}",  font='big',width=190), 'magenta', attrs=['bold'])
                print()
                print()
                print(text_fucker.bold + text_fucker.blue + "(╥﹏╥)  (╥﹏╥)  (╥﹏╥)  (╥﹏╥)" + text_fucker.end)
                print()
                print()
                break

                    
            if set(self.word) ==  set(self.word_list) and self.ratio < 1:
                cprint(figlet_format("CONGRATS,    U     HAVE    WON    !!!",  font='big',width=190), 'yellow', attrs=['bold'])

                time.sleep(2)
                print( text_fucker.bold + "DONT FORGET TO PAY UR TAXES"+ text_fucker.end)
                time.sleep(1)
                print(
                '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠉⠉⠉⠋⠛⠛⠛⠻⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠄⠄⠄⠄⠄⠄⠄⠂⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠹⣿⣿⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⢻⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠄⢠⠄⠄⡀⠄⠄⢀⠂⠄⠄⠄⠄⠄⠄⠄⠄⠄⡁⠄⠄⢛⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⡈⢔⠸⣐⢕⢕⢵⢰⢱⢰⢐⢤⡡⡢⣕⢄⢢⢠⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡁⠂⠅⢕⠌⡎⡎⣎⢎⢮⢮⣳⡳⣝⢮⢺⢜⢕⢕⢍⢎⠪⡐⠄⠁⠄⠸⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠄⠄⢅⠣⡡⡣⣣⡳⡵⣝⡮⣗⣗⡯⣗⣟⡮⡮⣳⣣⣳⢱⢱⠱⣐⠄⠂⠄⢿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠂⠄⠄⠄⠄⠄⠄⢂⢈⠢⡱⡱⡝⣮⣿⣟⣿⣽⣷⣿⣯⣿⣷⣿⣿⣿⣾⣯⣗⡕⡇⡇⠄⠂⡀⢹⣿\n'+\
                '⣿⣿⣿⣿⣿⡟⠄⠄⠄⠄⠄⠄⠂⠄⠄⠄⠄⠄⠄⠐⢀⢂⢕⢸⢨⢪⢳⡫⣟⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡺⡮⡣⡣⠠⢂⠒⢸⣿\n'+\
                '⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠐⠄⡂⠆⡇⣗⣝⢮⢾⣻⣞⣿⣿⣿⣿⣿⣿⣿⣿⢿⣽⣯⡯⣺⢸⢘⠨⠔⡅⢨⣿\n'+\
                '⣿⣿⠋⠉⠙⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠁⠄⠄⠄⡂⡪⡪⡪⡮⡮⡯⣻⣽⣾⣿⣿⣿⣟⣿⣿⣿⣽⣿⣿⡯⣯⡺⡸⡰⡱⢐⡅⣼⣿\n'+\
                '⣿⠡⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠈⠆⠱⠑⠝⠜⠕⡝⡝⣞⢯⢿⣿⣿⡿⣟⣿⣿⣿⡿⡿⣽⣷⣽⡸⡨⡪⣂⠊⣿⣿\n'+\
                '⣿⠡⠄⡨⣢⠐⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠍⡓⣗⡽⣝⠽⠍⠅⠑⠁⠉⠘⠘⠘⠵⡑⢜⢀⢀⢉⢽\n'+\
                '⣿⠁⠠⢱⢘⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠈⠱⣁⠜⡘⠌⠄⠄⡪⣳⣟⡮⢅⠤⠠⠄⠄⣀⣀⡀⡀⠄⠈⡂⢲⡪⡠⣿\n'+\
                '⣿⡇⠨⣺⢐⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠄⠄⠄⠤⡠⡢⢒⠦⠠⠄⠄⠄⡸⢽⣟⢮⠢⡂⡐⠄⡈⡀⠤⡀⠄⠑⢄⠨⢸⡺⣐⣿\n'+\
                '⣿⣿⠈⠕⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡂⡪⡐⡥⢤⣰⣰⣰⡴⡮⠢⠂⠄⠄⡊⢮⢺⢕⢵⢥⡬⣌⣒⡚⣔⢚⢌⢨⢚⠌⣾⡪⣾⣿\n'+\
                '⣿⣿⣆⠄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡑⢕⢕⡯⡷⣕⢧⢓⢭⠨⡀⠄⡂⠨⡨⣪⡳⣝⢝⡽⣻⣻⣞⢽⣲⢳⢱⢡⠱⠨⣟⢺⣿⣿\n'+\
                '⣿⣿⣿⡆⠄⡅⠇⡄⠄⠄⠄⠄⠄⠄⠄⠐⠨⢪⢹⢽⢽⣺⢝⠉⠁⠁⠄⠄⠄⢌⢎⡖⡯⡎⡗⢝⠜⣶⣯⣻⢮⡻⣟⣳⡕⠅⣷⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣶⣶⣿⣷⠄⠄⠄⠄⠄⠄⠄⠄⠈⠔⡑⠕⠝⠄⡀⠄⠄⠊⢆⠂⠨⡪⣺⣮⣿⡾⡜⣜⡜⣄⠙⢞⣿⢿⡿⣗⢝⢸⣾⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⡀⠄⠄⠄⠄⢀⠄⠠⠄⠠⠄⠄⠄⠄⠄⠄⠊⠺⡹⠳⡙⡜⡓⡭⡺⡀⠄⠣⡻⡹⡸⠨⣣⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠠⠄⠄⣂⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢄⠤⡤⡄⡆⡯⡢⡣⡣⡓⢕⠽⣄⠄⠨⡂⢌⣼⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠈⠆⠄⠸⡂⠄⠄⠄⢀⠄⢀⠈⠄⠂⠁⠙⠝⠼⠭⠣⠣⠣⠑⠌⠢⠣⡣⡠⡘⣰⣱⣿⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⢑⠄⠈⡱⠄⢘⠄⡀⠨⢐⣧⣳⣷⣶⣦⣤⣴⣶⣶⣶⡶⠄⡠⡢⡕⣜⠎⡮⣣⣿⣿⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠢⠄⠨⠄⠄⠣⡀⠄⢀⢀⢙⠃⡿⢿⠿⡿⡿⢟⢋⢔⡱⣝⢜⡜⡪⡪⣵⣿⣿⣿⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⡁⠄⠄⠄⠄⠄⠄⠄⠅⠄⠡⠄⠄⠡⢀⢂⠢⡡⠡⠣⡑⣏⢯⡻⡳⣹⡺⡪⢎⠎⡆⢣⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⣇⠄⠄⠄⠄⠄⠄⠄⠐⠄⠄⠁⠄⢈⠄⢂⠕⡕⡝⢕⢎⢎⢮⢎⢯⢺⢸⢬⠣⢃⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠨⡐⠌⢆⢇⢧⢭⣣⡳⣵⢫⣳⢱⠱⢑⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠁⡊⢌⢢⢡⢣⢪⡺⡪⡎⡎⡎⡚⣨⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠕⡅⢗⢕⡳⡭⣳⢕⠕⡱⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠌⠄⠑⠩⢈⢂⣱⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡀⢄⠄⣀⠄⡀⣀⢠⢄⣖⣖⣞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣱⡐⡕⡕⡽⣝⣟⣮⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n'+\
                '⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣵⣽⣸⣃⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
                return
            pointer += 1



    def print_word(self):
        print(self.word)
        cprint(figlet_format(f'  {self.word}', font='isometric3',width=190),
        'blue', attrs=['bold'])
            
    

running = True
cprint(figlet_format('  THE\nOFFICIAL\nHANG MAN\nCOMMAND\nLINE GAME', font='isometric3',width=120),
        'blue', attrs=['bold'])
time.sleep(1)
print(chr(27) + "[2J")
cprint(figlet_format('  THE\nOFFICIAL\nHANG MAN\nCOMMAND\nLINE GAME', font='isometric1',width=120),
'magenta', attrs=['bold'])
time.sleep(1)
print(chr(27) + "[2J")
cprint(figlet_format('  THE\nOFFICIAL\nHANG MAN\nCOMMAND\nLINE GAME', font='isometric3',width=120),
'yellow', attrs=['bold'])
time.sleep(1)
print(chr(27) + "[2J")
cprint(figlet_format('  THE\nOFFICIAL\nHANG MAN\nCOMMAND\nLINE GAME', font='isometric1',width=120),
'cyan', attrs=['bold'])
time.sleep(1)
print(chr(27) + "[2J")
cprint(figlet_format('  THE\nOFFICIAL\nHANG MAN\nCOMMAND\nLINE GAME', font='isometric3',width=120),
'green', attrs=['bold'])
print()
print()
uu = ""
while uu.upper() != 'obama is a war criminal'.upper():
    uu = input(text_fucker.bold + text_fucker.yellow+ "TYPE 'obama is a war criminal' TO CONTINUE!!!" + text_fucker.end)

while True:
    
    while True:
        try: 

            num_players = int(input("Enter the number of players "+ text_fucker.italics+" (Max # of players is"+text_fucker.red+" 5"+text_fucker.end+"): "+ text_fucker.end))

            if num_players < 1 or num_players > 5:
                raise ValueError
            break
        except ValueError:

            print("Please enter a digit "+text_fucker.red+" 1-5"+ text_fucker.end)
            continue
    
    temp = []

    for index, i in enumerate(range(num_players)):
        print()
        temp.append(Player(input(f"Enter "+ text_fucker.bold +f"Player {index+1}'s" +text_fucker.end +" name "+ text_fucker.italics + "(Default player name will be given upon no answer)" + text_fucker.end+": ")))
    #testers
    print()
    print(text_fucker.bold + f"{Player.get_count()} "+text_fucker.end+"Player(s) in Lobby: ")
    print("--"*50)
    random.shuffle(text_fucker.color_list)
    for index, i in enumerate(temp):
        i.set_color(text_fucker.color_list[index])
        print(text_fucker.color_list[index] + i.get_name()+text_fucker.end)
        print()
    print("--"*50)
    print()
    print()
    #ask to determine difficulty of game

    #actually design game logic and advancement which will be in the Game_runner runner() function
    chosen_word = ""
    while True:
        word_opt = input("Generate a random word "+text_fucker.bold + "enter 'y'"+ text_fucker.end+ text_fucker.red+
        " OR"+text_fucker.end+" Have a nonpartisan member choose a word for you "+text_fucker.bold + "enter 'n'"+ text_fucker.end + ": ")
        if word_opt in ('n','N'):
            while True:
                chosen_word = input("Enter a word under "+text_fucker.red+"26"+text_fucker.end+" characters: ")
                if len(chosen_word) >= 26 or not chosen_word.isalpha(): continue
                else: break
            
        elif word_opt in ('y','Y'): 
            word_list = requests.get('https://www.mit.edu/~ecprice/wordlist.10000'
            ).content.decode('utf-8').splitlines()
            chosen_word = random.choice(word_list)
            #print("word::   ", chosen_word)
            break



        else: 
            print("Please enter either a 'y' or 'n' as indicated")
            print()
            continue
        break
    print()
    print(text_fucker.yellow + text_fucker.bold + "THE CHOSEN WORD ISSSSSSSS " + text_fucker.end, end= '' )
    for i in range(0,5):
        time.sleep(.35)
        print(text_fucker.yellow + text_fucker.bold + "." + text_fucker.end,end= '')
    print()
    print(text_fucker.yellow + text_fucker.bold + "sike! that would defeat the purpose of the game !!!" + text_fucker.end) 
    time.sleep(2)
    print()
    print()
    print(text_fucker.bright_mag + "now " +text_fucker.end, end = '')
    time.sleep(1.5)
    diff = ""
    while True:
        print(text_fucker.bright_mag + "we can do this the EASY way "+text_fucker.end+text_fucker.bold+"(enter 'e') "+text_fucker.end, end ='')
        time.sleep(1.5)
        diff = input(text_fucker.bright_mag+ "or the HARD way ( ͡° ͜ʖ ͡°) "+text_fucker.end+text_fucker.bold+"(enter 'h'): "+ text_fucker.end)
        if diff in ('e','E'):
            diff = 'e'
            break
        elif diff in ('h','H'):
            diff = 'h'
            break
        else: continue
    current_runner = Game_runner(temp, chosen_word, diff)
    current_runner.runner()
    #-------------------------------------------------------------------------------------------------------------
    #if player decides to play again then :
    Player._count = 0

    again = input("Play again? Enter 'y' or 'n': " )
    if again in ('y','Y'):
        continue
    else:
        break
print()
print()
print()
cprint(figlet_format(f'G O O D   B Y E    !!!', font='isometric3',width=190),
        'blue', attrs=['bold'])
    


