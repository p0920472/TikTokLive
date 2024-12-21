import asyncio

from TikTokLive import TikTokLiveClient
from TikTokLive.client.logger import LogLevel
from TikTokLive.events import ConnectEvent, GiftEvent, CommentEvent

client: TikTokLiveClient = TikTokLiveClient(
    unique_id="@yudi.syahputrah"
)


@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    client.logger.info(f"Connected to @{event.unique_id}!")

@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    # client.logger.info("Received a gift!")

    # Can have a streak and streak is over
    if event.gift.streakable and not event.streaking:
        print(f"{event.user.unique_id} sent to {event.to_user.unique_id} {event.repeat_count}x \"{event.gift.name}\" value {event.value}")

    # Cannot have a streak
    elif not event.gift.streakable:
        print(f"{event.user.unique_id} sent to {event.to_user.unique_id} \"{event.gift.name}\" value {event.value}")
        

@client.on(CommentEvent)
async def on_comment(event: CommentEvent):
    # client.logger.info("Received a gift!")
    # Cannot have a streak
    print(f"Comment \"{event.user.unique_id}\" sent \"{event.comment}\"")
    

async def check_loop():
    # Run 24/7
    while True:

        # Check if they're live
        while not await client.is_live():
            client.logger.info("Client is currently not live. Checking again in 60 seconds.")
            await asyncio.sleep(60)  # Spamming the endpoint will get you blocked

        # Connect once they become live
        client.logger.info("Requested client is live!")
        await client.connect()


if __name__ == '__main__':
    client.logger.setLevel(LogLevel.INFO.value)
    # asyncio.run(check_loop())
    client.run()
