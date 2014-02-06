from __future__ import division
import blockext
from blockext import *
from myro import *
bot = Scribbler()


@command("stop all motors")
def stopmotors():
    bot.stop()
@command("move both motors at speed %n")
def straight(speed=100):
    bot.translate(speed/100)
@command("move left motor %n speed, right motor %n speed")
def turny(ls=100,rs=100):
    bot.motors(ls,rs)
@command("play tone %n for %n seconds")
def playtone(tone=500,time=1):
    bot.beep(time,tone)
@command("set S2 name to %s")
def nameset(name):
    bot.setName(name)
menu('ledpos',['right','left'])
menu('onoff',['on','off'])
@command('set %m.ledpos back LED to %m.onoff')
def setled(ledpos="right", onoff="on"):
    bot.setLED(ledpos,onoff)
    if onoff == 'off':
        bot.setLED(ledpos,'off')
@reporter('get line sensor %n value')
def getline(n=1):
    return bot.getLine(n - 1)
@reporter('get IR sensor %n value')
def getline(n=1):
    return bot.getIR(n - 1)
@reporter('get light sensor %n value')
def getlight(n=1):
    return bot.getLight(n - 1)
@reporter('S2 robot name')
def getname():
    return bot.getName()

@reset
def resetall():
    bot.stop()
    
blockext.run("Parallax S2 robot", 's2', 3610)
