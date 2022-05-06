import pygame

# 게임 스크린 크기
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 150

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("ZANDY")

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
    
    ## 게임 화면에 글자 표현
    # 폰트 선택 : pygame.font 모듈 SysFont() 메서드
    # - 파라미터 : 폰트, 크기, 두껍게, 이탤릭
    font = pygame.font.SysFont('FixedSys', 50, True, False)
    # 글자 표현 : render() 메서드
    # - 파라미터 : 텍스트, 안티앨리어스 여부, 색상, 배경색
    # -- 안티앨리어스(Anti-Aliasing) : 대상 픽셀의 주위 픽셀에 중간색을 넣어주어 멀리서 보면 부드럽게 해주는 기능
    text = font.render("LET'S PLANT ZANDY!!!", True, GREEN)
    # 화면에 텍스트 표시 : blit() 메서드
    # - 파라미터 : 글자 표현 변수, 출력할 위치 좌표값
    screen.blit(text, [57, 50])

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()