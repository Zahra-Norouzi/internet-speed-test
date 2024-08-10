import speedtest

s = speedtest.Speedtest()
s.get_servers()
s.get_best_server()
download_speed = s.download()
upload_speed = s.upload()
ping = s.results.ping

print(f"download speed: {download_speed / 1024 / 1024:.2f} Mbps")
print(f"Upload speed: {upload_speed / 1024 / 1024:.2f} Mbps")
print(f"Ping: {ping:.2f} ms")
