import asyncio

async def ping(host,number):
    ping_process = await asyncio.create_subprocess_shell(f"ping -c 1 {host}{number} > /dev/null 2>&1")
    await ping_process.wait()

    if ping_process.returncode == 0:
        print(f"{host}{number} | Online")
        await asyncio.sleep(0.1)
    else:
        pass

async def ping_all(ip,start,end):
    tasks = []
    for i in range(start,end):
        tasks.append(asyncio.create_task(ping(ip,i)))
    await asyncio.gather(*tasks)

ip = input("Ex.192.168.1.\nPlease Input IP : ")
inputStart = input("Start : ")
intStart = int(inputStart)
inputEnd = input("End : ")
intEnd = int(inputEnd)
asyncio.run(ping_all(ip,intStart,intEnd))