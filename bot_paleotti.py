import logging
from typing import Dict, Any, List, Optional

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# ================== CONFIGURAZIONE BASE ==================

# TOKEN DEL BOT (puoi lasciarlo così se è quello giusto)
BOT_TOKEN = "8556329067:AAG01gKTjkia1clf9L29EwsboyCS_hgRkQc"

# ID DELLE PERSONE CHE DEVONO RICEVERE L'ORDINE
OWNER_CHAT_IDS = [
    6260926202,  # PALEOTTI
    1189411829,  # Brossin
    1041813873,  # RobyIris88
]

# ================== DATI PRODOTTI ==================

PRODUCTS: List[Dict[str, Any]] = [
    {
        "id": "p1",
        "name": "Christmas Box Babbo Natale",
        "price": 15.0,
        "description": (
            "Tipologia: Scatola in latta 48 biscotti misti\n"
            "Design: Babbo Natale\n"
            "Dimensioni: 19,5 × 13,5 × 6 cm\n"
            "Peso: circa 370 g di biscotti\n"
            "Contenuto:\n"
            "• 12 biscotti alle mandorle\n"
            "• 12 biscotti alle nocciole\n"
            "• 12 biscotti al cocco\n"
            "• 12 biscotti al cioccolato\n"
        ),
    },
    {
        "id": "p2",
        "name": "Tazza Rossa + 12 biscotti al cioccolato",
        "price": 5.0,
        "description": (
            "Tipologia: Tazza + 12 biscotti al cioccolato\n"
            "Design: Tazza rossa in ceramica\n"
            "Dimensioni: 9 x 12,5 x h10,5 cm\n"
            "Peso: circa 90 g\n"
        ),
    },
    {
        "id": "p3",
        "name": "Tazza Rossa + 12 biscotti al cocco",
        "price": 5.0,
        "description": (
            "Tipologia: Tazza + 12 biscotti al cocco\n"
            "Design: Tazza rossa in ceramica\n"
            "Dimensioni: 9 x 12,5 x h10,5 cm\n"
            "Peso: circa 90 g\n"
        ),
    },
    {
        "id": "p4",
        "name": "Tazza Rossa + 12 biscotti alle mandorle",
        "price": 5.0,
        "description": (
            "Tipologia: Tazza + 12 biscotti alle mandorle\n"
            "Design: Tazza rossa in ceramica\n"
            "Dimensioni: 9 x 12,5 x h10,5 cm\n"
            "Peso: circa 100 g\n"
        ),
    },
    {
        "id": "p5",
        "name": "Tazza Rossa + 12 biscotti alle nocciole",
        "price": 5.0,
        "description": (
            "Tipologia: Tazza + 12 biscotti alle nocciole\n"
            "Design: Tazza rossa in ceramica\n"
            "Dimensioni: 9 x 12,5 x h10,5 cm\n"
            "Peso: circa 100 g\n"
        ),
    },
    {
        "id": "p6",
        "name": "Tazza Verde + 12 biscotti al cioccolato",
        "price": 5.0,
        "description": (
            "Tipologia: Tazza + 12 biscotti al cioccolato\n"
            "Design: Tazza verde in ceramica\n"
            "Dimensioni: 9 x 12,5 x h10,5 cm\n"
            "Peso: circa 90 g\n"
        ),
    },
    {
        "id": "p7",
        "name": "Tazza Verde + 12 biscotti al cocco",
        "price": 5.0,
        "description": (
            "Tipologia: Tazza + 12 biscotti al cocco\n"
            "Design: Tazza verde in ceramica\n"
            "Dimensioni: 9 x 12,5 x h10,5 cm\n"
            "Peso: circa 90 g\n"
        ),
    },
    {
        "id": "p8",
        "name": "Tazza Verde + 12 biscotti alle mandorle",
        "price": 5.0,
        "description": (
            "Tipologia: Tazza + 12 biscotti alle mandorle\n"
            "Design: Tazza verde in ceramica\n"
            "Dimensioni: 9 x 12,5 x h10,5 cm\n"
            "Peso: circa 100 g\n"
        ),
    },
    {
        "id": "p9",
        "name": "Tazza Verde + 12 biscotti alle nocciole",
        "price": 5.0,
        "description": (
            "Tipologia: Tazza + 12 biscotti alle nocciole\n"
            "Design: Tazza verde in ceramica\n"
            "Dimensioni: 9 x 12,5 x h10,5 cm\n"
            "Peso: circa 100 g\n"
        ),
    },
    {
        "id": "p10",
        "name": "Sacchetto classico al cioccolato (24 biscotti)",
        "price": 6.0,
        "description": (
            "Tipologia: Sacchetto da 24 biscotti al cioccolato\n"
            "Design: Sacchetto in plastica trasparente\n"
            "Dimensioni: 8,5 x 5 x h25 cm\n"
            "Peso: circa 180 g\n"
        ),
    },
    {
        "id": "p11",
        "name": "Sacchetto classico al cocco (24 biscotti)",
        "price": 6.0,
        "description": (
            "Tipologia: Sacchetto da 24 biscotti al cocco\n"
            "Design: Sacchetto in plastica trasparente\n"
            "Dimensioni: 8,5 x 5 x h25 cm\n"
            "Peso: circa 180 g\n"
        ),
    },
    {
        "id": "p12",
        "name": "Sacchetto classico alle mandorle (24 biscotti)",
        "price": 6.0,
        "description": (
            "Tipologia: Sacchetto da 24 biscotti alle mandorle\n"
            "Design: Sacchetto in plastica trasparente\n"
            "Dimensioni: 8,5 x 5 x h25 cm\n"
            "Peso: circa 200 g\n"
        ),
    },
    {
        "id": "p13",
        "name": "Sacchetto classico alle nocciole (24 biscotti)",
        "price": 6.0,
        "description": (
            "Tipologia: Sacchetto da 24 biscotti alle nocciole\n"
            "Design: Sacchetto in plastica trasparente\n"
            "Dimensioni: 8,5 x 5 x h25 cm\n"
            "Peso: circa 200 g\n"
        ),
    },
    {
        "id": "p14",
        "name": "Sacchetto mini al cioccolato (12 biscotti)",
        "price": 3.0,
        "description": (
            "Tipologia: Sacchetto da 12 biscotti al cioccolato\n"
            "Design: Sacchetto in plastica trasparente\n"
            "Dimensioni: 6,5 x 5 x h17 cm\n"
            "Peso: circa 90 g\n"
        ),
    },
    {
        "id": "p15",
        "name": "Sacchetto mini al cocco (12 biscotti)",
        "price": 3.0,
        "description": (
            "Tipologia: Sacchetto da 12 biscotti al cocco\n"
            "Design: Sacchetto in plastica trasparente\n"
            "Dimensioni: 6,5 x 5 x h17 cm\n"
            "Peso: circa 90 g\n"
        ),
    },
    {
        "id": "p16",
        "name": "Sacchetto mini alle mandorle (12 biscotti)",
        "price": 3.0,
        "description": (
            "Tipologia: Sacchetto da 12 biscotti alle mandorle\n"
            "Design: Sacchetto in plastica trasparente\n"
            "Dimensioni: 6,5 x 5 x h17 cm\n"
            "Peso: circa 100 g\n"
        ),
    },
    {
        "id": "p17",
        "name": "Sacchetto mini alle nocciole (12 biscotti)",
        "price": 3.0,
        "description": (
            "Tipologia: Sacchetto da 12 biscotti alle nocciole\n"
            "Design: Sacchetto in plastica trasparente\n"
            "Dimensioni: 6,5 x 5 x h17 cm\n"
            "Peso: circa 100 g\n"
        ),
    },
]

BISCOTTI_NOTE = (
    "Biscotti artigianali realizzati a mano, utilizzando solo materie prime di alta qualità, "
    "senza l’utilizzo di: conservanti, emulsionanti, coloranti, latticini, cereali, grassi "
    "idrogenati, aromi chimici."
)

SHIPPING_OPTIONS = [
    {"id": "hand", "label": "Consegna a mano", "cost": 0.0},
    {"id": "courier", "label": "Corriere espresso", "cost": 6.9},
]

HAND_ZONES = [
    "Buggiano",
    "Montecatini",
    "Monsummano",
    "Gragnano",
    "Firenze Osmannoro",
    "Prato (Esselunga)",
    "Lucca",
]

PAYMENT_METHODS = [
    {"id": "contanti", "label": "Contanti"},
    {"id": "paypal", "label": "PayPal"},
    {"id": "bonifico", "label": "Bonifico"},
    {"id": "btc_wos", "label": "Bitcoin (Wallet of Satoshi)"},
    {"id": "btc_satsmobi", "label": "Bitcoin (SatsMobi Telegram)"},
]

HELP_TEXT = (
    "🔎 <b>ASSISTENZA PALEOTTI</b>\n\n"
    "Se hai bisogno di ulteriori informazioni su prodotti, spedizioni o pagamenti:\n\n"
    "• WhatsApp: https://wa.me/qr/OWMKMVQ2NEEYJ1\n"
    "• Telegram: https://t.me/Paleotti\n\n"
    "Rimani aggiornato sulle novità PALEOTTI:\n"
    "• Canale WhatsApp: https://www.whatsapp.com/channel/0029VbBmVPmHbFVCJe95521W\n"
    "• Canale Telegram: https://t.me/+dtOXjMQfZD9lZGI0\n\n"
    "Premi INDIETRO per tornare alla schermata precedente."
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Dizionario rapido per id
PRODUCTS_BY_ID = {p["id"]: p for p in PRODUCTS}


# ================== UTILITY ==================


def format_price(value: float) -> str:
    return f"{value:.2f} €".replace(".", ",")


def get_cart(user_data: Dict[str, Any]) -> Dict[str, int]:
    return user_data.setdefault("cart", {})


def cart_total(cart: Dict[str, int]) -> float:
    total = 0.0
    for pid, qty in cart.items():
        p = PRODUCTS_BY_ID.get(pid)
        if p:
            total += p["price"] * qty
    return total


def format_cart(cart: Dict[str, int]) -> str:
    if not cart:
        return "Il carrello è vuoto."
    lines = []
    for pid, qty in cart.items():
        product = PRODUCTS_BY_ID.get(pid)
        if not product:
            continue
        line = f"• {product['name']} x {qty} = {format_price(product['price'] * qty)}"
        lines.append(line)
    lines.append(f"\nSubtotale prodotti: {format_price(cart_total(cart))}")
    return "\n".join(lines)


def build_main_menu() -> InlineKeyboardMarkup:
    """Menu principale con tutti i prodotti (start / indietro)."""
    return build_products_keyboard()


def build_products_keyboard() -> InlineKeyboardMarkup:
    rows = []
    for p in PRODUCTS:
        rows.append(
            [
                InlineKeyboardButton(
                    f"{p['name']} ({format_price(p['price'])})",
                    callback_data=f"prod:{p['id']}",
                )
            ]
        )

    rows.append(
        [InlineKeyboardButton("🧺 Vai al carrello", callback_data="cart:show")]
    )
    rows.append(
        [InlineKeyboardButton("🆘 Help", callback_data="menu:help")]
    )
    rows.append(
        [InlineKeyboardButton("⬅️ Indietro", callback_data="menu:main")]
    )
    return InlineKeyboardMarkup(rows)


def build_cart_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                "➕ Aggiungi altri prodotti", callback_data="menu:order"
            ),
        ],
        [
            InlineKeyboardButton("🧹 Svuota carrello", callback_data="cart:clear"),
            InlineKeyboardButton("✅ Procedi all'ordine", callback_data="order:shipping"),
        ],
        [
            InlineKeyboardButton("⬅️ Indietro", callback_data="menu:main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def build_shipping_keyboard() -> InlineKeyboardMarkup:
    rows = [
        [
            InlineKeyboardButton(
                f"{opt['label']} ({'gratuita' if opt['cost'] == 0 else format_price(opt['cost'])})",
                callback_data=f"ship:{opt['id']}",
            )
        ]
        for opt in SHIPPING_OPTIONS
    ]
    rows.append([InlineKeyboardButton("⬅️ Indietro", callback_data="cart:show")])
    return InlineKeyboardMarkup(rows)


def build_hand_zones_keyboard() -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(zone, callback_data=f"handzone:{zone}")]
        for zone in HAND_ZONES
    ]
    rows.append([InlineKeyboardButton("⬅️ Indietro", callback_data="order:shipping")])
    return InlineKeyboardMarkup(rows)


def build_payment_keyboard() -> InlineKeyboardMarkup:
    rows = [
        [
            InlineKeyboardButton(
                method["label"], callback_data=f"pay:{method['id']}"
            )
        ]
        for method in PAYMENT_METHODS
    ]
    rows.append([InlineKeyboardButton("⬅️ Indietro", callback_data="order:shipping")])
    return InlineKeyboardMarkup(rows)


def build_after_add_keyboard() -> InlineKeyboardMarkup:
    """Dopo aver aggiunto un prodotto: aggiungi altro o vai al carrello."""
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕ Aggiungi altri prodotti", callback_data="menu:order"
                )
            ],
            [
                InlineKeyboardButton("🧺 Vai al carrello", callback_data="cart:show"),
            ],
            [
                InlineKeyboardButton("⬅️ Indietro", callback_data="menu:main"),
            ],
        ]
    )


def build_summary_keyboard() -> InlineKeyboardMarkup:
    """Tastiera sotto al riepilogo finale."""
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📤 Invia ordine", callback_data="order:confirm"
                ),
            ],
            [
                InlineKeyboardButton(
                    "✏️ Modifica carrello", callback_data="order:edit_cart"
                ),
            ],
            [
                InlineKeyboardButton(
                    "❌ Annulla tutto", callback_data="order:cancel"
                ),
            ],
            [
                InlineKeyboardButton("🆘 Help", callback_data="order:help"),
            ],
        ]
    )


# ================== HANDLER COMANDI ==================


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_data = context.user_data
    user_data.clear()

    text = (
        "Benvenuto nel mondo PALEOTTI - Natura ad ogni morso! 🌿\n\n"
        "Da qui puoi ordinare tutti i nostri prodotti, cominciamo!\n\n"
        f"{BISCOTTI_NOTE}"
    )

    if update.message:
        await update.message.reply_text(text, reply_markup=build_products_keyboard())
    else:
        await update.callback_query.message.reply_text(
            text, reply_markup=build_products_keyboard()
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_html(HELP_TEXT)
    else:
        await update.callback_query.message.reply_html(HELP_TEXT)


# ================== CALLBACK (BOTTONI) ==================


async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data
    user_data = context.user_data
    cart = get_cart(user_data)

    # Menu principale
    if data == "menu:main":
        await query.edit_message_text(
            "Benvenuto nel mondo PALEOTTI - Natura ad ogni morso!\n\n"
            "Da qui puoi ordinare tutti i nostri prodotti, cominciamo!",
            reply_markup=build_products_keyboard(),
        )
        return

    # Help da menu
    if data == "menu:help":
        await query.edit_message_html(HELP_TEXT, reply_markup=build_main_menu())
        return

    # Schermata “scegli prodotti”
    if data == "menu:order":
        await query.edit_message_text(
            "Scegli i prodotti da aggiungere al carrello:",
            reply_markup=build_products_keyboard(),
        )
        return

    # Click su un prodotto: mostra dettagli e chiede quantità
    if data.startswith("prod:"):
        pid = data.split(":", 1)[1]
        product = PRODUCTS_BY_ID.get(pid)
        if not product:
            return

        user_data["pending_product"] = pid
        user_data["state"] = "ASK_QTY"

        text = (
            f"<b>{product['name']}</b>\n"
            f"Prezzo: {format_price(product['price'])}\n\n"
            f"{product['description']}\n\n"
            "Scrivi il <b>numero di pezzi</b> che vuoi aggiungere al carrello "
            "(es. 3)."
        )
        await query.edit_message_text(
            text=text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⬅️ Indietro", callback_data="menu:main")],
                ]
            ),
        )
        return

    # Carrello
    if data == "cart:show":
        text = f"🧺 <b>Il tuo carrello</b>\n\n{format_cart(cart)}"
        await query.edit_message_text(
            text=text, parse_mode="HTML", reply_markup=build_cart_keyboard()
        )
        return

    if data == "cart:clear":
        cart.clear()
        await query.edit_message_text(
            "Il carrello è stato svuotato.",
            reply_markup=build_main_menu(),
        )
        return

    # Inizio ordine: scelta spedizione
    if data == "order:shipping":
        if not cart:
            await query.edit_message_text(
                "Il carrello è vuoto. Aggiungi almeno un prodotto.",
                reply_markup=build_products_keyboard(),
            )
            return
        user_data["order"] = {}
        await query.edit_message_text(
            "Seleziona il metodo di spedizione:",
            reply_markup=build_shipping_keyboard(),
        )
        return

    if data.startswith("ship:"):
        ship_id = data.split(":", 1)[1]
        opt = next((o for o in SHIPPING_OPTIONS if o["id"] == ship_id), None)
        if not opt:
            return
        order = user_data.setdefault("order", {})
        order["shipping_id"] = ship_id
        order["shipping_label"] = opt["label"]
        order["shipping_cost"] = opt["cost"]

        if ship_id == "hand":
            await query.edit_message_text(
                "Seleziona la zona per la consegna a mano:",
                reply_markup=build_hand_zones_keyboard(),
            )
        else:
            await query.edit_message_text(
                "Seleziona il metodo di pagamento:",
                reply_markup=build_payment_keyboard(),
            )
        return

    if data.startswith("handzone:"):
        zone = data.split(":", 1)[1]
        order = user_data.setdefault("order", {})
        order["hand_zone"] = zone
        await query.edit_message_text(
            f"Zona scelta: <b>{zone}</b>\n\nOra seleziona il metodo di pagamento:",
            parse_mode="HTML",
            reply_markup=build_payment_keyboard(),
        )
        return

    # Scelta pagamento → inizio flusso dati cliente
    if data.startswith("pay:"):
        pay_id = data.split(":", 1)[1]
        method = next((m for m in PAYMENT_METHODS if m["id"] == pay_id), None)
        if not method:
            return
        order = user_data.setdefault("order", {})
        order["payment_id"] = pay_id
        order["payment_label"] = method["label"]

        user_data["state"] = "ASK_FIRST_NAME"
        await query.edit_message_text(
            "Perfetto! Ora ti chiedo alcuni dati per la spedizione.\n\n"
            "Inserisci il <b>nome</b>:",
            parse_mode="HTML",
        )
        return

    # Pulsanti dal riepilogo
    if data == "order:confirm":
        summary = user_data.get("last_summary")
        if not summary:
            await query.answer(
                "Nessun ordine da inviare, ricomincia da /start.", show_alert=True
            )
            return

        # Invia ai proprietari
        for owner_id in OWNER_CHAT_IDS:
            try:
                await context.bot.send_message(
                    chat_id=owner_id,
                    text=summary,
                    parse_mode="HTML",
                )
            except Exception as e:
                logger.error(f"Errore nell'invio dell'ordine a {owner_id}: {e}")

        user_data.clear()
        await query.edit_message_text(
            "✅ Il tuo ordine è stato inviato! Grazie 🙏\n\n"
            "Per qualsiasi dubbio puoi usare il tasto Help o contattare l'assistenza.",
        )
        return

    if data == "order:edit_cart":
        text = f"🧺 <b>Il tuo carrello</b>\n\n{format_cart(cart)}"
        await query.edit_message_text(
            text=text, parse_mode="HTML", reply_markup=build_cart_keyboard()
        )
        return

    if data == "order:cancel":
        user_data.clear()
        await query.edit_message_text(
            "L'ordine è stato annullato. Puoi ricominciare quando vuoi con /start.",
        )
        return

    if data == "order:help":
        await query.edit_message_html(HELP_TEXT, reply_markup=build_main_menu())
        return


# ================== RACCOLTA DATI CLIENTE ==================


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None:
        return

    user_data = context.user_data
    state: Optional[str] = user_data.get("state")

    # Nessun flusso attivo → mostro menu prodotti
    if not state:
        await update.message.reply_text(
            "Usa i pulsanti qui sotto per navigare nel bot.",
            reply_markup=build_main_menu(),
        )
        return

    text = update.message.text.strip()
    order = user_data.setdefault("order", {})

    # 1) Quantità prodotto
    if state == "ASK_QTY":
        pid = user_data.get("pending_product")
        product = PRODUCTS_BY_ID.get(pid) if pid else None
        if not product:
            user_data["state"] = None
            await update.message.reply_text(
                "Qualcosa è andato storto con il prodotto selezionato. Riprova.",
                reply_markup=build_products_keyboard(),
            )
            return

        try:
            qty = int(text)
            if qty <= 0:
                raise ValueError()
        except ValueError:
            await update.message.reply_text(
                "Per favore inserisci un numero intero positivo (es. 3)."
            )
            return

        cart = get_cart(user_data)
        cart[pid] = cart.get(pid, 0) + qty
        user_data["state"] = None
        user_data["pending_product"] = None

        await update.message.reply_text(
            f"Hai aggiunto {qty} x {product['name']} al carrello.\n\n"
            "Vuoi aggiungere altri prodotti o andare al carrello?",
            reply_markup=build_after_add_keyboard(),
        )
        return

    # 2) Dati cliente step-by-step

    if state == "ASK_FIRST_NAME":
        order["first_name"] = text
        user_data["state"] = "ASK_LAST_NAME"
        await update.message.reply_text("Inserisci il <b>cognome</b>:", parse_mode="HTML")
        return

    if state == "ASK_LAST_NAME":
        order["last_name"] = text
        user_data["state"] = "ASK_ADDRESS"
        await update.message.reply_text(
            "Inserisci l'<b>indirizzo completo</b> (via e numero civico):",
            parse_mode="HTML",
        )
        return

    if state == "ASK_ADDRESS":
        order["customer_address"] = text
        user_data["state"] = "ASK_CITY"
        await update.message.reply_text("Inserisci la <b>città</b>:", parse_mode="HTML")
        return

    if state == "ASK_CITY":
        order["customer_city"] = text
        user_data["state"] = "ASK_PROVINCE"
        await update.message.reply_text(
            "Inserisci la <b>provincia</b>:", parse_mode="HTML"
        )
        return

    if state == "ASK_PROVINCE":
        order["customer_province"] = text
        user_data["state"] = "ASK_CAP"
        await update.message.reply_text("Inserisci il <b>CAP</b>:", parse_mode="HTML")
        return

    if state == "ASK_CAP":
        order["customer_cap"] = text
        user_data["state"] = "ASK_INTERCOM"
        await update.message.reply_text(
            "Cognome scritto sul <b>citofono</b>:", parse_mode="HTML"
        )
        return

    if state == "ASK_INTERCOM":
        order["customer_intercom"] = text
        user_data["state"] = "ASK_PHONE"
        await update.message.reply_text(
            "Numero di <b>telefono</b> per il corriere / contatti:",
            parse_mode="HTML",
        )
        return

    if state == "ASK_PHONE":
        order["customer_phone"] = text
        user_data["state"] = "ASK_NOTES"
        await update.message.reply_text(
            "Note aggiuntive per l'ordine (allergie, orari, campanello, ecc.).\n"
            "Se non hai note, scrivi semplicemente 'nessuna'."
        )
        return

    if state == "ASK_NOTES":
        order["customer_notes"] = text
        user_data["state"] = None  # fine flusso
        await finalize_order(update, context)
        return


async def finalize_order(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Costruisce il riepilogo e lo mostra al cliente con i pulsanti finali."""
    user_data = context.user_data
    cart = get_cart(user_data)
    order = user_data.get("order", {})

    shipping_cost = float(order.get("shipping_cost", 0.0))
    products_total = cart_total(cart)
    total = products_total + shipping_cost

    lines = []
    lines.append("🧾 <b>Riepilogo ordine PALEOTTI</b>\n")
    lines.append("📦 <b>Prodotti</b>")
    for pid, qty in cart.items():
        p = PRODUCTS_BY_ID.get(pid)
        if not p:
            continue
        lines.append(f"• {p['name']} x {qty} = {format_price(p['price'] * qty)}")
    lines.append(f"\nSubtotale prodotti: {format_price(products_total)}")

    lines.append("\n🚚 <b>Spedizione</b>")
    lines.append(f"Metodo: {order.get('shipping_label', '-')}")
    if order.get("shipping_id") == "hand":
        zone = order.get("hand_zone", "-")
        lines.append(f"Zona consegna a mano: {zone}")
    lines.append(f"Costo spedizione: {format_price(shipping_cost)}")

    lines.append("\n💳 <b>Pagamento</b>")
    lines.append(f"Metodo: {order.get('payment_label', '-')}")

    lines.append("\n👤 <b>Dati cliente</b>")
    full_name = f"{order.get('first_name', '-') } {order.get('last_name', '')}".strip()
    lines.append(f"Nome e cognome: {full_name}")
    lines.append(f"Indirizzo: {order.get('customer_address', '-')}")

    lines.append(
        "Città / Provincia / CAP: "
        f"{order.get('customer_city', '-')}, "
        f"{order.get('customer_province', '-')}, "
        f"{order.get('customer_cap', '-')}"
    )
    lines.append(f"Citofono: {order.get('customer_intercom', '-')}")
    lines.append(f"Telefono: {order.get('customer_phone', '-')}")
    lines.append(f"Note: {order.get('customer_notes', '-')}")

    lines.append(f"\n💰 <b>TOTALE:</b> {format_price(total)}")

    summary = "\n".join(lines)
    user_data["last_summary"] = summary  # servirà quando preme "Invia ordine"

    await update.message.reply_html(
        text=summary,
        reply_markup=build_summary_keyboard(),
    )


# ================== MAIN ==================


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error("Eccezione nel bot", exc_info=context.error)


def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

    app.add_error_handler(error_handler)

    logger.info("Bot PALEOTTI avviato.")
    # PTB 20: metodo sincrono, nessun asyncio.run
    app.run_polling()


if __name__ == "__main__":
    main()
