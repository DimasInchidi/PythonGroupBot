from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging
import requests
from tinydb import TinyDB
import html
import re

info = TinyDB("info.json")
db = TinyDB("groups.json")
textsdb = TinyDB("texts.json")
langs = TinyDB("languages.json")
ignoredb = TinyDB("ignore.json")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def translate(msg, target):
    url = "https://translation.googleapis.com/language/translate/v2"
    result = requests.get(url, params={
        "target": target,
        "q": msg,
        "key": info.all()[0]["google_token"]
    }).json()
    lang = result["data"]["translations"][0]["translatedText"]
    r_lang = html.unescape(lang)
    return(r_lang)

def detect(msg):
    """Do an HTTP GET to detect a string's language.

    Using Google Translate API.
    """
    url = "https://translation.googleapis.com/language/translate/v2/detect"
    result = requests.get(url, params={
        "q": msg,
        "key": info.all()[0]["google_token"]
    }).json()
    lang = result["data"]["detections"][0][0]["language"]
    return(langs.all()[0][lang])

def button(bot, update):
    query = update.callback_query
    ID = query["id"]
    text = query["message"]["text"]
    lang = text.split()[5][:-1]
    translated_ = textsdb.all()[0][lang]

    bot.answerCallbackQuery(ID,
                            text=translated_,
                            show_alert=True)

def get_admin_ids(bot, chat_id):
    return [admin.user.id for admin in bot.getChatAdministrators(chat_id)]

def echo(bot, update):
    database = db.all()[0]
    if update.message and update.message.chat.id in info.all()[0]["allowed_groups"]:
        message = update.message
        id_ = message["message_id"]
        text = message["text"]
        for ig in ignoredb.all()[0]["to_ignore"]:
            text = re.sub(r"\b{}\b".format(ig), "", text)
        text = text.lstrip()
        text = text.rstrip()
        if text != "":
            detected_lang = detect(text).split()
            for lang, username in database.items():
                if detected_lang[0] == lang:
                    DETECT_META = False
                    if len(username) >= 2:
                        txt = "I've detected that you speak {}. You should join {}".format(lang, " or ".join(username))
                    else:
                        txt = "I've detected that you speak {}. You should join {}".format(lang, username[0])
                    keyboard = [[InlineKeyboardButton("Read in {}".format(lang), callback_data="1")]]
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    bot.sendMessage(chat_id=update.message.chat.id,
                        text=txt,
                        reply_to_message_id=int(id_),
                        reply_markup=reply_markup)
                    if len(text) > info.all()[0]["max_message_char"] and update.message.chat.id not in get_admin_ids(bot, update.message.chat.id):
                        update.message.bot.delete_message(
                            chat_id=update.message.chat.id,
                            message_id=id_)

def new(bot, update):
    """Add groups to a language key"""
    if update.message.from_user.id in get_admin_ids(bot, update.message.chat.id) and update.message.chat.id in info.all()[0]["allowed_groups"]:
        if update.message:
            # yo
            text = update.message["text"]
            text = text.split()
            if len(text) >= 3:
                key = text[1].lower()
                key1 = key[0].upper() + key[1:]
                groups_ = text[2:]
                _groups = db.all()[0][key1]
                _groups.extend(groups_)
                if key1 in db.all()[0]:
                    db.update({key1: _groups})
                else:
                    db.insert({key1: _groups})
            else:
                update.message.reply_text("You have to at least provide a language name and at least one group.")

def group(bot, update):
    """Returns a list of groups based on the provided language"""
    # Sorry PEP8
    if update.message.chat.id in info.all()[0]["allowed_groups"]:
        text = update.message["text"]
        text = text.split()
        if len(text) >= 2:
            key = text[1].lower()
            # You can use str.capitalize() here.
            key1 = key[0].upper() + key[1:]
            try:
                result = " ".join(db.all()[0][key1])
                reply_msg = "Group(s) for {}: {}".format(key1, result)
            except KeyError:
                reply_msg = "Couldn't find any group for that."
            update.message.reply_text(reply_msg)
        else:
            update.message.reply_text("You have to provide a language name.")

def ignore(bot, update):
    if update.message.from_user.id in get_admin_ids(bot, update.message.chat.id) and update.message.chat.id in info.all()[0]["allowed_groups"]:
        msg = update.message.reply_to_message
        if msg is None:
            msg = update.message
        text = msg["text"].split()
        if text[0] == "/ignore":
            del text[0]
        # What I'm doing here is not really necessary.
        if len(text) >= 1:
            _odataodata = ignoredb.all()[0]["to_ignore"]
            _old = []
            _new = []
            for txt_to_ignore in text:
                if txt_to_ignore in _odataodata:
                    _old.append(txt_to_ignore)
                else:
                    _new.append(txt_to_ignore)
            _odataodata.extend(_new)
            ignoredb.update({"to_ignore": _odataodata})
            if len(_new) <= 4:
                reply_msg = "Added \"`{}`\" to `ignore.json`. Ignored: {}".format(", ".join(text), len(_old))
            else:
                reply_msg = "Added {} *new* texts to `ignore.json`. Ignored: {}".format(len(_new), len(_old))
            update.message.reply_text(reply_msg, parse_mode="Markdown")
        else:
            update.message.reply_text("You have to at least add one thing.")

def ignorelist(bot, update):
    if update.message.from_user.id in get_admin_ids(bot, update.message.chat.id) and update.message.chat.id in info.all()[0]["allowed_groups"]:
        _odataodata = ignoredb.all()[0]["to_ignore"]
        update.message.reply_text("<code>{}</code>".format(_odataodata), parse_mode="HTML")

def _error(bot, update, error):
    """Log errors."""
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def groups(bot, update):
    """Returns the content of the database file"""
    if update.message.from_user.id in get_admin_ids(bot, update.message.chat.id):
        if update.message:
            text = """
<b>File</b>: <code>groups.json</code>
<b>KVS (database)</b>: <a href="https://github.com/msiemens/tinydb">TinyDB</a>
<b>Content</b>: <code>
{}</code>
""".format(db.all()[0])
            update.message.reply_text(text, parse_mode="HTML", disable_web_page_preview=True)

def main():
    """main function?"""
    updater = Updater(info.all()[0]["bot_token"])

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("new", new))
    dp.add_handler(CommandHandler("group", group))
    dp.add_handler(CommandHandler("groups", groups))
    dp.add_handler(CommandHandler("ignore", ignore))
    dp.add_handler(CommandHandler("ignorelist", ignorelist))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_error_handler(_error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
