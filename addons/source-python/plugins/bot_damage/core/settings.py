# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from settings.player import PlayerSettings

# Bot Damage
from .strings import common_strings


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
bot_damage_settings = PlayerSettings(
    "bot_damage", "bot_damage_", common_strings['section title'])

bot_damage_settings.add_int_setting(
    "modifier_to", 0, common_strings['damage_to title'], -1, 1)

bot_damage_settings.add_int_setting(
    "modifier_from", 0, common_strings['damage_from title'], -1, 1)
