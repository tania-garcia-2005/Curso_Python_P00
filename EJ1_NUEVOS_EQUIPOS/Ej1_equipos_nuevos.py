import random
equipos = [
    ["Héctor", "Addi", "Jesús Alberto"],
    ["Tania", "Patricia", "Rebeca"],
    ["Jamileth", "Bryan", "Rosalinda"],
    ["Galilea", "Jennifer", "Juan"]
]
personas = []
for equipo in equipos:
    for persona in equipo:
        personas.append(persona)
nuevos_equipos = []
while len(personas) > 1:
    persona1 = random.choice(personas)
    persona2 = random.choice(personas)
    nuevos_equipos.append([persona1, persona2])
    personas = [persona for persona in personas if persona != persona1 and persona != persona2]
for equipo in nuevos_equipos:
    print(f"Equipo: {equipo}")