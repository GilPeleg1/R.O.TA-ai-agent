import pygame
from Graphics import *
from Rota import Rota
from Human_Agent import Human_Agent
from Random_Agent import Random_Agent
from MinMaxAgent import MinMaxAgent
from DQN_Agent import DQN_Agent
from AlphaBetaAgent import AlphaBetaAgent 
import time

FPS = 60

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Roman tic tac toe')
environment = Rota()
graphics = Graphics(win, board = environment.state.board)

#Human Agent
#player1 = Human_Agent(player=1)
#player2 = Human_Agent(player=-1)

#Random Agent
#player1 = Random_Agent(player=1,env=environment)
#player2 = Random_Agent(player=-1,env=environment)

#MinMax Agent
#player2 = MinMaxAgent(player = -1,depth = 3, environment=environment)
player1 = MinMaxAgent(player = 1,depth = 3, environment=environment)

#Alpha Beta Agent
#player1 = AlphaBetaAgent(player = 1,depth = 5, environment=environment)
#player2 = AlphaBetaAgent(player = 2,depth = 3, environment=environment)

#DQN White Agent
#player1 = DQN_Agent(player=1,env = environment, parametes_path ="Data\\params_1.pth") #against random
#player1 = DQN_Agent(player=1,env = environment, parametes_path ="Data\\params_2.pth") #against minmax

#DQN Black Agent
#player2 = DQN_Agent(player=-1,env = environment, parametes_path ="Data\\Black\\params_vs_random_v2.pth", train=False) #black against random
player2 = DQN_Agent(player=-1,env = environment, parametes_path ="Data\\Black\\params_vs_MinMax.pth", train=False) #black against minmax depth 3

#DQN BlackWhite
#player1 = DQN_Agent(player=1,env = environment, parametes_path ="Data\\params_11.pth")
#player2 = DQN_Agent(player=01,env = environment, parametes_path ="Data\\params_11.pth")

def main():

    start = time.time()
    run = True
    clock = pygame.time.Clock()
    graphics.draw()
    player = player1
    action = None
    exp = False
    while(run):
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
            if event.type == pygame.K_ESCAPE and exp:
                exp = False
                pygame.event.clear()          


        if action and action[1] == "tomove":
            
            action= (action[0],player.get_Move_Action(event, graphics, environment.state))    
        else:
            action = player.get_Action(event = event,graphics= graphics, state = environment.state, train = False)

#        if action and len(action)>1 and action[1] == "tomove":
#            print("continued")
#            continue
        if action and len(action)>1 and action[1]!="tomove":
            #print(action,"action","    player=",player.player)
            if (environment.move(action, environment.state)):
                #graphics.blink(action, GREEN)
                player = switchPlayers(player)
                time.sleep(0.15)
                
            else: 
                a = 1 # to not make an error
                #graphics.blink(action, RED)
                
        elif action:
            blue = (0, 0, 255)
            temp = (action[0],action[0])
            pygame.display.update()
            #graphics.blink(temp,blue)

        #display functions, check if end of game.    
        graphics.draw()
        pygame.display.update()
        #time.sleep(0.2)
        if environment.is_end_of_game(environment.state)[0]:
            run = False
    
    print ("end of game!")
    time.sleep(1.5)
    pygame.quit()
    print("End of game")
    print(environment.state.board[1,1],"Won")
    score1, score2 = environment.state.score()
    print (time.time() - start)


def switchPlayers(player):
    if player == player1:
       return player2
    else:
        return player1

if __name__ == '__main__':
    main()
    
