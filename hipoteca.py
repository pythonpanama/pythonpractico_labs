# hipoteca.py
#
# Ejercicio 1.7

capital = 500000.0
tasa = 0.05
pago = 2684.11
pago_adicional = 1000.00
mes = 0
total_pagado = 0.0

while capital > 0:
    if mes < 12:
        pago += pago_adicional
    capital = capital * (1 + tasa / 12) - pago
    total_pagado = total_pagado + pago
    mes += 1

print('Total pagado', total_pagado)
print('Meses requeridos', mes)