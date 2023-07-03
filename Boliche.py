# ENTRADA - jogadas feitas
jogadas = list(map(int, input().split()))

pontuacao_total = 0
jogada_atual = 0


# PONTUAÇÃO
for frame in range(1, 11):
    
    # Strike
    if jogadas[jogada_atual] == 10:  
        pontuacao_total += 10 + jogadas[jogada_atual + 1] + jogadas[jogada_atual + 2]
        jogada_atual += 1
        
    # Spare
    elif jogadas[jogada_atual] + jogadas[jogada_atual + 1] == 10:  
        pontuacao_total += 10 + jogadas[jogada_atual + 2]
        jogada_atual += 2
    
    # Ponto Padrão
    else: 
        pontuacao_total += jogadas[jogada_atual] + jogadas[jogada_atual + 1] 
        jogada_atual += 2


# FRAMES 1 ATÉ 9
jogada_atual = 0 
for frame in range(1, 10): 
    
    # Strike
    if jogadas[jogada_atual] == 10:  
        print("X _ | ", end='')
        jogada_atual += 1
    
    # Spare
    elif jogadas[jogada_atual] + jogadas[jogada_atual + 1] == 10: 
        print(f"{jogadas[jogada_atual]} / | ", end='')
        jogada_atual += 2
    
    # Ponto Padrão
    else:
        print(f"{jogadas[jogada_atual]} {jogadas[jogada_atual + 1]} | ", end='') 
        jogada_atual += 2

# FRAME 10
for frame in range(10, 11):
    
    # Strike 
    if jogadas[jogada_atual] == 10: 
        print(f"X ", end='')

        # Strike - jogada 2
        if jogadas[jogada_atual + 1] == 10:
            print("X ", end='')

            # Strike - jogada bônus
            if jogadas[jogada_atual + 2] == 10:
                print("X")
            
            # Ponto Padrão - jogada bônus
            else:
                print(jogadas[jogada_atual + 2])
        
        # Spare - jogada 2
        elif jogadas[jogada_atual + 1] != 10 and jogadas[jogada_atual + 1] + jogadas[jogada_atual + 2] == 10:
            print(f"{jogadas[jogada_atual + 1]} / ")
        
        # Ponto Padrão - jogada 2 
        else:
            print(f"{jogadas[jogada_atual + 1]} {jogadas[jogada_atual + 2]}")
        
    # Spare com jogada bônus
    elif jogadas[jogada_atual] + jogadas[jogada_atual + 1] == 10: 
        
        # Strike na jogada bônus
        if jogadas[jogada_atual + 2] != 10:
            print(f"{jogadas[jogada_atual]} / {jogadas[jogada_atual + 2]}")
        
        # Ponto Padrão na jogada bônus
        else:
            print(f"{jogadas[jogada_atual]} / X")
    
    # Sem jogada bônus
    else:
        print(f"{jogadas[jogada_atual]} {jogadas[jogada_atual + 1]}")

# SAÍDA - Scoreboard
print(pontuacao_total)
