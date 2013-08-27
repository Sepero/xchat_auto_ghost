from random import choice
import string
import xchat

__module_name__ = "Auto Ghost"
__module_version__ = "0.20"
__module_description__ = "Ghost the default nick and change/identify as that user."

display = (__module_name__ + " " + __module_version__ + " has been loaded.",
        "    Module URL: https://github.com/Sepero/xchat_auto_ghost/",
        "    Author: Sepero 2013 - sepero 111 @ gmail . com",
        "         Remote Python developer and Linux administrator for hire.",)

for line in display:
    print("\0034" + line + "\003")

def set_nick(word, word_eol, userdata):
    desired_nick = xchat.get_prefs("irc_nick1")
    password = xchat.get_info("nickserv")
    
    if word[3] == desired_nick and password:
        randstring = ''.join(choice(string.lowercase) for i in xrange(16))
        xchat.command("nick %s" % randstring)
        xchat.command("nickserv ghost %s %s" % (desired_nick, password))
        xchat.command("nick %s" % desired_nick)
        xchat.command("nickserv identify %s" % password)
        return xchat.EAT_XCHAT
    
    return xchat.EAT_NONE

xchat.hook_server("433", set_nick, priority=xchat.PRI_HIGHEST)
