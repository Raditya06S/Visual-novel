
screen character_choose:

    add "gui/hero_select.png"


    imagebutton:
        idle "maleIdle"
        hover "maleHover"
        xpos 1008
        ypos 255
        focus_mask  True
        action [SetVariable("gender", "male"), SetVariable("main", "Budi"), Jump("name_input")]
    
    imagebutton:
        idle "femaleIdle"
        hover "femaleHover"
        xpos 215
        ypos 265
        focus_mask  True
        action [SetVariable("gender", "female"), SetVariable("main", "Siti"), Jump("name_input")]

screen name_input:
    add "gui/Siapa namamu.png"