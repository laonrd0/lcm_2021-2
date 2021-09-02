# -*- coding: utf-8 -*

"script que simula el funcionamiento de un cajero automático"

print("Cajeros ENES")
monto_retirar = int(input("Cual es el monto que de desas retirar (monto max. $6000): "))

while monto_retirar > 0 and monto_retirar <= 6000 and monto_retirar % 100 == 0:
    billetes_500  = int(monto_retirar / 500)
    monto_retirar = monto_retirar - (billetes_500 * 500)
    billetes_200  = int(monto_retirar /200)
    monto_retirar = monto_retirar - (billetes_200 * 200)
    billetes_100 = int(monto_retirar / 100)
    monto_retirar = monto_retirar - (billetes_100 * 100) 

print(f'Se entregan:\n {billetes_500} billetes de $500\n {billetes_200} billetes de $200\n {billetes_100} billetes de $100')

    
