respuesta = 12
numero    = 24

if respuesta > numero:
    resp = 'Te fuiste muy arriba'
if respuesta < numero:
    resp = 'Te fuiste muy abajo'
if resp == numero:
    resp = 'Ese es el numero, atinaste'
    
print(resp)

salario= 950

if salario >= 900:
    a=(salario*0.0975)
    b=(salario*0.0125)
    c=salario-a-b
    print('salario total: ', c)
if salario < 900:
    print( ' salario total: ', salario)

    tiempo = 10
    distancia = 0.5
    velocidad = 0.2

    if 10 > tiempo > 1 and velocidad*tiempo > 4 and distancia > 0.2 and tiempo and (not(velocidad/t**2 > 0.1) or distancia < 1 ) and (velocidad*tiempo > 0.5 or distancia/tiempo > 10):
    	print("Se choco")
    else: 
        print('no se choco')

   tabla_periodica = ['na', 'br', 'ca', 'cu', 'au', 'nd', 'ag']

for n in range(len(table_periodica)):
	table_periodica[n] = table_periodica[n].capitalize()


print(table_periodica)

 trabalenguas = ['Por', 'desenredar', 'el', 'enredo', 'que', 'ayer', 'enredé.', 'Hoy', 'enredo',
                'el', 'desenredo', 'que', 'desenredé', 'ayer.']

respu= ' '

for n in range(len(trabalenguas)):
    respu=respu+trabalenguas[n]+' '

print(respu)


num= 6
fact= 1

for i in range(fact,7,1):
    fact = fact * i

print(fact)

num=0
suma=0

for i in range(0,31,1):
    suma=suma+i

print(suma)

nombres = [
    'Himura Kenshin',
    'Kamiya Kaoru',
    'Myōjin Yahiko',
    'Sagara Sanosuke',
    'Takani Megumi',
    'Shinomori Aoshi',
    'Saitō Hajime',
    'Makimachi Misao'
]
nombresfinal= []
for n in range(len(nombres)):
    nombres[n] = nombres[n].lower()
    nombres[n] = nombres[n].replace(" ", "-")
    print(nombres[n])

 
edades = {'Juan':10, 'Javier': 4, 'Jonas':8, 'Nuria': 20, 'Edith': 18, 'Ana':14}

edadtotal = 0
for n in edades.values():
    edadtotal = edadtotal + n

print(edadtotal)

fact= 1
n = 1

while n < 7:
    fact = fact*(n)
    n += 1

print(fact)

lista = list(range(16))
num_impar=[]
n=0
n1=0

while n < len(lista):
    if lista[n] % 2 == 1:
        num_impar.append(lista[n])
    n +=1
while n1 < len(num_impar):
    print(num_impar[n1])
    n1 += 1



num = 456
n=0
mayor=0

while mayor < num:
    n += 1
    mayor=0
    mayor= n**2
    
print('El número más cercano es {}'.format(n-1))



palabras = ['Cretino', 'Vida mía', 'Baboso', 'Bocachancla','Cielo', 'Cielito', 'Mi vida', 'Mi luz', 
            'Luz de mis ojos', 'Bebecita', 'Cariño', 'Papacito', 'Zoquete', 'Cariño mío', 'Patan', 'Cari', 
            'Corazón', 'Mi rey', 'Lerdo','Osito', 'Bombón', 'Charlatan', 'Dulzura', 'Galletita', 
            'Fanfarrón']
ofensas = ['Baboso', 'Bocachancla', 'Charlatan', 'Cretino', 'Fanfarrón', 'Lerdo', 'Patan', 'Zoquete']

for piropos in palabras:
    if piropos  not in ofensas:
        print (piropos)


item = ['frutas', 'vegetales', 'juguetes', 'cereales', 'detergente', 'hogar', 'farmacia', 'papel', 'otros']
peso = [320, 655, 880, 375, 450, 200, 499, 1000, 932]

for n, w in zip(item, peso):
    print(n, w)


x0 = [0, 1, -2, 14, -5, 4, 5]
x1 = [1, 3, 5, 7, 9, 11, 13]
x2 = [2, 4, 6, 8, 10, 12, 14]
letras = ['A', 'B', 'C', 'D', 'F', 'E', 'F']

print(list(zip(x0,x1,x2,letras)))


tup = ((1,-1), (2,-2), (3,-3), (4,-4), (5,-5))

pos, neg = zip(*tup)

print(pos)
print(neg)


matriz5x4 = (( 1, 2, 3, 4),
             ( 5, 6, 7, 8),
             ( 9,10,11,12),
             (13,14,15,16),
             (17,18,19,20))

matriz4x5 = []
splitmat = zip(*matriz5x4)
matriz4x5=[list(v2) for v2 in splitmat]

print(matriz4x5)


conquistadores = ['Vasco Núnez de Balboa', 'Luis de Moscoso Alvarado', 'Juan de Cárdenas',
                  'Pedro de Heredia', 'Gutierre de Miranda', 'Juan de Salcedo']

lista=[x.split()[0] for x in conquistadores]
print(lista)


y= [ 2**(2**i)+1 for i in range(10)]
print(y)

major_league_players = {'Mel Allen':1978, 'Red Barber':1978, 'Jerry Coleman':2005,
          'Joe Garagiola, Sr.':1991, 'Curt Gowdy':1984, 'Ken Harrelson':2020,
          'Al Helfer':2019, 'Russ Hodges':1980}

player=[i  for i in major_league_players if major_league_players[i] >= 1980 and major_league_players[i] <= 2015 ]
print(player)



