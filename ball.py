import pygame

# 게임 스크린 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Ball")

# 스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 공 초기 위치
ball_x = int(SCREEN_WIDTH / 2)
ball_y = int(SCREEN_HEIGHT / 2)
# 공이 움직일 방향 값
ball_dx = 4
ball_dy = 4
# 공의 반지름 값
ball_size = 40

# 게임 종료 전까지 반복
done = False

# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    # 게임 로직 구간
    # 속도에 따라 원형 위치 변형
    ball_x += ball_dx
    ball_y += ball_dy
    
    # 공이 스크린을 벗어날 경우
    # (ball_x + ball_size)의 값이 SCREEN_WIDTH을 벗어난다면 공의 오른쪽 표면이 스크린 너비 크기를 벗어난다.
    # (ball_x - ball_size)의 값이 0보다 작으면 공의 왼쪽 표면이 스크린 왼쪽으로 벗어난다.
    # ball_dx = ball_dx * -1 을 하여 ball_dx의 값이 양수일 경우에는 음수로 바꾸고, 음수일 경우에는 양수로 바꾸어 방향을 반대로 바꿈
    if (ball_x + ball_size) > SCREEN_WIDTH or (ball_x - ball_size) < 0:
        ball_dx = ball_dx * -1
    if (ball_y + ball_size) > SCREEN_HEIGHT or (ball_y - ball_size) < 0:
        ball_dy = ball_dy * -1
    
    # 스크린 채우기
    screen.fill(WHITE)
    
    # 화면 그리기 구간
    # 공 그리기 : pygame.draw 모듈 circle() 메서드
    pygame.draw.circle(screen, BLUE, [ball_x, ball_y], ball_size, 0)
    
    # 화면 업데이트
    pygame.display.flip()
    
    # 초당 60 프레임으로 업데이트
    clock.tick(60)
    
# 게임 종료
pygame.quit()