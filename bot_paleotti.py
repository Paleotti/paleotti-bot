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

BOT_TOKEN = "8556329067:AAG01gKTjkia1clf9L29EwsboyCS_hgRkQc"

OWNER_CHAT_IDS = [
    6260926202,
    1189411829,
    1041813873,
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

# ================== UTILITY ==================

def get_product_by_id(product_id: str) -> Optional[Dict[str, Any]]:
    for p in PRODUCTS:
        if p["id"] == product_id:
            return p
    return None


def get_shipping_option(ship_id: str) -> Optional[Dict[str, Any]]:
    for s in SHIPPING_OPTIONS:
        if s["id"] == ship_id:
            return s
    return None


def get_payment_method(pay_id: str) -> Optional[Dict[str, Any]]:
    for p in PAYMENT_METHODS:
        if p["id"] == pay_id:
            return p
    return None


def format_cart(cart: List[Dict[str, Any]]) -> str:
    if not cart:
        return "Nessun prodotto nel carrello."
    lines = []
    total = 0.0
    for item in cart:
        subtotal = item["price"] * item["qty"]
        total += subtotal
        lines.append(f"- {item['name']} x{item['qty']} = {subtotal:.2f} €")
    lines.append(f"\nTotale parziale prodotti: {total:.2f} €")
    return "\n".join(lines)


def calc_cart_total(cart: List[Dict[str, Any]], shipping_cost: float) -> float:
    base = 0.0
    for item in cart:
        base += item["price"] * item["qty"]
    return base + shipping_cost


def base_keyboard_help_row() -> List[InlineKeyboardButton]:
    return [InlineKeyboardButton("HELP", callback_data="HELP")]
# ================== SCHERMATE PRINCIPALI ==================

async def show_main_menu(chat_id: int, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.setdefault("cart", [])
    context.user_data["step"] = "products"

    keyboard = []
    row = []

    for i, product in enumerate(PRODUCTS, start=1):
        row.append(
            InlineKeyboardButton(product["name"], callback_data=f"PROD_{product['id']}")
        )
        if i % 2 == 0:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)

    keyboard.append(base_keyboard_help_row())

    text = (
        "🍪 <b>Benvenuto nel mondo PALEOTTI</b>\n"
        "<i>Natura ad ogni morso!</i>\n\n"
        "Seleziona un prodotto per vedere i dettagli e scegliere la quantità.\n\n"
        f"{BISCOTTI_NOTE}"
    )

    await context.bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def show_product_details(chat_id: int, context: ContextTypes.DEFAULT_TYPE, product: Dict[str, Any]) -> None:
    context.user_data["current_product_id"] = product["id"]
    context.user_data["step"] = "quantity"

    text = (
        f"📦 <b>{product['name']}</b>\n\n"
        f"{product['description']}\n"
        f"Prezzo: <b>{product['price']:.2f} €</b>\n\n"
        "Seleziona la quantità:"
    )

    qty_buttons = [
        [
            InlineKeyboardButton("1", callback_data="QTY_1"),
            InlineKeyboardButton("2", callback_data="QTY_2"),
            InlineKeyboardButton("3", callback_data="QTY_3"),
        ],
        [
            InlineKeyboardButton("4", callback_data="QTY_4"),
            InlineKeyboardButton("5", callback_data="QTY_5"),
        ],
        base_keyboard_help_row(),
        [InlineKeyboardButton("⬅️ Indietro", callback_data="BACK_TO_PRODUCTS")],
    ]

    await context.bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(qty_buttons),
    )


async def ask_add_more(chat_id: int, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["step"] = "add_more"
    cart = context.user_data.get("cart", [])

    text = (
        "✅ Prodotto aggiunto al carrello.\n\n"
        "Carrello attuale:\n"
        f"{format_cart(cart)}\n\n"
        "Vuoi aggiungere altri prodotti?"
    )

    keyboard = [
        [
            InlineKeyboardButton("➕ Sì, aggiungi altri", callback_data="MORE_yes"),
            InlineKeyboardButton("➡️ No, procedi", callback_data="MORE_no"),
        ],
        base_keyboard_help_row(),
        [InlineKeyboardButton("⬅️ Indietro", callback_data="BACK_TO_PRODUCTS")],
    ]

    await context.bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def ask_shipping(chat_id: int, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["step"] = "shipping"

    keyboard = [
        [InlineKeyboardButton(s["label"], callback_data=f"SHIP_{s['id']}")]
        for s in SHIPPING_OPTIONS
    ]

    keyboard.append(base_keyboard_help_row())
    keyboard.append([InlineKeyboardButton("⬅️ Indietro", callback_data="BACK_TO_CART")])

    text = (
        "🚚 Seleziona il metodo di spedizione:\n\n"
        "• Consegna a mano nelle zone indicate\n"
        "• Corriere espresso 24/48h (6,90 €)\n"
    )

    await context.bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def ask_hand_zone(chat_id: int, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["step"] = "hand_zone"

    keyboard = []
    row = []
    for i, zona in enumerate(HAND_ZONES, start=1):
        row.append(InlineKeyboardButton(zona, callback_data=f"HANDZONE_{i}"))
        if i % 2 == 0:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)

    keyboard.append(base_keyboard_help_row())
    keyboard.append([InlineKeyboardButton("⬅️ Indietro", callback_data="BACK_TO_SHIPPING")])

    await context.bot.send_message(
        chat_id=chat_id,
        text="Scegli la zona per la consegna a mano:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
async def ask_payment(chat_id: int, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["step"] = "payment"

    keyboard = [
        [InlineKeyboardButton(p["label"], callback_data=f"PAY_{p['id']}")]
        for p in PAYMENT_METHODS
    ]

    keyboard.append(base_keyboard_help_row())
    keyboard.append([InlineKeyboardButton("⬅️ Indietro", callback_data="BACK_TO_SHIPPING")])

    text = "💳 Seleziona il metodo di pagamento:"

    await context.bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def show_summary(chat_id: int, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["step"] = "summary"

    cart = context.user_data.get("cart", [])
    shipping_id = context.user_data.get("shipping_id")
    payment_id = context.user_data.get("payment_id")
    shipping_data = context.user_data.get("shipping_data", {})

    shipping = get_shipping_option(shipping_id)
    payment = get_payment_method(payment_id)

    if not cart or not shipping or not payment:
        await context.bot.send_message(chat_id, "Errore: dati ordine incompleti. Riprova con /start")
        context.user_data.clear()
        return

    shipping_cost = shipping["cost"]
    total = calc_cart_total(cart, shipping_cost)

    cart_text = format_cart(cart)

    shipping_text = shipping["label"]
    if shipping_cost > 0:
        shipping_text += f" +{shipping_cost:.2f} €"

    payment_text = payment["label"]

    shipping_block = ""
    if shipping_id == "courier":
        shipping_block = (
            "\n\n<b>Dati spedizione:</b>\n"
            f"Nome: {shipping_data.get('nome', '')}\n"
            f"Cognome: {shipping_data.get('cognome', '')}\n"
            f"Telefono: {shipping_data.get('telefono', '')}\n"
            f"Indirizzo: {shipping_data.get('indirizzo', '')}\n"
            f"CAP: {shipping_data.get('cap', '')}\n"
            f"Città: {shipping_data.get('citta', '')}\n"
            f"Provincia: {shipping_data.get('provincia', '')}\n"
            f"Citofono: {shipping_data.get('citofono', '')}\n"
        )
    elif shipping_id == "hand":
        zona = shipping_data.get("zona_hand", "")
        if zona:
            shipping_block = f"\n\nZona consegna a mano: {zona}\n"

    text = (
        "🧾 <b>Riepilogo ordine PALEOTTI</b>\n\n"
        f"{cart_text}\n\n"
        f"Spedizione: {shipping_text}\n"
        f"Pagamento: {payment_text}"
        f"{shipping_block}\n"
        f"<b>Totale finale: {total:.2f} €</b>\n\n"
        "Confermi l’ordine?"
    )

    keyboard = [
        [
            InlineKeyboardButton("✅ Conferma ordine", callback_data="CONFIRM_yes"),
            InlineKeyboardButton("❌ Annulla", callback_data="CONFIRM_no"),
        ],
        base_keyboard_help_row(),
        [InlineKeyboardButton("⬅️ Indietro", callback_data="BACK_TO_PAYMENT")],
    ]

    await context.bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def show_help_screen(chat_id: int, context: ContextTypes.DEFAULT_TYPE) -> None:
    prev_step = context.user_data.get("step")
    context.user_data["prev_step"] = prev_step
    context.user_data["step"] = "help"

    keyboard = [
        [InlineKeyboardButton("⬅️ INDIETRO", callback_data="BACK_FROM_HELP")],
        [
            InlineKeyboardButton("WhatsApp", url="https://wa.me/qr/OWMKMVQ2NEEYJ1"),
            InlineKeyboardButton("Telegram", url="https://t.me/Paleotti"),
        ],
        [
            InlineKeyboardButton("Canale WhatsApp", url="https://www.whatsapp.com/channel/0029VbBmVPmHbFVCJe95521W"),
            InlineKeyboardButton("Canale Telegram", url="https://t.me/+dtOXjMQfZD9lZGI0"),
        ],
    ]

    await context.bot.send_message(
        chat_id=chat_id,
        text=HELP_TEXT,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def return_from_help(chat_id: int, context: ContextTypes.DEFAULT_TYPE) -> None:
    prev = context.user_data.get("prev_step")
    context.user_data["step"] = prev

    if prev == "products":
        await show_main_menu(chat_id, context)
        return

    if prev == "quantity":
        pid = context.user_data.get("current_product_id")
        product = get_product_by_id(pid)
        await show_product_details(chat_id, context, product)
        return

    if prev == "add_more":
        await ask_add_more(chat_id, context)
        return

    if prev == "shipping":
        await ask_shipping(chat_id, context)
        return

    if prev == "hand_zone":
        await ask_hand_zone(chat_id, context)
        return

    if prev == "payment":
        await ask_payment(chat_id, context)
        return

    if prev == "summary":
        await show_summary(chat_id, context)
        return

    await show_main_menu(chat_id, context)
async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    data = query.data or ""
    chat_id = query.message.chat_id
    await query.answer()

    # ================= HELP =================
    if data == "HELP":
        await show_help_screen(chat_id, context)
        return

    if data == "BACK_FROM_HELP":
        await return_from_help(chat_id, context)
        return

    # ================= TORNA INDIETRO =================
    if data == "BACK_TO_PRODUCTS":
        await show_main_menu(chat_id, context)
        return

    if data == "BACK_TO_CART":
        await ask_add_more(chat_id, context)
        return

    if data == "BACK_TO_SHIPPING":
        await ask_shipping(chat_id, context)
        return

    if data == "BACK_TO_PAYMENT":
        await ask_payment(chat_id, context)
        return

    # ================= SELEZIONE PRODOTTO =================
    if data.startswith("PROD_"):
        product_id = data.replace("PROD_", "")
        product = get_product_by_id(product_id)

        if not product:
            await context.bot.send_message(chat_id, "Errore: prodotto non trovato. Riprova con /start")
            return

        await show_product_details(chat_id, context, product)
        return

    # ================= SELEZIONE QUANTITÀ =================
    if data.startswith("QTY_"):
        qty = int(data.replace("QTY_", ""))
        product_id = context.user_data.get("current_product_id")
        product = get_product_by_id(product_id)

        if not product:
            await context.bot.send_message(chat_id, "Errore: prodotto non trovato.")
            return

        cart = context.user_data.setdefault("cart", [])
        cart.append({
            "product_id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "qty": qty,
        })

        await ask_add_more(chat_id, context)
        return

    # ================= AGGIUNGERE ALTRI PRODOTTI =================
    if data.startswith("MORE_"):
        choose = data.replace("MORE_", "")

        if choose == "yes":
            await show_main_menu(chat_id, context)
        else:
            await ask_shipping(chat_id, context)
        return

    # ================= METODO DI SPEDIZIONE =================
    if data.startswith("SHIP_"):
        ship_id = data.replace("SHIP_", "")
        shipping = get_shipping_option(ship_id)

        if not shipping:
            await context.bot.send_message(chat_id, "Errore nella selezione della spedizione.")
            return

        context.user_data["shipping_id"] = ship_id

        if ship_id == "courier":
            context.user_data["shipping_data"] = {}
            context.user_data["step"] = "ship_name"

            keyboard = [
                [InlineKeyboardButton("⬅️ Indietro", callback_data="BACK_TO_SHIPPING")],
                base_keyboard_help_row(),
            ]

            await context.bot.send_message(
                chat_id,
                "Per la spedizione con corriere ho bisogno dei tuoi dati.\n\n"
                "👉 Inserisci il tuo <b>nome</b>:",
                parse_mode="HTML",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        else:
            await ask_hand_zone(chat_id, context)

        return

    # ================= CONSEGNA A MANO — ZONA =================
    if data.startswith("HANDZONE_"):
        idx = int(data.replace("HANDZONE_", "")) - 1
        zona = HAND_ZONES[idx] if 0 <= idx < len(HAND_ZONES) else None

        if not zona:
            await context.bot.send_message(chat_id, "Errore nella scelta della zona.")
            return

        sd = context.user_data.setdefault("shipping_data", {})
        sd["zona_hand"] = zona

        await ask_payment(chat_id, context)
        return

    # ================= METODO DI PAGAMENTO =================
    if data.startswith("PAY_"):
        pay_id = data.replace("PAY_", "")
        payment = get_payment_method(pay_id)

        if not payment:
            await context.bot.send_message(chat_id, "Errore nella selezione del pagamento.")
            return

        context.user_data["payment_id"] = pay_id
        await show_summary(chat_id, context)
        return

    # ================= CONFERMA ORDINE =================
    if data.startswith("CONFIRM_"):
        choice = data.replace("CONFIRM_", "")

        if choice == "no":
            await context.bot.send_message(chat_id, "Ordine annullato. Puoi ripartire con /start")
            context.user_data.clear()
            return

        # --- PREPARA I DATI ORDINE ---
        cart = context.user_data.get("cart", [])
        shipping_id = context.user_data.get("shipping_id")
        payment_id = context.user_data.get("payment_id")
        shipping_data = context.user_data.get("shipping_data", {})

        shipping = get_shipping_option(shipping_id)
        payment = get_payment_method(payment_id)

        shipping_cost = shipping["cost"]
        total = calc_cart_total(cart, shipping_cost)

        cart_text = format_cart(cart)
        shipping_text = shipping["label"] + (f" +{shipping_cost:.2f} €" if shipping_cost > 0 else "")
        payment_text = payment["label"]

        # --- BLOCCHI SPEDIZIONE ---
        shipping_block_user = ""
        shipping_block_owner = ""

        if shipping_id == "courier":
            shipping_block_user = (
                "\n\n<b>Dati spedizione:</b>\n"
                f"Nome: {shipping_data.get('nome')}\n"
                f"Cognome: {shipping_data.get('cognome')}\n"
                f"Telefono: {shipping_data.get('telefono')}\n"
                f"Indirizzo: {shipping_data.get('indirizzo')}\n"
                f"CAP: {shipping_data.get('cap')}\n"
                f"Città: {shipping_data.get('citta')}\n"
                f"Provincia: {shipping_data.get('provincia')}\n"
                f"Citofono: {shipping_data.get('citofono')}\n"
            )

            shipping_block_owner = shipping_block_user.replace("<b>", "").replace("</b>", "")

        elif shipping_id == "hand":
            zona = shipping_data.get("zona_hand")
            shipping_block_user = f"\n\nZona consegna a mano: {zona}"
            shipping_block_owner = f"\n\nZONA CONSEGNA A MANO: {zona}"

        # --- NOME CLIENTE ---
        user = query.from_user
        username = user.username or f"{user.first_name or ''} {user.last_name or ''}".strip()
        username = username or "Utente"

        # --- MESSAGGIO PER L'UTENTE ---
        summary = (
            "🧾 <b>Ordine confermato!</b>\n\n"
            f"{cart_text}\n\n"
            f"Spedizione: {shipping_text}\n"
            f"Pagamento: {payment_text}"
            f"{shipping_block_user}\n\n"
            f"<b>Totale: {total:.2f} €</b>\n"
            "Grazie per il tuo ordine da <b>PALEOTTI</b>!"
        )

        await context.bot.send_message(chat_id, summary, parse_mode="HTML")

        # --- NOTIFICA AI TITOLARI ---
        owner_msg = (
            "📬 <b>NUOVO ORDINE PALEOTTI</b>\n\n"
            f"Cliente: {username} (id: {user.id})\n\n"
            f"{cart_text}\n\n"
            f"Spedizione: {shipping_text}\n"
            f"Pagamento: {payment_text}"
            f"{shipping_block_owner}\n\n"
            f"Totale: {total:.2f} €"
        )

        for admin in OWNER_CHAT_IDS:
            try:
                await context.bot.send_message(admin, owner_msg, parse_mode="HTML")
            except Exception as e:
                logger.error(f"Errore invio a {admin}: {e}")

        context.user_data.clear()
        return

    # Se arriva qui, nessun comando riconosciuto
    await context.bot.send_message(chat_id, "Azione non riconosciuta. Usa /start.")
# ================== HANDLER TESTO (DATI SPEDIZIONE) ==================

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    step = context.user_data.get("step")
    if not step or not step.startswith("ship_"):
        return  # Ignora messaggi non relativi ai dati spedizione

    chat_id = update.effective_chat.id
    text = (update.message.text or "").strip()
    sd = context.user_data.setdefault("shipping_data", {})

    # NOME
    if step == "ship_name":
        sd["nome"] = text
        context.user_data["step"] = "ship_surname"

        await update.message.reply_text("Inserisci il tuo cognome:")
        return

    # COGNOME
    if step == "ship_surname":
        sd["cognome"] = text
        context.user_data["step"] = "ship_phone"

        await update.message.reply_text("Inserisci il tuo numero di telefono:")
        return

    # TELEFONO
    if step == "ship_phone":
        sd["telefono"] = text
        context.user_data["step"] = "ship_address"

        await update.message.reply_text("Inserisci il tuo indirizzo completo (via + numero civico):")
        return

    # INDIRIZZO
    if step == "ship_address":
        sd["indirizzo"] = text
        context.user_data["step"] = "ship_cap"

        await update.message.reply_text("Inserisci il CAP:")
        return

    # CAP
    if step == "ship_cap":
        sd["cap"] = text
        context.user_data["step"] = "ship_city"

        await update.message.reply_text("Inserisci la città:")
        return

    # CITTÀ
    if step == "ship_city":
        sd["citta"] = text
        context.user_data["step"] = "ship_province"

        await update.message.reply_text("Inserisci la provincia:")
        return

    # PROVINCIA
    if step == "ship_province":
        sd["provincia"] = text
        context.user_data["step"] = "ship_citofono"

        await update.message.reply_text("Inserisci il cognome sul citofono:")
        return

    # CITOFONO → FINE
    if step == "ship_citofono":
        sd["citofono"] = text
        context.user_data["step"] = "shipping_done"

        await update.message.reply_text("Perfetto! Ora scegli il metodo di pagamento.")
        await ask_payment(chat_id, context)
        return


# ================== ERROR LOGGING ==================

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(f"Errore: {context.error}")


# ================== MAIN ==================

def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Comandi
    app.add_handler(CommandHandler("start", start))

    # Pulsanti
    app.add_handler(CallbackQueryHandler(callback_handler))

    # Messaggi di testo (per indirizzi spedizione)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

    # Gestione errori
    app.add_error_handler(error_handler)

    print("Bot PALEOTTI in esecuzione...")
    app.run_polling()


if __name__ == "__main__":
    main()
