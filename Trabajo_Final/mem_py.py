#Programa ejecutable
from src.Components import login


def main():
    """Ejecuta la aplicacion"""
    try:
        login.start()
    except: FileNotFoundError #libvlc.dll
        print("libvlc.dll")
if __name__ == "__main__":
    main()