#!/usr/bin/env python3

import configparser
import asyncio
import sys
import os
import argparse
from telegram import Bot
from telegram.error import TelegramError

def init():
    logo = r"""  _______ ______ _      ______ _______ _____ ________     __
 |__   __|  ____| |    |  ____|__   __|_   _|  ____\ \   / /
    | |  | |__  | |    | |__     | |    | | | |__   \ \_/ / 
    | |  |  __| | |    |  __|    | |    | | |  __|   \   /  
    | |  | |____| |____| |____   | |   _| |_| |       | |   
    |_|  |______|______|______|  |_|  |_____|_|       |_|  
    
                                        By: 0xdead4f V1.0.0
                                        """

    print(logo)
    parser = argparse.ArgumentParser(description='Telegram Message Sender')
    subparsers = parser.add_subparsers(dest='mode', help='Choose the mode of operation')

    parser_text = subparsers.add_parser('text', help='Send a text message')
    parser_text.add_argument('-f', '--file', type=str, help='Path to a file contain the message', default="NO_FILE")
    parser_text.add_argument('-m', '--message', type=str, help='Message to send', default="",dest="text")
    parser_text.add_argument('-tid', '--thread-id', type=str, help='Input a thread ID', default="",dest="tid")
    parser_text.add_argument('-cid', '--chat-id', type=str, help='Optional Chat ID', default=False, dest='chat_id')
    parser_text.add_argument('--silent', help='Silent Mode', default=False, dest='silent',action="store_true")

    parser_document = subparsers.add_parser('document', help='Send a document')
    parser_document.add_argument('-f', '--file', type=str, help='Path to a file', default="NO_FILE")
    parser_document.add_argument('-m', '--message', type=str, help='Message to send with the document', default="",dest="text")
    parser_document.add_argument('-tid', '--thread-id', type=str, help='Optional Input a thread ID', default="",dest="tid")
    parser_document.add_argument('-cid', '--chat-id', type=str, help='Optional Chat ID', default=False, dest='chat_id')
    parser_document.add_argument('--silent', type=str, help='Silent Mode', default=False, dest='silent')

    args = parser.parse_args()

    config_file = os.path.expanduser('~/.config/teletify/config.ini')
    config = configparser.ConfigParser()
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file not found: {config_file}")
    
    config.read(config_file)
    
    try:
        bot_api_key = config['telegram']['bot_api_key']
        default_chat_id = config['telegram']['default_chat_id']
    except KeyError as e:
        raise KeyError(f"Missing key in configuration file: {e}")

    return args,bot_api_key, default_chat_id

async def sendText(args,chat_id,bot_api_key):
    if args.chat_id != False:
        chat_id = args.chat_id
    bot = Bot(token=bot_api_key)

    if not sys.stdin.isatty():
        args.text = sys.stdin.read().strip()
    try:
        if args.text != "":
            sent_message = await bot.send_message(chat_id=chat_id, text=args.text, message_thread_id=args.tid)
            if args.silent != True:
                print(f"Message sent: {sent_message}")
            else:
                print("Message Succesfully sent!")
        if args.file and args.file != "NO_FILE":
            message_text = ""
            with open(args.file, 'r') as file:
                file_content = file.read().strip()
                message_text += f"{file_content}\n"
            sent_message = await bot.send_message(chat_id=chat_id, text=args.text, message_thread_id=args.tid)
            if args.silent != True:
                print(f"Message sent: {sent_message}")
            else:
                print("Message Succesfully sent!")
    except Exception as e:
        print(f"Error sending message: {e}")

async def sendDocument(args, chat_id, bot_api_key):
    if args.chat_id != False:
        chat_id = args.chat_id
    bot = Bot(token=bot_api_key)

    try:
        if args.file and args.file != "NO_FILE":
            with open(args.file, 'rb') as file:
                sent_message = await bot.send_document(chat_id=chat_id, document=file, caption=args.text, message_thread_id=args.tid)
                if args.silent != True:
                    print(f"Document sent: {sent_message}")
                else:
                    print("Document Successfully sent!")
    except TelegramError as e:
        print(f"Error sending document: {e}")

if __name__ == '__main__':
    args,bot_api_key, default_chat_id = init()
    if args.mode == "text":
        asyncio.run(sendText(args,default_chat_id,bot_api_key))
    elif args.mode == "document":
        asyncio.run(sendDocument(args,default_chat_id,bot_api_key))


