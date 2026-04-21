import pyperclip

def reverse_backslash(path) :
    return path.replace('\\', '/')

if __name__ == "__main__" :
    clipboard_txt = pyperclip.paste()
    print(f"clipboard: {clipboard_txt}")
    clipboard_rev = reverse_backslash(clipboard_txt)
    pyperclip.copy(clipboard_rev)
    print(f"new clipboard: {clipboard_rev}")