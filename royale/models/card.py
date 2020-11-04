class Card:
    def __init__(self, name: str, type: str, arena: int, rarity: str, id, cost,
                 icon, hash):
        self.name = name

        # For CHAPTER 4 - CHALLENGE 2 - Map:
        #   tid_card_type_building to Building
        #   tid_card_type_spell to Spell
        #   tid_card_type_character to Troop
        self.type = type.replace('tid_card_type_',
                                 '').replace('character',
                                             'troop').capitalize()

        self.arena = arena
        self.rarity = rarity

        # TODO: Are these 4 fields needed?
        self.id = id
        self.cost = cost
        self.icon = icon
        self.hash = hash
