import logging
import subprocess
import time
import r2d2

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')
    r2d2.say(update.message.text)

def say(update, context):
    print(update.message.text)
    r2d2.say(update.message.text)

def tell(update, context):
    print(update.message.text[5:])
    r2d2.textToSpeech(update.message.text[5:])
    
def turnled(update, context):
    r2d2.turnLed(str(context.args[0]))

def offled(update, context):
    r2d2.turnOffLed(str(context.args[0]))

def turnoffall(update, context):
    r2d2.turnOffAll()

def turnonall(update, context):
    r2d2.turnOnAll()

def setvolume(update, context):
    r2d2.setVolume(context.args[0])

def shout(update, context):
    r2d2.shout()

def voice_handler(update, context):
    file = context.bot.getFile(update.message.voice.file_id)
    r2d2.turnLed("red")
    r2d2.turnLed("blue")
    file.download("./sound.wav")
    r2d2.playSound()
    
def audio_handler(update, context):
    file = context.bot.getFile(update.message.audio.file_id)
    r2d2.turnLed("red")
    r2d2.turnLed("blue")
    file.download("./sound.wav")
    r2d2.playSound()
    
def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("R2D2 Help! \n/say\n/turnled + ledColor\n/offled + ledColor\n/turnoffall\n/turnonall\n/setvolume + number(0-100)")


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)
    
def stopsound(update,context):
    r2d2.stopSound()
    
def cry(update, context):
    r2d2.playSoundCry()

def main():
    
    #process = subprocess.call('r2d2.py')
    
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1674500154:AAECv9uAIiqmFHrrQoURlOD_c1Lfla-MYys", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("say", say))
    dp.add_handler(CommandHandler("turnled", turnled))
    dp.add_handler(CommandHandler("offled", offled))
    dp.add_handler(CommandHandler("turnoffall", turnoffall))
    dp.add_handler(CommandHandler("turnonall", turnonall))
    dp.add_handler(CommandHandler("tell", tell))
    dp.add_handler(CommandHandler("setvolume", setvolume))
    dp.add_handler(CommandHandler("shout", shout))
    dp.add_handler(CommandHandler("stopSound", stopsound))
    dp.add_handler(CommandHandler("cry", cry))
    dp.add_handler(CommandHandler("stop", stopsound))
    dp.add_handler(MessageHandler(Filters.voice, voice_handler))
    dp.add_handler(MessageHandler(Filters.audio, audio_handler))
    

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    
    r2d2.main()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    #updater.idle()


if __name__ == '__main__':
    main()