import pygame
import os
import sys
import random
from time import sleep

'''
스네이크 게임 규칙
- 네모난 공간에 뱀이 한 마리 놓인다.
- 뱀은 멈추지 않고 머리가 향하는 방향으로 이동한다.
- 플레이어는 뱀의 머리 방향만 바꿀 수 있다. (게임 조작)
- 뱀이 벽이나 자신의 몸에 부딪히면 죽는다.
- 먹이를 먹을 때마다 길이가 길어지고, 속도가 빨라진다. (게임의 난이도 증가)
'''

# 게임 스크린 전역변수
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 게임 화면 전역변수
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE

# 방향 전역변수
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 색상 전역변수
WHITE = (255, 255, 255)
ORANGE = (250, 150, 0)
GRAY = (100, 100, 100)

# 뱀 객체
class Snake(object):
    def __init__(self):
        self.create()
    # 뱀 생성
    def create(self):
        self.length = 2
        self.positions = [(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
    # 뱀 방향 조정
    def control(self, xy):
        if (xy[0] * -1, xy[1] * -1) == self.direction:
            return
        else:
            self.direction = xy
    # 뱀 이동
    def move(self):
        # 뱀의 현재 위치 정보가 있는 self.positions에서 [0]번째, 즉 뱀의 머리 부분을 cur 변수로 할당
        cur = self.positions[0]
        x, y = self.direction
        # 뱀이 GRID_SIZE 단위로 움직이게 함
        new = (cur[0] + (x * GRID_SIZE)), (cur[1] + (y * GRID_SIZE))
        # 뱀이 자기 몸동에 닿았을 경우 뱀 처음부터 다시 생성
        # self.positions 변수에서 머리를 제외한 부분이 몸통
        if new in self.positions[2:]:
            sleep(1)   # 1초 정지
            self.create()
        # 뱀이 게임 화면을 넘어갈 경우 뱀 처음부터 다시 생성
        elif new[0] < 0 or new[0] >= SCREEN_WIDTH or new[1] < 0 or new[1] >= SCREEN_HEIGHT:
            sleep(1)
            self.create()
        # 뱀이 정상적으로 이동하는 경우
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
    # 뱀이 먹이를 먹을 때
    def eat(self):
        self.length += 1
    # 뱀 그리기
    def draw(self, screen):
        # color 튜플 변수로 빨간색, 초록색, 파란색
        red, green, blue = 50 / (self.length - 1), 150, 150 / (self.length - 1)
        for i, p in enumerate(self.positions):
            color = (100 + red * i, green, blue * i)
            # 스네이크 게임은 GRID_SIZE 크기의 사각형으로 모든 객체들을 구성
            # 사각형 객체를 만들기 위해
            # pygame.Rect() 함수를 이용해 self.positions에 포함된 각각의 위치 p에 GRID_SIZE 크기의 사각형을 생성하여 rect 변수에 할당
            rect = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            # pygame.draw.rect() 함수를 통해서 사각형 rect를 color 변수의 색상으로 객체를 그림
            pygame.draw.rect(screen, color, rect)

# 먹이 객체
class Feed(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = ORANGE
        self.create()
    # 먹이 생성
    def create(self):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        self.position = x * GRID_SIZE, y * GRID_SIZE
    # 먹이 그리기
    def draw(self, screen):
        rect = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.color, rect)

# 게임 객체
class Game(object):
    def __init__(self):
        self.snake = Snake()
        self.feed = Feed()
        self.speed = 20
    # 게임 이벤트 처리 및 조작
    def process_events(self):
        # pygame.event.get() 함수를 이용하여 게임 이벤트들을 계속 받아옴
        for event in pygame.event.get():
            # 게임 종료
            if event.type == pygame.QUIT:
                return True
            # 키보드가 눌린 이벤트
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.control(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.control(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.control(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.control(RIGHT)
        return False
    # 게임 로직 수행
    def run_logic(self):
        # 뱀 계속 움직이기
        self.snake.move()
        # 뱀이 먹이를 먹었는지 체크
        self.check_eat(self.snake, self.feed)
        # 게임 속도
        self.speed = (20 + self.snake.length) / 4
    # 뱀이 먹이를 먹었는지 체크
    def check_eat(self, snake, feed):
        if snake.positions[0] == feed.position:
            snake.eat()
            feed.create()
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    # 게임 정보 출력
    def draw_info(self, length, speed, screen):
        info = "Length: " + str(length) + "    " + "Speed: " + str(round(speed, 2))
        font_path = resource_path("assets/NanumGothicCoding-Bold.ttf")
        font = pygame.font.Font(font_path, 26)
        text_obj = font.render(info, 1, GRAY)
        # 텍스트를 표시할 사각형 정보를 get_rect() 메서드를 통해 text_rect로 받아옴
        text_rect = text_obj.get_rect()
        text_rect.x, text_rect.y = 10, 10
        # 게임 화면에 text 반영
        screen.blit(text_obj, text_rect)
    # 게임 프레임 처리
    def display_frame(self, screen):
        screen.fill(WHITE)
        self.draw_info(self.snake.length, self.speed, screen)
        self.snake.draw(screen)
        self.feed.draw(screen)
        screen.blit(screen, (0, 0))

# 리소스 경로 설정
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def main():
    # 게임 초기화 및 환경 설정
    pygame.init()
    pygame.display.set_caption('Snake Game')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Game()

    done = False
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        pygame.display.flip()
        clock.tick(game.speed)

    pygame.quit()

if __name__ == '__main__':
    main()