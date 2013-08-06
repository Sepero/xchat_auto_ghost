__module_name__ = "Auto Ghost"
__module_version__ = "0.1.0"
__module_description__ = "Ghost the default nick and change to it."

print "\0034",__module_name__, __module_version__,"has been loaded\003"

import xchat
import time

def on_server_connected(word, word_eol, userdata):
    chan = xchat.get_context()
    desired_nick = xchat.get_prefs("irc_nick1")
    current_nick = xchat.get_info("nick")
    password = xchat.get_info("nickserv")
    
    if password:
        if current_nick != desired_nick:
            xchat.command("msg nickserv ghost %s %s" % (desired_nick, password))
            time.sleep(1)
            xchat.command("nick %s" % desired_nick)
            time.sleep(1)
    
        xchat.command("msg nickserv identify %s" % password)
    
    return xchat.EAT_NONE

xchat.hook_server("255", on_server_connected)
