import webview # python version (3.11.9) 

# webview.create_window("Caesar Cipher", "index.html")

webview.create_window(
    "Caesar Cipher",
    "index.html",
    width=1500,
    height=1000,
    resizable=True
)

webview.start()

