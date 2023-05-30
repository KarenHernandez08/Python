def operacion(cantidad, balance, tipo='deposito'):
    
    def deposito(cantidad, balance):
        return cantidad + balance
    
    def retiro (cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None
        
    print(deposito(10,200))
    print(retiro(50, 20))

    if tipo == 'deposito':
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro (cantidad, balance)

resultado=operacion(10,30)
print(resultado)
