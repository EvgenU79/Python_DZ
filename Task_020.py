# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.

list = {1:"AEIOULNSTR", 2:"DG", 3:"BCMP", 4:"FHVWY", 5:"K", 8:"JX", 10:"QZ"}

word = input("Введите слово: ").upper()
sum = 0
for i in word:
    for k, v in list.items():
        if i in v:
            sum += k
print(sum)
