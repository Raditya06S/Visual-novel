# Example: character base definitions
image mc_normal = ConditionSwitch(
    "gender == 'male'", Image ("images/Main/Male/mmc_normal.png"),
    "gender == 'female'", im.Scale("images/Main/Female/fmc_normal.png", 450, 450)
)

image mc sad = ConditionSwitch(
    "gender == 'male'", "images/Chara/Main/Male/mmc_sad.png",
    "gender == 'female'", "images/Chara/Main/Female/fmc_sad.png",
)

image mc neutral = ConditionSwitch(
    "gender == 'male'", "images/Chara/Main/Male/mmc_neutral.png",
    "gender == 'female'", "images/Chara/Main/Female/fmc_neutral.png",
)
