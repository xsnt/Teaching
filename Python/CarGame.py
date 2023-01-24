## ajuda, ligar, desligar, fechar

while True:
    comando = input("Açao: ").lower()
    if comando == "fechar":
      break
    match comando:
      case "ajuda":
        print("ligar - liga o carro")
        print("desligar - desliga o carro")
        print("fechar - fecha o programa")
      case "ligar":
        print("Carro ligado!")
      case "desligar":
       print("Carro desligado!")
print("Jogo Terminado.")