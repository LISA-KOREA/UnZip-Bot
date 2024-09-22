# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/UnZip-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/UnZip-Bot




import os
import time
import shutil
import zipfile
import tempfile
from pyrogram import Client, filters
from Unzip.progress import progress_for_pyrogram, humanbytes, TimeFormatter
import asyncio

active_tasks = {}

@Client.on_message(filters.document)
async def handle_file(client, message):
    user_id = message.from_user.id
    document = message.document

    if document.mime_type == 'application/zip':
        download_message = None
        file_path = None
        unzip_dir = None
        try:
            download_message = await message.reply("⏳ Downloading the ZIP file...")
            start = time.time()

            file_path = await message.download(
                file_name=document.file_name,
                progress=progress_for_pyrogram,
                progress_args=("⬇️ Downloading...", download_message, start)
            )

            await download_message.edit("⏳ Extracting the ZIP file...")

            unzip_dir = os.path.join(tempfile.gettempdir(), f'unzipped_{user_id}')
            os.makedirs(unzip_dir, exist_ok=True)

            task = asyncio.create_task(extract_and_send_files(client, message, file_path, unzip_dir, download_message, start))
            active_tasks[user_id] = task

            await task

        except zipfile.BadZipFile:
            await download_message.edit("❌ The file you sent is not a valid ZIP file.")
        except asyncio.CancelledError:
            await download_message.edit("❌ Unzipping has been cancelled.")
        except Exception as e:
            await download_message.edit(f"❌ An error occurred: {e}")
        finally:
            if file_path and os.path.exists(file_path):
                os.remove(file_path)
            if unzip_dir and os.path.exists(unzip_dir):
                shutil.rmtree(unzip_dir)
            active_tasks.pop(user_id, None)

    else:
        await message.reply("⚠️ Please send a valid ZIP file.")


async def extract_and_send_files(client, message, file_path, unzip_dir, download_message, start):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(unzip_dir)

    await download_message.edit("⬆️ Sending the extracted files...")

    for root, _, files in os.walk(unzip_dir):
        for file_name in files:
            extracted_file_path = os.path.join(root, file_name)
            await client.send_document(
                chat_id=message.chat.id,
                document=extracted_file_path,
                progress=progress_for_pyrogram,
                progress_args=("⬆️ Uploading...", download_message, start)
            )

    await download_message.edit("✅ All files have been extracted and sent successfully.")


