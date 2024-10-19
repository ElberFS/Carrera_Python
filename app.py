import turtle
import random
import time

# Configuración de la pantalla
pantalla = turtle.Screen()
pantalla.title("Carrera de Tortugas")
pantalla.setup(width=900, height=500)
pantalla.bgcolor("lightgray")

# Función para dibujar líneas y texto
def dibujar_linea(pos, orientacion, largo, grosor, color="black"):
    linea = turtle.Turtle()
    linea.penup()
    linea.goto(pos)
    linea.pendown()
    linea.setheading(orientacion)
    linea.color(color)
    linea.width(grosor)
    linea.forward(largo)
    linea.hideturtle()

# Función para dibujar las líneas punteadas de los carriles
def dibujar_carril(pos_y):
    carril = turtle.Turtle()
    carril.penup()
    carril.goto(-350, pos_y)
    carril.setheading(0)
    carril.color("white")
    carril.width(2)
    for _ in range(35):
        carril.pendown()
        carril.forward(10)
        carril.penup()
        carril.forward(10)
    carril.hideturtle()

# Dibujar pista, líneas y texto
dibujar_linea((-350, 125), 0, 700, 5, "white")  # Pista superior
dibujar_linea((-350, -125), 0, 700, 5, "white")  # Pista inferior
dibujar_carril(50)  # Carril superior
dibujar_carril(-50)  # Carril inferior
dibujar_linea((-350, 150), -90, 300, 5)  # Línea de inicio
dibujar_linea((350, 150), -90, 300, 5)   # Línea de meta

# Texto de inicio y meta
def mostrar_texto(texto, pos):
    texto_tortuga = turtle.Turtle()
    texto_tortuga.hideturtle()
    texto_tortuga.penup()
    texto_tortuga.goto(pos)
    texto_tortuga.write(texto, align="center", font=("Arial", 16, "bold"))

mostrar_texto("INICIO", (-370, 160))
mostrar_texto("META", (370, 160))

# Crear los tortugas
colores = ['red', 'blue', 'green']
tortugas = []
pos_y = [100, 0, -100]

for i, color in enumerate(colores):
    tortuga = turtle.Turtle(shape='turtle')
    tortuga.shapesize(stretch_wid=1.5, stretch_len=1.5)
    tortuga.color(color)
    tortuga.penup()
    tortuga.goto(-350, pos_y[i])
    tortugas.append(tortuga)

# Función para mover los tortugas
def mover_tortuga(tortuga):
    tortuga.forward(random.randint(1, 5))

# Función para el conteo regresivo
def conteo_regresivo():
    contador = turtle.Turtle()
    contador.hideturtle()
    contador.penup()
    contador.goto(0, 0)
    for i in range(3, 0, -1):
        contador.write(i, align="center", font=("Arial", 48, "bold"))
        time.sleep(1)
        contador.clear()
    contador.write("¡YA!", align="center", font=("Arial", 48, "bold"))
    time.sleep(1)
    contador.clear()

# Iniciar carrera
conteo_regresivo()

carrera_terminada = False
while not carrera_terminada:
    for tortuga in tortugas:
        mover_tortuga(tortuga)
        if tortuga.xcor() >= 350:
            carrera_terminada = True
            ganador = tortuga.color()[0]
            print(f"La tortuga de color {ganador} ha ganado la carrera!")
            break

# Mostrar ganador
mostrar_texto(f"La tortuga de color {ganador} ha ganado la carrera!", (0, 160))

pantalla.mainloop()
