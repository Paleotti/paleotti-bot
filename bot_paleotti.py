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

# <<< METTI QUI IL TUO TOKEN >>>
BOT_TOKEN = "8556329067:AAG01gKTjkia1clf9L29EwsboyCS_hgRkQc"

# <<< ID DELLE PERSONE CHE DEVONO RICEVERE L'ORDINE >>>
OWNER_CHAT_IDS = [
    6260926202,  # <--- PALEOTTI
    1189411829,  # <--- Brossin
    1041813873,  # <--- RobyIris88
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

# Dizionario prodotti rapido per id
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
    keyboard = [
        [
            InlineKeyboardButton("📦 Catalogo prodotti", callback_data="menu:catalog"),
            InlineKeyboardButton("🛒 Fai un ordine", callback_data="menu:order"),
        ],
        [
            InlineKeyboardButton("ℹ️ Assistenza", callback_data="menu:help"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def build_products_keyboard() -> InlineKeyboardMarkup:
    # Un pulsante per aggiungere ogni prodotto + pulsanti carrello
    rows = []
    for p in PRODUCTS:
        rows.append(
            [
                InlineKeyboardButton(
                    f"{p['name']} ({format_price(p['price'])})",
                    callback_data=f"add:{p['id']}",
                )
            ]
        )
    rows.append(
        [
            InlineKeyboardButton("🧺 Vedi carrello", callback_data="cart:show"),
        ]
    )
    rows.append(
        [
            InlineKeyboardButton("⬅️ Indietro", callback_data="menu:main"),
        ]
    )
    return InlineKeyboardMarkup(rows)


def build_cart_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("➕ Aggiungi altri prodotti", callback_data="menu:order"),
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


# ================== HANDLER COMANDI ==================


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_data = context.user_data
    user_data.clear()
    text = (
        "Benvenuto nel bot PALEOTTI! 🎄\n\n"
        "Puoi vedere il catalogo, aggiungere prodotti al carrello e inviare il tuo ordine.\n\n"
        f"{BISCOTTI_NOTE}"
    )
    if update.message:
        await update.message.reply_text(text, reply_markup=build_main_menu())
    else:
        await update.callback_query.message.reply_text(
            text, reply_markup=build_main_menu()
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

    # Menu
    if data == "menu:main":
        await query.edit_message_text(
            "Seleziona una voce dal menu:", reply_markup=build_main_menu()
        )
        return

    if data == "menu:catalog":
        # Mostro elenco con descrizioni
        lines = []
        for p in PRODUCTS:
            lines.append(f"<b>{p['name']}</b> – {format_price(p['price'])}")
            lines.append(p["description"])
            lines.append("")
        text = "\n".join(lines)
        await query.edit_message_text(
            text=text,
            parse_mode="HTML",
            reply_markup=build_products_keyboard(),
        )
        return

    if data == "menu:order":
        await query.edit_message_text(
            "Scegli i prodotti da aggiungere al carrello:",
            reply_markup=build_products_keyboard(),
        )
        return

    if data == "menu:help":
        await query.edit_message_html(HELP_TEXT, reply_markup=build_main_menu())
        return

    # Aggiunta prodotto
    if data.startswith("add:"):
        pid = data.split(":", 1)[1]
        if pid in PRODUCTS_BY_ID:
            cart[pid] = cart.get(pid, 0) + 1
            product = PRODUCTS_BY_ID[pid]
            await query.answer(
                text=f"Aggiunto: {product['name']}", show_alert=False
            )
        await query.edit_message_reply_markup(reply_markup=build_products_keyboard())
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

    if data.startswith("pay:"):
        pay_id = data.split(":", 1)[1]
        method = next((m for m in PAYMENT_METHODS if m["id"] == pay_id), None)
        if not method:
            return
        order = user_data.setdefault("order", {})
        order["payment_id"] = pay_id
        order["payment_label"] = method["label"]

        # Ora iniziamo a chiedere i dati del cliente
        user_data["state"] = "ASK_NAME"
        if query.message.chat.type in ("group", "supergroup"):
            prefix = "Ti scrivo in privato per completare l'ordine."
        else:
            prefix = ""
        await query.edit_message_text(
            f"{prefix}\n\nCome ti chiami? (Nome e Cognome)",
        )
        return


# ================== RACCOLTA DATI CLIENTE ==================


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None:
        return

    user_data = context.user_data
    state: Optional[str] = user_data.get("state")

    if not state:
        # Nessun flusso attivo → mostro menu
        await update.message.reply_text(
            "Usa il menu per navigare nel bot.",
            reply_markup=build_main_menu(),
        )
        return

    text = update.message.text.strip()
    order = user_data.setdefault("order", {})

    if state == "ASK_NAME":
        order["customer_name"] = text
        user_data["state"] = "ASK_ADDRESS"
        await update.message.reply_text("Indirizzo completo (via, n°, CAP, città):")
        return

    if state == "ASK_ADDRESS":
        order["customer_address"] = text
        user_data["state"] = "ASK_PHONE"
        await update.message.reply_text("Numero di telefono:")
        return

    if state == "ASK_PHONE":
        order["customer_phone"] = text
        user_data["state"] = "ASK_EMAIL"
        await update.message.reply_text("Email (opzionale, puoi anche scrivere 'nessuna'):")
        return

    if state == "ASK_EMAIL":
        order["customer_email"] = text
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
    """Costruisce il riepilogo e lo manda al cliente e agli owner."""
    user_data = context.user_data
    cart = get_cart(user_data)
    order = user_data.get("order", {})

    shipping_cost = float(order.get("shipping_cost", 0.0))
    products_total = cart_total(cart)
    total = products_total + shipping_cost

    lines = []
    lines.append("🧾 <b>Nuovo ordine PALEOTTI</b>\n")
    lines.append("📦 <b>Prodotti</b>")
    for pid, qty in cart.items():
        p = PRODUCTS_BY_ID.get(pid)
        if not p:
            continue
        lines.append(
            f"• {p['name']} x {qty} = {format_price(p['price'] * qty)}"
        )
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
    lines.append(f"Nome: {order.get('customer_name', '-')}")
    lines.append(f"Indirizzo: {order.get('customer_address', '-')}")
    lines.append(f"Telefono: {order.get('customer_phone', '-')}")
    lines.append(f"Email: {order.get('customer_email', '-')}")
    lines.append(f"Note: {order.get('customer_notes', '-')}")

    lines.append(f"\n💰 <b>TOTALE:</b> {format_price(total)}")

    summary = "\n".join(lines)

    # Invia al cliente
    await update.message.reply_html(
        text="Grazie! Questo è il riepilogo del tuo ordine:\n\n" + summary
    )

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

    # Reset carrello e ordine
    user_data.clear()


# ================== MAIN ==================


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error("Eccezione nel bot", exc_info=context.error)


async def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

    app.add_error_handler(error_handler)

    logger.info("Bot PALEOTTI avviato.")
    await app.run_polling(close_loop=False)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
