#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: October 2019
# FPlesson 7 screen

import ugame
import stage
import constants

# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("ball.bmp")
# a list of sprites that will be updated every frame
sprites = []

a_button = constants.button_state["button_up"]
b_button = constants.button_state["button_up"]
start_button = constants.button_state["button_up"]
select_button = constants.button_state["button_up"]

# get sound ready
boom_sound = open("boom.wav", 'rb')
sound = ugame.audio
sound.stop()
sound.mute(False)


def main():

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("ball.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, constants.SCREEN_X,
                            constants.SCREEN_Y)

    # a list of sprites that will be updated every frame
    sprites = []

    text = []
    text1 = stage.Text(width=29, height=12, font=None,
                       palette=constants.NEW_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None,
                       palette=constants.NEW_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the background layer
    game.layers = text + sprites + [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    while True:
        # get user inputs
        keys = ugame.buttons.get_pressed()

        # start button is pressed
        if keys & ugame.K_START != 0:
            game_scene()

        game.tick()


def game_scene():
    # comment

    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # this function sets the background

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 10, 8)

    # create a sprite
    # parameters (image_bank_1, image # in bank, x, y)
    ball_one = stage.Sprite(image_bank_1, 3, 64, 56)
    sprites.append(ball_one)
    ball_two = stage.Sprite(image_bank_1, 2, 75, 56)
    sprites.insert(0, ball_two)  # insert at top of sprite list

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the background layer
    game.layers = sprites + [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    while True:
        # get user inputs
        keys = ugame.buttons.get_pressed()
        # print(keys)

        # A button fire
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if keys & ugame.K_UP != 0:
            if ball_one.y < 0:
                ball_one.move(ball_one.x, 0)
            else:
                ball_one.move(ball_one.x, ball_one.y - 1)
            pass
        if keys & ugame.K_DOWN != 0:
            if ball_one.y > constants.SCREEN_Y - constants.SCREEN_GRID_Y:
                ball_one.move(ball_one.x, constants.SCREEN_Y -
                              constants.SPRITE_SIZE)
            else:
                ball_one.move(ball_one.x, ball_one.y + 1)
            pass
        if keys & ugame.K_LEFT != 0:
            if ball_one.x < 0:
                ball_one.move(0, ball_one.y)
            else:
                ball_one.move(ball_one.x - 1, ball_one.y)
            pass
        if keys & ugame.K_RIGHT != 0:
            if ball_one.x > constants.SCREEN_X - constants.SCREEN_GRID_X:
                ball_one.move(constants.SCREEN_X - constants.SPRITE_SIZE,
                              ball_one.y)
            else:
                ball_one.move(ball_one.x + 1, ball_one.y)
            pass

        # play sound if A is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
        # update game logic

        # redraw sprtie list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    main()
