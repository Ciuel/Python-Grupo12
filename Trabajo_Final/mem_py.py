#Programa ejecutable
from src.Components import login,config

def main():
    login.start()
    config.start("3")


if __name__=="__main__":
    main()