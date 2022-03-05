class Aluno:
    def __init__(self,nome,nota1,nota2):                        # setter
        self.nome = nome
        self.media = ((nota1 + nota2)/2)

    def media(self):                                            # getter
        return self.media

    def nome(self):                                             # getter
        return self.nome


nome = input("Informe o nome do aluno: ")
nota1 = int( input("Informe a primeira nota: "))
nota2 = int( input("Informe a segunda nota: "))

aluno1 = Aluno(nome,nota1,nota2)


print ('A média das notas de {} é {}'.format(aluno1.nome, aluno1.media))
