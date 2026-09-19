from core.i18n import get_text
from core.nexus import settings

COFFEE = "coffee"

def get_legacy_dict(var_name: str, lang_code: str):
    STATUS_MSG = {
        "_HOME" : {
            "📊 ↓ SERVER ↓ 📊" : "roxybasicneedbot", "📶 STORAGE 📶" : "status|server", "🥥 DATABASE 🥥" : "status|db",
            "🌝 ↓ GET LIST ↓ 🌝": "roxybasicneedbot", "💎 ADMIN 💎" : "status|admin", "👤 USERS 👤" : "status|users", get_text('BACK_HOME', lang_code) : "Home|A"},
        "DB" : """📂 DATABASE :\n\n**◍ Database Users :** `{}` 📍\n**◍ Database Chats :** `{}` 📍""",
        "SERVER" : "**◍ Total Space     :** `{}`\n**◍ Used Space     :** `{}({}%)`\n**◍ Free Space      :** `{}`\n**◍ CPU Usage      :** `{}%`\n"
                   "**◍ RAM Usage     :** `{}`%\n**◍ Current Work  :** `{}`\n**◍ Message Id     :** `{}`",
        "USERS" : "Users in Database are.", "NO_DB" : "No dataBASE set Yet 💩", "ADMIN" : "**Total ADMIN:** __{}__\n",
        "BACK" : { get_text('BACK_HOME', lang_code) : "status|home" }, "HOME" : "`Now, select any option below to get current STATUS 💱.. `",}
    feedbackMsg = { "message": f"{get_text('FEEDBACK', lang_code)}", "button": { get_text('BUY_ME_A_COFFEE', lang_code) : COFFEE }}
    BAN = {
        "UCantUse" : get_text('BAN', lang_code), "UCantUseDB" : get_text('BAN', lang_code) + get_text('REASON', lang_code), "GroupCantUse" : get_text('BAN_G', lang_code), "GroupCantUseDB" : get_text('BAN_G', lang_code) + get_text('REASON', lang_code),
        "cbNotU" : get_text('BAN_CB', lang_code), "Fool" : get_text('FOOL', lang_code), "Force" : get_text('FORCE', lang_code), "ForceCB" : { get_text('JOIN_CHANNEL', lang_code) : "{0}", get_text('REFRESH', lang_code) : "refresh{1}" },
        "banCB" : {get_text('CREATE_BOT', lang_code) : "https://t.me/roxybasicneed1", get_text('SOURCE', lang_code) : f"{settings.SOURCE_CODE}", get_text('CHANNEL', lang_code) : "https://t.me/roxybasicneedbot1"}}
    PDF_MESSAGE = {
        "pg" : get_text('PG_NUM', lang_code) , "pdf" : get_text('PDF_REPLY', lang_code), "encryptCB" : { get_text('DECRYPT', lang_code) : "#decrypt", get_text('CLOSE', lang_code) : "close|all" },
        "pdf_button" : { get_text('META', lang_code)[1:] : "#metadata", get_text('PREVIEW', lang_code)[1:] : "#preview", get_text('ENCRYPT', lang_code)[1:] : "#encrypt", get_text('DECRYPT', lang_code)[1:] : "#decrypt", get_text('SPLIT', lang_code)[1:] : "#split",
            get_text('MERGE', lang_code)[1:] : "#merge", get_text('RENAME', lang_code)[1:] : "#rename", get_text('URL', lang_code)[1:] : "link", get_text('WATERMARK', lang_code)[1:] : "pdf|wa", get_text('STAMP', lang_code)[1:] : "pdf|stp", 
            get_text('IMAGE', lang_code)[1:] : "pdf|img", get_text('TEXT', lang_code)[1:] : "pdf|txt", get_text('COMPRESS', lang_code)[1:] : "pdf|compress", get_text('MORE', lang_code) : "pdf|more", get_text('CLOSE', lang_code) : "close|all" },
        "all_pdf_button" : { get_text('META', lang_code)[1:] : "#metadata", get_text('PREVIEW', lang_code)[1:] : "#preview", get_text('ENCRYPT', lang_code)[1:] : "#encrypt", get_text('DECRYPT', lang_code)[1:] : "#decrypt",
            get_text('SPLIT', lang_code)[1:] : "#split", get_text('MERGE', lang_code)[1:] : "#merge", get_text('RENAME', lang_code)[1:] : "#rename", get_text('URL', lang_code)[1:] : "link", get_text('WATERMARK', lang_code)[1:] : "pdf|wa",
            get_text('STAMP', lang_code)[1:] : "pdf|stp", get_text('IMAGE', lang_code)[1:] : "pdf|img", get_text('TEXT', lang_code)[1:] : "pdf|txt", get_text('COMPRESS', lang_code)[1:] : "pdf|compress", get_text('OCR', lang_code)[1:] : "#ocr",
            get_text('ROTATE', lang_code)[1:] : "pdf|rotate", get_text('FORMAT', lang_code)[1:] : "pdf|format", get_text('ADD_PG', lang_code)[1:] : "close|dev", get_text('DEL_PG', lang_code)[1:] : "#deletePg",
            get_text('FILTER', lang_code)[1:] : "pdf|filter", get_text('ZOOM', lang_code)[1:] : "#zoom", get_text('PART_PDF', lang_code)[1:] : "#partPDF", get_text('REMOVE_LINKS', lang_code)[1:] : "#urlRemover",
            get_text('HEADER', lang_code)[1:] : "close|dev", get_text('FOOTER', lang_code)[1:] : "close|dev", get_text('ADD_PGNUM', lang_code)[1:] : "close|dev", get_text('LESS', lang_code) : "pdf", get_text('CLOSE', lang_code) : "close|all" },
        "error" : get_text('CODEC', lang_code), "errorCB" : { get_text('CODEC_CB', lang_code) : "error", get_text('CLOSE', lang_code) : "close|all" }, "encrypt" : get_text('ENCRYTED_FILE', lang_code),}
    BUTTONS = {
        "format" : { get_text('HELP', lang_code) : "roxybasicneedbot|format", "1 × 1" : "#1-format", "✌ 1 × 2 ✌" : "#2-format-H", "✌ 2 × 1 ✌" : "#2-format-V",
                     "🤟 1 × 3 🤟" : "#3-format-H", "🤟 3 × 1 🤟" : "#3-format-V", "2 × 2" : "#4-format", get_text('BACK', lang_code) : "pdf" },
        "compress" : { get_text('COMPRESS', lang_code) : "roxybasicneedbot", "📄 Low (Best Quality)" : "#compress|low", "⚖️ Medium (Balanced)" : "#compress|medium", "🗜️ High (Smallest)" : "#compress|high", get_text('BACK', lang_code) : "pdf" },
        "filter" : { get_text('HELP', lang_code) : "roxybasicneedbot|format", get_text('DRAW', lang_code) : "#draw", get_text('BAW', lang_code) : "#baw", get_text('SAT', lang_code) : "#sat", get_text('INV', lang_code) : "#inv", get_text('BACK', lang_code) : "pdf" },
        "toImage" : { get_text('P2IMG', lang_code) : "roxybasicneedbot", get_text('P2I', lang_code) : "pdf|img|img", get_text('P2D', lang_code) : "pdf|img|doc", get_text('P2Z', lang_code) : "pdf|img|zip", get_text('P2T', lang_code) : "pdf|img|tar", get_text('BACK', lang_code) : "pdf" },
        "imgRange" : { get_text('P2IMG_', lang_code) : "roxybasicneedbot", get_text('ALL', lang_code) : "#p2img|{}A", get_text('CUSTOM', lang_code) : "#p2img|{}C", get_text('BACK', lang_code) : "pdf|img" },
        "rotate" : { get_text('B_ROTATE', lang_code) : "roxybasicneedbot", "90°" : "#rot90", "180°" : "#rot180", "270°" : "#rot270", "360°" : "#rot360", get_text('BACK', lang_code) : "pdf" },
        "txt" : { get_text('B_TEXT', lang_code) : "roxybasicneedbot", get_text('B_TEXT_M', lang_code) : "#textM", "🧾 TXT 🧾" : "#textT", "🌐 HTML 🌐" : "#textH", "🎀 JSON 🎀" : "#textJ", get_text('BACK', lang_code) : "pdf" },
        "type" : { get_text('B_WATERMARK', lang_code) : "roxybasicneedbot", get_text('B_TEXT_T', lang_code) : "pdf|wa|txt", get_text('IMAGE', lang_code) : "pdf|wa|img", get_text('B_PDF', lang_code) : "pdf|wa|pdf", get_text('BACK', lang_code) : "pdf" },
        "op" : { get_text('WATER_OP', lang_code) : "roxybasicneedbot", "𝟙𝟘" : "pdf|wa|{}|o01", "𝟚𝟘" : "pdf|wa|{}|o02", "𝟛𝟘" : "pdf|wa|{}|o03", "𝟜𝟘" : "pdf|wa|{}|o04",
            "𝟝𝟘" : "pdf|wa|{}|o05", "𝟞𝟘" : "pdf|wa|{}|o06", "𝟟𝟘" : "pdf|wa|{}|o07", "𝟠𝟘" : "pdf|wa|{}|o08", "𝟡𝟘" : "pdf|wa|{}|o09",
            "𝟙𝟘𝟘" : "pdf|wa|{}|o10", get_text('BACK', lang_code) : "pdf|wa" },
        "po" : { get_text('WATER_PO', lang_code) : "roxybasicneedbot", get_text('TOP', lang_code) : "wa|{0}|{1}|pT", get_text('MIDDLE', lang_code) : "wa|{0}|{1}|pM", get_text('BOTTOM', lang_code) : "wa|{0}|{1}|pB", get_text('BACK', lang_code) : "pdf|wa|{0}" },
        "poTXT" : { get_text('WATER_PO', lang_code) : "roxybasicneedbot", get_text('TOP', lang_code) : "pdf|wa|{0}|{1}|pT", get_text('MIDDLE', lang_code) : "pdf|wa|{0}|{1}|pM", get_text('BOTTOM', lang_code) : "pdf|wa|{0}|{1}|pB", get_text('BACK', lang_code) : "pdf|wa|{0}" },
        "color" : { get_text('WATER_COLOR', lang_code) : "roxybasicneedbot", "᠎᠎᠎⚪️" : "#wa|{0}|{1}|{2}|W", "᠎⚫️" : "#wa|{0}|{1}|{2}|B", "᠎᠎🟤" : "#wa|{0}|{1}|{2}|C",
            "᠎🔴" : "#wa|{0}|{1}|{2}|R", "᠎᠎🟢" : "#wa|{0}|{1}|{2}|G", "🔵" : "#wa|{0}|{1}|{2}|N", "᠎᠎🟡" : "#wa|{0}|{1}|{2}|Y",
            "᠎᠎🟠" : "#wa|{0}|{1}|{2}|O", "🟣" : "#wa|{0}|{1}|{2}|V", get_text('BACK', lang_code) : "pdf|wa|{0}|{1}" },
        "stamp" : { get_text('B_STAMP', lang_code) : "roxybasicneedbot", "Not For Public Release 🤧" : "pdf|stp|10", "For Public Release 🥱" : "pdf|stp|8",
            "Confidential 🤫" : "pdf|stp|2", "Departmental 🤝" : "pdf|stp|3", "Experimental 🔬" : "pdf|stp|4", "Expired 🐀" : "pdf|stp|5",
            "Final 🔧" : "pdf|stp|6", "For Comment 🗯️" : "pdf|stp|7", "Not Approved 😒" : "pdf|stp|9", "Approved 🥳" : "pdf|stp|0",
            "Sold ✊" : "pdf|stp|11", "Top Secret 😷" : "pdf|stp|12", "Draft 👀" : "pdf|stp|13", "AsIs 🤏" : "pdf|stp|1", get_text('BACK', lang_code) : "pdf"},
        "trade" : { get_text('BACK', lang_code) : "pdf" },
        "stampA" : { get_text('STAMP_COLOR', lang_code) : "roxybasicneedbot", "Red ❤️" : "#spP|{}|r", "Blue 💙" : "#spP|{}|b", "Green 💚" : "#spP|{}|g", "Yellow 💛" : "#spP|{}|c1",
            "Pink 💜" : "#spP|{}|c2", "Hue 💚" : "#spP|{}|c3", "White 🤍" : "#spP|{}|c4", "Black 🖤" : "#spP|{}|c5", get_text('BACK', lang_code) : "pdf|stp" }}
    PROGRESS = {"progress" : get_text('PROGRESS', lang_code) , "upFileCB" : {f"📤 .. {get_text('UPLOADING', lang_code)} .. 📤" : "roxybasicneedbot"}, "cbPRO_D" : ["📤 {:.2f}% 📤", get_text('CANCEL', lang_code)], "cbPRO_U" : ["📤 {:.2f}% 📤", get_text('CANCEL', lang_code)], "workInP" : get_text('W_I_P', lang_code)}
    GENERATE = {"noQueue" : get_text('NO_QUEUE', lang_code), "noImages" : get_text('NO_IMG', lang_code), "currDL" : get_text('DL_IMG', lang_code), "geting" : get_text('GEN_PDF', lang_code), "getFileNm" : get_text('REN_PDF', lang_code), "deleteQueue" : get_text('DLT_QUEUE', lang_code), "getingCB" : {get_text('GEN_CB', lang_code) : "roxybasicneedbot"},}
    DOCUMENT = {
        "replyCB" : { get_text('AIO', lang_code) : "aio" , get_text('SINGLE_USE', lang_code) : "pdf", get_text('CLOSE', lang_code) : "close|all" }, "_replyCB" : PDF_MESSAGE['pdf_button'],
        "reply" : PDF_MESSAGE['pdf'], "upFile" : get_text('START_UPLOAD', lang_code), "process" : get_text('PROCESSING', lang_code), "inWork" : get_text('W_I_P', lang_code), "big" : get_text('BIG', lang_code),
        "download" : get_text('START_DOWNL', lang_code), "refresh" : { get_text('REFRESH', lang_code) : "{}" }, "dlImage" : get_text('DL_IMG', lang_code), "noAPI" : get_text('NO_API', lang_code), "error" : get_text('ERROR', lang_code),
        "takeTime" : get_text('TAKE_TIME', lang_code), "fromFile" : get_text('CONVERTED', lang_code), "unsupport" : get_text('UNSUPPORT', lang_code), "cancelCB" : { get_text('CANCEL', lang_code) : "close|me" }, "generate" : { get_text('GENERATE', lang_code) : "generate" },
        "generateRN" : { get_text('GENERATE', lang_code) : "generate", get_text('RENAME', lang_code) : "generateREN" }, "setHdImg" : get_text('HD', lang_code), "setDefault" : { get_text('BACK_DEFAULT', lang_code) : "close|hd" }, "useDOCKER" : get_text('NOT_DOKR', lang_code),
        "bigCB" : { get_text('BIG_SUPP', lang_code) : "https://github.com/RoxyBasicNeedBot" }, "imageAdded" : get_text('IMG_ADDED', lang_code)}
    AIO = {
        "true" : get_text('TRUE', lang_code), "false" : get_text('FALSE', lang_code), "aio" : get_text('PASS_REQUIRED', lang_code), "waitPASS" : get_text('WAIT_TXT', lang_code), "passMSG" : get_text('AIO_QN', lang_code),
        "aio_button" : {get_text('HELP', lang_code) :"roxybasicneedbot|aioInput", get_text('YES', lang_code):"aioInput|enc", get_text('NO', lang_code) :"aioInput|dec", get_text('MOVE', lang_code) :"aioInput|dec" },
        "out_button" : { get_text('META', lang_code) : "roxybasicneedbot|aio|met", get_text('PREVIEW', lang_code) : "roxybasicneedbot|aio|pre", get_text('COMPRESS', lang_code): "roxybasicneedbot|aio|com", get_text('B_TEXT_T', lang_code) : "roxybasicneedbot|aio|txt", get_text('ROTATE', lang_code) : "roxybasicneedbot|aio|rot", get_text('FORMAT', lang_code) : "roxybasicneedbot|aio|for",
            get_text('ENCRYPT', lang_code) : "roxybasicneedbot|aio|enc", get_text('WATERMARK', lang_code) : "roxybasicneedbot|aio|wat", get_text('RENAME', lang_code) : "roxybasicneedbot|aio|rnm", get_text('BACK', lang_code) : "aio", get_text('PROCEED', lang_code) : "processAIO" },
        "out_values": ["aio|met|{F}", "aio|pre|{F}", "aio|com|{F}", "aio|txt|{F}", "aio|rot|{F}", "aio|for|{F}", "aio|enc|{F}", "aio|wat|{F}", "aio|rnm|{F}" ]}
    gDOCUMENT = { "admin" : get_text('ADMIN_ONLY', lang_code), "notDOC" : get_text('NOT_DOC', lang_code), "Gadmin" : get_text('G_ADMIN', lang_code), "adminO" : get_text('NOT_YOUR', lang_code) }
    gDOCUMENT.update(DOCUMENT)
    noHelp = get_text('WASTE', lang_code)
    URL = {
        "notPDF" : get_text('CODEC', lang_code), "close" : { get_text('CLOSE', lang_code) : "close|all" }, "get" : { get_text('GET_TG_PDF', lang_code) : "getFile"}, "error" : get_text('ERROR', lang_code), "view" : get_text('VIEW_ONLY', lang_code),
        "done" : get_text('DONE', lang_code), "_error_" : get_text('TEXT_REPLY', lang_code), "openCB" : {get_text('OPEN_BROW', lang_code) : "{}"}, "_error" : get_text('ERROR', lang_code),"_get" : get_text('TG_PDF', lang_code) }
    getFILE = {
        "wait" : get_text('CHECK', lang_code), "inWork" : DOCUMENT['inWork'], "big" : get_text('BIG', lang_code), "dl" : {f"📥 ..{get_text('DOWNLOADING', lang_code)}.. 📥" : "roxybasicneedbot"},
        "up" : {f"📤 ..{get_text('UPLOADING', lang_code)}..  📤" : "roxybasicneedbot"}, "complete" : { get_text('COMPLETED', lang_code) : f"{str(settings.SOURCE_CODE)}"}}
    cbAns = [get_text('NOT_DEV', lang_code), get_text('STILL_ERROR', lang_code), get_text('CANCELED', lang_code), get_text('NOT_ENCRYPT', lang_code), get_text('NOTHING_OFF', lang_code) , get_text('COMPLETED', lang_code) ]
    LINK = {
        "gen" : get_text('GENERATING', lang_code), "no" : get_text('UNKNOWN_ERROR', lang_code), "notify" : get_text('NOTIFY', lang_code), "_gen" : get_text('URL_PROCES', lang_code), "type" : get_text('URL_TYPE', lang_code),
        "notify_pvt" : { get_text('NOTIFY_CB', lang_code) : "link-pvt-ntf", get_text('MUTE_CB', lang_code) : "link-pvt-mut"}, "notify_pub" : { get_text('NOTIFY_CB', lang_code) : "link-pbc-ntf", get_text('MUTE_CB', lang_code) : "link-pbc-mut"},
        "typeBTN" : { get_text('PUBLIC', lang_code) : "link-pub", get_text('PRIVATE', lang_code) : "link-pvt" }, "link" : get_text('GEN_LINK', lang_code), "error" : get_text('ERROR_', lang_code) }
    INDEX = {
        "rot360" : get_text('YOUR_ERROR', lang_code), "ocrError" : get_text('OWN_RES', lang_code), "notEncrypt": get_text('NOT_ENCRYPT', lang_code), "largeNo" : get_text('MORE_PGS', lang_code), "inWork" : get_text('W_I_P', lang_code), "process" : get_text('PROCESSING', lang_code),
        "pyromodASK_1" : get_text('ASK_PASS', lang_code), "pyromodASK_2" : get_text('ASK_NAME', lang_code), "pyromodASK_3" : get_text('ASK_MERGE', lang_code), "download" : get_text('START_DOWNL', lang_code), "button" : { get_text('CANCEL', lang_code) : "close|me" }, "error" : get_text('ERROR', lang_code),
        "decrypt_error" : get_text('PASS_ERROR', lang_code), "cantCompress" : get_text('CANT_COMP', lang_code), "completed" : get_text('DL_COMPLETED', lang_code), "upload" : get_text('START_UPLOAD', lang_code), "encrypt_caption" : get_text('ENCRYPT_CAPT', lang_code),
        "rename_caption" : get_text('RENAME_CAPT', lang_code), "exit" : get_text('EXIT', lang_code), "compress_caption" : get_text('COMP_CAPT', lang_code),
        "askImage" : get_text('ASK_PG', lang_code), "pdfToImgError" : get_text('ASK_PG_ERROR', lang_code),
        "_total" : get_text('TOTAL_PG', lang_code), "_canceledAT" : get_text('CANCEL_AT', lang_code), "_upload" : get_text('UPLOADING_AL', lang_code), "finished" : get_text('COMPLETED_SUCC', lang_code), "cancelCB" : get_text('EXIT', lang_code),
        "_cancelCB" : {get_text('CANCEL', lang_code) : "close|P2I"}, "_canceledCB" : {get_text('CANCELED_CB', lang_code) : "close|P2IDONE"}, "_completed" : {get_text('COMPLETED', lang_code) : "close|P2ICOMP"},
        "sizeLoad" : get_text('SIZE_LOAD', lang_code), "mergeDl" : get_text('MERGE_DL', lang_code), "merge" : get_text('START_MERGE', lang_code), "watermark_txt" : get_text('WATERMARK_TXT', lang_code), "watermark_pdf" : get_text('WATERMARK_PDF', lang_code),
        "watermark_img" : get_text('WATERMARK_IMG', lang_code), "adding_wa" : get_text('ADD_WATERMARK', lang_code), "readAgain" : get_text('READ_AGAIN', lang_code), "zipTAR" : get_text('ZIP_CONVERT', lang_code), "aio" : get_text('AIO_PROCESS', lang_code),
        "pyromodASK_4" : get_text('ASK_PG_', lang_code), "pdfSplitError" : get_text('ASK_PGERROR', lang_code)}
    INLINE = {
        "search" : get_text('SEARCH', lang_code), "openBot" : get_text('OPEN_BOT', lang_code), 'query' : get_text('TOTAL', lang_code), 'lang_t' : get_text('SET_LANG', lang_code), "lang_d" : get_text('LANG', lang_code), 'caption' : get_text('INLINE_CAP', lang_code),
        "lang_b" : { get_text('SELECT_LANG', lang_code) : "roxybasicneedbot" }, 'sear_t' : get_text('SEARCH_PDF', lang_code), 'sear_d' : get_text('SEARCH_DES', lang_code), 'noDB' : '🏃‍♂️🏃‍♂️', 'refer_t' : get_text('REFER_T', lang_code),
        'min' : get_text('MIN_SEARCH', lang_code), 'process' : get_text('PROCESSING', lang_code), 'nothing' : get_text('NO_RESULT', lang_code), "select" : get_text('GET_PDF', lang_code), 'description' : get_text('INLINE_DES', lang_code),
        'cbNotU' : BAN['cbNotU'], 'old' : get_text('OLD_QUEUE', lang_code), 'inWork' : get_text('W_I_P', lang_code), 'edit' : [get_text('GET_PDF', lang_code), get_text('SEARCH_PDF', lang_code), get_text('OPEN_BOT', lang_code)], 'refer_d' : get_text('REFER_D', lang_code),}
    BETA = {"cant": get_text('CANT_USE', lang_code), 'refer': get_text('REFER', lang_code), 'nowbeta': get_text('NOW_BETA', lang_code), 'nownotbeta': get_text('NOW_NOT_BETA', lang_code) }
    pdf2TXT = {
        "upload" : DOCUMENT['upFile'], "exit" : get_text('EXIT', lang_code), "nothing" : get_text('NOTHING', lang_code), "TEXT" : get_text('TEXT2PDF', lang_code), "start" : get_text('TEXT2PDF_S', lang_code),  "askC" : get_text('TEXT2PDF_P', lang_code),
        "fifteen" : { "{}" : "roxybasicneedbot", "1" : "{}|1", "2" : "{}|2", "3" : "{}|3", "4" : "{}|4", "5" : "{}|5", "6" : "{}|6", "7" : "{}|7",
        "8" : "{}|8", "9" : "{}|9", "10" : "{}|10","11" : "{}|11", "12" : "{}|12", "13" : "{}|13", "14" : "{}|14", "15" : "{}|15", 
        get_text('USE_DEFAULT', lang_code) : "{}|_"}, "askT" : get_text('TEXT2PDF_T', lang_code), "size_btn" : {get_text('SELECT_SCALE', lang_code) : "roxybasicneedbot", "1" : "t2p|1", "2" : "t2p|2", get_text('CLOSE', lang_code) : "close|me"},
        "six_" : { "{}" : "roxybasicneedbot", "1" : "{}|1:", "2" : "{}|2:", "3" : "{}|3:", "4" : "{}|4:", "5" : "{}|5:", "+" : "{}|6:", get_text('USE_DEFAULT', lang_code) : "{}|_:"},
        "six" : { "{}" : "roxybasicneedbot", "1" : "{}|1", "2" : "{}|2", "3" : "{}|3", "4" : "{}|4", "5" : "{}|5", "6" : "{}|6", get_text('USE_DEFAULT', lang_code) : "{}|_"},
        "font_btn" : { get_text('BACK', lang_code) : "pdf" },
        "error" : get_text('ERROR', lang_code) }
    HELP = {}
    
    RESTART = { "msg" : get_text('RESTART', lang_code), "btn" : { get_text('CLOSE', lang_code) : "close|mee" }}
    HOME = {
        "HomeA" : get_text('HOME_A', lang_code), "HomeB" : get_text('HOME_B', lang_code), "HomeC" : get_text('HOME_C', lang_code), "HomeD" : get_text('HOME_D', lang_code), "search" : [get_text('SEARCH_PDF', lang_code), get_text('BETA_MSG', lang_code)],
        "HomeACB" : { get_text('SETTINGS', lang_code) : "Home|B", get_text('LANGUAGE', lang_code) : "set|lang", get_text('HELP', lang_code) : "Home|C", get_text('CHANNEL', lang_code) : f"{str(settings.OWNED_CHANNEL)}",
                     get_text('SOURCE', lang_code) : f"{str(settings.SOURCE_CODE)}", get_text('ADD_GROUP', lang_code) : "https://t.me/{}?startgroup=True" },
        "HomeAdminCB" : { get_text('SETTINGS', lang_code) : "Home|B", get_text('LANGUAGE', lang_code) : "set|lang", get_text('HELP', lang_code) : "Home|C",
            "🗽 STATUS 🗽" : f"status|home", get_text('ADD_GROUP', lang_code) : "https://t.me/{}?startgroup=True", get_text('CLOSE', lang_code) : "close|mee" },
        "HomeBCB" : { get_text('THUMB', lang_code) : "set|thumb", get_text('NAME', lang_code) : "set|fname", get_text('API', lang_code) : "set|api", get_text('CAPTION', lang_code) : "set|capt", get_text('BACK_HOME', lang_code) : "Home|B2A" },
        "HomeCCB" : { get_text('BACK_HOME', lang_code) : "Home|A", get_text('INSTRUCTIONS', lang_code) : "Home|D" }, "HomeDCB" : { get_text('HELP', lang_code) : "Home|C", get_text('BACK_HOME', lang_code) : "Home|A" } }
    HomeG = { "HomeACB" : { get_text('LANGUAGE', lang_code) : "set|lang", get_text('HELP', lang_code) : "Home|C", get_text('CHANNEL', lang_code) : f"{str(settings.OWNED_CHANNEL)}",
        get_text('SOURCE', lang_code) : f"{settings.SOURCE_CODE}", get_text('CLOSE', lang_code) : "close|mee" }, "HomeA" : get_text('HOME_A', lang_code)}
    SETTINGS = {
        "lang" : get_text('SELECT_LANG', lang_code), "default" : [get_text('DEFAULT', lang_code), get_text('CUSTOM', lang_code)], "cant" : get_text('CANT_USE', lang_code), "wait" : { get_text('WAIT', lang_code) : "roxybasicneedbot" },
        "feedbtn" : { get_text('REPORT', lang_code) : settings.REPORT }, "chgLang" : { get_text('SET_LANG', lang_code) : "roxybasicneedbot"}, "askApi" : get_text('ASK_API', lang_code),
        "result" : [get_text('RES_FAIL', lang_code), get_text('RES_SUCCESS', lang_code)], "waitApi" : { get_text('OPEN_BROW', lang_code) : "https://www.convertapi.com/a/signin" }, "error" : get_text('ERROR_DB', lang_code),
        "back" : [{ get_text('BACK_HOME', lang_code) : "Home|B2S" }, { get_text('BACK_HOME', lang_code) : "Home|B2A" }], "feedback" : get_text('LANG_FEED', lang_code), "ask" : [get_text('SEND', lang_code), get_text('SEND_FAST', lang_code)],
        "thumb" : [{ get_text('SET_THUMB', lang_code) : "roxybasicneedbot", get_text('ADD', lang_code) : "set|thumb+", get_text('BACK_HOME', lang_code) : "Home|B"},
                   { get_text('SET_THUMB', lang_code) : "roxybasicneedbot", get_text('CHANGE', lang_code) : "set|thumb+", get_text('DELETE', lang_code) : "set|thumb-", get_text('BACK_HOME', lang_code) : "Home|B2S"}],
        "fname" : [{ get_text('SET_NAME', lang_code) : "roxybasicneedbot", get_text('ADD', lang_code) : "set|fname+", get_text('BACK_HOME', lang_code) : "Home|B2S"},
                   {get_text('SET_NAME', lang_code) : "roxybasicneedbot", get_text('CHANGE', lang_code) : "set|fname+", get_text('DELETE', lang_code) : "set|fname-", get_text('BACK_HOME', lang_code) : "Home|B2S"}],
        "api" : [{ get_text('SET_API', lang_code) : "roxybasicneedbot", get_text('ADD', lang_code) : "set|api+", get_text('BACK_HOME', lang_code) : "Home|B2S"},
                 { get_text('SET_API', lang_code) : "roxybasicneedbot", get_text('CHANGE', lang_code) : "set|api+", get_text('DELETE', lang_code) : "set|api-", get_text('BACK_HOME', lang_code) : "Home|B2S"}],
        "capt" : [{ get_text('SET_CAPT', lang_code) : "roxybasicneedbot", get_text('ADD', lang_code) : "set|capt+", get_text('BACK_HOME', lang_code) : "Home|B2S"},
                  { get_text('SET_CAPT', lang_code) : "roxybasicneedbot", get_text('CHANGE', lang_code) : "set|capt+", get_text('DELETE', lang_code) : "set|capt-", get_text('BACK_HOME', lang_code) : "Home|B2S"}] }
    
    _START_CMD = "𝘞𝘦𝘭𝘤𝘰𝘮𝘦 𝘵𝘰 𝘵𝘩𝘦 𝘣𝕠𝘵 👋"
    _TXT2PDF_CMD = "📝 𝘊𝘳𝘦𝘢𝘵𝘦 𝘗𝘋𝘍 𝘧𝘳𝘰𝘮 𝘵𝘦𝘹𝘵"
    _CANCEL_CMD = "🚫 𝘊𝘢𝘯𝘤𝘦𝘭 𝘤𝘶𝘳𝘳𝘦𝘯𝘵 𝘰𝘱𝘦𝘳𝘢𝘵𝘪𝘰𝘯"
    _DELETE_CMD = "🗑️ 𝘋𝘦𝘭𝘦𝘵𝘦 𝘤𝘶𝘳𝘳𝘦𝘯𝘵 𝘧𝘪𝘭𝘦𝘴"
    _BETA_CMD = "✨ 𝘈𝘤𝘤𝘦𝘴𝘴 𝘣𝘦𝘵𝘢 𝘧𝘦𝘢𝘵𝘶𝘳𝘦s"
    _HD_CMD = "🖼️ 𝘎𝘦𝘵 𝘏𝘋 𝘪𝘮𝘢𝘨𝘦"
    
    BOT_COMMAND = { 
        "start" : _START_CMD, 
        "txt2pdf" : _TXT2PDF_CMD,
        "cancel" : _CANCEL_CMD,
        "delete" : _DELETE_CMD,
        "beta" : _BETA_CMD,
        "hd" : _HD_CMD
    }
    
    _STOP_CB = { get_text('_STOP_CB_', lang_code) : "ping_me" }

    _map = {
        'HOME': locals().get('HOME', {}),
        'HomeG': locals().get('HomeG', {}),
        'SETTINGS': locals().get('SETTINGS', {}),
        'BOT_COMMAND': locals().get('BOT_COMMAND', {}),
        'STATUS_MSG': locals().get('STATUS_MSG', {}),
        'feedbackMsg': locals().get('feedbackMsg', {}),
        'BAN': locals().get('BAN', {}),
        'PDF_MESSAGE': locals().get('PDF_MESSAGE', {}),
        'BUTTONS': locals().get('BUTTONS', {}),
        'PROGRESS': locals().get('PROGRESS', {}),
        'GENERATE': locals().get('GENERATE', {}),
        'DOCUMENT': locals().get('DOCUMENT', {}),
        'AIO': locals().get('AIO', {}),
        'gDOCUMENT': locals().get('gDOCUMENT', {}),
        'noHelp': locals().get('noHelp', ""),
        'URL': locals().get('URL', {}),
        'getFILE': locals().get('getFILE', {}),
        'cbAns': locals().get('cbAns', []),
        'LINK': locals().get('LINK', {}),
        'INDEX': locals().get('INDEX', {}),
        'INLINE': locals().get('INLINE', {}),
        'BETA': locals().get('BETA', {}),
        'pdf2TXT': locals().get('pdf2TXT', {}),
        'HELP': locals().get('HELP', {}),
        'RESTART': locals().get('RESTART', {}),
        '_STOP_CB': _STOP_CB,
        '_STOP_CB_': _STOP_CB,
        '_STOP': get_text('_STOP', lang_code),
        '_BETA_MESSAGE': get_text('_BETA_MESSAGE', lang_code),
        '_SELECT_HEAD_FONT': get_text('_SELECT_HEAD_FONT', lang_code),
        '_SELECT_PARA_FONT': get_text('_SELECT_PARA_FONT', lang_code),
        '_SELECT_COLOR': get_text('_SELECT_COLOR', lang_code),
        '_SELECT_BG_COLOR': get_text('_SELECT_BG_COLOR', lang_code),
        '_W_I_P': get_text('W_I_P', lang_code),
        'W_I_P': get_text('W_I_P', lang_code)
    }
    if var_name in _map:
        return _map[var_name]
    up = var_name.upper()
    if up in _map:
        return _map[up]
    low = var_name.lower()
    if low in _map:
        return _map[low]
    clean = var_name.lstrip('_')
    if clean in _map:
        return _map[clean]
    if f'_{var_name}' in _map:
        return _map[f'_{var_name}']
    return {}
