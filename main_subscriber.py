from main.subscribers.subscriber import Subscriber
import asyncio

subscriber = Subscriber()
async def main():
    await asyncio.gather(subscriber.subscribeOnCalculateTopic(), subscriber.subscribeOnTextEditTopic(),  subscriber.subscribeOnFileEditTopic())

asyncio.run(main())