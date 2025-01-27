import asyncio
import websockets

# Replace with your static ngrok endpoint (TCP URL)
NGROK_ENDPOINT = "ws://0.tcp.in.ngrok.io:16029"

async def client():
    try:
        async with websockets.connect(NGROK_ENDPOINT) as websocket:
            print("Connected to the server.")
            while True:
                # Send a message (e.g., simulated data) to the server
                message = input("Enter a message to send: ")
                await websocket.send(message)
                print(f"Message sent: {message}")

                # Receive a broadcast message from the server
                response = await websocket.recv()
                print(f"Received: {response}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(client())