"""
Script dos decoradores
"""

# Add the path of my main folder to python
import sys; sys.path.append(sys.path[0][:-sys.path[0][::-1].index('/')])

# Importando o modo do programa
with open('files_requiered/mode_program.txt','r') as mode_txt:
    mode_program = mode_txt.read(); mode_txt.close()

def my_decorator(func):
    "Decorador para selecionar o decorador adequado"

    # Delimitador de exibicao
    delimitador = '\n'+40*'='+'\n'
     
    if   (mode_program == 'ambos'):

        # Obtendo as informacoes da funcao original
        @resgateInformacao(func)
        def decorador(*args):
            "Exibindo o codigo da funcao"

            # Dando um titulo a mensagem de exibicao
            codigo  = delimitador+"Codigo"+delimitador
            
            # Obetendo codigo da funcao
            codigo += func.__doc__.partition('=== Code ===')[-1]

            # Dando um print no codigo
            print(codigo)

            # Dando um titulo a mensagem de exibicao
            sheel  = delimitador+f"No Sheel"+delimitador

            # Texto simulando chamada de funcao no sheel do Python
            sheel += f"\n>>> {func.__name__}("
            
            # Exibindo os parametros passados
            for arg in args: sheel += f'{arg},'

            # Fechando parenteses
            sheel  = sheel[:-1]+')\n'

            # Exibindo resultado da funcao
            sheel += str(func(*args)) + '\n'

            # Dando o print noo simulador do Sheel
            print(sheel)

            return None

    elif (mode_program == 'codigo'):

        # Obtendo as informacoes da funcao original
        @resgateInformacao(func)
        def decorador():
            "Exibindo o codigo da funcao"

            # Dando um titulo a mensagem de exibicao
            codigo  = "\nCodigo:"
            
            # Obetendo codigo da funcao
            codigo += func.__doc__.partition('=== Code ===')[-1]

            # Dando um print
            print(codigo)            

            return None

    elif (mode_program == 'sheel'):

        # Obtendo as informacoes da funcao original
        @resgateInformacao(func)
        def decorador(*args):
            "Simulando a chamada da funcao no sheel"

            # Texto simulando chamada de funcao no sheel do Python
            sheel  = f"\nNo sheel:\n\n>>> {func.__name__}("
            
            # Exibindo os parametros passados
            for arg in args: sheel += f'{arg},'

            # Fechando parenteses
            sheel  = sheel[:-1]+')\n'

            # Exibindo resultado da funcao
            sheel += str(func(*args)) + '\n'

            # Dando o print
            print(sheel)

            return None

    else:

        # Obtendo as informacoes da funcao original
        @resgateInformacao(func)
        def decorador(*args):
            "Reproduzindo a propria funcao"
            return func(*args)

    return decorador

# ==================================== #
if (__name__ == '__main__'):

    # Testando o decorador
    @meu_decorador
    def f(x,y=0):
        """f(x) -> float

        === Code ===
    def f(x):
        return x"""

        return x
# ==================================== #
