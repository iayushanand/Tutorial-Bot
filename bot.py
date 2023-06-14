import revolt
import asyncio

class RevoltBot(revolt.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user.name}")
    
    async def on_message(self, message: revolt.Message):
        if message.content.startswith(".hello"):
            author = message.author
            await message.reply(f"Hi {author.mention}")
        
        if message.content.startswith(".ping"):
            await message.reply("Pong!")

async def main():
    async with revolt.utils.client_session() as session:
        client = RevoltBot(session = session, token = "your-bot-token")
        await client.start()

if __name__ == "__main__":
    asyncio.run(main())
