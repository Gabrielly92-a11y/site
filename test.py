import time 

letra_musica = """"
    imagine there´s no heaven
    it´s easy if you try
    no hell below us
    above us, only sky
    imagine all the people
    living for today....aha-ah..
    
    imagine there´s no countries
    it isn´t hard to do
    nothing to kill or die for
    and no religion, too
    imagine all the people
    living life in peace... you...
    
    you may say i´m a dreamer
    but i´m not the only one
    i hope someday you´ll join us
    and the world will be as one
    
    imagine no possessions
    i wonder if you can
    no need for greed or hunger
    a brotherhood of man
    imagine all the people
    sharing all the world... you..
    
    you may say i´m a dreamer
    but i´m not the only one
    i hope someday you´ll join us
    and the world wiil live as one"""

for linha in letra_musica.split('\n'):
    print(f"\033{linha}\033[0m")
    time.sleep(1.5)

print(letra_musica)