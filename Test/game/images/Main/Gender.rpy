image mc = ConditionSwitch(
    "gender == 'male'", Image ("images/Chara/Main/Male/male.png"),
    "gender == 'female'", Image ("images/Chara/Main/Female/female.png"),
)
