import sopel.module as module
import sopel.tools as tools


strings = {
    "limite" : "Mi spiace, ma hai raggiunto il limite massimo di uova ottenibili! / I'm sorry, but you can't claim any more eggs!",
    "egg" : "Ecco il tuo UOVO / Here's you EGG %s  https://usercontent.twoopy.nl/6b4f281c5a446791/image.png .",
    "left" : "Ti sono rimasti %s tentativi / You've got %s attempts left.",
    "adminegg" : "Hai ricevuto un uovo da %s. / You received an egg from %s . https://usercontent.twoopy.nl/6b4f281c5a446791/image.png",
    "admineggself" : "Ti sei dato un uovo da solo %s (monello!)"
}

class easteregg:
    
    def __init__(self):
        self.user = {}

    def egg(self , bot , trigger):
        if trigger.nick not in self.user:
            self.user[trigger.nick] = 0
        if self.user[trigger.nick] >= 3:
            bot.notice(strings["limite"] , trigger.nick)
            return
        self.user[trigger.nick] += 1
        bot.notice(strings["egg"] % (trigger.nick) , trigger.nick)
        bot.notice(strings["left"] % ( str(3 - self.user[trigger.nick]) , str(3 - self.user[trigger.nick])) , trigger.nick)

    def adminegg(self , bot , trigger):
        try:
           bot.notice(strings["adminegg"] % (trigger.nick , trigger.nick) , trigger.group(3))
        except:
           bot.notice(strings["admineggself"] % (trigger.nick) , trigger.nick)
        bot.notice("Uovo consegnato correttamente :P" , trigger.nick)


eggita = easteregg()


@module.commands("easteregg")
@module.example(".easteregg")
@module.require_chanmsg
def eegg(bot , trigger):
    eggita.egg(bot , trigger)

@module.commands("giveegg")
@module.example(".giveegg giovannetor")

@module.require_chanmsg
def giveegg(bot , trigger):
    if trigger.admin:
        eggita.adminegg(bot , trigger)
    else:
        bot.say("You can't give eggs :) ")
        bot.notice("Because you suck o.o" , trigger.nick)
