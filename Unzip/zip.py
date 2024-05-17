import os
import time
import shutil
import zipfile
import tempfile
from pyrogram import Client, filters




@Client.on_message(filters.document)
async def handle_file(client, message):
    document = message.document
    if document.mime_type == 'application/zip':
        try:
            download_message = await message.reply("Downloading the ZIP file...")
            start = time.time()
            file_path = await message.download(file_name=document.file_name, progress=progress_for_pyrogram, progress_args=("Downloading...", download_message, start))
            await download_message.edit("Extracting the ZIP file...")

            try:
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    unzip_dir = os.path.join(tempfile.gettempdir(), 'unzipped')
                    os.makedirs(unzip_dir, exist_ok=True)
                    zip_ref.extractall(unzip_dir)
                    await download_message.edit("Sending the extracted files...")

                    for root, _, files in os.walk(unzip_dir):
                        for file_name in files:
                            file_path = os.path.join(root, file_name)
                            await client.send_document(
                                chat_id=message.chat.id,
                                document=file_path,
                                progress=progress_for_pyrogram,
                                progress_args=("Uploading...", download_message, start)
                            )
                
                os.remove(file_path)
                shutil.rmtree(unzip_dir)
                await download_message.edit("All files have been extracted and sent successfully.")
            except zipfile.BadZipFile:
                await download_message.edit("The file you sent is not a valid ZIP file.")
        except Exception as e:
            await message.reply(f"An error occurred: {e}")
    else:
        await message.reply("Please send a ZIP file.")

  
