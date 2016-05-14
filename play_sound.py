# -*- coding: utf-8 -*-
import winsound


def play_sound(file_address):
    winsound.PlaySound(file_address, winsound.SND_FILENAME)