warlocks_monster_names_en = {
    1: ['White', 'Yellow', 'Blue', 'Red', 'Green', 'Black', 'Brown'],
    2: ['Azure', 'Ivory', 'Teal', 'Silver', 'Purple', 'Navy blue', 'Pea green'],
    3: ['Gray', 'Orange', 'Maroon', 'Charcoal', 'Aquamarine', 'Coral', 'Fuchsia'],
    4: ['Wheat', 'Lime', 'Crimson', 'Khaki', 'Hot pink', 'Magenta', 'Olden', 'Plum', 'Olive', 'Cyan'],
    5: ['Fire Elemental'],
    6: ['Ice Elemental']
}

warlocks_monster_classes_en = {
    1: 'Goblin',
    2: 'Ogre',
    3: 'Troll',
    4: 'Giant',
    5: 'Fire Elemental',
    6: 'Ice Elemental'
}

warlocks_spell_names_en = {
    1: 'Dispel Magic',
    2: 'Counter Spell',
    3: 'Magic Mirror',
    4: 'Summon Goblin',
    5: 'Summon Ogre',
    6: 'Summon Troll',
    7: 'Summon Giant',
    8: 'Summon Fire Elemental',
    9: 'Summon Ice Elemental',
    10: 'Haste',
    11: 'Time Stop',
    12: 'Protection',
    13: 'Resist Heat',
    14: 'Resist Cold',
    15: 'Paralysis',
    16: 'Amnesia',
    17: 'Fear',
    18: 'Maladroitness',
    19: 'Charm Monster',
    20: 'Charm Person',
    21: 'Disease',
    22: 'Poison',
    23: 'Cure Light Wounds',
    24: 'Cure Heavy Wounds',
    25: 'Anti-Spell',
    26: 'Blindness',
    27: 'Invisibility',
    28: 'Permanency',
    29: 'Delay Effect',
    30: 'Remove Enchantment',
    31: 'Shield',
    32: 'Magic Missile',
    33: 'Cause Light Wounds',
    34: 'Cause Heavy Wounds',
    35: 'Fireball',
    36: 'Lightning Bolt',
    37: 'Clap of Lightning',
    38: 'Finger of Death',
    39: 'Fire Storm',
    40: 'Ice Storm',
}

warlocks_spell_effects_en = {
    'MShield': 'Magic Shield',
    'MagicMirror': 'Magic Mirror',
    'Haste': 'Haste',
    'TimeStop': 'Time Stop',
    'Protection': 'Protection',
    'ResistHeat': 'Resist Heat',
    'ResistCold': 'Resist Cold',
    'Paralysis': 'Paralysis',
    'Amnesia': 'Amnesia',
    'Fear': 'Fear',
    'Maladroitness': 'Maladroitness',
    'CharmPerson': 'Charm Person',
    'Disease': 'Disease',
    'Poison': 'Poison',
    'Blindness': 'Blindness',
    'Invisibility': 'Invisibility',
    'Permanency': 'Permanency',
    'DelayEffect': 'Delay Effect',
    'PShield': 'Shield'
}

warlocks_text_strings_en = {

    'gestureN': '{name} makes no gesture with {pronoun} {handname}.',
    'gestureC': '{name} claps.',
    'gestureC2': '{name} flailingly half-claps with {pronoun} {handname}.',
    'gestureD': '{name} points the digit of {pronoun} {handname}.',
    'gestureF': '{name} wiggles the fingers of {pronoun} {handname}.',
    'gestureP': '{name} proffers the palm of {pronoun} {handname}.',
    'gestureS': '{name} snaps the fingers of {pronoun} {handname}.',
    'gestureW': '{name} waves {pronoun} {handname}.',
    'gestureT': '{name} stabs with {pronoun} {handname}.',

    'resultActorDies': '{name} dies.',
    'resultActorSurrenders': '{name} surrenders.',
    'resultActorSuicides': "{name} stops {pronoun} heart through force of will alone.",
    'resultActorVictorious': '{name} is victorious!',
    'resultTeamVictorious': 'Team of {some_str} is victorious!',
    'resultDraw': 'No Warlocks remaining. An ignominious end to a battle.',

    'effectParalysis1': "{targetname}'s {handname} is paralyzed.",
    'effectParalysis2': "{name} can't move to attack.",
    'effectAmnesia1': "{targetname} forgets what he's doing, and makes the same gestures as last round!",
    'effectAmnesia2': "{name} forgets to attack anyone.",
    'effectFear1': "{targetname} quakes in fear!",
    'effectFear2': "{name} is too scared to attack.",
    'effectMaladroitness1': "{targetname} is rendered maladroit!",
    'effectMaladroitness2': "{name} tries to attack, but trips on its feet.",
    'effectCharmPerson1': "{targetname} is charmed into making the wrong gesture with {pronoun} {handname}.",
    'effectCharmPerson2': "{name} is charmed, but ends up making the gestures {pronoun} intended anyway!",

    'effectMindSpellCancel': '{targetname} shakes {pronoun} head and regains control, as enchantments cancel each other out.',

    'effectPermanency': '{name} attempts to make the spell permanent!',
    'effectDelaySpell': '{name} banks a spell for later.',

    'effectResistHeat': "{attackname} basks in the fiery heat.",
    'effectResistCold': "{attackname} enjoys the icy chill.",

    'effectShieldFromElemental': "{attackname}'s shield keeps the {name} at bay.",
    'effectShieldFromMonster': "{name} attacks {attackname}, but is deflected by a shield.",

    'effectStormProtectedByMShield': '{targetname} is protected by a magical shield.',
    'effectFireStormIceStormCancel': 'Fire and Ice storms cancel each other out, leaving just a gentle breeze.',
    'effectFireStormIceElementalCancel': 'Ice Elemental melts, calming and cooling the Fire Storm.',
    'effectIceStormFireElementalCancel': 'The Fire Elemental melts the oncoming Ice Storm, and is destroyed by the ensuing water.',
    'effectElementalAbsorbedByStorm': 'The {some_str} flies away with the storm.',
    'effectFireElementalIceElementalCancel': 'Opposing Elementals destroy each other!',
    'effectFireElementalsMerge': 'Fire Elementals merge into one.',
    'effectIceElementalsMerge': 'Ice Elementals merge into one.',

    'effectFireStormResistHeat': "{targetname} basks in the heat of the Fire Storm.",
    'effectFireStormDamaged': "{targetname} is burnt in the raging Fire Storm, for 5 damage.",
    'effectIceStormResistHeat': "{targetname} looks comfortable in the cooling Ice Storm.",
    'effectIceStormDamaged': "{targetname} is frozen by the raging Ice Storm, for 5 damage.",

    'effectPoisonFatal': "{name}'s Poison is fatal.",
    'effectDiseaseFatal': "{name}'s Disease is fatal.",
    'effectSickness1': "{name} starts coughing up blood.",
    'effectSickness2': "{name} staggers weakly.",
    'effectSickness3': "{name} is sweating feverishly.",
    'effectSickness4': "{name} is having difficulty breathing.",
    'effectSickness5': "{name} is looking pale.",
    'effectSickness6': "{name} is a bit nauseous.",
    'effectSickness7': "{name}'s stomach rumbles.", # not used
    'effectBlindness1': "{name}'s eyes are covered with scales!",
    'effectBlindness2': "The scales are removed from {name}'s eyes.",
    'effectInvisibility1': "There is a flash, and {name} disappears!",
    'effectInvisibility2': "{name} fades back into visibility.",

    'effectTimeStop': "This turn took place outside of time.",
    'effectHaste': "Fast warlocks sneak in an extra set of gestures.",

    'attackOrder': "{name} orders {targetname} to attack {attackname}.",
    'attackMissesBlindness': "{name} attacks {attackname} but misses due to Blindness.",
    'attackMissesInvisibility': "{name} attacks {attackname} but misses due to Invisibility.",
    'attackMissesNobody': "{name} wanders around aimlessly.",
    'stabMissesNobody': "{name} doesn't attack anyone.",

    'attackFireElem': "The Fire Elemental runs amok!",
    'attackIceElem': "The Ice Elemental runs amok!",
    'attackFireElemHasted': "In a burst of speed, the Fire Elemental runs amok again!",
    'attackIceElemHasted': "In a burst of speed, the Ice Elemental runs amok again!",
    'attackFireElemTimestopped': "Outside of time, the Fire Elemental runs amok again!",
    'attackIceElemTimestopped': "Outside of time, the Ice Elemental runs amok again!",

    'attackMonsterHasted': "In a burst of speed, {name} attacks again!",
    'attackMonsterTimestopped': "Outside time, {name} attacks again!",

    'damagedByFireElem': "{attackname} is burnt for {damage} damage.",
    'damagedByIceElem': "{attackname} is frozen for {damage} damage.",
    'damagedByMonster': "{name} attacks {attackname} for {damage} damage.",

    'castGenericNobody': "{name} casts {spellname} at nobody.",
    'castGenericPoM': "{name} casts {spellname} at {targetname}.",
    'castGenericHand': "{name} casts {spellname} at the monster {targetname} is summoning with {pronoun} {handname}.",
    'castDelayedNobody': "{name} casts banked {spellname} at nobody.",
    'castDelayedPoM': "{name} casts banked {spellname} at {targetname}.",
    'castDelayedHand': "{name} casts banked {spellname} at the monster {targetname} is summoning with {pronoun} {handname}.",
    'castMissesInvisibility': "{spellname} misses {targetname} due to Invisibility.",
    'castMissesBlindness': "{spellname} misses {targetname} due to Blindness.",
    'castReflected': "{spellname} is reflected from {targetname}'s Magic Mirror back at {name}.",
    'castReflectedInvisibility': "{spellname} is reflected from {targetname}'s Magic Mirror, but misses due to Invisibility.",
    'castReflectedBlindness': "{spellname} is reflected from {targetname}'s Magic Mirror, but misses due to Blindness.",
    'castReflectedInfinite': "{spellname} is reflected between {name} and {targetname} Magic Mirrors until it's gone.",

    'castDispelMagicResolved': "All magical effects are erased! All other spells fail!",
    'castCounterSpellNobody': "A Counter Spell drifts away aimlessly.",
    'castCounterSpellResolved': "{targetname} is covered by a magical glowing shield.",
    'castMagicMirrorNobody': "A Magic Mirror dissipates into the air.",
    'castMagicMirrorCountered': "{name}'s Magic Mirror is absorbed into a glow.",
    'castMagicMirrorResolved': "{targetname} is covered by a reflective shield.",
    'сastSummonMonsterNobody': 'A summoned creature, finding no master, returns from whence it came.',
    'castSummonMonsterCountered': "{name}'s {targetname} is absorbed into a Counterspell glow.",
    'castSummonMonsterResolved': "{attackname} is summoned to serve {targetname}.",
    'castFireElementalResolved': "{name} casts Summon Fire Elemental at {targetname}.",
    'castIceElementalResolved': "{name} casts Summon Ice Elemental at {targetname}.",
    'castFireElementalResolved2': "A Fire Elemental appears in a furious roar of flame!",
    'castIceElementalResolved2': "An Ice Elemental appears in a sudden rush of arctic wind!",
    'castHasteNobody': '',
    'castHasteCountered': "{targetname} shield sparkles rapidly for a moment.",
    'castHasteResolved': "{targetname} speeds up!",
    'castTimeStopNobody': '',
    'castTimeStopCountered': "{targetname} shield looks thicker for a moment, then fades back.",
    'castTimeStopResolved': "{targetname} flickers out of time!",
    'castProtectionNobody': '',
    'castProtectionCountered': "{targetname}'s shield looks momentarily more solid.",
    'castProtectionResolved': "{targetname} is surrounded by a thick shimmering shield.",
    'castResistHeatNobody': '',
    'castResistHeatCountered': "{targetname}'s shield looks thicker for a moment, then fades back.",
    'castResistHeatResolved': "{targetname} is covered in a coat of sparkling frost.",
    'castResistHeatDestroysFireElemental': 'Fire Elemental is destroyed by a Resist Heat spell.',
    'castResistColdNobody': '',
    'castResistColdCountered': "{targetname}'s shield looks thicker for a moment, then fades back.",
    'castResistColdResolved': "{targetname} is covered by a warm glow.",
    'castResistColdDestroysIceElemental': 'Ice Elemental is destroyed by a Resist Cold spell.',
    'castMindSpellNobody': "The haze of an enchantment spell drifts aimlessly over the circle, and dissipates.",
    'castMindSpellCountered': "'s shield blurs for a moment.",
    'castMindSpellOverridenByPermanent': "The permanent mindspell on {targetname} overrides the {spellname} effect.",
    'castParalysisResolved': "{targetname}'s hands start to stiffen.",
    'castAmnesiaResolved': "{targetname} starts to look blank.",
    'castFearResolved': "{targetname} cringes in fear.",
    'castMaladroitnessResolved': "{targetname} starts to lose coordination.",
    'castCharmMonsterWrongTargetType': "{targetname} ignores {name}'s appeal to {pronoun} baser instincts.",
    'castCharmMonsterElemental': "{targetname} is indifferent to {name}'s charms.",
    'castCharmMonsterResolved': "{targetname} looks, glassy-eyed, at {name}",
    'castCharmPersonWrongTargetType': "{targetname} appears unaffected by {name}'s intellectual charms.",
    'castCharmPersonResolved': "{targetname} looks intrigued by {name}.",
    'castSicknessNobody': "",
    'castSicknessCountered': "{targetname}'s shield turns a greenish hue for a moment.",
    'castSicknessResolved': "{targetname} starts to look sick.",
    'castCureWoundsNobody': "",
    'castCureWoundsCountered': "Tiny holes in {targetname}'s shield are sealed up.",
    'castCureWoundsResolved': "{targetname} is healed.",
    'castAntiSpellNobody': "",
    'castAntiSpellCountered': "{targetname}'s shield fizzles slightly.",
    'castAntiSpellResolved': "{targetname}'s half-done spells fizzle and die.",
    'castBlindnessNobody': "",
    'castBlindnessCountered': "{targetname}'s shield disappears for a moment.",
    'castBlindnessResolved': "Scales start to grow over {targetname}'s eyes!",
    'castBlindnessResolvedMonster': "{targetname} is hit by a Blindness spell, and is annihilated by the magical overload.",
    'castInvisibilityNobody': "",
    'castInvisibilityCountered': "{targetname}'s shield disappears for a moment.",
    'castInvisibilityResolved': "{targetname} begins to shimmer.",
    'castInvisibilityResolvedMonster': "{targetname} is hit by an Invisibility spell, and is annihilated by the magical overload.",
    'castPermanencyAndDelayNobody': "",
    'castPermanencyAndDelayCountered': "{targetname}'s shield intensified momentarily.",
    'castPermanencyAndDelayResolved': "{targetname} begins glowing faintly.",
    'castRemoveEnchantmentNobody': "",
    'castRemoveEnchantmentCountered': "{targetname}'s shield flickers, but remains firm.",
    'castRemoveEnchantmentResolved': "{targetname}'s surrounding magical energies are grounded.",
    'castRemoveEnchantmentResolvedMonster': "{targetname} is hit by Remove Enchantment, and starts coming apart at the seams.",
    'castShieldNobody': "The shimmer of a shield briefly covers the circle, then dissolves.",
    'castShieldCountered': "",
    'castShieldResolved': "{targetname} is covered by a shimmering shield.",
    'castMagicMissileNobody': "A magic missile flies off into the distance.",
    'castMagicMissileCountered': "A magic missile bounces off {targetname}'s shield.",
    'castMagicMissileResolved': "{targetname} is hit by a Magic Missile, for 1 damage.",
    'castCauseWoundsNobody': "",
    'castCauseWoundsCountered': "Holes open up in {targetname}'s shield, but then close up again.",
    'castCauseWoundsResolved': "Wounds appear all over {targetname}'s body!",
    'castFireballNobody': "A fireball flies into the distance and burns itself out.",
    'castFireballCountered': "A fireball strikes, and flames roar all around {targetname}'s shield.",
    'castFireballResolved': "A fireball strikes {targetname}, burning {pronoun} for 5 damage.",
    'castFireballResistHeat': "A fireball strikes, and flames roar around {targetname}. {pronoun} stands calmly in the inferno.",
    'castFireballIceElemental': "Ice Elemental is destroyed by a Fireball spell",
    'castLightningBoltNobody': "A bolt of lightning arcs to the ground.",
    'castLightningBoltCountered': "Lightning sparks all around {targetname}'s shield.",
    'castLightningBoltResolved': "{targetname} is hit by a bolt of lightning, for 5 damage.",
    'castClapOfLightningFizzle': "{name} tries to cast Clap of Lightning, but doesn't have the charge for it.",
    'castFingerOfDeathNobody': "",
    'castFingerOfDeathResolved': "{targetname} is touched with the Finger of Death.",
    'castFireStormResolved': "A Fire Storm rages through the circle!",
    'castIceStormResolved': "An Ice Storm rages through the circle!",
}
