def CenterWindow(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")


kullaniciAdi = ""
kullaniciID = 0


def PopulateTreeview(tree, data):
    for row in data:
        tree.insert("", "end", values=list(row))
