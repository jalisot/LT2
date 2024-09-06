from classTitular import   Titular, Conta

if __name__ == '__main__':
    t1 = Titular('joao','lisot', '750-3')
    print(t1) 
    print(t1.get_nome()) 
    t1.set_nome('luiz') 
    print(t1.get_nome())
    print(t1.get_sobrenome())
    print(t1.get_cpf())
    print(t1.get_nomeCompleto())




    c1 = Conta('203040', t1, '5000.50' )
    print(c1)
    print(c1.get_numero())

    
