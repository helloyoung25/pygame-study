# 마우스 조작 인터페이스

import pygame
import os

# 게임 스크린 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색 정의
GREEN = (100, 200, 100)

# pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Mouse")

# 스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# assets 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

# 마우스 이미지 초기 설정
mouse_image = pygame.image.load(os.path.join(assets_path, 'mouse.png'))
mouse_x = int(SCREEN_WIDTH / 2)
mouse_y = int(SCREEN_HEIGHT / 2)

# 마우스 커서 숨기기
# 마우스 커서 위치에 이미지가 있어야 하므로 기본 마우스 커서는 숨겨줘야 함
# set_visible(False) : 마우스 커서 숨김 / set_visible(True) : 마우서 커서 보임
pygame.mouse.set_visible(False)

# 게임 종료 전까지 반복
done = False

# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    # 게임 로직 구간
    
    # 마우스 위치값 가져오기 : pygame.mouse 모듈 get_pos() 메서드
    pos = pygame.mouse.get_pos()
    # x값
    mouse_x = pos[0]
    # y값
    mouse_y = pos[1]
    
    # 스크린 화면 채우기
    screen.fill(GREEN)
    
    # 화면 그리기
    
    # 마우스 이미지 그리기
    screen.blit(mouse_image, [mouse_x, mouse_y])
    
    # 화면 업데이트
    pygame.display.flip()
    
    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()