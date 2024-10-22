# Codico paython
#grupo: Emanuelle,Felipe,Murilo Amorim, Tatielle
viaturas=float(input("Quantas viaturas tem disponiveis no seu bairro?"))
iluminação=str(input("Tem iluminação de qualidade de noite?"))
policia=str(input("Tem bases de segurança próximos?"))
movimentado=str(input("Seu bairro é movimentado?"))
assalto=str(input("Tem assalto com freqüencia?"))
satisfacao=float(input("De 0 a 10 quanto é a sua insatisfação com o bairro?"))
if viaturas<=4 and iluminação=="nao" and policia=="nao"and  movimentado=="nao" and assalto=="sim" and satisfacao<=3:
    print("Bairro não é seguro")
else:
    print("Bairro seguro")
