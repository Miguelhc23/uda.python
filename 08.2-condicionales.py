
balance =500
if balance > 0:
    print('puedes pagar')

balance =500
if balance >= 600:
    print('puedes pagar')
else:
    print('No tienes saldo')

likes= 200
if likes >= 200:
    print('Exelente, 200 likes')
else:
    print('casi llegas a los 200')

lenguaje = 'PHP'
if lenguaje == 'python':
    print ('exelente dexicion')

#un if anidado (se encuentra dentro de otro )
usuario_autenticar =True
usuario_admin=False
if usuario_autenticar:
        if usuario_admin:
            print('ACCESO TOTAL')
        else:
            print('acceso al sistema')
else:
        print('debes inicar sesion')



