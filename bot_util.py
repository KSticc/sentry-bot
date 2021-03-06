from discord.ext import commands
import random
import time

def GetRand():
    random.seed(time.ctime())
    ii = random.randint(0, 1)
    if ii != 0:
        return 0
    if ii == 0:
        return str(random.randint(1, 100))

class UtilCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='thotdect', help='Thot detector for easier crusades')
    async def thotdect(self, ctx, user: str = 0):
        if user != 0: user = user
        if user == 0: user = ctx.author
        #await ctx.send('f')
        await ctx.send(str(user) + " is " + str(GetRand()) + "% thot") #str(GetRand())


    @commands.command(name='vanfact', help='Returns a random fact about Vanadius')
    async def vanfact(self, ctx):
        vanadiusfacts = [
            'Collectibles with red sparkles will set your spawn point.',
            'Most sentries have depression. This is because nobody has played Vanadius.',
            'Sentries very slightly speed up after a short time of chasing you. Eventually, they can get so fast they start yeeting.',
            'There are 15 collectibles in Vanadius. In version 1.0, a rare bug can occur which allows you to get more than 15.',
            'Vanadius\'s save files aren\'t encrypted. This means it\'s easy to modify save data in an unintended way.',
            'There was originally going to be a way to get back to the Cave area of the game.',
            'If you return to the Deep Lab after completing it, you get to access the hideout of the Big Sentry, among a few other small changes.',
            'There used to be green flasks, which would home in on the player. As time went on, they would spin faster and faster until eventually exploding. They can still be found in the testing room',
            'The testing room can be accessed by getting all 15 collectibles and going through a very challenging area in the Power Plant.',
            'Purple flasks were originally missiles.',
            'The gears in the Clock Tower originally looked like green Sentries.',
            'An early concept for a sentry was the Missile Sentry. It would shoot missiles at the player if they got too close. The idea was scrapped and the sprite was used for normal sentries.',
            'There were plans for an icy area near the end of the game. This idea was scrapped after implementation of ice failed horribly.',
            'There were plans for a speed boosting tile. The player would gain more speed the longer they walked on it. This proved to be buggy and has since been removed.',
            'Vanadius devlogs are available on Twitter by @KSticcGames if you scroll down far enough.',
            'There were originally safe areas, that, when stepped in, would cause sentries to retreat. These were replaced by safety pressure plates, which were removed late in development.',
            'Most of the tilesets in the game went through many iterations, so the final ones are about the 3rd or 4th iteration.',
            'Vanadius is available to download for Windows at ksting.itch.io/vanadius.',
            'One of the lore signs states that a previous subject has escaped. The only reason this exists is to set up for a possible prequel.',
            'There are many inherent issues reported by the 3 people who have played the game, such as "The robot walks to slow" and "The pixel art is too chunky".',
            'Vanadius took about a year and a half to develop using GameMaker Studio 2.',
            'A bug in version 1.1 causes the game to not start at all due to an incorrect file dependency. This could have been easily avoided with one line of code.',
            'A corrupted version of the game exists where ui elements are buggy and text is wildly incorrect',
            'In early builds of the game, a larger, thinner font was used. This was scrapped in favor of a custom font.',
            'The earliest known prototype for Vanadius dates back to April of 2018',
            'Multiple sprites went unused during development. One of these includes the player looking down at the floor, as if depressed.',
            'An early sprite for falling had the player in a t-pose like position as they fell. This animation was removed as it didn\'t fit the perspective.',
            'An early sprite, called \'battlebot.png\', shows a subject seemingly fused with a sentry. These enemies would have appeared in the Power Plant and they would have shot missiles.',
            'Various unused themes for areas were planned. These include an underground shipwreck, an icy area, and an area whose main mechanics would have been fire and water.',
            'The Clock Tower was originally going to be a bonus level.',
            'Various ideas go unused from the planning stages of development, such as moving platforms and glass walls.',
            'The only reason Vanadius exists is because the idea of having to sneak around like the Green Arrow sounded cool. Ultimately, the game turned out to be nothing like that.',
            'In the very, very early brainstorming stages, Vanadius was originally planned to be a metroidvania. This idea may still be acted upon.',
            'Most of the ideas from the original planning drawing made it into the final game one way or another.',
        ]
        await ctx.send("Fun Fact: " + random.choice(vanadiusfacts))


    @commands.command(name = 'copypasta', help = 'Returns Copypasta. Arguments: idk',hidden=1)
    async def copypasta(self, ctx, type='none'):
        if type == 'idk':
            await ctx.send('''Idk is an abbreviation of the phrase I don’t know. Idk is part of the newly developed dialect called text speak or SMS language. This dialect is mostly used in informal communication, and especially when communicating via text messages or instant messages. The phrase idk has been part of text speak since at least 2002.
            
You can use idk the same way you use the phrase I don’t know. In informal writing, and especially in text messages, the rules of capitalization are lax at best, so you can choose how you want to treat idk. The one rule that has come about in text speak is that writing a word in all caps means you’re either shouting it or are otherwise trying to emphasize it or amplify its effect. If you’re using idk in a more formal context, you should always make sure you capitalize it—or not—consistently.''')

        if type != 'idk':
            await ctx.send('You most specify and argument you fool')


    @commands.command(name = 'bruh', help = 'Bruh Moment')
    async def bruh(self,ctx):
        bruh_moments = [
            'Bruh Moment',
            'This is a certified Bruh Moment',
            'Bruh',
        ]
        await ctx.send(random.choice(bruh_moments))


    @commands.command(name = 'sentryspeed', help = 'Calculate the speed of a sentry. Arguments: Time in seconds')
    async def sentryspeed(self,ctx,secs=0):
        print(secs)
        if isinstance(secs,int):
            base_speed = 5
            added = secs/5
            speedtime = base_speed+added
            await ctx.send('A Sentry would be moving '+str(speedtime)+'MPH after '+str(secs)+' seconds')
        else:
            await ctx.send('Give a time in whole seconds.')


    @commands.command(name = 'sciquote', help = 'Give a quote from Black Mesa\'s very own')
    async def sciquote(self,ctx):
        scientistquotes = [
            'Do you think we should appeal to the *alien* authorities?',
            'I am rather looking forward to this analysis, aren\'t you?',
            'Are you thinking what I\'m thinking?',
            'Have you been able to get the beverage machine to work yet?',
            'Quick! It\'s about to go critical!',
            'Good morning, Gordon.',
            'Now, now, if you follow standard insertion procedures, everything will be fine.',
            'I...I can\'t hold on much...longer...',
            'I\'m not so sure I want to get to the surface. What if the world finds out what we were doing down here?',
            'Take me with you! I\'m the one man who knows everything!',
            'Oh my God...we\'re doomed!',
            'Don\'t shoot! I\'m with the science team!',
            'No...No! No! Get it off me! Get it off! Get it off!',
            'Freeman, you fool!',
            'It can\'t get any worse than this.',
            'I can\'t take much more of this.',
            'You are completely wrong.',
            'No, I don\'t want to die!',
            'Do you know who ate all the donuts?',
            'Have you ever seen anything like this?',
            'Don''t you find this all rather fascinating?',
            'Freeman.',
            'Don\'t you find this all rather fascinating?',
            'I believe this will make for a notable paper, don\'t you?',
            'Don\'t worry, I am a doctor.',
            'Someone has hidden my glasses again.',
            'I certainly hope you know what you\'re doing.',
            'I predicted all of this, you know. All of it!',
            'Kindly lower your voice.',
            'This is madness! I\'m getting out of here!',
            'I\'d give my right hemisphere for a few hours of sleep.',
            'Well, there goes our grant money.',
            'You\'ll just have to wait until *after* the test.',
            'Please, leave me *alone* until after the experiment.',
            'I can\'t be bothered right now.',
            'Excuse me, Gordon, but I\'m rather busy now.',
            'Weren\'t you supposed to be in the test chamber half an hour ago?',
            'Shut up.',
            'You aren\'t going soft on that ethics issue again, are you?',
            'I believe something smells quite foul here.',
            'Stop asking that question.',
            'Why do we all have to wear these *ridiculous* ties?',
            'My God, *what* are you doing?',
            'Who is responsible for this mess?',
            'Ah, you\'ve been wounded.',
            'https://www.youtube.com/watch?v=NMk6LLDGp5I',
            'https://www.youtube.com/watch?v=yv-7D3XQ9ww',
            'https://www.youtube.com/watch?v=WotwTcGVYuE',
        ]
        await ctx.send(random.choice(scientistquotes))

    @commands.command(name = 'guardquote', help = 'Give a quote from Barney Calhoun')
    async def guardquote(self,ctx):
        guardquotes = [
            "You aren't scared, are you?",
            "I wish it hadn't come to this.",
            "Hey, catch me later, I'll buy you a beer.",
            "Can we do this later?",
            "What do you want on your tombstone?",
            "I have a bad feeling about this.",
            "Now I wonder if those boys could have made a bigger mess.",
            "I'm never gonna make it. You better go on without me.",
            "What is this thing? Some kinda weapon?",
            "I'll bet that stings a bit.",
            "I would really like a cold one right now.",
            "Any idea how many of our crew have died?",
            "It can't get any worse than this, can it?",
            "I'd like to get my hands on the guy responsible for this mess.",
            "Our luck has to change sooner or later.",
            "You don't still think this is a drill, do you?",
            "You have any idea what's going on?",
            "You ever seen anything like this?",
            "This is all happening because of you scientists!",
        ]
        await ctx.send(random.choice(guardquotes))


    @commands.command(name='expand', help='space',aliases = ['exp'])
    async def expand(self, ctx, message: str = "f"):
      if len(message) < 2:
        await ctx.send("Enter a valid string that's longer that 1 character you fool!")
      else:
        expstring = ""
        for stri in message:
          expstring = expstring + stri
          expstring = expstring + " "
        
        await ctx.send(expstring)

    @commands.command(name='expandupper', help='SPACE',aliases = ['expu'])
    async def expandupper(self, ctx, message: str = "f"):
      if len(message) < 2:
        await ctx.send("Enter a valid string that's longer that 1 character you fool!")
      else:
        expstring = ""
        for stri in message:
          expstring = expstring + stri
          expstring = expstring + " "
        
        await ctx.send(expstring.upper())


def setup(bot):
    bot.add_cog(UtilCommands(bot))