__module_name__ = "Auto Ghost"
__module_version__ = "0.1.1"
__module_description__ = "Ghost the default nick and change/identify as that user."

display = (__module_name__ + " " + __module_version__ + " has been loaded.",
"Module URL: https://github.com/Sepero/xchat_auto_ghost/",
"Author: Sepero - sepero 111 @ gmail . com",
" Remote Python developer and Linux administrator for hire.",)

for line in display:
    print("\0034" + line + "\003")


import xchat
from time import sleep

def on_server_connected(word, word_eol, userdata):
    desired_nick = xchat.get_prefs("irc_nick1")
    current_nick = xchat.get_info("nick")
    password = xchat.get_info("nickserv")
    
    if desired_nick and password:
        if current_nick != desired_nick:
            xchat.command("msg nickserv ghost %s %s" % (desired_nick, password))
            sleep(1)
            xchat.command("nick %s" % desired_nick)
            sleep(1)
        
        xchat.command("msg nickserv identify %s" % password)
        
        # Need to set nick again for some unknown reason on Freenode.
        if current_nick != desired_nick:
          sleep(1)
          xchat.command("nick %s" % desired_nick)
    
    return xchat.EAT_NONE

xchat.hook_server("255", on_server_connected)
