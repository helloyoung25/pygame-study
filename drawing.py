import pygame

# 게임 스크린 크기
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Drawing")

# 스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 게임 종료 전까지 반복
done = False

# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
          
    # 게임 로직 구간

    # 화면 삭제 구간

    # 스크린 채우기
    screen.fill(WHITE)

    # 화면 그리기 구간
    ### 선, 도형, 글자 그리기 위치 ###
    ## 선 그리기 : pygame.draw 모듈 line() 메서드
    # - 파라미터 : screen, 색상, 시작 위치 좌표값 [x, y], 끝날 위치 좌표값 [x, y], 선 두께
    pygame.draw.line(screen, RED, [50, 50], [500, 50], 10)
    pygame.draw.line(screen, GREEN, [50, 100], [500, 100], 10)
    pygame.draw.line(screen, BLUE, [50, 150], [500, 150], 10)
    ## 사각형 그리기 : pygame.draw 모듈 rect() 메서드
    # - 파라미터 : screen, 색상, 사각형의 왼쪽 위와 오른쪽 아래 좌표값, 선 두께
    # -- 선 두께 : 0보다 작으면 사각형이 그려지지 않음. 0보다 크면 선의 두께로 사용. 0일 경우 사각형을 색깔로 채운 형태
    pygame.draw.rect(screen, RED, [50, 200, 150, 150], 4)
    ## 다각형 그리기 : pygame.draw 모듈 polygon() 메서드
    # - 파라미터 : screen, 색상, 각의 좌표값들을 리스트로 묶어서 표현, 선 두께
    pygame.draw.polygon(screen, GREEN, [[350, 200], [250, 350], [450, 350]], 4)
    ## 원형 그리기 : pygame.draw 모듈 circle() 메서드
    # - 파라미터 : screen, 색상, 중앙값 좌표값, 반지름 값, 선 두께
    pygame.draw.circle(screen, BLUE, [150, 450], 60, 4)
    ## 타원 그리기 : pygame.draw 모듈 ellipse() 메서드
    # - 파라미터 : screen, 색상, 두 개의 좌표값, 선두께
    pygame.draw.ellipse(screen, BLUE, [250, 400, 200, 100], 0)
    ## 게임 화면에 글자 표현
    # 폰트 선택 : pygame.font 모듈 SysFont() 메서드
    # - 파라미터 : 폰트, 크기, 두껍게, 이탤릭
    font = pygame.font.SysFont('FixedSys', 40, True, False)
    # 글자 표현 : render() 메서드
    # - 파라미터 : 텍스트, 안티앨리어스 여부, 색상, 배경색
    # -- 안티앨리어스(Anti-Aliasing) : 대상 픽셀의 주위 픽셀에 중간색을 넣어주어 멀리서 보면 부드럽게 해주는 기능
    text = font.render("Hello pygame", True, BLACK)
    # 화면에 텍스트 표시 : blit() 메서드
    # - 파라미터 : 글자 표현 변수, 출력할 위치 좌표값
    screen.blit(text, [200, 600])

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()