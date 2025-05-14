dia = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
azu = [130, 160, 95, 175, 160]     
sal = [2000, 2400, 1800, 2400, 2700] 
sis = [115, 130, 110, 125, 175]    
dia_p = [75, 85, 70, 78, 95]      

def eva_azu(n):
    if 70 <= n <= 140:
        return "Normal"
    else:
        return "Alerta: azúcar fuera de rango"

def eva_sal(n):
    if n <= 2300:
        return "Normal"
    else:
        return "Alerta: sal elevada"

def eva_pre(s, d):
    if s < 120 and d < 80:
        return "Presión Normal"
    elif 120 <= s <= 129 and d < 80:
        return "Presión Elevada"
    elif 130 <= s <= 139 or 80 <= d <= 89:
        return "Hipertensión Etapa 1"
    elif s >= 140 or d >= 90:
        return "Hipertensión Etapa 2"
    else:
        return "Datos inválidos"

print("Evaluación semanal de salud:\n")
for i in range(len(dia)):
    print(f"{dia[i]}:")
    e_azu = eva_azu(azu[i])
    e_sal = eva_sal(sal[i])
    e_pre = eva_pre(sis[i], dia_p[i])
    
    print(f"  Azúcar: {azu[i]} mg/dL - {e_azu}")
    print(f"  Sal: {sal[i]} mg - {e_sal}")
    print(f"  Presión: {sis[i]}/{dia_p[i]} mmHg - {e_pre}")
    print()

p_azu = sum(azu) / len(azu)
p_sal = sum(sal) / len(sal)
p_sis = sum(sis) / len(sis)
p_dia = sum(dia_p) / len(dia_p)

print("Promedios semanales:")
print(f"  Azúcar: {p_azu:.2f} mg/dL")
print(f"  Sal: {p_sal:.2f} mg")
print(f"  Presión: {p_sis:.2f}/{p_dia:.2f} mmHg")
