#Capitulo 3. Ejercicio propuesto 18

import tkinter as tk

def calcular_salarios():
    try:
        codigo_empleado = entry_codigo_empleado.get()
        nombres = entry_nombres.get()
        horas_trabajadas_mes = int(entry_horas_trabajadas_mes.get())
        valor_hora = int(entry_valor_hora.get())
        porcentaje_retencion = int(entry_porcentaje_retencion.get()) / 100

        salario_bruto = horas_trabajadas_mes * valor_hora
        salario_neto = salario_bruto * (1 - porcentaje_retencion)

        resultado.set(f"El código es: {codigo_empleado}\nSu nombre es: {nombres}\nEl salario bruto es: ${salario_bruto:.2f}\nEl salario neto es: ${salario_neto:}")
    except ValueError:
        resultado.set("Valores inválidos")

root = tk.Tk()
root.title("Calcule su salario")

tk.Label(root, text="Código del empleado:").grid(row=0, column=0)
entry_codigo_empleado = tk.Entry(root)
entry_codigo_empleado.grid(row=0, column=1)

tk.Label(root, text="Nombre del empleado:").grid(row=1, column=0)
entry_nombres = tk.Entry(root)
entry_nombres.grid(row=1, column=1)

tk.Label(root, text="Horas trabajadas al mes:").grid(row=2, column=0)
entry_horas_trabajadas_mes = tk.Entry(root)
entry_horas_trabajadas_mes.grid(row=2, column=1)

tk.Label(root, text="Valor hora trabajada:").grid(row=3, column=0)
entry_valor_hora = tk.Entry(root)
entry_valor_hora.grid(row=3, column=1)

tk.Label(root, text="Porcentaje de retención en la fuente:").grid(row=4, column=0)
entry_porcentaje_retencion = tk.Entry(root)
entry_porcentaje_retencion.grid(row=4, column=1)

tk.Button(root, text="Calcular", command=calcular_salarios).grid(row=5, column=0, columnspan=2)

resultado = tk.StringVar()
tk.Label(root, textvariable=resultado).grid(row=6, column=0, columnspan=2)

root.mainloop()
