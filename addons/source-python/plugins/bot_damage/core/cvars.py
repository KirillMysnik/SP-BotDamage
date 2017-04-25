# =============================================================================
# >> IMPORTS
# =============================================================================
# Custom Package
from controlled_cvars import ControlledConfigManager
from controlled_cvars.handlers import bool_handler, float_handler

# PLRBots
from ..info import info
from .strings import config_strings


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
config_manager = ControlledConfigManager(
    info.name + "/main", cvar_prefix='bot_damage_')

config_manager.section(config_strings['section general'])
config_manager.controlled_cvar(
    bool_handler,
    "send_popup_on_connect",
    default=1,
    description=config_strings['send_popup_on_connect'],
)

config_manager.section(config_strings['section damage_to'])
config_manager.controlled_cvar(
    float_handler,
    "damage_to_lower_multiplier",
    default=0.33,
    description=config_strings['damage_to_lower_multiplier'],
)
config_manager.controlled_cvar(
    float_handler,
    "damage_to_higher_multiplier",
    default=3.0,
    description=config_strings['damage_to_higher_multiplier'],
)

config_manager.section(config_strings['section damage_from'])
config_manager.controlled_cvar(
    float_handler,
    "damage_from_lower_multiplier",
    default=0.33,
    description=config_strings['damage_from_lower_multiplier'],
)
config_manager.controlled_cvar(
    float_handler,
    "damage_from_higher_multiplier",
    default=3.0,
    description=config_strings['damage_from_higher_multiplier'],
)

config_manager.write()
config_manager.execute()
