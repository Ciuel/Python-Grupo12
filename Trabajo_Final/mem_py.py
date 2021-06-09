#Programa ejecutable
from src.Components import login
from distutils.spawn import find_executable

def main():
    """Ejecuta la aplicacion"""

    print( find_executable("vlc.exe") is not None)
    login.start()

if __name__ == "__main__":
    main()