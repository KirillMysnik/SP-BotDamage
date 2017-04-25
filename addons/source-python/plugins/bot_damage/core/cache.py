# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
from enum import IntEnum

# Source.Python
from events import Event
from players.dictionary import PlayerDictionary

# Bot Damage
from .cvars import config_manager
from .settings import bot_damage_settings


# =============================================================================
# >> CLASSES
# =============================================================================
class DamageMultiplier(IntEnum):
    LOWER = -1
    USUAL = 0
    HIGHER = 1


class PlayerSettingCache:
    def __init__(self, index, setting, cvar_lower, cvar_higher):
        self._index = index
        self._setting = setting
        self._cvar_lower = cvar_lower
        self._cvar_higher = cvar_higher

        self._multiplier = 1.0

    def refresh(self):
        value = DamageMultiplier(self._setting.get_setting(self._index))

        if value == DamageMultiplier.LOWER:
            self._multiplier = config_manager[self._cvar_lower]

        elif value == DamageMultiplier.HIGHER:
            self._multiplier = config_manager[self._cvar_higher]

        else:
            self._multiplier = 1.0

    @property
    def multiplier(self):
        return self._multiplier


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
caches_to = PlayerDictionary(lambda index: PlayerSettingCache(
    index,
    bot_damage_settings['modifier_to'],
    'damage_to_lower_multiplier',
    'damage_to_higher_multiplier'
))

caches_from = PlayerDictionary(lambda index: PlayerSettingCache(
    index,
    bot_damage_settings['modifier_from'],
    'damage_from_lower_multiplier',
    'damage_from_higher_multiplier'
))


# =============================================================================
# >> EVENTS
# =============================================================================
@Event('player_spawn')
def on_player_spawn(game_event):
    for caches in (caches_from, caches_to):
        cache = caches.from_userid(game_event['userid'])
        cache.refresh()
