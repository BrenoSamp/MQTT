from main.subscribers.subscriber import Subscriber
import asyncio

subscriber = Subscriber()
async def calculate():
    subscriber.subscribeOnCalculateTopic()
async def textEdit():
    subscriber.subscribeOnTextEditTopic()
async def fileEdit():
    subscriber.subscribeOnTextEditTopic()
async def main():
    await asyncio.gather(calculate(), textEdit(), fileEdit())

asyncio.run(main())