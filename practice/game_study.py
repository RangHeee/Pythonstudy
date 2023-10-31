from functions_study import *

# 게임 진행
def game_start():
    minerals = mineral_init()

    for i in range(10):
        left_scale = input(print("왼쪽 저울에 몇 개의 보석을 올리시겠습니까? "))
        right_scale = input(print("오른쪽 저울에 몇 개의 보석을 올리시겠습니까? "))


def mineral_init():
    mineral_weights = []
    for _ in range(3):