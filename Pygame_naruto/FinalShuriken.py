import pygame, sys
import os
import time
import random
import pygame.mixer
from pygame.locals import*

pygame.init()
 
display_width = 787
display_height = 657

black = (0,0,0)
white = (255,255,255)
rasen = (240,255,255)
bright_red = (255,255,255)
bright_rasen = (224,255,255)
DeepSkyBlue = (0,191,255)
LightSkyBlue = (135,206,250)
SkyBlue	= (135,206,235)
block_color = (53,115,255)
Aqua = (0,255,255)

 
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption(' - Naruto - Final Shuriken ')
clock = pygame.time.Clock()

lista = []


def ranking(scorefinal):
    global lista
    pygame.init()
    pygame.font.init()
    posição = 1
    screen = pygame.display.set_mode((847,596))
    smallText = pygame.font.SysFont("mistral",30)
    folder = 'img'
    fundo = pygame.image.load(os.path.join(folder,"Ran.jpg"))
    screen.blit(fundo,(0,0))
    lista.append(scorefinal)
    lista.sort(reverse=True)
    ranque = smallText.render("--------------RANKING--------------",1,(white))
    novamente = smallText.render("-APERTE A TECLA DE ESPAÇO PARA TENTAR MAIS UMA VEZ!-",1,(white))
    sair = smallText.render("-PARA SAIR APERTE A TECLA X-",1,(white))
    y = 80
    x = 0
    i = 0
    print(" - Nome e Pontuação - ")
    nome = input("Digite seu nome")
    if nome == ' ':
        nome = input("Digite um nome válido")
    print("pontuação do",nome,"foi",scorefinal)
    
    for i in lista:
        if posição == 11:
            break
        posicao = str(posição) + "-   "  + str(i) + "  PONTOS"
        rank = smallText.render(posicao,1,(white))
        screen.blit(rank,(320,y))
        y += 20
        posição += 1
        opcao = True
    while opcao == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    narutoGame()
                    
                if event.key == pygame.K_x:
                    pygame.quit()
                    quit()
        
       
                pygame.quit()
                sys.exit() 
        screen.blit(ranque,(300,50))
        screen.blit(novamente,(150,480))
        screen.blit(sair,(180,520))
        pygame.display.update()
    

    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

   
        if click[0] == 1 and action != None:
            action()
     
            
            
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("mistral",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()

def creditos():
    folder = "img"
    #creditos
    creditos = pygame.image.load(os.path.join(folder,"CREDITOS.png"))
    screen.blit(creditos,(0,0))

def inst():
    folder = "img"
    #creditos
    ins = pygame.image.load(os.path.join(folder,"instr.png"))
    screen.blit(ins,(0,0))
    


def game_intro():

    intro = True
    folder = "img"
    pygame.mixer.pre_init()
    pygame.mixer.music.load('op.ogg')
    pygame.mixer.music.play(-1)
    #creditos
    menu = pygame.image.load(os.path.join(folder,"menu.jpg"))
    while intro == True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
         
                
        #colocar imagem do menu
        screen.blit(menu,(0,0))
       

        button("JOGO",600,540,50,50,white,bright_rasen,narutoGame)
        button("CRÉDITOS",0,560,100,50,Aqua,white,creditos)
        button("INSTRUÇÕES",0,510,100,50,LightSkyBlue,white,inst)
        button("SAIR",0,610,100,50,DeepSkyBlue,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)
        
    
    
def gameover(scorefinal):
    largura = 847
    altura = 596

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((largura,altura))
    pygame.display.set_caption(" - Naruto: Final Shuriken -")
    relogio = pygame.time.Clock()
    screen.fill((255, 255, 255))
    #Musicas e img
    folder = "img"
    #Naruto
    gameOver = pygame.image.load(os.path.join(folder,"gameover.jpg"))
    smallText = pygame.font.SysFont("mistral",15)
    ranque = smallText.render("-APERTE A TECLA DE ESPAÇO PARA IR AO RANKING!-",1,(white))
    aviso = smallText.render("*APÓS APERTAR ESPAÇO, ESCREVA SEU NOME NO SHEEL DO PYTHON PARA MELHOR VISÃO DA SUA PONTUAÇÃO",1,(white))
    perdedor = True
    pygame.mixer.pre_init()
    pygame.mixer.music.load('gameOver.ogg')
    pygame.mixer.music.play(-1)
    while perdedor != False:
        time.sleep(1)
        screen.blit(gameOver,(0,0))
        screen.blit(ranque,(150,500))
        screen.blit(aviso,(100,530))
        for event in pygame.event.get():
                pygame.display.update()
                pygame.display.flip()
                if event.type ==  pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        ranking(scorefinal)
                        perdedor = True

       
        
        


def venceu(scorefinal):
    
    largura = 847
    altura = 596

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((largura,altura))
    pygame.display.set_caption(" - Naruto: Final Shuriken -")
    relogio = pygame.time.Clock()
    screen.fill((255, 255, 255))
    #Musicas e img
    folder = "img"
    #Naruto
    youwin = pygame.image.load(os.path.join(folder,"youwin.jpg"))
    smallText = pygame.font.SysFont("mistral",15)
    ranque = smallText.render("-APERTE A TECLA DE ESPAÇO PARA IR AO RANKING!-",1,(black))
    aviso = smallText.render("*APÓS APERTAR ESPAÇO, ESCREVA SEU NOME NO SHEEL DO PYTHON PARA MELHOR VISÃO DA SUA PONTUAÇÃO",1,(black))
    vencedor = True
    pygame.mixer.pre_init()
    pygame.mixer.music.load('gameWin.ogg')
    pygame.mixer.music.play(-1)
    while vencedor != False:
        time.sleep(1)
        screen.blit(youwin,(0,0))
        screen.blit(ranque,(150,500))
        screen.blit(aviso,(100,530))
        for event in pygame.event.get():
                pygame.display.update()
                pygame.display.flip()
                if event.type ==  pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        ranking(scorefinal)
                        vencedor = False
        
    
    
def narutoGame():
    largura = 847
    altura = 596
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.pre_init()
    pygame.mixer.music.stop()
    screen = pygame.display.set_mode((largura,altura))
    pygame.display.set_caption(" - Naruto: Final Shuriken -")
    relogio = pygame.time.Clock()
    screen.fill((255, 255, 255))

    folder = "img"
    #Naruto
    image = pygame.image.load(os.path.join(folder,"Naruto_correndoR1.png"))
    image2 = pygame.image.load(os.path.join(folder,"Naruto_correndoR2.png"))
    image3 = pygame.image.load(os.path.join(folder,"Naruto_correndoL1.png"))
    image4 = pygame.image.load(os.path.join(folder,"Naruto_correndoL2.png"))
    imagemFundo = pygame.image.load(os.path.join(folder,"cenario2.jpg"))

    #NarutoRasengan
    Rasengan1 = pygame.image.load(os.path.join(folder,"Rasengan1.png"))
    Rasengan2 = pygame.image.load(os.path.join(folder,"Rasengan2.png"))
    Rasengan3 = pygame.image.load(os.path.join(folder,"Rasengan3.png"))
    Rasengan4 = pygame.image.load(os.path.join(folder,"Rasengan4.png"))
    Rasengan5 = pygame.image.load(os.path.join(folder,"Rasengan5.png"))
    Rasengan6 = pygame.image.load(os.path.join(folder,"Rasengan6.png"))
    Rasengan7 = pygame.image.load(os.path.join(folder,"Rasengan7.png"))
    Rasengan8 = pygame.image.load(os.path.join(folder,"Rasengan8.png"))
    Rasengan9 = pygame.image.load(os.path.join(folder,"Rasengan9.png"))
    Rasengan10 = pygame.image.load(os.path.join(folder,"Rasengan10.png"))
    Rasenshuriken1 = pygame.image.load(os.path.join(folder,"Rasenshuriken2.png"))
    Rasenshuriken2 = pygame.image.load(os.path.join(folder,"Rasenshuriken3.png"))
    Rasenshuriken3 = pygame.image.load(os.path.join(folder,"Rasenshuriken4.png"))
    deidara1 = pygame.image.load(os.path.join(folder,"d1.png"))
    deidara2 = pygame.image.load(os.path.join(folder,"d2.png"))
    deidara3 = pygame.image.load(os.path.join(folder,"d3.png"))
    explosiond = pygame.image.load(os.path.join(folder,"Expl5.png"))
    RasenColision1 = pygame.image.load(os.path.join(folder,"Rasengancolision1.png"))
    RasenColision2 = pygame.image.load(os.path.join(folder,"Rasengancolision2.png"))
    RasenColision3 = pygame.image.load(os.path.join(folder,"Rasengancolision3.png"))
    RasenColision4 = pygame.image.load(os.path.join(folder,"Rasengancolision3-4.png"))
    RasenColision5 = pygame.image.load(os.path.join(folder,"Rasengancolision4-5 1.png"))
    RasenColision6 = pygame.image.load(os.path.join(folder,"Rasengancolision5.png"))
    RasenColision7 = pygame.image.load(os.path.join(folder,"Rasengancolision5-6.png"))
    RasenColision8 = pygame.image.load(os.path.join(folder,"Rasengancolision6.png"))
    RasenColision9 = pygame.image.load(os.path.join(folder,"Rasengancolision7.png"))
    RasenColision10 = pygame.image.load(os.path.join(folder,"Rasengancolision8.png"))
    RasenColision11 = pygame.image.load(os.path.join(folder,"Rasengancolision9.png"))
    RasenColision12 = pygame.image.load(os.path.join(folder,"Rasengancolision10.png"))
    vidinha = pygame.image.load(os.path.join(folder,"vida.png"))
    dei1 = pygame.image.load(os.path.join(folder,"life.png"))
    dei2 = pygame.image.load(os.path.join(folder,"life2.png"))
    dei3 = pygame.image.load(os.path.join(folder,"life3.png"))

    #Musicas e Sons
    musica1 = pygame.mixer.Sound('combatenvl1.ogg')
    musica2 = pygame.mixer.Sound('combatenvl2.ogg')
    musica3 = pygame.mixer.Sound('combatenvl3.ogg')
    Rasengan_s = pygame.mixer.Sound('Rasengan.ogg')

    
  
    '''text = fonte_colisao.render("{0:.0f}".format(tempo),1,(255,255,255)
    screen.blit(text, (150,350))'''
    


    x = 200
    cont = 0
    d = 0
    y = 480
    deidarax = 600
    deidaray = 70
    expy = 70
    expx = 400
    score = 0
    font = pygame.font.SysFont(None, 20)
    exp = [deidara3,deidara3,deidara3,deidara3]
    deidaravelocidade = 1
    velpombo = 1
    vida = 3
    level = 25
    scorefinal = 0

    pygame.font.init()
    font_padrao = pygame.font.get_default_font()
    fonte_colisao = pygame.font.SysFont( font_padrao, 25)
    jogando = True

    while jogando == True:
         relogio.tick(100)
         tempoo = pygame.time.get_ticks()/1000
         tempo = tempoo
         pygame.display.flip()
         
         for event in pygame.event.get():
                pygame.display.update()
                pygame.display.flip()
                
                #Animação andar para frente
                if event.type ==  pygame.QUIT:
                    pygame.quit()
                    sys.exit()
         screen.blit(imagemFundo, (0,0))
         screen.blit(Rasengan10, (x,y))
         screen.blit(deidara1, (deidarax,deidaray))
         if vida == 3:
             musica1.play()
             screen.blit(vidinha, (0,0))
             screen.blit(vidinha, (65,0))
             screen.blit(vidinha, (130,0))
         elif vida == 2:
             musica1.stop()
             musica2.play()
             screen.blit(vidinha, (0,0))
             screen.blit(vidinha, (65,0))
         elif vida == 1:
             musica2.stop()
             musica3.play()
             screen.blit(vidinha, (0,0))
         if level>20 and level<=30:
             screen.blit(dei1,(750,20))
         elif level>10 and level<=20:
             screen.blit(dei2,(750,20))
         elif level>0 and level<=10:
             screen.blit(dei3,(750,20))
         if d == 0:
             deidarax = deidarax - deidaravelocidade
         if d == 1:
             deidarax = deidarax + deidaravelocidade
         if expy >480:
            screen.blit(explosiond, (expx,480))
            pygame.display.update()
            time.sleep(0.1)
            expy = 0
            expx = random.randint(10,800)
         screen.blit(deidara3,(expx, expy))
         expy = expy + velpombo
         #pontuação
         text = font.render(str(score), True, (255,255,255))
         screen.blit(text, [700, 20])
         temp = font.render(str("{0:.0f}".format(tempo)), True, (255,255,255))
         screen.blit(temp, [0, 530])
         pont = font.render("Pontuação:", True, (255,255,255))
         screen.blit(pont, [620, 20])
         
         if deidarax>790:
            deidarax = 700
            d = 0
         elif deidarax<0:
             deidarax = 40
             d = 1
         
         if x<0:
            x = 0
         elif x>800:
            x = 800
         tecla = pygame.key.get_pressed()
         if (x-expx)>-60 and (x-expx)<90 and (y-expy)>-60 and (y-expy)<90: #Colisão passaro-Naruto
                screen.blit(explosiond, (expx,480))
                time.sleep(0.1)
                vida = vida - 1
                x = 10
                y = 480
                pygame.display.update()                
                if vida == 0:
                    musica3.stop()
                    scorefinal = score
                    jogando = False
                    gameover(scorefinal)
                    print("Você ainda é fraco")
             
         if tecla[K_RIGHT]:
            if cont == 0:
                for b in range(1):
                    for e in range(4):
                            screen.blit(imagemFundo, (0,0))
                            narandando = [image2]
                            screen.blit(narandando[b], (x,y))
                            x = x+5
                            screen.blit(deidara1, (deidarax,deidaray))
                            if d == 0:
                                deidarax = deidarax - deidaravelocidade*2
                            if d == 1:
                                deidarax = deidarax + deidaravelocidade*2
                            # copiando o texto para a superfície
                            screen.blit(exp[e],(expx, expy))
                            expy = expy + velpombo
                            pont = font.render("Pontuação:", True, (255,255,255))
                            screen.blit(pont, [620, 20])
                            text = font.render(str(score), True, (255,255,255))
                            screen.blit(text, [700, 20])
                            temp = font.render(str("{0:.0f}".format(tempo)), True, (255,255,255))
                            screen.blit(temp, [0, 530])
                            cont = 1
                            exp = [deidara3,deidara3,deidara3,deidara3]
                            if vida == 3:
                                screen.blit(vidinha, (0,0))
                                screen.blit(vidinha, (65,0))
                                screen.blit(vidinha, (130,0))
                            elif vida == 2:
                                screen.blit(vidinha, (0,0))
                                screen.blit(vidinha, (65,0))
                            elif vida == 1:
                                screen.blit(vidinha, (0,0))
                            if level>20 and level<=30:
                                screen.blit(dei1,(750,20))
                            elif level>10 and level<=20:
                                screen.blit(dei2,(750,20))
                            elif level>0 and level<=10:
                                screen.blit(dei3,(750,20))

                            if expy >480:
                                screen.blit(explosiond, (expx,480))
                                pygame.display.update()
                                time.sleep(0.1)
                                expy = 0
                                expx = random.randint(10,800)
            
            elif cont == 1:
                for b in range(1):
                   
                        for w in range(4):
                            screen.blit(imagemFundo, (0,0))
                            narandando = [image]
                            screen.blit(narandando[b], (x,y))
                            x = x+5
                            screen.blit(deidara1, (deidarax,deidaray))
                            # copiando o texto para a superfície
                            pont = font.render("Pontuação:", True, (255,255,255))
                            screen.blit(pont, [620, 20])
                            text = font.render(str(score), True, (255,255,255))
                            screen.blit(text, [700, 20])
                            temp = font.render(str("{0:.0f}".format(tempo)), True, (255,255,255))
                            screen.blit(temp, [0, 530])
                            cont = 0
                            exp = [deidara3,deidara3,deidara3,deidara3]
                            screen.blit(exp[w],(expx, expy))
                            expy = expy + velpombo
                            if vida == 3:
                                screen.blit(vidinha, (0,0))
                                screen.blit(vidinha, (65,0))
                                screen.blit(vidinha, (130,0))
                            elif vida == 2:
                                screen.blit(vidinha, (0,0))
                                screen.blit(vidinha, (65,0))
                            elif vida == 1:
                                screen.blit(vidinha, (0,0))
                            if level>20 and level<=30:
                                screen.blit(dei1,(750,20))
                            elif level>10 and level<=20:
                                screen.blit(dei2,(750,20))
                            elif level>0 and level<=10:
                                screen.blit(dei3,(750,20))
            
                            if expy >480:
                                screen.blit(explosiond, (expx,480))
                                pygame.display.update()
                                time.sleep(0.1)
                                expy = 0
                                expx = random.randint(10,700)
       
        
                            
            #Animação andar para trás        
                
         if tecla[K_LEFT]:
            if cont == 0:
                for b in range(1):
                        for e in range(4):
                            screen.blit(imagemFundo, (0,0))
                            screen.blit(image3, (x,y))
                            x = x-5
                            screen.blit(deidara1, (deidarax,deidaray))
                            if d == 0:
                                deidarax = deidarax - deidaravelocidade
                            if d == 1:
                                deidarax = deidarax + deidaravelocidade
                            pont = font.render("Pontuação:", True, (255,255,255))
                            screen.blit(pont, [620, 20])
                            text = font.render(str(score), True, (255,255,255))
                            screen.blit(text, [700, 20])
                            temp = font.render(str("{0:.0f}".format(tempo)), True, (255,255,255))
                            screen.blit(temp, [0, 530])
                            exp = [deidara3,deidara3,deidara3,deidara3]
                            screen.blit(exp[e],(expx, expy))
                            expy = expy + velpombo
                            cont = 1
                            if vida == 3:
                                screen.blit(vidinha, (0,0))
                                screen.blit(vidinha, (65,0))
                                screen.blit(vidinha, (130,0))
                            elif vida == 2:
                                screen.blit(vidinha, (0,0))
                                screen.blit(vidinha, (65,0))
                            elif vida == 1:
                                screen.blit(vidinha, (0,0))
                                
                            if level>20 and level<=30:
                                screen.blit(dei1,(750,20))
                            elif level>10 and level<=20:
                                screen.blit(dei2,(750,20))
                            elif level>0 and level<=10:
                                screen.blit(dei3,(750,20))
                            

                            if expy >480:
                                screen.blit(explosiond, (expx,480))
                                pygame.display.update()
                                time.sleep(0.1)
                                expy = 0
                                expx = random.randint(10,700)

            elif cont == 1:
                for b in range(1):
                        for e in range(4):
                            screen.blit(imagemFundo, (0,0))
                            screen.blit(image4, (x,y))
                            x = x-5
                            screen.blit(deidara1, (deidarax,deidaray))
                            pont = font.render("Pontuação:", True, (255,255,255))
                            screen.blit(pont, [620, 20])
                            text = font.render(str(score), True, (255,255,255))
                            screen.blit(text, [700, 20])
                            temp = font.render(str("{0:.0f}".format(tempo)), True, (255,255,255))
                            screen.blit(temp, [0, 530])
                            exp = [deidara3,deidara3,deidara3,deidara3]
                            screen.blit(exp[e],(expx, expy))
                            expy = expy + velpombo
                            cont = 0
                            if vida == 3:
                                screen.blit(vidinha, (0,0))
                                screen.blit(vidinha, (65,0))
                                screen.blit(vidinha, (130,0))
                            elif vida == 2:
                                screen.blit(vidinha, (0,0))
                                screen.blit(vidinha, (65,0))
                            elif vida == 1:
                                screen.blit(vidinha, (0,0))

                            if level>20 and level<=30:
                                screen.blit(dei1,(750,20))
                            elif level>10 and level<=20:
                                screen.blit(dei2,(750,20))
                            elif level>0 and level<=10:
                                screen.blit(dei3,(750,20))
                       
                            if expy >480:
                                screen.blit(explosiond, (expx,480))
                                pygame.display.update()
                                time.sleep(0.1)
                                expy = 0
                                expx = random.randint(10,700)

                            
            #ANIMAÇÃO RASENGAN 
                
         if tecla[K_SPACE]:
                i = 1
                z = 1
                a = 1
                Rasengan_s.play()
                #Movimento do Naruto ao fazer o rasengan
                for i in range(1,4):
                    screen.blit(imagemFundo, (0,0))
                    Rasengans = [Rasengan1, Rasengan2,Rasengan3,Rasengan4]
                    screen.blit(Rasengans[i], (x,y))
                    screen.blit(deidara1, (deidarax,deidaray))
                    if d == 0:
                         deidarax = deidarax - deidaravelocidade*2
                    if d == 1:
                         deidarax = deidarax + deidaravelocidade*2
                    pont = font.render("Pontuação:", True, (255,255,255))
                    screen.blit(pont, [620, 20])
                    text = font.render(str(score), True, (255,255,255))
                    screen.blit(text, [700, 20])
                    temp = font.render(str("{0:.0f}".format(tempo)), True, (255,255,255))
                    screen.blit(temp, [0, 530])
                    screen.blit(deidara3,(expx, expy))
                    expy = expy + velpombo
                    if vida == 3:
                         musica1.play()
                         screen.blit(vidinha, (0,0))
                         screen.blit(vidinha, (65,0))
                         screen.blit(vidinha, (130,0))
                    elif vida == 2:
                         musica1.stop()
                         musica2.play()
                         screen.blit(vidinha, (0,0))
                         screen.blit(vidinha, (65,0))
                    elif vida == 1:
                         musica2.stop()
                         musica3.play()
                         screen.blit(vidinha, (0,0))
                    if level>20 and level<=30:
                         screen.blit(dei1,(750,20))
                    elif level>10 and level<=20:
                         screen.blit(dei2,(750,20))
                    elif level>0 and level<=10:
                         screen.blit(dei3,(750,20))
                         pygame.display.update()
                         time.sleep(0.1)
                    
                                
                    if expy >480:
                                screen.blit(explosiond, (expx,480))
                                pygame.display.update()
                                time.sleep(0.1)
                                expy = 0
                                expx = random.randint(10,700)
                            
                for z in range(1,4):
                    screen.blit(imagemFundo, (0,0))
                    Rasengans = [Rasengan5, Rasengan6,Rasengan7,Rasengan8]
                    screen.blit(Rasengans[z], (x,(y-30)))
                    screen.blit(deidara1, (deidarax,deidaray))
                    if d == 0:
                        deidarax = deidarax - deidaravelocidade*2
                    if d == 1:
                        deidarax = deidarax + deidaravelocidade*2
                    pont = font.render("Pontuação:", True, (255,255,255))
                    screen.blit(pont, [620, 20])
                    text = font.render(str(score), True, (255,255,255))
                    screen.blit(text, [700, 20])
                    temp = font.render(str("{0:.0f}".format(tempo)), True, (255,255,255))
                    screen.blit(temp, [0, 530])
                    screen.blit(deidara3,(expx, expy))
                    expy = expy + velpombo
                    if vida == 3:
                         musica1.play()
                         screen.blit(vidinha, (0,0))
                         screen.blit(vidinha, (65,0))
                         screen.blit(vidinha, (130,0))
                    elif vida == 2:
                         musica1.stop()
                         musica2.play()
                         screen.blit(vidinha, (0,0))
                         screen.blit(vidinha, (65,0))
                    elif vida == 1:
                         musica2.stop()
                         musica3.play()
                         screen.blit(vidinha, (0,0))
                    if level>20 and level<=30:
                         screen.blit(dei1,(750,20))
                    elif level>10 and level<=20:
                         screen.blit(dei2,(750,20))
                    elif level>0 and level<=10:
                         screen.blit(dei3,(750,20))
                    pygame.display.update()
                    time.sleep(0.1)
                
                    if expy >480:
                                screen.blit(explosiond, (expx,480))
                                pygame.display.update()
                                time.sleep(0.1)
                                expy = 0
                                expx = random.randint(10,700)

                for a in range(2):
                    screen.blit(imagemFundo, (0,0))
                    Rasengans = [Rasengan9, Rasengan10]
                    screen.blit(Rasengans[a], (x,y))
                    screen.blit(deidara1, (deidarax,deidaray))
                    if d == 0:
                         deidarax = deidarax - deidaravelocidade*2
                    if d == 1:
                         deidarax = deidarax + deidaravelocidade*2
                    pont = font.render("Pontuação:", True, (255,255,255))
                    screen.blit(pont, [620, 20])
                    text = font.render(str(score), True, (255,255,255))
                    screen.blit(text, [700, 20])
                    temp = font.render(str("{0:.0f}".format(tempo)), True, (255,255,255))
                    screen.blit(temp, [0, 530])
                    screen.blit(deidara3,(expx, expy))
                    expy = expy + velpombo
                    if vida == 3:
                         musica1.play()
                         screen.blit(vidinha, (0,0))
                         screen.blit(vidinha, (65,0))
                         screen.blit(vidinha, (130,0))
                    elif vida == 2:
                         musica1.stop()
                         musica2.play()
                         screen.blit(vidinha, (0,0))
                         screen.blit(vidinha, (65,0))
                    elif vida == 1:
                         musica2.stop()
                         musica3.play()
                         screen.blit(vidinha, (0,0))
                    if level>20 and level<=30:
                         screen.blit(dei1,(750,20))
                    elif level>10 and level<=20:
                         screen.blit(dei2,(750,20))
                    elif level>0 and level<=10:
                         screen.blit(dei3,(750,20))
                    pygame.display.update()
                    time.sleep(0.2)
                   
                    if expy >480:
                            screen.blit(explosiond, (expx,480))
                            pygame.display.update()
                            time.sleep(0.1)
                            expy = 0
                            expx = random.randint(10,700)

                #Trajetoria RasenShuriken
                yrasen = 290
                xrasen = x
                for r in range(15):
                    Rasengan_s.stop()
                    screen.blit(imagemFundo, (0,0))
                    Rasenshuriken = [ Rasenshuriken1,Rasenshuriken2,Rasenshuriken3,Rasenshuriken1,Rasenshuriken2,Rasenshuriken3,Rasenshuriken1,Rasenshuriken2,Rasenshuriken3,Rasenshuriken1,Rasenshuriken2,Rasenshuriken3,Rasenshuriken1,Rasenshuriken2,Rasenshuriken3]
                    screen.blit(Rasengan10, (x,y))
                    screen.blit(deidara1, (deidarax,deidaray))
                    if d == 0:
                         deidarax = deidarax - deidaravelocidade*2
                    if d == 1:
                         deidarax = deidarax + deidaravelocidade*2
                    yrasen = yrasen - 30
                    screen.blit(Rasenshuriken[r], (xrasen,yrasen))
                    pont = font.render("Pontuação:", True, (255,255,255))
                    screen.blit(pont, [620, 20])
                    text = font.render(str(score), True, (255,255,255))
                    screen.blit(text, [700, 20])
                    temp = font.render(str("{0:.0f}".format(tempo)), True, (255,255,255))
                    screen.blit(temp, [0, 530])
                    screen.blit(deidara3,(expx, expy))
                    expy = expy + velpombo
                    if vida == 3:
                         musica1.play()
                         screen.blit(vidinha, (0,0))
                         screen.blit(vidinha, (65,0))
                         screen.blit(vidinha, (130,0))
                    elif vida == 2:
                         musica1.stop()
                         musica2.play()
                         screen.blit(vidinha, (0,0))
                         screen.blit(vidinha, (65,0))
                    elif vida == 1:
                         musica2.stop()
                         musica3.play()
                         screen.blit(vidinha, (0,0))
                    if level>20 and level<=30:
                         screen.blit(dei1,(750,20))
                    elif level>10 and level<=20:
                         screen.blit(dei2,(750,20))
                    elif level>0 and level<=10:
                         screen.blit(dei3,(750,20))

                    pygame.display.update()
                    time.sleep(0.025)
                    
                
                                
                    if expy >480:
                            screen.blit(explosiond, (expx,300))
                            pygame.display.update()
                            time.sleep(0.1)
                            expy = 0
                            expx = random.randint(10,700)
                    elif (xrasen-expx)>-50 and (xrasen-expx)<90  :
                        for c in range(12):
                            score = score + 300
                            screen.blit(imagemFundo, (0,0))
                            screen.blit(Rasengan10, (x,y))
                            Rasencol = [RasenColision1, RasenColision2,RasenColision3,RasenColision4,RasenColision5,RasenColision6,RasenColision7,RasenColision8,RasenColision9,RasenColision10,RasenColision11,RasenColision12]
                            screen.blit(Rasencol[c], (expx,expy))
                            expy = -20
                            expx = random.randint(10,700)
                            screen.blit(deidara1, (deidarax,deidaray))
                            deidarax = random.randint(10,700)
                            pygame.display.update()
                            time.sleep(0.1)
                            break
                        
                        
                    elif (xrasen-deidarax)>-50 and (xrasen-deidarax)<90  :
                        score = score + 1000
                        level = level - 1
                        if level>20 and level<30:
                            screen.blit(dei1,(700,10))
                        elif level>10 and level<20:
                            screen.blit(dei2,(700,10))
                        elif level>0 and level<10:
                            screen.blit(dei3,(700,10))
                        print(level)
                        if level == 0:#SE O JOGADOR VENCER
                            musica1.stop()
                            musica2.stop()
                            musica3.stop()
                            scorefinal = score
                            jogando = False
                            venceu(scorefinal)
                            print("Você venceu, fim de jogo")
                        pont = font.render(str(score), True, (255,255,255))
                        screen.blit(pont, [700, 100])
                        print(score)
                        tempo = 0
                        pont = font.render("Pontuação:", True, (255,255,255))
                        screen.blit(pont, [620, 20])
                        text = font.render(str(score), True, (255,255,255))
                        screen.blit(text, [700, 20])
                        temp = font.render(str("{0:.0f}".format(tempo)), True, (255,255,255))
                        screen.blit(temp, [0, 530])
                        expy = expy + velpombo
                        screen.blit(text, [0, 370])
                        pygame.display.update()
                        for c in range(12):
                            screen.blit(imagemFundo, (0,0))
                            screen.blit(Rasengan10, (x,y))
                            Rasencol = [RasenColision1, RasenColision2,RasenColision3,RasenColision4,RasenColision5,RasenColision6,RasenColision7,RasenColision8,RasenColision9,RasenColision10,RasenColision11,RasenColision12]
                            screen.blit(Rasencol[c], (deidarax,deidaray))
                            screen.blit(deidara3,(expx, expy))
                            expy = expy + velpombo
                            deidarax = random.randint(10,700)
                            deidaravelocidade = deidaravelocidade + 0.1
                            velpombo = velpombo + 0.05
                            pygame.display.update()
                            time.sleep(0.1)
                            if expy >480:
                                screen.blit(explosiond, (expx,480))
                                pygame.display.update()
                                time.sleep(0.1)
                                expy = 0
                                expx = random.randint(10,700)
                        break
                                
                    if yrasen<-70:
                        break

game_intro()                             
narutoGame()        

            
