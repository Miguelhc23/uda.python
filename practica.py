
faltas = 4  # Número máximo de faltas permitidas
adeudo = False  # Variable booleana que indica si se tiene adeudo o no
pago = True  # Variable booleana que indica si se tiene todo pagado o no

if faltas >= 3:
    print('Estás reprobado por exceder el número de faltas permitidas')
elif adeudo:
    print('Tienes falta por adeudo')
elif not pago:
    print('Tienes falta por falta de pago')
else:
    print('No tienes faltas')


