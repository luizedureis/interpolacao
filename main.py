from internal.controllers.main_controller import MainController


def main():
    ctrl = MainController()
    print("Olá, vamos trabalhar com imagens!")

    while True:
        image_path = input("Digite o nome do arquivo que vamos trabalhar (ou 'sair' para encerrar): ")
        if image_path.lower() == 'sair':
            print("Encerrando o programa.")
            break

        if not ctrl.carregarImg(image_path):
            break

        while True:
            operacao = input(
                "Escolha a operação: zoom, rotacionar, deblur, redirecionar (ainda não implementado) "
                "ou 'voltar' para escolher outra imagem: "
            ).lower()

            if operacao == "zoom":
                try:
                    zoom_valor = float(input("Informe o valor do zoom (até 3x): "))
                    ctrl.zoomImg(zoom_valor, printImg=True)
                except ValueError:
                    print("Valor inválido para zoom. Tente novamente.")

            elif operacao == "rotacionar":
                try:
                    angulo = int(input("Informe o ângulo (em graus) para rotacionar: "))
                    ctrl.rotacionarImg(angulo, printImg=True)
                except ValueError:
                    print("Valor inválido para o ângulo. Tente novamente.")

            elif operacao == "deblur":
                try:
                    deblur_valor = float(input("Informe a intensidade do deblur: "))
                    ctrl.deblurImg(deblur_valor, printImg=True)
                except ValueError:
                    print("Valor inválido para deblur. Tente novamente.")

            elif operacao == "redirecionar":
                print("A opção 'redirecionar' ainda não foi implementada.")

            elif operacao == "voltar":
                print("Retornando para o menu principal de carregamento de imagens.\n")
                break

            elif operacao == "sair":
                print("Encerrando o programa.")
                return

            else:
                print("Opção inválida. Por favor, escolha uma operação válida.")

if __name__ == "__main__":
    main()
