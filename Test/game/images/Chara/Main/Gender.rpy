image mc normal = ConditionSwitch(
    "gender == 'male'", im.Scale("images/Chara/Main/Male/mmc_normal.png", 550, 550),
    "gender == 'female'", im.Scale("images/Chara/Main/Female/fmc_normal.png", 550, 550)
)

image mc confused = ConditionSwitch(
    "gender == 'male'", im.Scale("images/Chara/Main/Male/mmc_confused.png", 550, 550),
    "gender == 'female'", im.Scale("images/Chara/Main/Female/fmc_confused.png", 550, 550)
)


image mc shock = ConditionSwitch(
    "gender == 'male'", im.Scale("images/Chara/Main/Male/mmc_shock.png", 550, 550),
    "gender == 'female'", im.Scale("images/Chara/Main/Female/fmc_shock.png", 550, 550)
)

image mc happy = ConditionSwitch(
    "gender == 'male'", im.Scale("images/Chara/Main/Male/mmc_happy.png", 550, 550),
    "gender == 'female'", im.Scale("images/Chara/Main/Female/fmc_happy.png", 550, 550)
)


