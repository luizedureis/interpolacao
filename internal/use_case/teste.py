import asyncio


async def worker(output_queue):
    while True:
        user_input = input("Digite algo (ou 'exit' para sair): ")  # Entrada do usuário

        await output_queue.put(user_input)  # Envia o dado para a main

        if user_input.lower() == "exit":
            break  # Sai do loop


async def main():
    queue = asyncio.Queue()

    worker_task = asyncio.create_task(worker(queue))  # Inicia o worker

    while True:
        message = await queue.get()  # Aguarda uma mensagem do worker
        print(f"📩 Main recebeu: {message}")

        if message.lower() == "exit":
            break  # Encerra o programa

    await worker_task  # Aguarda o término do worker


asyncio.run(main())
