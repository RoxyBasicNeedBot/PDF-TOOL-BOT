# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import fitz
from tracer import tracer
from sentinel import *


async def zipTarPDF(
    input_file: str, cDIR: str, callbackQuery, dlMSG, imageList: list, text: str
) -> (bool, str):
    """ """
    try:
        cancel = await util.createBUTTON(btn=text["_cancelCB"])
        canceled = await util.createBUTTON(btn=text["_canceledCB"])
        completed = await util.createBUTTON(btn=text["_completed"])

        fileType = "zip" if callbackQuery.data.startswith("#p2img|zip") else "tar"

        with fitz.open(input_file) as doc:
            directory = f"{cDIR}/pgs"
            os.mkdir(directory)
            number_of_pages = doc.page_count
            if callbackQuery.data.endswith("A") and number_of_pages <= 50:
                imageList = list(range(1, number_of_pages + 1))
            elif callbackQuery.data.endswith("A"):
                imageList = list(range(1, 50))

            await dlMSG.edit(
                text=text["_total"].format(len(imageList)), reply_markup=cancel
            )
            mat = fitz.Matrix(2, 2)
            convertedPages = 0

            for i in imageList:
                page = doc.load_page(i - 1)
                pix = page.get_pixmap(matrix=mat)
                convertedPages += 1
                if convertedPages % 5 == 0:
                    await dlMSG.edit(
                        text="`processing {}/{}` 😎".format(
                            convertedPages, len(imageList)
                        ),
                        reply_markup=cancel,
                    )
                    if not await work.work(callbackQuery, "check", False):
                        return True, await dlMSG.edit(
                            text=text["_canceledAT"].format(
                                convertedPages, len(imageList)
                            ),
                            reply_markup=canceled,
                        )
                pix.save(f"{cDIR}/pgs/{i}.jpg", jpg_quality=85)

            output_path = f"{cDIR}/zipORtar"

            if fileType == "zip":
                path = shutil.make_archive(output_path, "zip", directory)
            elif fileType == "tar":
                path = shutil.make_archive(output_path, "tar", directory)

        return True, path

    except Exception as e:
        shutil.rmtree(f"{cDIR}/pgs")
        logger.error(f"🐞 Error: {e}", exc_info=True)
        return False, str(e)
