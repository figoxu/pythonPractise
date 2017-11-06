#coding=utf-8
#!/usr/bin/env python3

"""
    ###     ####         ######
          ###  ###      #    ###
    ###         ###       ######
    ###      ####       ###   ##
    ###    ####        ###    ##
    ###   ##########    ##### ###

i2a creates ASCII art from images right on your terminal.

Usage: i2a [options] [FILE]

Options:
  -h --help            Show this on screen.
  -v --version         Show version.
  -c --colors          Show colored output.
  -b --bold            Output bold characters
  --bg=(BLACK|WHITE)   Specify the background color.
  --contrast=<factor>  Manually set contrast [default: 1.5].
  --alt-chars          Use an alternate set of characters. 
"""

from docopt import docopt

__version__ = 'demo 1.0'

if __name__ == '__main__':
    args = docopt(__doc__, version=__version__)
    print(args)


