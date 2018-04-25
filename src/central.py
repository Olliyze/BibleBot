'''
    Copyright (c) 2018 Elliott Pardee <vypr [at] vypr [dot] space>
    This file is part of BibleBot.

    BibleBot is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    BibleBot is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with BibleBot.  If not, see <http://www.gnu.org/licenses/>.
'''

from extensions.vylogger import VyLogger
from data import languages
import configparser
import os
import tinydb
import math
import time

dir_path = os.path.dirname(os.path.realpath(__file__))

config = configparser.ConfigParser()
config.read(dir_path + "/config.ini")

logger = VyLogger("default")

db = tinydb.TinyDB(dir_path + "/../databases/db")
versionDB = tinydb.TinyDB(dir_path + "/../databases/versiondb")

languages = languages

dividers = {
    "first": config["BibleBot"]["dividingBrackets"][0],
    "second": config["BibleBot"]["dividingBrackets"][1]
}


def capitalizeFirstLetter(string):
    return string[0].upper() + string[1:]


def splitter(s):
    middle = math.floor(len(s) / 2)
    before = s.rfind(" ", middle)
    after = s.index(" ", middle + 1)

    if before == -1 or (after != -1 and middle - before >= after - middle):
        middle = after
    else:
        middle = before

    return {
        "first": s[0:middle],
        "second": s[middle + 1:]
    }


def logMessage(level, shard, sender, source, msg):
    if shard is None:
        shard = 1

    message = "[shard " + str(shard) + "] <" + \
        sender + "@" + source + "> " + msg

    if level == "warn":
        logger.warning(message)
    elif level == "err":
        logger.error(message)
    elif level == "info":
        logger.info(message)
    elif level == "debug":
        logger.debug(message)


def sleep(milliseconds):
    time.sleep(milliseconds / 1000.0)