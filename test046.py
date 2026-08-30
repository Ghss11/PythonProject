import random


def jogar():
    print("--- JOGO DE ADIVINHAÇÃO INTERCALADO ---")

    numero_pc = random.randint(1, 100)
    baixo, alto = 1, 100

    while True:
        # --- SEU TURNO ---
        try:
            chute_user = int(input("\n[VOCÊ] Seu palpite (1-100): "))
            if chute_user < numero_pc:
                print("DICA: O meu é MAIOR!")
            elif chute_user > numero_pc:
                print("DICA: O meu é MENOR!")
            else:
                print("✨ VOCÊ VENCEU!")
                break
        except ValueError:
            print("Erro! Digite um número.")

        # --- TURNO DO PC ---
        chute_pc = (baixo + alto) // 2
        print(f"\n[PC] Eu acho que é: {chute_pc}")
        dica = input("Dica: (A)certou, (M)aior ou (m)enor: ").strip
        if dica == 'a':
            print("🤖 O PC VENCEU!")
            break
        elif dica in 'Mm':
            baixo = chute_pc + 1
        else:
            alto = chute_pc - 1


# ESTA LINHA É A MAIS IMPORTANTE: ELA CHAMA O JOGO!
jogar()