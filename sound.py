import pygame
import os

# 게임 스크린 크기
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 400

# 색 정의
BLACK = (0, 0, 0)

# pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Sound")

# 스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# assets 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

# 배경 이미지 로드
background_image = pygame.image.load(os.path.join(assets_path, 'equalizer.png'))

# 배경 음악 로드 : pygame.mixer.music 모듈 load() 메서드
pygame.mixer.music.load(os.path.join(assets_path, 'bgm.wav'))
# 배경 음악 재생 : pygame.mixer.music 모듈 play() 메서드
pygame.mixer.music.play(-1)   # 무한 반복 재생

# 효과음 로드 : pygame.mixer.Sound() 매서드
sound = pygame.mixer.Sound(os.path.join(assets_path, 'sound.wav'))

# 게임 종료 전까지 반복
done = False

# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # 사운드 제어를 위한 반복 구간
        # 마우스 클릭 이벤트 타입 pygame.MOUSEBUTTONDOWN : 효과음 sound에 대해서 play() 메서드로 효과음 재생
        if event.type == pygame.MOUSEBUTTONDOWN:
            sound.play()   # 효과음 재생
    
    # 게임 로직 구간
    
    # 화면 삭제 구간
    
    # 스크린 채우기
    screen.fill(BLACK)
    
    # 화면 그리기 구간
    
    # 배경 이미지 그리기
    screen.blit(background_image, background_image.get_rect())
    
    # 화면 업데이트
    pygame.display.flip()
    
    # 초당 60 프레임으로 업데이트
    clock.tick(60)
    
# 게임 종료
pygame.quit()