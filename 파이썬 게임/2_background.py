import pygame

pygame.init() #초기화 파이 게임 실행을 위한. 반드시 필요 

# 화면 크기 설정

screen_width = 480 #가로 크기 
screen_height = 640 #세로 크기 
screen = pygame.display.set_mode((screen_width,screen_height)) #화면을 세팅한다.

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름 -> 추가 명령 없을 시에 바로 종료된다. 


#배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\주민성\\Desktop\\파이썬 구현연습\\파이썬 게임\\background.png") 



#이벤트 루프 
running = True #게임이 실행중인가? 
while running :
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가? 
            running = False # 게임이 진행중이 아님 
      
    screen.blit(background,(0,0)) # 배경 그리기 
    #screen.fill((0,0,225)) 
      
    pygame.display.update() #게임 화면을 다시그리기        
             
# pygame 종료 
pygame.quit() 




