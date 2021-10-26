print("Hora da verdade")
print("Digite a primeira nota")
a=int(input())
print("Digite a segunda nota")
b=int(input())
print("Digite a terceira nota")
c=int(input())
print("Digite a quarta nota")
d=int(input())

e = (a+b+c+d)
print("a soma e: ")
print(e)
f = e / 4
print("a media e: ")
print(f)
if f < 60:
    print("aluno reprovado")
    print("Estude mais da proxima vez")
if f > 60:
    print("aluno aprovado")
    print("Parabens")
    if f>90:
        print("Sua media foi impressionante!!")
        

    

print(":)")
