promedio=(30+16+40)/3
print('resultado final: ', + promedio)

a=(6*2.8)/0.5
b=a/12
print(int(b)+1)

# un recipiente cilindrico de agua tiene (en pie cubicos)
recipiente1 = 1e3
# Se tiene otro recipiente de agua (in cubic metres)
recipiente2 = 1.8e3


# haga las siguientes operaciones
# decremente la variable del recipiente 2 al 20%
recipiente2=recipiente2-(recipiente2*0.2)
# añada la variable de recipiente 1 a recipiente 2
recipiente2=recipiente2+recipiente1
# incremente el volumen del recipiente 1 al 5%
recipiente1=recipiente1+(recipiente1*0.05)
# decremente el recipiente 1 por 15%
recipiente1=recipiente1-(recipiente1*0.15)
# decremente el 0.3% del recipiente 1, 
recipiente1=recipiente1-(recipiente1*0.003)
# decremente el 1% del recipiente2
recipiente2=recipiente2-(recipiente2*0.01)
# sume ambas variables en el recipiente1
recipiente1=recipiente1+recipiente2
# imprima el nuevo valor de las variables
print('Resultado esperado: ', recipiente1, recipiente2)


# temperatura de pais vs área de estudio
tempPTY, areaPTY = 38.5, 102
tempCOL, areaCOL = 29.2, 150

# temp/m2
tempm2_pty = tempPTY/areaPTY
tempm2_col = tempCOL/areaCOL

# escriba el restante de código que indica si la temp/m2 de pty es mayor a la temp/m2 de col
print('Resultado esperado: ', tempm2_pty>tempm2_col)

print('¿Porqué en Python para comparar no podemos utilizar = sino ==?')
print('')
print('porque el simbolo == en python significa "igual que" y el simbolo = lo usamos para asignar valores.')


# TODO:  Arregle lo que está mal

quote = 'Ser-O-No-''Ser''-''He allí-El Dilema'
# LA RESPUESTA ESPERADA DEBE SER:  Ser-O-No-Ser-He allí-El Dilema
print(quote)


fruta = 25
vegetales = 12

total_fruta_y_vegetal = fruta + vegetales
print('Resultado esperado ', total_fruta_y_vegetal)
print(type(total_fruta_y_vegetal))

username = 'Ignacio'
ts = "04:50"
url = "http://minegocio.com/id/nmasaya/me"

# TODO: imprimir un mensaje como que se muestra a continuación
print(username,'exited the', url, 'at', ts)

nombre = "Juan"
seg_nombre = "Javier"
apellido = "Jimenez"

# calcular el largo del nombre
name_length = len(nombre)+len(seg_nombre)+len(apellido)

# Ahora que calculó el largo del nombre intente  ver si cabe en la licencia
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

print(type("12"))

print(type(12.3))

print(type(len('i am a string')))

print("""¿Qué pasa cuando se llama al método islower() para cuando es un punto flotante?
Retorna True
Retorna False
Retorna error

respuesta: da error """)

name='camila rojas'
x=name.index('j')
print(x)

# Escriba un código donde asigne un valor a una variable
# Ahora imprima en pantalla con print() pero usando .format() para las variables que se asigno anteriormente e imprima estas dos variables
v1= 'camila rojas'
v2= '24'
print('hola mi nombre es {} y tengo {} años'.format(v1,v2))

mes = 8
dias_del_mes = [31,28,31,30,31,30,31,31,30,31,30,31]

# Use indexing para determinar el número de días en el mes 8
num_dias =  dias_del_mes[mes-1] 
print(num_dias)

dias = ['Feb 8, 1980', 'Dic 8, 1949', 
        'Mar 20, 1492', 'Abril 12, 1999',
        'Jun 12, 2010']
                 
# Imprima los ultimos tres elementos de la lista
print(dias[2:])

#Suponga que tenemos las siguientes expresiones:

p1 = "Quisiera que se terminara la materia" 
p2 = ["Quisiera", "que", "se", "terminara", "la", "materia"]

#¿Qué sucede cuando evaluamos estos casos con cada una de las palabras p1 y p2?

p2[4] = "que"
p2[0]= "Quisira que"
#p1[30]="a"
p2[0:2] = ["Que", "quisiera"]

print('al evaluar el caso de p1 da error, ya que es una cadena y no una lista, por ello lo deje en comentario', p1)
print('  ')
print("""Al evaluar los casos para p2 recibimos lo siguiente {}""" .format(p2))


a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

names = ["Uno", "Dos", "Tres", "Cuatro"]
print(" & ".join(sorted(names)))

names = ["Norberto", "Ignacio", "Luis", "Tito"]
names.append("Armando")
print(sorted(names))

tuple_a = 2, 8
tuple_b = (8, 2)

print(tuple_a == tuple_b)
print(tuple_a[1])

a = [1, 2, 2, 4, 4, 4, 8, 8, 8, 8]
b = set(a)
print(len(a) - len(b))

a = [0, -1, -1, 2, 1, 2, 7, 9, 12, 15]
b = set(a)
b.add(111)
b.pop()
print(b)
print(' ')
print('sí el 111 seguira siendo parte del set')

my_dict={ 'Panama':5.9, 'Costa Rica':6.2, 'Colombia':8.4, 'mexico':1.2}
print(my_dict)

print("""¿Cuáles de las siguientes pueden ser utilizadas como diccionario?

str
list
int
float

*str, int, float pueden ser utilizadas como diccionario""" )

my_dict={ 'Panama':5.9, 'Costa Rica':6.2, 'Colombia':8.4, 'mexico':1.2}
print(my_dict['veraguas'])

items = {'harina': [20, 10, 15, 8, 32, 15], 
 'carne': [3,4,2,8,2,4], 
 'pan': [2, 3, 3], 
 'cc': [0.3, 0.5, 0.8, 0.3, 1]}

print(items['harina'][2])
print(items['carne'][2])
print(items['pan'][2])
print(items['cc'][2])

datos = {'Ana':{'edad':24, 'peso':110, 'sexo':'F'},
         'Javi':{'edad':12, 'peso':90, 'sexo':'M'}}
print(datos)
print(datos.get('Javi'))
print(datos.get('Juan'), 'No existe Juan')


datos = {'Ana':{'edad':24, 'peso':110, 'sexo':'F', 'estudiante':True},
         'Javi':{'edad':12, 'peso':90, 'sexo':'M', 'estudiante': False}}


print(datos['Ana']['estudiante'])

print(datos['Javi']['estudiante'])

