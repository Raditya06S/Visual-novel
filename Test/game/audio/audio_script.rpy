init python:
    renpy.music.register_channel("Loop", "bgm")
    renpy.music.register_channel("SFX", "sfx")
    renpy.music.register_channel("Sound", "bgs")


define audio.bgm_home = "audio/bgm/home.mp3"