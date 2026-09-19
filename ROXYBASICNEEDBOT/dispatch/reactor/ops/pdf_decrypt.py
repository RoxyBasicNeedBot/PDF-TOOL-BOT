# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import fitz
from tracer import tracer

async def decryptPDF(input_file: str, password: str, cDIR: str) -> (bool, str):
    try:
        """
        Decryption of a PDF file involves removing the encryption that has been applied to the
        file so that it can be read and accessed by an authorized user.

        parameter:
            input_file : Here is the path of the file that the user entered
            password   : Password entered by the user for pdf encryption
            cDIR       : This is the location of the directory that belongs to the specific user.

        return:
            bool        : Return True when the request is successful
            output_path : This is the path where the output file can be found.
        """
        output_path = f"{cDIR}/outPut.pdf"
        logger.debug(f"🔍 Opening encrypted PDF: {input_file}")
        with fitz.open(input_file) as iNPUT:
            logger.debug(f"📄 PDF opened, is_encrypted: {iNPUT.is_encrypted}")
            
            # Try authenticating with user password first (matches our encryption method)
            # During encryption, we set owner_pw="nabil" and user_pw=user_password
            # PyMuPDF allows both passwords to decrypt, but we try user password first
            logger.debug(f"🔑 Trying authentication with user password: '{password}'")
            auth_result = iNPUT.authenticate(f"{password}")
            logger.debug(f"{'✅' if auth_result else '❌'} User password authentication: {auth_result}")
            
            # If that fails, try the hardcoded owner password for backward compatibility
            # with files encrypted using the old method
            if not auth_result:
                logger.debug(f"🔑 User password failed, trying owner password: 'nabil'")
                auth_result = iNPUT.authenticate("nabil")
                logger.debug(f"{'✅' if auth_result else '❌'} Owner password authentication: {auth_result}")
            
            if not auth_result:
                logger.error(f"❌ Both authentication attempts failed for password '{password}'")
                return False, "Incorrect password. Authentication failed."
            
            logger.debug(f"✅ Authentication successful! Saving decrypted PDF to: {output_path}")
            # Save decrypted PDF
            iNPUT.save(output_path)
            logger.debug(f"💾 Decrypted PDF saved successfully")
        return True, output_path

    except Exception as e:
        logger.error(f"🐞 Error: {e}", exc_info=True)
        return False, str(e)
