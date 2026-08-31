import base64

encoded_dictionary = [
        "YWRhcHRpdmU=", "YWdlbnQ=", "YWxnb3JpdGht=", "YW5hbHl0aWNz=", "YXN5bmNocm9ub3Vz=", "YXV0b21hdGlvbg==",
        "YmFja2VuZA==", "YmFuZHdpZHRo=", "YmluYXJ5=", "Ym90bmV0=", "Ym90dGxlbmVjay==", "Ynl0ZWNvZGU=",
        "Y2x1c3Rlcg==", "Y29tcGlsZXI=", "Y29tcHV0ZQ==", "Y29udGFpbmVy=", "ZGFlbW9u=", "ZGF0YWJhc2U=",
        "ZGVidWdnaW5n=", "ZGVwbG95=", "ZGlzdHJpYnV0ZWQ=", "ZG9ja2Vy=", "ZG9tYWlu=", "ZW5jcnlwdGlvbg==",
        "ZXRoZXJuZXQ=", "ZmlyZXdhbGw=", "ZmlybXdhcmU=", "ZnJhbWV3b3Jr", "Z2F0ZXdheQ==", "Z3JhZGllbnQ=",
        "aGFyZHdhcmU=", "aGFzaA==", "aGV1cmlzdGlj=", "aHlwZXJ2aXNvcg==", "aW5kZXg=", "aW5oZXJpdGFuY2U=",
        "aW5qZWN0aW9u=", "aW5zdGFuY2U=", "aW50ZXJmYWNl=", "aW50ZXJwcmV0ZXI=", "aXRlcmF0aW9u=", "amF2YXNjcmlwdA==",
        "anNvbg==", "a2VybmVs=", "a3ViZXJuZXRlcw==", "bGF0ZW5jeQ==", "bGlicmFyeQ==", "bG9hZGJhbGFuY2luZw==",
        "bG9ja3k=", "bG9nZ2luZw==", "bWFsd2FyZQ==", "bWVtb3J5=", "bWljcm9zZXJ2aWNl=", "bWlkZGxld2FyZQ==",
        "bW9ub2xpdGg=", "bXVsdGl0aHJlYWRpbmc=", "bmFtc3BhY2U=", "bmV0d29yaw==", "bm9kZQ==", "b2JqZWN0=",
        "b3B0aW1pemF0aW9u=", "cGFja2V0=", "cGF0Y2g=", "cGF5bG9hZA==", "cGlwZWxpbmU=", "cG9pbnRlcg==",
        "cG9seW1vcnBoaXNt=", "cHJvY2Vzcw==", "cHJvdG9jb2w=", "cXVlcnk=", "cXVldWU=", "cXVhbnR1bQ==",
        "cmVjdXJzaW9u=", "cmVmYWN0b3I=", "cmVwb3NpdG9yeQ==", "cmVxdWVzdA==", "cmVzb3VyY2U=", "cmVzcG9uc2U=",
        "cmVzdGFwaQ==", "cm91dGVy=", "cnVudGltZQ==", "c2NhbGFiaWxpdHk=", "c2NhbGFy=", "c2FuZGJveA==",
        "c2NyaXB0=", "c2VnbWVudGF0aW9u=", "c2VydmVy=", "c2Vzc2lvbg==", "c2hlbGw=", "c25pcHBldA==",
        "c29ja2V0=", "c291cmNl=", "c3RhY2s=", "c3RhdGU=", "c3RhdGlj=", "c3RyZWFt=",
        "c3RyaW5n=", "c3Vicm91dGluZQ==", "c3luYXBzZQ==", "c3ludGF4=", "dGVsZXRlbHJ5=", "dGVuc29y=",
        "dGhyZWFk=", "dG9rZW4=", "dHJhbnNhY3Rpb24=", "dHVubmVs=", "dW5pY29kZQ==", "dXRpbGl0eQ==",
        "dmFyaWFibGU=", "dmVjdG9y=", "dmlydHVhbA==", "dmlydHVhbGl6YXRpb24=", "dnVsbmVyYWJpbGl0eQ==",
        "d2Vic29ja2V0=", "d2lkZ2V0=", "d29ya2Zsb3c="
]

decoded_words = []
for item in encoded_dictionary:
    try:
        padded_item = item + '=' * (-len(item) % 4)
        decoded_bytes = base64.b64decode(padded_item)
        decoded_words.append(decoded_bytes.decode('utf-8'))
    except Exception as e:
        decoded_words.append(f"[--- ERROR DECODING ---: {item}]")

print(decoded_words)
