# joiner.py

import json
import time
import os
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError, UserPrivacyRestrictedError
from telethon.tl.functions.messages import ImportChatInviteRequest
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class TelegramGroupJoiner:
    def __init__(self, config_path='config.json', session_folder='sessions'):
        self.config = self.load_config(config_path)
        self.api_id = self.config['api_id']
        self.api_hash = self.config['api_hash']
        self.phone_number = self.config['phone_number']
        self.invite_links = self.config['invite_links']
        self.session_folder = session_folder
        os.makedirs(self.session_folder, exist_ok=True)
        self.client = TelegramClient(os.path.join(self.session_folder, 'session_name'), self.api_id, self.api_hash)

    @staticmethod
    def load_config(path):
        with open(path, 'r') as f:
            return json.load(f)

    async def join_group(self, invite_link):
        try:
            await self.client(ImportChatInviteRequest(invite_link))
            print(f"{Fore.GREEN}Successfully joined {invite_link}{Style.RESET_ALL}")
        except FloodWaitError as e:
            print(f"{Fore.YELLOW}Rate limited. Sleeping for {e.seconds} seconds.{Style.RESET_ALL}")
            await asyncio.sleep(e.seconds)
        except UserPrivacyRestrictedError:
            print(f"{Fore.RED}Failed to join {invite_link}: Privacy restrictions.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Failed to join {invite_link}: {e}{Style.RESET_ALL}")

    async def join_all_groups(self):
        for link in self.invite_links:
            await self.join_group(link)
            await asyncio.sleep(5)

    async def main(self):
        await self.client.start(phone=self.phone_number)
        await self.join_all_groups()

if __name__ == '__main__':
    import asyncio
    joiner = TelegramGroupJoiner()
    with joiner.client:
        joiner.client.loop.run_until_complete(joiner.main())
