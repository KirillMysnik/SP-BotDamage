# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from entities import TakeDamageInfo
from entities.entity import Entity
from entities.hooks import EntityCondition, EntityPreHook
from events import Event
from memory import make_object
from players.entity import Player
from players.dictionary import PlayerDictionary

# Bot Damage
from .core.cache import caches_from, caches_to
from .core.cvars import config_manager
from .core.settings import bot_damage_settings


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
sent_popups = PlayerDictionary(lambda index: False)


# =============================================================================
# >> EVENTS
# =============================================================================
@Event('player_spawn')
def on_player_spawn(game_event):
    if not config_manager['send_popup_on_connect']:
        return

    player = Player.from_userid(game_event['userid'])
    if player.is_bot():
        return

    if sent_popups[player.index]:
        return

    bot_damage_settings.menu.send(player.index)
    sent_popups[player.index] = True


# =============================================================================
# >> HOOKS
# =============================================================================
@EntityPreHook(EntityCondition.is_player, 'on_take_damage')
def pre_on_take_damage(args):
    # Get the victim
    victim = make_object(Player, args[0])

    # Get TakeDamageInfo object
    info = make_object(TakeDamageInfo, args[1])

    # Was it a self-inflicted damage?
    if info.attacker == victim.index:
        return

    # Check if attacker is a player
    entity = Entity(info.attacker)
    if not entity.is_player():
        return

    # Get the attacker
    attacker = Player(info.attacker)

    # Do our thing
    if attacker.is_bot() and not victim.is_bot():
        info.damage *= caches_from[victim.index].multiplier

    elif not attacker.is_bot() and victim.is_bot():
        info.damage *= caches_to[attacker.index].multiplier
