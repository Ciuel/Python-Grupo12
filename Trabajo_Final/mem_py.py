#Programa ejecutable
from src.Components import score
from src.Components import login, config


def main():
    login.start()
    config.start("3")
    score.start()



if __name__=="__main__":
    main()