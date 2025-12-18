#Common
default main = "Protagonist" 
define narrator = Character(None, window_style="narration_window", what_style="narration_text",
window_auto_hide=True
)

define hrd = Character("Paul", color="#296436")
image hrd confused = At(im.Scale("images/Chara/hrd_confused.png", 2300, 2300), Transform(xalign=0.5, yalign=0))
image hrd happy = At(im.Scale("images/Chara/hrd_happy.png", 2300, 2300), Transform(xalign=0.5, yalign=0))
image hrd normal = At(im.Scale("images/Chara/hrd_normal.png", 2300, 2300), Transform(xalign=0.5, yalign=0))
image hrd thinking = At(im.Scale("images/Chara/hrd_thinking.png", 2300, 2300), Transform(xalign=0.5, yalign=0))


define randP = Character("Orang misterius", color="#e81010")
image randP = At(im.Scale("images/Chara/randP.png", 2300, 2300), Transform(xalign=0.5, yalign=0))

define bos = Character("Bos Brando", color="#e8880bff")
image bos confused = At(im.Scale("images/Chara/bos_confused.png", 2300, 2300), Transform(xalign=0.5, yalign=0))
image bos happy = At(im.Scale("images/Chara/bos_happy.png", 2300, 2300), Transform(xalign=0.5, yalign=0))
image bos normal = At(im.Scale("images/Chara/bos_normal.png", 2300, 2300), Transform(xalign=0.5, yalign=0))
image bos thinking = At(im.Scale("images/Chara/bos_thinking.png", 2300, 2300), Transform(xalign=0.5, yalign=0))

define rekan = Character("Juleya", color="#2c0aefd2")
image rekan normal = At(im.Scale("images/Chara/rekan_normal.png", 2700, 2200), Transform(xalign=1, yalign=-1))
image rekan happy = At(im.Scale("images/Chara/rekan_happy.png", 2700, 2200), Transform(xalign=1, yalign=-1))
image rekan nervous = At(im.Scale("images/Chara/rekan_nervous.png", 2700, 2200), Transform(xalign=1, yalign=-1))
image rekan shock = At(im.Scale("images/Chara/rekan_shock.png", 2700, 2200), Transform(xalign=1, yalign=-1))

define kakak = Character("Kakak", color="#989608f5")
image kakak happy = At(im.Scale("images/Chara/kakak_happy.png", 2000, 2000), Transform(xalign=0.5, yalign=-0.1))
image kakak normal = At(im.Scale("images/Chara/kakak_normal.png", 2000, 2000), Transform(xalign=0.5, yalign=-0.1))

define staffKopi = Character("Staff Coffe Shop", color="#740c057a")
image sk concerned = At(im.Scale("images/Chara/sk_concerned.png", 2000, 2000), Transform(xalign=0.5, yalign=-0.1))
image sk happy = At(im.Scale("images/Chara/sk_happy.png", 2000, 2000), Transform(xalign=0.5, yalign=-0.1))
image sk normal = At(im.Scale("images/Chara/sk_normal.png", 2000, 2000), Transform(xalign=0.5, yalign=-0.1))
image sk thinking = At(im.Scale("images/Chara/sk_thinking.png", 2000, 2000), Transform(xalign=0.5, yalign=-0.1))

define managerKeu = Character("Manager Keuangan", color="#fa00b3f5")
image manKeu confused = At(im.Scale("images/Chara/manKeu_confused.png", 2000, 2000), Transform(xalign=0.5, yalign=-0.1))
image manKeu happy = At(im.Scale("images/Chara/manKeu_happy.png", 2000, 2000), Transform(xalign=0.5, yalign=-0.1))
image manKeu normal = At(im.Scale("images/Chara/manKeu_normal.png", 2000, 2000), Transform(xalign=0.5, yalign=-0.1))
image manKeu thinking = At(im.Scale("images/Chara/manKeu_thinking.png", 2000, 2000), Transform(xalign=0.5, yalign=-0.1))

define staff = Character("Parto", color="#f904e5d2")
image staff normal = At(im.Scale("images/Chara/staff_normal.png", 2000, 2000), Transform(xalign=0.5, yalign=-0.1))
image staff happy = At(im.Scale("images/Chara/staff_happy.png", 2000, 2000), Transform(xalign=0.5, yalign=-0.1))
image staff shock = At(im.Scale("images/Chara/staff_shock.png", 2000, 2000), Transform(xalign=0.5, yalign=-0.1))
image staff thinking = At(im.Scale("images/Chara/staff_thinking.png", 2000, 2000), Transform(xalign=0.5, yalign=-0.1))
