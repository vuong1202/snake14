#import
import pygame,random,sys
pygame.init()
#âm nhạc
music_feed=pygame.mixer.Sound("feed.wav")
music_die=pygame.mixer.Sound("die.wav")
music_nen=pygame.mixer.Sound("music_nen.mp3")
music_start=pygame.mixer.Sound("start.mp3")
# load hình ảnh
WIDTH=1000
HEIGHT=520
m = 20 # kích thước chiều cao và chiều rộng
Imghead = pygame.transform.scale(pygame.image.load('heads.png'),(m,m))
Imgfood = pygame.transform.scale(pygame.image.load('apple.png'),(m,m))
ImgWall=pygame.transform.scale(pygame.image.load('fire.png'),(60,240))
ImgOver=pygame.transform.scale(pygame.image.load('over1.jpg'),(WIDTH,HEIGHT))
ImgStart=pygame.transform.scale(pygame.image.load('start.jpg'),(WIDTH,HEIGHT))
ImgBg=pygame.transform.scale(pygame.image.load('bg.jpg'),(WIDTH-180,HEIGHT))
ImgBg1=pygame.transform.scale(pygame.image.load('bg1.jpg'),(WIDTH-180,HEIGHT))
ImgBg2=pygame.transform.scale(pygame.image.load('bg2.jpg'),(WIDTH-180,HEIGHT))
ImgBg3=pygame.transform.scale(pygame.image.load('bg3.jpg'),(WIDTH-180,HEIGHT))
ImgBg4=pygame.transform.scale(pygame.image.load('bg4.jpg'),(WIDTH-180,HEIGHT))

Imgv=pygame.transform.scale(pygame.image.load('bg1.png'),(180,180))

# tạo cửa sổ
gameSurface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Snake')
# màu sắc
black = pygame.Color(0,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
font = pygame.font.SysFont('Time New Roman', 30)
#điểm cao nhất
class Topscore:
    def __init__(self):
        self.high_score = 0
    def top_score(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score

topscore = Topscore()
#hàm game over
def game_over():
    music_nen.stop()
    music_die.play()
    topscore.top_score(SCORE)
    gameSurface.blit(ImgOver,(0,0))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                music_die.stop()
                main()
        pygame.display.update()
#hàm start game
def start_game():
    gameSurface.blit(ImgStart,(0,0))
    music_start.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                main()
        pygame.display.update()
#hàm check level
def check_level(SCORE):
    global LEVEL
    global Imgbody
    if SCORE <5:
        pygame.time.delay(250)
        Imgbody = pygame.transform.scale(pygame.image.load('ball.png'),(m,m))
        LEVEL = 1
        gameSurface.blit(ImgBg,(0,0))
    elif SCORE <10:
        LEVEL = 2
        pygame.time.delay(150)
        Imgbody = pygame.transform.scale(pygame.image.load('ball1.png'),(m,m))
        gameSurface.blit(ImgBg1,(0,0))
    elif SCORE <15:
        LEVEL = 3
        pygame.time.delay(100)
        Imgbody = pygame.transform.scale(pygame.image.load('ball2.png'),(m,m))
        gameSurface.blit(ImgBg2,(0,0))
    elif SCORE <20:
        LEVEL = 4
        pygame.time.delay(50)
        Imgbody = pygame.transform.scale(pygame.image.load('ball3.png'),(m,m))
        gameSurface.blit(ImgBg3,(0,0))
    else:
        LEVEL = 5
        pygame.time.delay(30)
        Imgbody = pygame.transform.scale(pygame.image.load('ball4.png'),(m,m))
        gameSurface.blit(ImgBg4,(0,0))
# hàm main
def main():
    music_nen.play()
    music_start.stop()
    snakepos = [100,60]   #vị trí con rắn xuất hiện 
    snakebody = [[100,60],[80,60],[60,60]]  # 3 ô cho rắn
    foodpos = [300, 260]
    foodflat = True
    direction = 'RIGHT'
    changeto = direction
    global SCORE
    SCORE = 0
    global  HIGH_SCORE
    
    while True:
        gameSurface.fill(black)
        check_level(SCORE)
        snakebody.insert(0,list(snakepos))
        if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
            SCORE += 1
            music_feed.play()
            foodflat = False
        else:
            snakebody.pop()
        for event in pygame.event.get():    #bắt sự kiêện
            if event.type == pygame.QUIT:    # click X out game
                pygame.quit()
            # xử lý phím
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    changeto = 'RIGHT'
                if event.key == pygame.K_LEFT:
                    changeto = 'LEFT'
                if event.key == pygame.K_UP:
                    changeto = 'UP'
                if event.key == pygame.K_DOWN:
                    changeto = 'DOWN'
        # di chuyển
        if changeto == 'RIGHT' and not direction=="LEFT" : 
            direction = 'RIGHT'      
        elif changeto == 'LEFT' and not direction=="RIGHT":
            direction = 'LEFT'
        elif changeto == 'UP' and not direction=="DOWN":
            direction = 'UP'
        elif changeto == 'DOWN' and not direction=="UP":
            direction = 'DOWN'
        # cập nhật vị trí mới
        if direction == 'RIGHT':
            snakepos[0] += m
        elif direction == 'LEFT':
            snakepos[0] -= m
        elif direction == 'UP':
            snakepos[1] -= m
        elif direction == 'DOWN':
            snakepos[1] += m
        # sản sinh thức ăn
        if foodflat == False:
            foodx = random.randint(1,80)
            if foodx == 20 or foodx ==50 :foodx=30
            foody = random.randint(1,50)      
            if foodx %2 != 0 : foodx += 1
            if foody %2 != 0 : foody += 1
            foodpos = [foodx * 10, foody * 10]
        foodflat = True
        
    #chạm biên  
        if snakepos[0] > 810 or snakepos[0] < 0:
            game_over()
        if snakepos[1] > 510 or snakepos[1] < 0:
            game_over()
    #chạm tường
        if (snakepos[0]==220 and snakepos[1] >140 and snakepos[1]<400)or(snakepos[0] ==520 and snakepos[1] >100 and snakepos[1]<360):
            game_over()  
    # chạm chính mình
        for b in snakebody[1:]:
            if snakepos[0] == b[0] and snakepos[1] == b[1]:
                game_over()
        #  cập nhật lên cửa sổ
        
        sfont = font.render('Score: '+str(SCORE), True, green)
        sfont_rect = sfont.get_rect()
        sfont_rect.center = (880, 80)
        gameSurface.blit(sfont, sfont_rect)

        lfont = font.render('Level: '+str(LEVEL), True, green)
        lfont_rect = lfont.get_rect()
        lfont_rect.center = (880, 30)
        gameSurface.blit(lfont, lfont_rect)

        tfont = font.render('Top Score: '+str(topscore.high_score),True,green)
        tfont_rect = tfont.get_rect()
        tfont_rect.center = (900, 130)
        gameSurface.blit(tfont, tfont_rect)

        gameSurface.blit(Imgv,pygame.Rect(820,300,m,m))
        gameSurface.blit(ImgWall,pygame.Rect(200,160,m,m))    # hiển thị UFO
        gameSurface.blit(ImgWall,pygame.Rect(500,120,m,m))    
        for pos in snakebody:
            gameSurface.blit(Imgbody,pygame.Rect(pos[0],pos[1],m,m))  # hiển thị thân rắn
            gameSurface.blit(Imghead,pygame.Rect(snakebody[0][0],snakebody[0][1],m,m)) # đầu rắn
            gameSurface.blit(Imgfood,pygame.Rect(foodpos[0],foodpos[1],m,m))

            
        # đường viền
        pygame.draw.rect(gameSurface,blue,(0,0,820,520),2)
        pygame.display.update()
        pygame.display.flip()
start_game()