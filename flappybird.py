import pygame,sys,random, os
# -------------TẠO HÀM------------------# 
def draw_bg():
    screen.blit(bg,(bg_x,0)) 
    screen.blit(bg,(bg_x+x,0))
def draw_floor():
    screen.blit(floor,(floor_x,floor_y)) 
    screen.blit(floor,(floor_x+x,floor_y))

def create_pige():
    random_pige_pos = random.choice(pige_height)
    random_pige_space =random.choice(height)
    bottom_pige = pige_surface.get_rect(midtop =(500,random_pige_pos))
    top_pige = pige_surface.get_rect(midbottom =(500,random_pige_pos-random_pige_space))
    return bottom_pige, top_pige
def move_pige(piges):
    for pige in piges :
        pige.centerx -= 4
    return piges
def draw_pige(piges):
    for pige in piges :
        if pige.bottom >= floor_y : 
            screen.blit(pige_surface,pige)
        else:
            flip_pige = pygame.transform.flip(pige_surface,False,True)
            screen.blit(flip_pige,pige)

def check_collision(piges):
    for pige in piges:
        if bird_rect.colliderect(pige):
            pygame.time.set_timer(spawnstart,0)
            # pygame.time.set_timer(spawnpige,0)
            hit_sound.play()
            return False
    if bird_rect.top <= -100 or bird_rect.bottom >= floor_y:
        pygame.time.set_timer(spawnstart,0)
        # pygame.time.set_timer(spawnpige,0)
        hit_sound.play()
        return False
    return True
    
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1,-bird_movement*3,1)
    return new_bird
def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
    return new_bird, new_bird_rect

def draw_score(game_state):
    if game_state == 'main game':
        score_suface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_suface.get_rect(center = (x/2,100))
        screen.blit(score_suface,score_rect)

        high_score_suface = game_font.render(f'Ki luc: {int(high_score)}',True,(255,255,255))
        high_score_rect = high_score_suface.get_rect(center = (x/2,50))
        screen.blit(high_score_suface,high_score_rect)
    if game_state == 'game over':
        score_suface = game_font.render(f'Diem: {int(score)}',True,(255,255,255))
        score_rect = score_suface.get_rect(center = (x/2,100))
        screen.blit(score_suface,score_rect)

        high_score_suface = game_font.render(f'Ki luc: {int(high_score)}',True,(255,255,255))
        high_score_rect = high_score_suface.get_rect(center = (x/2,50))
        screen.blit(high_score_suface,high_score_rect)

        exit_suface = game_font.render(f'exit: x',True,(255,255,255))
        exit_rect = exit_suface.get_rect(center = (x/2,630))
        screen.blit(exit_suface,exit_rect)
        
    if game_state == 'game_start':
        game_start_font = pygame.font.Font(font_path, 60)
        start_suface = game_start_font.render(f'FlappyBird',True,(255,255,255))
        start_rect = start_suface.get_rect(center = (x/2,150))
        screen.blit(start_suface,start_rect)
        
        exit_suface = game_font.render(f'exit: x',True,(255,255,255))
        exit_rect = exit_suface.get_rect(center = (x/2,530))
        screen.blit(exit_suface,exit_rect)
        
        exit_suface = game_font.render(f'switch bg: b',True,(255,255,255))
        exit_rect = exit_suface.get_rect(center = (x/2,580))
        screen.blit(exit_suface,exit_rect)
    
def  update_score(score,high_score):
    if score > high_score:
        high_score = score
        save_high_score(high_score)  # Lưu vào file
    return high_score

# Tìm đường dẫn thư mục phù hợp để lưu high_score.txt
def get_high_score_path():
    '''check lại phần này'''
    if getattr(sys, 'frozen', False):  # Kiểm tra nếu đang chạy dưới dạng .exe
        # base_dir = os.path.dirname(sys.executable)  # Lưu cùng thư mục .exe
        base_dir = os.path.join(os.getenv('AppData'), 'FlappyBird')  # Lưu trong %APPDATA%
        os.makedirs(base_dir, exist_ok=True)  # Tạo thư mục nếu chưa có
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Chạy bằng Python

    return os.path.join(base_dir, "high_score.txt")

def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 0

def save_high_score(high_score):
    with open("high_score.txt", "w") as file:
        file.write(str(high_score))


# --------------TẠO BIẾN---------------#
x=432
y=768
floor_x = 0
floor_y = 650
bg_x = 0
toc_do=80
gravity=0.25
bird_movement = 0
game_active = False
game_start = False
score = 0
high_score = load_high_score()
pige_height = [300,320,340,360,380,400,420,440,460,480,500]
start_height = [370,380,390,400,410]
height = [190,200,180]
tg = [1050,1100,1200]
tg_start = [5050,7050]

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
pygame.init()
pygame.display.set_caption('Flappy Bird')
screen= pygame.display.set_mode((x,y)) 
clock = pygame.time.Clock()

# Lấy đường dẫn thư mục chứa file đã đóng gói
'''check lại phần này'''
if getattr(sys, 'frozen', False):  # Khi chạy file .exe
    base_path = sys._MEIPASS
else:  # Khi chạy file .py
    base_path = os.path.abspath(".")
    
# ----------------chèn font-----------#
font_path = os.path.join(base_path, "04B_19.ttf")
game_font = pygame.font.Font(font_path, 40)

#------------------------CHÈN HÌNH ẢNH---------------------#
# bg = pygame.transform.scale2x(pygame.image.load(os.path.join(base_path, "assets", "background-night.png")).convert())
bg0 = pygame.transform.scale2x(pygame.image.load(os.path.join(base_path, "assets", "background-night.png")).convert())
bg1 = pygame.transform.scale2x(pygame.image.load(os.path.join(base_path, "assets", "background-morning.jpg")).convert())
bg_list = [bg0,bg1]
stt_bg = 0
bg = bg_list[stt_bg]

floor = pygame.transform.scale2x(pygame.image.load(os.path.join(base_path, "assets", "floor.png")).convert())

bird_down = pygame.transform.scale2x(pygame.image.load(os.path.join(base_path, "assets", "yellowbird-downflap.png")).convert_alpha())
bird_mid = pygame.transform.scale2x(pygame.image.load(os.path.join(base_path, "assets", "yellowbird-midflap.png")).convert_alpha())
bird_up = pygame.transform.scale2x(pygame.image.load(os.path.join(base_path, "assets", "yellowbird-upflap.png")).convert_alpha())

bird_list = [bird_down,bird_mid,bird_up]
bird_index = 0
bird = bird_list[bird_index] 
bird_rect = bird.get_rect(center = (100,300))
birdflap = pygame.USEREVENT + 0
pygame.time.set_timer(birdflap,200)

pige_surface = pygame.transform.scale2x(pygame.image.load(os.path.join(base_path, "assets", "pipe-green.png")).convert())
pige_list = []
spawnpige = pygame.USEREVENT + 1
pygame.time.set_timer(spawnpige,random.choice(tg))

start_surface = pygame.transform.scale(pygame.image.load(os.path.join(base_path, "assets", "start.png")).convert_alpha(),(30,30))
random_start_pos = random.choice(start_height)
test_start = False
spawnstart = pygame.USEREVENT + 2
pygame.time.set_timer(spawnstart,5000)

game_over_suface = pygame.transform.scale2x(pygame.image.load(os.path.join(base_path, "assets", "message.png")).convert_alpha())
game_over_rect = game_over_suface.get_rect(center=(x/2,y/2))

#---------------CHÈN ÂM THANH-------------#
flap_sound = pygame.mixer.Sound(os.path.join(base_path, "sound", "sfx_wing.wav"))
hit_sound = pygame.mixer.Sound(os.path.join(base_path, "sound", "sfx_hit.wav"))
score_sound = pygame.mixer.Sound(os.path.join(base_path, "sound", "sfx_point.wav"))

# #--------------------- LẶP WHILE TẠO GAME----------------#
game = True
while game:
    # nền
    bg_x -= 4
    draw_bg()
    if bg_x <= -x: 
        bg_x =0   
    # for lấy tất cả sự kiện
    for event in pygame.event.get():
        # thoát game
        if event.type == pygame.QUIT:
            game =False
            pygame.quit()
            print("End game Flappy Bird.")
            sys.exit()
        # sự kiện với bàn phím
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE and not game_start:
                game_active = True
                game_start = True
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = -5
                flap_sound.play()
            if event.key == pygame.K_SPACE and not game_active:
                pige_list.clear()
                pygame.time.set_timer(spawnstart,random.choice(tg_start))
                # pygame.time.set_timer(spawnpige,random.choice(tg))
                game_active=True
                test_start = False
                bird_rect.center = (100,300)
                bird_movement = 0 
                score = 0
                toc_do=80
            if event.key == pygame.K_x:
                game = False
                pygame.quit()
                print("End game Flappy Bird.")
                sys.exit() 
            if event.key == pygame.K_b:
                stt_bg = (stt_bg + 1) % len(bg_list)
                bg = bg_list[stt_bg]


        # sự kiện với chuột
        if event.type == pygame.MOUSEBUTTONUP and not game_start:
            game_active = True
            game_start = True
        if event.type == pygame.MOUSEBUTTONUP and game_active:
            bird_movement = -5
            flap_sound.play()
        if event.type == pygame.MOUSEBUTTONUP and not game_active:
            pige_list.clear()
            pygame.time.set_timer(spawnstart,random.choice(tg_start))
            # pygame.time.set_timer(spawnpige,random.choice(tg))
            game_active=True
            test_start = False
            bird_rect.center = (100,300)
            bird_movement = 0 
            score = 0
            toc_do=80

        # sự kiện tạo với ống
        if event.type == spawnpige and game_start:
            pige_list.extend(create_pige())
            score_active=False
        # sự kiện với ngôi sao
        if event.type == spawnstart and game_start:
            new_start = start_surface.get_rect(center = (500,random.choice(start_height)))
            test_start = True
            score_start = False
        # sự kiện với chim
        if event.type == birdflap and game_start:
            if bird_index < 2:
                bird_index +=1
            else:
                bird_index =0
            bird, bird_rect = bird_animation()
    # hoạt động của game
    if game_start:
        if game_active:
            bird_movement += gravity   
            rotated_bird = rotate_bird(bird)
            bird_rect.centery += bird_movement
            screen.blit(rotated_bird,bird_rect)
            game_active = check_collision(pige_list)
            pige_list = move_pige(pige_list)
            draw_pige(pige_list)
            # tính điểm khi qua ống
            for pige in pige_list :
                if bird_rect.centerx > pige.centerx and score_active==False :
                    score += 1
                    toc_do += 1
                    score_active=True
                    score_sound.play()
            if test_start :
                new_start.centerx -= 4
                screen.blit(start_surface,new_start)
                # tính điểm khi chạm ngôi sao
                if bird_rect.colliderect(new_start) and score_start==False :
                    score += 2
                    new_start.centerx -= 500
                    score_start=True
                    score_sound.play()
            high_score =  update_score(score,high_score)
            draw_score('main game')
        else:
            screen.blit(game_over_suface,game_over_rect)
            high_score =  update_score(score,high_score)
            draw_score('game over')
    else:
        draw_score('game_start')
        screen.blit(bird,bird.get_rect(center = (x/2,(y-(y-floor_y))/2)))
    floor_x -= 4
    draw_floor()
    if floor_x <= -x: 
        floor_x =0
    pygame.display.update()
    clock.tick(toc_do)