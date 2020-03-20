"""
--------------------------------------------------------------------------------
Computacao II - UFRJ
--------------------------------------------------------------------------------
Professor: Dr. Natanael Quintino
--------------------------------------------------------------------------------
Tópicos:

    0. Revisão de Computação I

    1. Classes e Objetos

        1.1 Definindo classes
        1.2 Instanciando e Acessando Objetos
        1.3 Métodos Mágicos
        1.4 Métodos Privados
        1.5 Herança
        1.6 Polimorfismo e Agregação

    2. Tratamento de Exceções

        2.1 Estrutura: 'try', 'except', 'else', 'finally'
        2.2 Algumas Exceções Predefinidas
        2.3 Personalizando Exceções

    3. Noções de escopo

        3.1 Escopos para variáveis: 'local' e 'global'
        3.2 Escopos para funções e módulos

    4. Persistência de Dados

        4.1 Abrindo arquivos
        4.2 Manipulando arquivos de texto
        4.3 Manipulando arquivos binarios

    5. Interface Gráfica (REVISAR)

        5.1 Criando Janelas
        5.2 Adicionando Widgets
        5.3 Editando Menu e Status Bar
        5.4 Utilizando Eventos

    6. Modulos numpy, scipy e matplotlib

        6.1 Conhecendo o 'numpy'
        6.2 Conhecendo o 'scipy'
        6.3 Conhecendo o 'matplotlib'

--------------------------------------------------------------------------------
"""

# Informacoes sobre o programa
__author__     = "Natanael Quitino"
__copyright__  = "Copyright 2020, Lectures Notes"
__credits__    = ["Natanael Quintino"]
__license__    = ""
__version__    = "0.1.0"
__maintainer__ = "Natanael Quintino"
__email__      = "natanaelquintino@gmail.com"
__status__     = "Dev"

# Add the path of my folders to python
import sys; sys.path.extend(['./decorators_script/','./files_requiered/',
                             './scripts/'])

# Importing python modules
import functools, time

# ============================================================================ #
# MAIN PROGRAM
# ============================================================================ #
# Show the topics and subtopics
print(__doc__); time.sleep(5)

# Choosing the mode of program
mode_program_choose = input('''
> O que desejas:
(1) Questões;
(2) Gabarito;
(3) Ambos.
 ''')

# Get the answer
mode_program = {'1':'questions','2':'answers','3':'both'}[mode_program_choose]

# Export the mode's choice
with open('files_requiered/mode_program.txt','w') as mode_txt:
    mode_txt.write(mode_program); mode_txt.close()

# Importing need packages
from decorators import my_decorator

# Get the user's choice
choice = input('\n> Escolha o tópico desejado: ')

# Convert choice in a number type
choice = eval(choice)

# Topic's identifyer
if (type(choice) == int):

    # Set the topic title
    if   (choice == 0): topic = "Revisão de Computação I"
    elif (choice == 1): topic = "Classes e Objetos"
    elif (choice == 2): topic = "Tratamento de Exceções"
    elif (choice == 3): topic = "Noções de escopo"
    elif (choice == 4): topic = "Persistência de dados"
    elif (choice == 5): topic = "Interface Gráfica"
    elif (choice == 6): topic = "Módulos numpy, scipy, matplotlib"

    # Show the Topic choose
    print("")
    
    if (choice > 0):
        # Get the user's subtopic choice
        choice = input('\n> Agora o subtópico desejado: ')

        # Convert choice in a number type
        choice = eval(choice)

# Call of the programs from user's choice
if   (choice == 0)  : file = 'reviewComp1.py'
elif (choice == 1.1): file = 'classDefinitions.py'
elif (choice == 1.2): file = 'instancingObjects.py'
elif (choice == 1.3): file = 'magicMethods.py'
elif (choice == 1.4): file = 'privateMethods.py'
elif (choice == 1.5): file = 'heritage.py'
elif (choice == 1.6): file = 'polimorfismAgregation.py'

elif (choice == 2.1): file = 'structureExceptions.py'
elif (choice == 2.2): file = 'pythonExceptions.py'
elif (choice == 2.3): file = 'personalExceptions.py'

elif (choice == 3.1): file = 'scopeVariables.py'
elif (choice == 3.2): file = 'scopeFunctionsModules.py'

elif (choice == 4.1): file = 'openFiles.py'
elif (choice == 4.2): file = 'manipulateFileTxt.py'
elif (choice == 4.3): file = 'manipulateFileBinary.py'

elif (choice == 5.1): file = 'createWindows.py'
elif (choice == 5.2): file = 'addWidgets.py'
elif (choice == 5.3): file = 'menuStatusBar.py'
elif (choice == 5.4): file = 'usingEvents.py'

elif (choice == 6.1): file = 'learningNumpy.py'
elif (choice == 6.2): file = 'learningScipy.py'
elif (choice == 6.2): file = 'learningSympy.py'
elif (choice == 6.3): file = 'learningMatplotlib.py'

# Execute the program choose
exec(open(file).read())
# ============================================================================ #
