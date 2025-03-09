import pygame
import random
from Ammo import Ammo
from Paddle import Paddle
from QuizAnswer import QuizAnswer
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Atari Breakout")
clock = pygame.time.Clock()
running = True
alive = True
score = 0

pygame.font.init()

QUESTION_FONT = pygame.font.SysFont("Arial", SCREEN_HEIGHT // 12, bold=True)
SCORE_FONT = pygame.font.SysFont("Arial", SCREEN_HEIGHT // 24, bold=True)
question_surface = QUESTION_FONT.render("1 + 1 = ?", True, "white")
score_surface = SCORE_FONT.render(str(score), True, "white")

ammos = []
paddle = Paddle()

questions = [
    ["What's ROE's mascot?", [
        "panda",
        "roadrunner",
        "cardinal"
    ], 1],
    ["Which color is NOT ROE-themed?", [
        "green",
        "white",
        "red"
    ], 2],
    ["Who created this?", [
        "Adam",
        "Nicolas",
        "Iker"
    ], 0],
    ["What is NOT ROE?", [
        "The Best",
        "Dog-themed",
        "IB"
    ], 1],
    ["Which of the following streets is near ROE?", [
        "Alabama",
        "Avalon",
        "Glenwood"
    ], 1],
    ["Who's the music teacher?", [
        "Mr. Fuller",
        "Ms. Casas",
        "Ms. Lambert"
    ], 0],
    ["What year was it when ROE opened?", [
        "1929",
        "1928",
        "1927"
    ], 0],
    ["Who's the creator's teacher?", [
        "Ms. Ghosh",
        "Ms. Jones",
        "Both"
    ], 2],
    ["What's the current principal's first name?", [
        "Dedrick",
        "William",
        "Ima"
    ], 1],
    ["How many houses are there?", [
        "4",
        "7",
        "5"
    ], 2]
]

answers = [
    QuizAnswer("1", 300),
    QuizAnswer("2", 600),
    QuizAnswer("3", 900)
]
correct_answer = 1

def load_question():
    global question_surface, answers, correct_answer, questions

    if len(questions) == 0:
        return

    current = questions[random.randint(0, len(questions) - 1)]

    question_surface = QUESTION_FONT.render(current[0], True, "white")
    answers = [
        QuizAnswer(current[1][0], 300),
        QuizAnswer(current[1][1], 600),
        QuizAnswer(current[1][2], 900)
    ]
    correct_answer = current[2]

load_question()

while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            new_ammos = []
            for ammo in ammos:
                if ammo.y >= -10:
                    new_ammos.append(ammo)
            ammos = new_ammos
            ammos.append(Ammo(paddle.x))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move("left")
    if keys[pygame.K_RIGHT]:
        paddle.move("right")
    
    for ammo in ammos:
        if ammo.y >= -10:
            ammo.move()
        paddle.ball_collides(ammo)

        if ammo.y >= -10:
            ammo.draw(screen)

        if ammo.y <= 0:       
            question_surface = QUESTION_FONT.render("GAME OVER", True, "red")
            score = 0

    paddle.draw(screen)

    for i, answer in enumerate(answers):
        answer.draw(screen)
        if answer.is_shot(ammos) and len(questions) > 0 and alive:
            ammos = []
            if i == correct_answer:
                score += 1
                score_surface = SCORE_FONT.render(str(score), True, "white")
                load_question()
            else:
                question_surface = QUESTION_FONT.render("GAME OVER", True, "red")
                score = 0

    if score == 555:
        question_surface = QUESTION_FONT.render("YOU WIN", True, "green")
    
    screen.blit(question_surface, (
        SCREEN_WIDTH / 2 - question_surface.get_width() / 2,
        40
    ))

    screen.blit(score_surface, (10, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()