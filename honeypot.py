
import asyncio, csv, datetime, os

LOGFILE = "connections.csv"
PORT = 2222

async def handle(reader, writer):
    addr = writer.get_extra_info('peername')
    ip, port = addr[0], addr[1]
    banner = "SSH-2.0-OpenSSH_8.9p1 FakeHost\r\n"
    writer.write(banner.encode()); await writer.drain()
    timestamp = datetime.datetime.utcnow().isoformat()
    session_data = []
    try:
        while True:
            data = await reader.readline()
            if not data: break
            txt = data.decode(errors='ignore').rstrip()
            session_data.append((timestamp, ip, port, txt))
           
            writer.write(b"$ ".encode()); await writer.drain()
    except Exception:
        pass
    finally:
        writer.close()
        await writer.wait_closed()
   
        exists = os.path.exists(LOGFILE)
        with open(LOGFILE, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if not exists:
                w.writerow(["ts","src_ip","src_port","data"])
            for row in session_data:
                w.writerow(row)

async def main():
    server = await asyncio.start_server(handle, "0.0.0.0", PORT)
    addrs = ", ".join(str(s.getsockname()) for s in server.sockets)
    print(f"Honeypot listening on {addrs} — logs->{LOGFILE}")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
