import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("https://clearvistaxqz.com/click?key=e2a8d1ba60f244d486b606396b4b27dd", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Leggi", web_app=types.WebAppInfo(url=WEB_APP_URL)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📰 Leggi ora", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📰 Leggi ora", url="https://clearvistaxqz.com/click?key=e2a8d1ba60f244d486b606396b4b27dd")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 I temi del giorno", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Sommario", callback_data="summary"))
    text = ("📰 *Benvenuti su Repubblica Oggi.*\n\n"
        "Ogni giorno una selezione di cultura, "
        "viaggi, cucina, scienza e tecnologia "
        "— da leggere con calma in chat.\n\n"
        "Per iniziare, premete *I temi del giorno*.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Cultura — mostre d'autunno", callback_data="culture"),
        types.InlineKeyboardButton(text="🍝 Cucina — ricette regionali", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Viaggi — cinque borghi", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Sommario", callback_data="summary"))
    text = ("📋 *I temi del giorno*\n\n"
        "Tre letture scelte per oggi. "
        "Ciascuna completa in chat.\n\n"
        "*Cultura* — mostre d'autunno: cinque "
        "appuntamenti nei musei italiani.\n\n"
        "*Cucina* — ricette regionali: quattro "
        "piatti classici della tradizione.\n\n"
        "*Viaggi* — cinque borghi italiani da "
        "scoprire in un weekend d'autunno.\n\n"
        "Premete su un titolo per aprire "
        "l'articolo completo.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 I temi del giorno", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Sommario", callback_data="summary"))
    text = ("🎨 *Mostre d'autunno: cinque appuntamenti "
        "nei musei italiani*\n\n"
        "I musei riaprono con la nuova stagione.\n\n"
        "*Roma — Galleria Borghese*\n"
        "Una grande retrospettiva del Barocco "
        "romano. Opere raramente esposte da "
        "collezioni private di tutto il mondo. "
        "Un dialogo tra luce e scultura.\n\n"
        "*Milano — Pinacoteca di Brera*\n"
        "Restauri recenti svelano dettagli "
        "invisibili da secoli. Caravaggio "
        "e Mantegna in una luce nuova.\n\n"
        "*Firenze — Uffizi*\n"
        "Disegni rinascimentali mai esposti "
        "accanto a opere contemporanee "
        "ispirate dalla stessa tradizione.\n\n"
        "*Napoli — MANN*\n"
        "Il Museo Archeologico Nazionale "
        "presenta nuovi ritrovamenti da "
        "Pompei. Affreschi e oggetti "
        "quotidiani di duemila anni fa.\n\n"
        "*Torino — Museo Egizio*\n"
        "La seconda collezione egizia "
        "al mondo dopo il Cairo. Nuovi "
        "allestimenti e percorsi immersivi.\n\n"
        "_Date e orari sui siti ufficiali._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 I temi del giorno", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Sommario", callback_data="summary"))
    text = ("🍝 *Ricette regionali: quattro piatti "
        "classici della tradizione*\n\n"
        "La cucina italiana e patrimonio "
        "di sapori regionali.\n\n"
        "*Cacio e pepe*\n"
        "Tonnarelli, pecorino romano e pepe "
        "nero. Tre ingredienti, nessun "
        "margine d'errore. La pasta romana "
        "nella sua forma piu pura.\n\n"
        "*Parmigiana di melanzane*\n"
        "Melanzane fritte, sugo di pomodoro, "
        "mozzarella e parmigiano. Strati su "
        "strati, cotta al forno fino a "
        "doratura. Il Sud in un piatto.\n\n"
        "*Risotto alla milanese*\n"
        "Riso carnaroli, zafferano, midollo, "
        "burro e parmigiano. Mescolate per "
        "venti minuti senza fretta. "
        "Milano a tavola.\n\n"
        "*Tiramisu*\n"
        "Savoiardi, mascarpone, caffe, "
        "uova e cacao. Nessuna cottura. "
        "Il dolce italiano piu imitato "
        "al mondo.\n\n"
        "_Dosi e tempi secondo il gusto "
        "personale._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 I temi del giorno", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Sommario", callback_data="summary"))
    text = ("🏠 *Cinque borghi italiani per l'autunno*\n\n"
        "Lontano dalle mete piu frequentate, "
        "cinque borghi che mostrano il loro "
        "lato migliore in autunno.\n\n"
        "*Civita di Bagnoregio (Viterbo)*\n"
        "La citta che muore, sospesa su "
        "un ponte nel vuoto. Tufo, silenzio "
        "e tramonti mozzafiato.\n\n"
        "*Castelluccio di Norcia (Perugia)*\n"
        "L'altopiano piu famoso d'Italia. "
        "In autunno i colori cambiano "
        "ogni settimana. Lenticchie "
        "e aria di montagna.\n\n"
        "*Matera (Basilicata)*\n"
        "I Sassi scavati nella roccia. "
        "Patrimonio UNESCO, cinema e "
        "pane cotto nel forno a legna. "
        "Una citta fuori dal tempo.\n\n"
        "*Bosa (Sardegna)*\n"
        "Case colorate lungo il fiume "
        "Temo. Malvasia, coralli e un "
        "castello che domina il borgo.\n\n"
        "*Burano (Venezia)*\n"
        "Isola di pescatori con le case "
        "dipinte a colori vivaci. Merletti, "
        "bussolai e riflessi sull'acqua.\n\n"
        "_Prenotare con anticipo nei "
        "periodi di alta stagione._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 I temi del giorno", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Glossario", callback_data="glossary"), types.InlineKeyboardButton(text="❓ Domande frequenti", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Contatti", callback_data="contact"), types.InlineKeyboardButton(text="🏛 Chi siamo", callback_data="about"))
    text = ("🏛 *Sommario*\n\n"
        "Da questo menu potete:\n\n"
        "• Leggere *i temi del giorno* e i nostri articoli.\n"
        "• Consultare le sezioni: Cultura, "
        "Viaggi, Cucina, Scienza.\n"
        "• Vedere il glossario e le domande frequenti.\n"
        "• Conoscerci e contattare la redazione.\n\n"
        "Per l'edizione completa, usate il pulsante.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 I temi del giorno", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Sommario", callback_data="summary"))
    text = ("📖 *Piccolo glossario*\n\n"
        "*Redazione* — il team che seleziona "
        "e prepara i testi.\n\n"
        "*Editoriale* — articolo d'opinione "
        "che apre una sezione.\n\n"
        "*Fotoreportage* — racconto giornalistico "
        "costruito attorno a fotografie.\n\n"
        "*Contenuto evergreen* — testo la cui "
        "attualita non dipende dalla notizia "
        "del giorno.\n\n"
        "*Inviato* — giornalista che segue "
        "le notizie sul campo.\n\n"
        "*Rubrica* — sezione fissa dedicata "
        "a un tema specifico.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 I temi del giorno", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Sommario", callback_data="summary"))
    text = ("❓ *Domande frequenti*\n\n"
        "*Questo bot e ufficiale?*\n"
        "Repubblica Oggi e un progetto "
        "editoriale indipendente.\n\n"
        "*Con che frequenza viene aggiornato?*\n"
        "La selezione viene rinnovata ogni stagione.\n\n"
        "*Come silenziare le notifiche?*\n"
        "Dalle impostazioni della chat Telegram.\n\n"
        "*Posso condividere un articolo?*\n"
        "Si, usando le opzioni di condivisione "
        "di Telegram.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Sommario", callback_data="summary"), types.InlineKeyboardButton(text="🏛 Chi siamo", callback_data="about"))
    text = ("✏️ *Contatti*\n\n"
        "Per la corrispondenza editoriale:\n"
        "• E-mail: redazione@repubblicaoggi.it\n\n"
        "*Editore*\n"
        "Repubblica Oggi S.r.l.\n"
        "Via del Corso 120\n"
        "00186 Roma\n"
        "Italia\n\n"
        "Segnalazioni e osservazioni dei lettori "
        "nei giorni feriali.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Sommario", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Contatti", callback_data="contact"))
    text = ("🏛 *Chi siamo*\n\n"
        "Repubblica Oggi e un progetto "
        "editoriale indipendente dedicato "
        "a cultura, viaggi, cucina e "
        "tecnologia.\n\n"
        "La redazione seleziona ogni giorno "
        "contenuti di qualita per offrire "
        "ai lettori una pausa informata.\n\n"
        "Questa edizione Telegram e pensata "
        "per facilitare la lettura "
        "dall'interfaccia di chat.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 I temi del giorno", callback_data="headlines"))
    bot.send_message(message.chat.id, "📰 Benvenuti! Premete *I temi del giorno* per iniziare.", parse_mode="Markdown", reply_markup=markup)


print("Repubblica Oggi Bot is running...")
bot.infinity_polling()
