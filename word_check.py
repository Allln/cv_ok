import base64
encoded_dictionary = [
    "YXV0b21hdGlvbg==", "Y3liZXJuZXRpY3M=", "aW50ZWxsaWdlbmNl", "bmV1cmFs", "dGVuc29y",
    "YWxnb3JpdGht", "c3luYXBzZQ==", "aGV1cmlzdGlj", "b3B0aW1pemF0aW9u", "Z3JhZGllbnQ=",
    "bWFjaGluZQ==", "bGVhcm5pbmc=", "YXJjaGl0ZWN0dXJl", "bWljcm9zZXJ2aWNl", "dHJhZGluZw==",
    "a2luZw==", "cXVlZW4=", "Y2F0", "ZG9n", "b2NlYW4=", "d2F0ZXI=",
    "Y29mZmVl", "dGVh", "Y2xvdWQ=", "ZGF0YWJhc2U=", "bGF0ZW5jeQ==",
    "cHJvdG9jb2w=", "ZmlyZQ==", "aWNl", "YXBwbGU=", "ZnJ1aXQ="
]
decoded_dictionary = [base64.b64decode(s).decode('utf-8') for s in encoded_dictionary]
print(decoded_dictionary)