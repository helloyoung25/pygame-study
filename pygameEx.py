import pygame

# 게임 스크린 크기 (전역변수)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색 정의 : RGB값 사용 (전역변수)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# pygame 사용하기 전에 항상 초기화 필수
# pygame 초기화
pygame.init()

# 윈도우 제목 : pygame.display 모듈 set_caption() 메서드
pygame.display.set_caption("pygame")

# 스크린 정의 (윈도우 크기) : pygame.display 모듈 set_mode() 메서드
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임 화면 업데이트를 위해 시간에 대한 기능 필요
# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 게임 종료 전까지 반복
done = False    # 게임이 진행 중인지 확인하는 변수
# done이 True라면 게임이 계속 진행 중이라는 의미

# 게임 반복 구간
# 게임에서 필요한 이벤트와 화면 업데이트를 처리
# 이벤트와 로직 발생 -> 키 조작이나 처리 필요
while not done:    # 게임이 진행되는 동안 계속 반복 작어블 하는 while 루프
    # 이벤트 반복 구간
    # 현재 이벤트들을 가져와서 반복 : pygame.event 모듈 get() 메서드
    for event in pygame.event.get():
        # 어떤 이벤트가 발생했는지 확인
        if event.type == pygame.QUIT:
            # QUIT는 윈도우 창을 닫을 때 발생하는 이벤트
            # 창이 닫히는 이벤트가 발생한다면
            done = True    # 반복을 중단시켜 게임 종료
            
    # 게임 로직 구간

    # 화면 삭제 구간
             
    # 스크린 채우기
    screen.fill(WHITE)

    # 화면 그리기 구간

    # 화면 업데이트
    # pygame.display.flip()
    # - 화면의 변경되는 부분을 반영하고 있는 버퍼 전체 flip()을 통해서 외부 화면으로 한 번만 반영해주는 역할. 화면 전체의 업데이트 사용.
    # pygame.display.update()
    # - 픽셀 단위로 화면의 일부만 업데이트하는 역할. 화면 일부만 업데이트 사용.
    pygame.display.flip()

    # 초당 60프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()