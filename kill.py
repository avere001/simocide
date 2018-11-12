"""
Simocide

This mod adds a command to kill any sim. Currently only does so by starving said sim.

|kill Malcolm Landgraab

Will starve Malcolm Langraab to death immediately
"""
import sims4.commands
import services
    
@sims4.commands.Command('kill', command_type=sims4.commands.CommandType.Live)
def killSim(first_name:str="", last_name:str="" , _connection=None):
    """
    starves a sim to death
    
    first_name: first name of sim
    last_name: last name of sim
    """
    output = sims4.commands.CheatOutput(_connection)

    if last_name == "":
        output("Usage: kill first_name last_name")
        return

    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    
    sim_info = services.sim_info_manager().get_sim_info_by_name(first_name, last_name)
    if sim_info is not None:
        coms = sim_info.commodity_tracker.get_all_commodities()
        hunger = getMotiveByName(coms, "hunger")
        output("Goodbye, {} {}!".format(first_name, last_name))
        hunger.set_value(hunger.min_value)
    else:
        output("No sim found named {} {}!".format(first_name, last_name))

def getCommodityName(com):
    """ extracts the name of the commodity """
    return str(com).split('(')[1].split('@')[0]

def getMotiveByName(coms, com_name):
    """ retrieves the appropriate motive """
    com_name = "motive_" + com_name.capitalize()
    for com in coms:
        if getCommodityName(com) == com_name:
            return com
    return None
