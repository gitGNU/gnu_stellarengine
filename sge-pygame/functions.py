# Copyright (C) 2012, 2013, 2014 Julian Marchant <onpon4@riseup.net>
# 
# This file is part of the Pygame SGE.
# 
# The Pygame SGE is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# The Pygame SGE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with the Pygame SGE.  If not, see <http://www.gnu.org/licenses/>.

import os
import math

import pygame

import sge


__all__ = ['show_message', 'get_text_entry']


def show_message(text, buttons=('OK',), default=0):
    """Show a dialog box and return the button pressed.

    Arguments:

    - ``text`` -- The message to show in the dialog box as a string.
    - ``buttons`` -- A list or tuple of strings to put in each of the
      buttons from left to right.
    - ``default`` -- The number of the button to select by default,
      where ``0`` is the first button.

    While the dialog box is being shown, all events are stopped.

    The return value is the number of the button which was pressed,
    where ``0`` is the first button.  If the dialog box was closed in
    any way other than clicking on one of the buttons (including by
    clicking an "X" button or similar), :const:`None` is returned.

    """
    return _show_modal(text, default, False, buttons)


def get_text_entry(text, default=''):
    """Show a text entry dialog box and return the text entered.

    Arguments:

    - ``text`` -- The message to show in the dialog box as a string.
    - ``default`` -- The text to put in the text entry field initially.

    The text entry dialog box is mostly the same as the regular dialog
    box -- see the documentation for :func:`sge.show_message` for more
    information -- but there are some key differences:

    There is always an OK button and a Cancel button.  If the OK button
    is clicked, the text in the text entry field is returned.  If the
    Cancel button is clicked, :const:`None` is returned.

    """
    pygame.key.set_repeat(500, 20)
    text = _show_modal(text, default, True, ('Cancel', 'OK'))
    pygame.key.set_repeat()
    return text


def _show_modal(text, default, text_entry, buttons):
    # Show a dialog box.  Text entry if ``text_entry`` is True, buttons
    # are made by the strings in ``buttons``.   If is text entry, return
    # the text if button 1 is pressed or None if button 0 is pressed,
    # else return the button number pressed.  Select ``default`` if this
    # isn't a text entry dialog, else select button 1 by default.  If it
    # is a text entry dialog, ``default`` is the default text entry.
    window = pygame.display.get_surface()
    screenshot = window.copy()
    background = screenshot.copy()
    sge.font_directories.append(os.path.dirname(__file__))
    font = sge.Font("DroidSans-Bold.ttf", size=12)
    del sge.font_directories[-1]
    window_rect = window.get_rect()
    screen_w, screen_h = background.get_size()
    button_w = 80
    button_h = 24

    for button in buttons:
        button_w = max(button_w, font.get_width(button))
    
    box_w = min(screen_w, max(320, (button_w + 4) * len(buttons) + 4))
    box_h = button_h + 12
    text_entry_w = box_w - 8
    text_entry_h = font._font.get_linesize() + 4
    if text_entry:
        box_h += text_entry_h + 8
    text_w = box_w - 16
    text_h = font.get_height(text, text_w)

    while box_h + text_h > screen_h and box_w < screen_w:
        box_w = min(box_w + 4, screen_w)
        text_w = box_w - 16
        text_h = font.get_height(text, text_w)

    box_h = max(120, box_h + text_h)
    button_w = min(80, int(box_w / len(buttons)))

    cursor = pygame.Surface((1, font._font.get_linesize()))
    mydir = os.path.dirname(__file__)
    try:
        box_fill = pygame.image.load(
            os.path.join(mydir, 'sge_dialogbox.png')).convert_alpha()
        box_left = pygame.image.load(
            os.path.join(mydir, 'sge_dialogbox_left.png')).convert_alpha()
        box_right = pygame.image.load(
            os.path.join(mydir, 'sge_dialogbox_right.png')).convert_alpha()
        box_top = pygame.image.load(
            os.path.join(mydir, 'sge_dialogbox_top.png')).convert_alpha()
        box_bottom = pygame.image.load(
            os.path.join(mydir, 'sge_dialogbox_bottom.png')).convert_alpha()
        box_topleft = pygame.image.load(
            os.path.join(mydir, 'sge_dialogbox_topleft.png')).convert_alpha()
        box_topright = pygame.image.load(
            os.path.join(mydir, 'sge_dialogbox_topright.png')).convert_alpha()
        box_bottomleft = pygame.image.load(os.path.join(
            mydir, 'sge_dialogbox_bottomleft.png')).convert_alpha()
        box_bottomright = pygame.image.load(os.path.join(
            mydir, 'sge_dialogbox_bottomright.png')).convert_alpha()
        text_entry_fill = pygame.image.load(
            os.path.join(mydir, 'sge_text_entry.png')).convert_alpha()
        text_entry_left = pygame.image.load(
            os.path.join(mydir, 'sge_text_entry_left.png')).convert_alpha()
        text_entry_right = pygame.image.load(
            os.path.join(mydir, 'sge_text_entry_right.png')).convert_alpha()
        text_entry_top = pygame.image.load(
            os.path.join(mydir, 'sge_text_entry_top.png')).convert_alpha()
        text_entry_bottom = pygame.image.load(
            os.path.join(mydir, 'sge_text_entry_bottom.png')).convert_alpha()
        text_entry_topleft = pygame.image.load(
            os.path.join(mydir, 'sge_text_entry_topleft.png')).convert_alpha()
        text_entry_topright = pygame.image.load(
            os.path.join(mydir, 'sge_text_entry_topright.png')).convert_alpha()
        text_entry_bottomleft = pygame.image.load(os.path.join(
            mydir, 'sge_text_entry_bottomleft.png')).convert_alpha()
        text_entry_bottomright = pygame.image.load(os.path.join(
            mydir, 'sge_text_entry_bottomright.png')).convert_alpha()
        button_fill = pygame.image.load(
            os.path.join(mydir, 'sge_button.png')).convert_alpha()
        button_left = pygame.image.load(
            os.path.join(mydir, 'sge_button_left.png')).convert_alpha()
        button_right = pygame.image.load(
            os.path.join(mydir, 'sge_button_right.png')).convert_alpha()
        button_top = pygame.image.load(
            os.path.join(mydir, 'sge_button_top.png')).convert_alpha()
        button_bottom = pygame.image.load(
            os.path.join(mydir, 'sge_button_bottom.png')).convert_alpha()
        button_topleft = pygame.image.load(
            os.path.join(mydir, 'sge_button_topleft.png')).convert_alpha()
        button_topright = pygame.image.load(
            os.path.join(mydir, 'sge_button_topright.png')).convert_alpha()
        button_bottomleft = pygame.image.load(
            os.path.join(mydir, 'sge_button_bottomleft.png')).convert_alpha()
        button_bottomright = pygame.image.load(
            os.path.join(mydir, 'sge_button_bottomright.png')).convert_alpha()
        button_selected_fill = pygame.image.load(
            os.path.join(mydir, 'sge_button_selected.png')).convert_alpha()
        button_selected_left = pygame.image.load(os.path.join(
            mydir, 'sge_button_selected_left.png')).convert_alpha()
        button_selected_right = pygame.image.load(os.path.join(
            mydir, 'sge_button_selected_right.png')).convert_alpha()
        button_selected_top = pygame.image.load(
            os.path.join(mydir, 'sge_button_selected_top.png')).convert_alpha()
        button_selected_bottom = pygame.image.load(os.path.join(
            mydir, 'sge_button_selected_bottom.png')).convert_alpha()
        button_selected_topleft = pygame.image.load(os.path.join(
            mydir, 'sge_button_selected_topleft.png')).convert_alpha()
        button_selected_topright = pygame.image.load(os.path.join(
            mydir, 'sge_button_selected_topright.png')).convert_alpha()
        button_selected_bottomleft = pygame.image.load(os.path.join(
            mydir, 'sge_button_selected_bottomleft.png')).convert_alpha()
        button_selected_bottomright = pygame.image.load(os.path.join(
            mydir, 'sge_button_selected_bottomright.png')).convert_alpha()
        button_press_fill = pygame.image.load(
            os.path.join(mydir, 'sge_button_press.png')).convert_alpha()
        button_press_left = pygame.image.load(
            os.path.join(mydir, 'sge_button_press_left.png')).convert_alpha()
        button_press_right = pygame.image.load(
            os.path.join(mydir, 'sge_button_press_right.png')).convert_alpha()
        button_press_top = pygame.image.load(
            os.path.join(mydir, 'sge_button_press_top.png')).convert_alpha()
        button_press_bottom = pygame.image.load(
            os.path.join(mydir, 'sge_button_press_bottom.png')).convert_alpha()
        button_press_topleft = pygame.image.load(os.path.join(
            mydir, 'sge_button_press_topleft.png')).convert_alpha()
        button_press_topright = pygame.image.load(os.path.join(
            mydir, 'sge_button_press_topright.png')).convert_alpha()
        button_press_bottomleft = pygame.image.load(os.path.join(
            mydir, 'sge_button_press_bottomleft.png')).convert_alpha()
        button_press_bottomright = pygame.image.load(os.path.join(
            mydir, 'sge_button_press_bottomright.png')).convert_alpha()
    except pygame.error as e:
        if sge.DEBUG:
            print(e)
        box_fill = pygame.Surface((1, 1))
        box_left = pygame.Surface((1, 1))
        box_right = pygame.Surface((1, 1))
        box_top = pygame.Surface((1, 1))
        box_bottom = pygame.Surface((1, 1))
        box_topleft = pygame.Surface((1, 1))
        box_topright = pygame.Surface((1, 1))
        box_bottomleft = pygame.Surface((1, 1))
        box_bottomright = pygame.Surface((1, 1))
        text_entry_fill = pygame.Surface((1, 1))
        text_entry_left = pygame.Surface((1, 1))
        text_entry_right = pygame.Surface((1, 1))
        text_entry_top = pygame.Surface((1, 1))
        text_entry_bottom = pygame.Surface((1, 1))
        text_entry_topleft = pygame.Surface((1, 1))
        text_entry_topright = pygame.Surface((1, 1))
        text_entry_bottomleft = pygame.Surface((1, 1))
        text_entry_bottomright = pygame.Surface((1, 1))
        button_fill = pygame.Surface((1, 1))
        button_left = pygame.Surface((1, 1))
        button_right = pygame.Surface((1, 1))
        button_top = pygame.Surface((1, 1))
        button_bottom = pygame.Surface((1, 1))
        button_topleft = pygame.Surface((1, 1))
        button_topright = pygame.Surface((1, 1))
        button_bottomleft = pygame.Surface((1, 1))
        button_bottomright = pygame.Surface((1, 1))
        button_selected_fill = pygame.Surface((1, 1))
        button_selected_left = pygame.Surface((1, 1))
        button_selected_right = pygame.Surface((1, 1))
        button_selected_top = pygame.Surface((1, 1))
        button_selected_bottom = pygame.Surface((1, 1))
        button_selected_topleft = pygame.Surface((1, 1))
        button_selected_topright = pygame.Surface((1, 1))
        button_selected_bottomleft = pygame.Surface((1, 1))
        button_selected_bottomright = pygame.Surface((1, 1))
        button_press_fill = pygame.Surface((1, 1))
        button_press_left = pygame.Surface((1, 1))
        button_press_right = pygame.Surface((1, 1))
        button_press_top = pygame.Surface((1, 1))
        button_press_bottom = pygame.Surface((1, 1))
        button_press_topleft = pygame.Surface((1, 1))
        button_press_topright = pygame.Surface((1, 1))
        button_press_bottomleft = pygame.Surface((1, 1))
        button_press_bottomright = pygame.Surface((1, 1))
        box_fill.fill((255, 255, 255))
        text_entry_fill.fill((255, 255, 255))
        button_fill.fill((255, 255, 255))
        button_selected_fill.fill((0, 255, 255))
        button_press_fill.fill((0, 0, 255))

    # Box image
    box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
    for i in range(0, box_w, box_fill.get_width()):
        for j in range(0, box_h, box_fill.get_height()):
            box.blit(box_fill, (i, j))

    # Clear the way for the corners and edges (so transparency works
    # properly)
    box.fill(pygame.Color(0, 0, 0, 0),
             pygame.Rect((0, 0), box_topleft.get_size()))
    box.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (box_w - box_topright.get_width(), 0), box_topright.get_size()))
    box.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (0, box_h - box_bottomleft.get_height()),
        box_bottomleft.get_size()))
    box.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (box_w - box_bottomright.get_width(),
         box_h - box_bottomright.get_height()),
        box_bottomright.get_size()))

    box.blit(box_topleft, (0, 0))
    box.blit(box_topright, (box_w - box_topright.get_width(), 0))
    box.blit(box_bottomleft, (0, box_h - box_bottomleft.get_height()))
    box.blit(box_bottomright, (box_w - box_bottomright.get_width(),
                               box_h - box_bottomright.get_height()))
    for i in range(box_topleft.get_width(), box_w - box_topright.get_width(),
                    box_top.get_width()):
        box.blit(box_top, (i, 0))
    for i in range(box_bottomleft.get_width(),
                    box_w - box_bottomright.get_width(),
                    box_bottom.get_width()):
        box.blit(box_bottom, (i, box_h - box_bottom.get_height()))
    for i in range(box_topleft.get_height(),
                    box_h - box_bottomleft.get_height(),
                    box_left.get_height()):
        box.blit(box_left, (0, i))
    for i in range(box_topright.get_height(),
                    box_h - box_bottomright.get_height(),
                    box_right.get_height()):
        box.blit(box_right, (box_w - box_right.get_width(), i))
    box_rect = box.get_rect(center=window_rect.center)

    # Text Entry image
    text_entry_field = pygame.Surface((text_entry_w, text_entry_h),
                                      pygame.SRCALPHA)
    for i in range(0, text_entry_w, text_entry_fill.get_width()):
        for j in range(0, text_entry_h, text_entry_fill.get_height()):
            text_entry_field.blit(text_entry_fill, (i, j))

    # Clear the way for the corners and edges (so transparency works
    # properly)
    text_entry_field.fill(pygame.Color(0, 0, 0, 0),
                          pygame.Rect((0, 0), text_entry_topleft.get_size()))
    text_entry_field.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (text_entry_w - text_entry_topright.get_width(), 0),
        text_entry_topright.get_size()))
    text_entry_field.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (0, text_entry_h - text_entry_bottomleft.get_height()),
        text_entry_bottomleft.get_size()))
    text_entry_field.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (text_entry_w - text_entry_bottomright.get_width(),
         text_entry_h - text_entry_bottomright.get_height()),
        text_entry_bottomright.get_size()))

    text_entry_field.blit(text_entry_topleft, (0, 0))
    text_entry_field.blit(text_entry_topright,
                          (text_entry_w - text_entry_topright.get_width(), 0))
    text_entry_field.blit(text_entry_bottomleft, (
        0, text_entry_h - text_entry_bottomleft.get_height()))
    text_entry_field.blit(text_entry_bottomright,
                          (text_entry_w - text_entry_bottomright.get_width(),
                           text_entry_h - text_entry_bottomright.get_height()))
    for i in range(text_entry_topleft.get_width(),
                    text_entry_w - text_entry_topright.get_width(),
                    text_entry_top.get_width()):
        text_entry_field.blit(text_entry_top, (i, 0))
    for i in range(text_entry_bottomleft.get_width(),
                    text_entry_w - text_entry_bottomright.get_width(),
                    text_entry_bottom.get_width()):
        text_entry_field.blit(text_entry_bottom, (
            i, text_entry_h - text_entry_bottom.get_height()))
    for i in range(text_entry_topleft.get_height(),
                    text_entry_h - text_entry_bottomleft.get_height(),
                    text_entry_left.get_height()):
        text_entry_field.blit(text_entry_left, (0, i))
    for i in range(text_entry_topright.get_height(),
                    text_entry_h - text_entry_bottomright.get_height(),
                    text_entry_right.get_height()):
        text_entry_field.blit(text_entry_right, (
            text_entry_w - text_entry_right.get_width(), i))

    text_entry_rect = text_entry_field.get_rect()
    text_entry_rect.left = 4
    text_entry_rect.bottom = box_h - button_h - text_entry_h + 4
    if text_entry:
        box.blit(text_entry_field, text_entry_rect)
    text_entry_rect.w -= 8
    text_entry_rect.h -= 4
    text_entry_rect.left += box_rect.left + 4
    text_entry_rect.top += box_rect.top + 2

    # Button image
    button = pygame.Surface((button_w, button_h), pygame.SRCALPHA)
    for i in range(0, button_w, button_fill.get_width()):
        for j in range(0, button_h, button_fill.get_height()):
            button.blit(button_fill, (i, j))

    # Clear the way for the corners and edges (so transparency works
    # properly)
    button.fill(pygame.Color(0, 0, 0, 0),
                pygame.Rect((0, 0), button_topleft.get_size()))
    button.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (button_w - button_topright.get_width(), 0),
        button_topright.get_size()))
    button.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (0, button_h - button_bottomleft.get_height()),
        button_bottomleft.get_size()))
    button.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (button_w - button_bottomright.get_width(),
         button_h - button_bottomright.get_height()),
        button_bottomright.get_size()))

    button.blit(button_topleft, (0, 0))
    button.blit(button_topright, (button_w - button_topright.get_width(), 0))
    button.blit(button_bottomleft,
                (0, button_h - button_bottomleft.get_height()))
    button.blit(button_bottomright,
                (button_w - button_bottomright.get_width(),
                 button_h - button_bottomright.get_height()))
    for i in range(button_topleft.get_width(),
                    button_w - button_topright.get_width(),
                    button_top.get_width()):
        button.blit(button_top, (i, 0))
    for i in range(button_bottomleft.get_width(),
                    button_w - button_bottomright.get_width(),
                    button_bottom.get_width()):
        button.blit(button_bottom, (i, button_h - button_bottom.get_height()))
    for i in range(button_topleft.get_height(),
                    button_h - button_bottomleft.get_height(),
                    button_left.get_height()):
        button.blit(button_left, (0, i))
    for i in range(button_topright.get_height(),
                    button_h - button_bottomright.get_height(),
                    button_right.get_height()):
        button.blit(button_right, (button_w - button_right.get_width(), i))

    # Button image when selected
    button_selected = pygame.Surface((button_w, button_h), pygame.SRCALPHA)
    for i in range(0, button_w, button_selected_fill.get_width()):
        for j in range(0, button_h, button_selected_fill.get_height()):
            button_selected.blit(button_selected_fill, (i, j))

    # Clear the way for the corners and edges (so transparency works
    # properly)
    button_selected.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (0, 0), button_selected_topleft.get_size()))
    button_selected.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (button_w - button_selected_topright.get_width(), 0),
        button_selected_topright.get_size()))
    button_selected.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (0, button_h - button_selected_bottomleft.get_height()),
        button_selected_bottomleft.get_size()))
    button_selected.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (button_w - button_selected_bottomright.get_width(),
         button_h - button_selected_bottomright.get_height()),
        button_selected_bottomright.get_size()))

    button_selected.blit(button_selected_topleft, (0, 0))
    button_selected.blit(button_selected_topright,
                         (button_w - button_selected_topright.get_width(), 0))
    button_selected.blit(
        button_selected_bottomleft,
        (0, button_h - button_selected_bottomleft.get_height()))
    button_selected.blit(button_selected_bottomright,
                         (button_w - button_selected_bottomright.get_width(),
                          button_h - button_selected_bottomright.get_height()))
    for i in range(button_selected_topleft.get_width(),
                    button_w - button_selected_topright.get_width(),
                    button_selected_top.get_width()):
        button_selected.blit(button_selected_top, (i, 0))
    for i in range(button_selected_bottomleft.get_width(),
                    button_w - button_selected_bottomright.get_width(),
                    button_selected_bottom.get_width()):
        button_selected.blit(
            button_selected_bottom,
            (i, button_h - button_selected_bottom.get_height()))
    for i in range(button_selected_topleft.get_height(),
                    button_h - button_selected_bottomleft.get_height(),
                    button_selected_left.get_height()):
        button_selected.blit(button_selected_left, (0, i))
    for i in range(button_selected_topright.get_height(),
                    button_h - button_selected_bottomright.get_height(),
                    button_selected_right.get_height()):
        button_selected.blit(
            button_selected_right,
            (button_w - button_selected_right.get_width(), i))

    # Button image when pressed
    button_press = pygame.Surface((button_w, button_h), pygame.SRCALPHA)
    for i in range(0, button_w, button_press_fill.get_width()):
        for j in range(0, button_h, button_press_fill.get_height()):
            button_press.blit(button_press_fill, (i, j))

    # Clear the way for the corners and edges (so transparency works
    # properly)
    button_press.fill(pygame.Color(0, 0, 0, 0),
                      pygame.Rect((0, 0), button_press_topleft.get_size()))
    button_press.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (button_w - button_press_topright.get_width(), 0),
        button_press_topright.get_size()))
    button_press.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (0, button_h - button_press_bottomleft.get_height()),
        button_press_bottomleft.get_size()))
    button_press.fill(pygame.Color(0, 0, 0, 0), pygame.Rect(
        (button_w - button_press_bottomright.get_width(),
         button_h - button_press_bottomright.get_height()),
        button_press_bottomright.get_size()))

    button_press.blit(button_press_topleft, (0, 0))
    button_press.blit(button_press_topright,
                      (button_w - button_press_topright.get_width(), 0))
    button_press.blit(button_press_bottomleft,
                      (0, button_h - button_press_bottomleft.get_height()))
    button_press.blit(button_press_bottomright,
                      (button_w - button_press_bottomright.get_width(),
                       button_h - button_press_bottomright.get_height()))
    for i in range(button_press_topleft.get_width(),
                    button_w - button_press_topright.get_width(),
                    button_press_top.get_width()):
        button_press.blit(button_press_top, (i, 0))
    for i in range(button_press_bottomleft.get_width(),
                    button_w - button_press_bottomright.get_width(),
                    button_press_bottom.get_width()):
        button_press.blit(button_press_bottom,
                          (i, button_h - button_press_bottom.get_height()))
    for i in range(button_press_topleft.get_height(),
                    button_h - button_press_bottomleft.get_height(),
                    button_press_left.get_height()):
        button_press.blit(button_press_left, (0, i))
    for i in range(button_press_topright.get_height(),
                    button_h - button_press_bottomright.get_height(),
                    button_press_right.get_height()):
        button_press.blit(button_press_right,
                          (button_w - button_press_right.get_width(), i))

    message_sprite = sge.Sprite(width=text_w, height=text_h)
    message_sprite.draw_text(font, text, 0, 0, text_w, text_h, color='black')
    box.blit(message_sprite._baseimages[0], (4, 4))
    del sge.game.sprites[message_sprite.id]

    selected_buttons = []
    press_buttons = []
    button_rects = []
    button_y = box_h - 8
    for i in range(len(buttons)):
        button_surf = button.copy()
        button_selected_surf = button_selected.copy()
        button_press_surf = button_press.copy()
        rendered_text = font._font.render(buttons[i], True, (0, 0, 0))
        button_rect = button_surf.get_rect()
        render_rect = rendered_text.get_rect(center=button_rect.center)
        button_surf.blit(rendered_text, render_rect)
        button_selected_surf.blit(rendered_text, render_rect)
        button_press_surf.blit(rendered_text, render_rect)
        selected_buttons.append(button_selected_surf)
        press_buttons.append(button_press_surf)

        button_x = box_w * (1 + 2 * i) / (len(buttons) * 2)
        button_rect.centerx = button_x
        button_rect.bottom = button_y
        box.blit(button_surf, button_rect)

        button_rect.left += box_rect.left
        button_rect.top += box_rect.top
        button_rects.append(button_rect)

    background.blit(box, box_rect)

    if text_entry:
        text_entered = default
        cursor_position = len(default)
        selection = 1
    else:
        selection = default
        text_entered = ""
        cursor_position = 0
    prev_axis_value = []
    for j in range(sge.joystick.get_joysticks()):
        axes = []
        for a in range(sge.joystick.get_axes(j)):
            axes.append(0)
        prev_axis_value.append(axes)
    button_entered = None
    button_clicked = None
    text_entry_offset = min(
        0, text_entry_rect.w - font._font.size(text_entered)[0])
    orig_screenshot = screenshot
    orig_background = background
    sge.game._clock.tick()

    # Make the mouse cursor visible
    pygame.mouse.set_visible(True)

    while sge.game._running:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if text_entry:
                        if cursor_position < len(text_entered):
                            cursor_position += 1
                    else:
                        selection += 1
                        selection %= len(buttons)
                elif event.key == pygame.K_LEFT:
                    if text_entry:
                        if cursor_position > 0:
                            cursor_position -= 1
                    else:
                        selection -= 1
                        selection %= len(buttons)
                elif event.key == pygame.K_TAB:
                    selection += 1
                    selection %= len(buttons)
                elif event.key == pygame.K_RETURN:
                    button_entered = selection
                elif event.key == pygame.K_BACKSPACE:
                    if text_entry and cursor_position > 0:
                        text_entered_list = list(text_entered)
                        del text_entered_list[cursor_position - 1]
                        text_entered = ''.join(text_entered_list)
                        cursor_position -= 1
                elif event.key == pygame.K_DELETE:
                    if text_entry and cursor_position < len(text_entered):
                        text_entered_list = list(text_entered)
                        del text_entered_list[cursor_position]
                        text_entered = ''.join(text_entered_list)
                elif event.key == pygame.K_ESCAPE:
                    _finish_modal()
                    return
                elif event.unicode:
                    if text_entry:
                        text_entered_list = list(text_entered)
                        text_entered_list.insert(cursor_position,
                                                 event.unicode)
                        text_entered = ''.join(text_entered_list)
                        cursor_position += 1
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_RETURN or
                        event.key == pygame.K_KP_ENTER):
                    if button_entered == selection:
                        if text_entry:
                            if selection:
                                _finish_modal()
                                return text_entered
                            else:
                                _finish_modal()
                                return None
                        else:
                            _finish_modal()
                            return selection
                    else:
                        button_entered = None
            elif event.type == pygame.JOYAXISMOTION:
                if (event.joy < len(prev_axis_value) and
                        event.axis < len(prev_axis_value[event.joy])):
                    if (event.value >= 0.75 and
                            prev_axis_value[event.joy][event.axis] < 0.75):
                        selection += 1
                        selection %= len(buttons)
                    elif (event.value <= -0.75 and
                          prev_axis_value[event.joy][event.axis] > -0.75):
                        selection -= 1
                        selection %= len(buttons)
                    prev_axis_value[event.joy][event.axis] = event.value
            elif event.type == pygame.JOYHATMOTION:
                x, y = event.value
                if y == 0:
                    if x == 1:
                        selection += 1
                        selection %= len(buttons)
                    elif x == -1:
                        selection -= 1
                        selection %= len(buttons)
            elif event.type == pygame.JOYBALLMOTION:
                x = event.rel[0]
                if x >= 0.75:
                    selection += 1
                    selection %= len(buttons)
                elif x <= -0.75:
                    selection -= 1
                    selection %= len(buttons)
            elif event.type == pygame.JOYBUTTONDOWN:
                button_entered = selection
            elif event.type == pygame.JOYBUTTONUP:
                if button_entered == selection:
                    if text_entry:
                        if selection:
                            _finish_modal()
                            return text_entered
                        else:
                            _finish_modal()
                            return None
                    else:
                        _finish_modal()
                        return selection
                else:
                    button_entered = None
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                for i in range(len(button_rects)):
                    rect = button_rects[i]
                    if (rect.left <= x <= rect.right and
                            rect.top <= y <= rect.bottom):
                        selection = i
                        break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == sge.MOUSE_BUTTONS['left']:
                    x, y = event.pos
                    for i in range(len(button_rects)):
                        rect = button_rects[i]
                        if (rect.left <= x <= rect.right and
                                rect.top <= y <= rect.bottom):
                            button_clicked = i
                            break
            elif event.type == pygame.MOUSEBUTTONUP:
                if (event.button == sge.MOUSE_BUTTONS['left'] and
                        button_clicked is not None):
                    x, y = event.pos
                    rect = button_rects[button_clicked]
                    if (rect.left <= x <= rect.right and
                            rect.top <= y <= rect.bottom):
                        if text_entry:
                            if button_clicked:
                                _finish_modal()
                                return text_entered
                            else:
                                _finish_modal()
                                return
                        else:
                            _finish_modal()
                            return button_clicked
                    else:
                        button_clicked = None
            elif event.type == pygame.QUIT:
                if sge.DEBUG:
                    print('Quit requested by the system.')
                pygame.event.post(event)
                _finish_modal()
                return
            elif event.type == pygame.VIDEORESIZE:
                if sge.DEBUG:
                    print('Video resize detected.')
                sge.game._window_width = event.w
                sge.game._window_height = event.h
                sge.game._set_mode()
                sge.game._background_changed = True
            elif event.type == sge.MUSIC_END_EVENT:
                if sge.game._music_queue:
                    music = sge.game._music_queue.pop(0)
                    music[0].play(*music[1:])

        # Time management
        sge.game._clock.tick(60)

        # Music control
        sge.game._handle_music()
        
        # Redraw
        window.blit(background, (0, 0))
        window.blit(selected_buttons[selection], button_rects[selection])

        if button_entered is not None and button_entered == selection:
            window.blit(press_buttons[button_entered],
                        button_rects[button_entered])
        if button_clicked is not None:
            x, y = pygame.mouse.get_pos()
            rect = button_rects[button_clicked]
            if (rect.left <= x <= rect.right and
                    rect.top <= y <= rect.bottom):
                window.blit(press_buttons[button_clicked],
                            button_rects[button_clicked])

        if text_entry:
            # Find cursor position, adjust offset
            text_before_cursor = text_entered[:cursor_position]
            cursor_base_x = font._font.size(text_before_cursor)[0]
            cursor_x = cursor_base_x + text_entry_offset
            if cursor_x >= text_entry_rect.w:
                text_entry_offset -= cursor_x - text_entry_rect.w - 1
            elif cursor_x < 0:
                text_entry_offset -= cursor_x
            cursor_x = cursor_base_x + text_entry_offset

            # Render text
            rendered_text = font._font.render(text_entered, True, (0, 0, 0))
            text_render_surf = pygame.Surface(text_entry_rect.size,
                                              pygame.SRCALPHA)
            text_render_surf.fill(pygame.Color(0, 0, 0, 0))
            text_render_surf.blit(rendered_text, (text_entry_offset, 0))
            text_render_surf.blit(cursor, (cursor_x, 0))
            window.blit(text_render_surf, text_entry_rect)

        pygame.display.flip()


def _finish_modal():
    sge.game._background_changed = True
    sge.game.mouse.set_cursor()
