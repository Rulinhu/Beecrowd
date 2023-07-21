n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10

print("Media: %0.1f" %media)

if media >= 5.0 and media < 7.0:
	print("Aluno em exame.")
	ex = float(input())
	print("Nota do exame: %0.1f" %ex)
	final = (ex + media) /2
	
	if final >= 5.0:
		print("Aluno aprovado.")
	if final <5.0:
		print ("Aluno reprovado.")
		
	print("Media final: %0.1f" %final)

if media >= 7.0:
	print("Aluno aprovado.")

if media < 5.0:
	print("Aluno reprovado.")