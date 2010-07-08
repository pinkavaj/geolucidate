# -*- coding: utf-8 -*-

import re

parser_re = re.compile(u"""
    # Latitude direction, first position: one of N, S, NORTH, SOUTH
    (?P<latdir>NORTH|SOUTH|[NS])?                    
    # Latitude degrees: two digits 0-90
    (?P<latdeg>([0-8][0-9])|90)
    # Optional space or degree mark separating degrees and minutes
    (\ |(?P<degmark>º|\ DEGREES,\ ))?
    (?P<latminsec>
    # Latitude minutes: two digits 0-59
    (?P<latmin>[0-5][0-9])
    # If there was a degree mark before, look for punctuation after the minutes
    (?(degmark)(\'|\ MINUTES(,\ )?))?
    (
    # Latitude seconds: two digits 0-59
    (?P<latsec>([0-9]|[0-5][0-9]))(?(degmark)("|\ SECONDS\ ))|
    # Decimal fraction of minutes
    (?P<latdecsec>\\.\\d{1,2}))?
    )?
    # Latitude direction, second position, optionally preceded by a space
    (\ ?(?P<latdir2>(?(latdir)|(NORTH|SOUTH|[NS]))))
    # Latitude/longitude delimiter: space, forward slash, comma, or none
    (\ ?[ /]\ ?|,\ )?
    # Longitude direction, first position: one of N, S, NORTH, SOUTH
    (?P<longdir>EAST|WEST|[EW])?
    # Longitude degrees: two or three digits
    (?P<longdeg>\\d{2,3}?)
    # If there was a degree mark before, look for another one here
    (\ |(?(degmark)(º|\ DEGREES,\ )))?
    (?(latminsec) #Only look for minutes and seconds in the longitude if they were there in the latitude
    (?P<longminsec>
    # Longitude minutes: two digits
    (?P<longmin>[0-5][0-9])
    # If there was a degree mark before, look for punctuation after the minutes
    (?(degmark)('|\ MINUTES(,\ )?))?
    # Longitude seconds: two digits 0-59
    ((?P<longsec>([0-5][0-9]))(?(degmark)("|\ SECONDS\ ))|
    # Decimal fraction of minutes
    (?P<longdecsec>\\.\\d{1,2}))?
    ))
    #Longitude direction, second position: optionally preceded by a space
    ((?(longdir)|\ ?(?P<longdir2>(EAST|WEST|[EW]))))
    """,re.VERBOSE|re.UNICODE|re.IGNORECASE)