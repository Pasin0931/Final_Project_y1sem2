player =          {"health": 50, "power": 2, "critical": 0.05, "stamina": 50}

# knight_class = {"health": 100, "power": 2, "critical": 0.05, "stamina": 50}
# warrior_class = {"health": 50, "power": 5, "critical": 0.20, "stamina": 35}

# -------------------------

skeleton =        {"health": 5,   "power": 10, "critical": 0.02}
goblin =          {"health": 15,  "power": 8,  "critical": 0.03}
mushroom =        {"health": 25,  "power": 6,  "critical": 0.01}
big_mushroom =    {"health": 45,  "power": 10, "critical": 0.01}
flying_eye =      {"health": 20,  "power": 7,  "critical": 0.04}

# -------------------------

minotaur =        {"health": 200, "power": 4,  "critical": 0.06}
stone_golem =     {"health": 300, "power": 3,  "critical": 0.04}
tarnished_widow = {"health": 250, "power": 5,  "critical": 0.08}


lv1_sts = {
    "enemy": ["skeleton", "skeleton", "skeleton", "skeleton", "skeleton",
              "goblin", "goblin", "goblin", "goblin", "goblin",
              "mushroom", "mushroom", "mushroom",
              "big_mushroom",
              "flying_eye"],
    "boss":  ["minotaur", "minotaur", "minotaur", "minotaur", "minotaur",
              "golem", "golem"]
}

lv2_sts = {
    "enemy": ["skeleton", "skeleton", "skeleton", "skeleton", "skeleton",
              "goblin", "goblin", "goblin", "goblin", "goblin",
              "mushroom", "mushroom", "mushroom",
              "big_mushroom",
              "flying_eye"],
    "boss":  ["minotaur", "minotaur", "minotaur",
              "golem", "golem", "golem"]
}

lv3_sts = {
    "enemy": ["skeleton",
              "goblin", "goblin",
              "mushroom", "mushroom", "mushroom", "mushroom", "mushroom",
              "big_mushroom", "big_mushroom",
              "flying_eye", "flying_eye"],
    "boss":  ["minotaur", "minotaur",
              "golem", "golem", "golem", "golem",
              "widow"]
}

lv4_sts = {
    "enemy": ["skeleton",
              "goblin",
              "mushroom", "mushroom", "mushroom", "mushroom",
              "big_mushroom", "big_mushroom",
              "flying_eye", "flying_eye", "flying_eye", "flying_eye"],
    "boss":  ["golem", "golem", "golem",
              "widow", "widow", "widow"]
}

lv5_sts = {
    "enemy": ["skeleton", "skeleton", "skeleton", "skeleton",
              "mushroom", "mushroom", "mushroom",
              "big_mushroom", "big_mushroom", "big_mushroom",
              "flying_eye", "flying_eye", "flying_eye", "flying_eye"],
    "boss":  ["golem",
              "widow", "widow", "widow", "widow", "widow"]
}