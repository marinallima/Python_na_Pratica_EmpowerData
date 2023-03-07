#!/usr/bin/env python
# coding: utf-8

# <img src="https://i.imgur.com/RCb4dXy.png" alt="Semana Python na Prática"/>

# <h2> O que vamos aprender nessa aula?</h2>
# 
# - **Criar nosso primeiro código em Python para:**
#     - imprimir dados na tela do computador
#     - receber dados do usuário
#     - entender o que são os tipos de dados
#     - converter tipos de dados
#     - utilizar variáveis para armazenar dados
#     - instalar e utilizar a biblioteca `fpdf`
#    
#     
#     
# - **Desafio da aula:**
#     - Você começou a aprender python e agora vai desenvolver um pequeno sistema para emitir orçamentos de forma automática.
#     - O orçamento deve ser emitido em **PDF** e **conter as seguintes informações**:
#         - Descrição do projeto
#         - Quantidade de horas estimadas no projeto
#         - Valor da hora trabalhada
#         - Prazo de entrega estimado
#         - Valor total estimado
#     
#     
#     

# <h2 style="color: #37709F">Nosso primeiro código em Python</h2>

# <h3 style="color: #2F666F">O ambiente Jupyter Notebook</h3>
# 
# - Células de texto (Markdown)
# - Células de código (Code)
# - Comentários no Python

# Isso é uma célula de texto

# In[1]:


# isso é um comentário no Python


# <h3 style="color: #2F666F">Imprimindo dados na tela do computador</h3>
# 
# - Para imprimir dados na tela do computador, utilizamos a função **print()**.

# In[2]:


print("Semana Python na Prática")


# In[3]:


print("Meu primeiro código")


# <h3 style="color: #2F666F">Tipos de Dados: textos e números</h3>
# 
# - Texto: **str**
# - Numérico:
#     - inteiro: **int**
#     - com casa decimal: **float**
#     - **ATENÇÃO:** o separador de cadas decimais no Python é o **ponto** e não a vírgula
#         - **10,3** (errado)
#         - **10.3** (correto)
# - Para verificar o tipo de dados, podemos utilizar a função **type()**.
# 
# 
# - **Operadores aritméticos:**
#     - adição: +
#     - subtração: -
#     - multiplicação: * (asterisco)
#     - divisão: / (barra)

# In[4]:


# isso é um tipo texto
print("10")


# In[5]:


type("10")


# In[6]:


# isso é um tipo numérico (número inteiro)
print(10)


# In[7]:


type(10)


# In[8]:


# isso é um tipo númerico (número com casa decimal)
print(10.5)


# In[9]:


type(10.5)


# In[10]:


print(10 + 1)


# In[11]:


print(10 -5)


# In[12]:


print(10 * 10)


# In[13]:


print(100 / 10)


# In[14]:


# CUIDADO!!!! Não podemos realizar cálculos com textos e nem entre tipos diferentes!
print("10 + 20")


# In[15]:


# gera um erro, pois estamos somando um texto com um número inteiro!
print("10" + 10)


# <h3 style="color: #2F666F">Recebendo dados do usuário</h3>
# 
# - Para receber dados de um usuário, podemos utilizar a função **input()**.

# In[ ]:


input()


# In[ ]:


input("Digite o seu nome: ")
input("Digite a sua idade: ")


# <h3 style="color: #2F666F">Variáveis: guardando informações</h3>
# 
# - Variáveis são **espaços na memória do computador** que o Python utiliza para guardar um dado.
# - Nome de variáveis não podem:
#     - ser palavras reservadas da linguagem
#     - começar com um número
#     - conter espaço em branco e nem caracteres especiais (acento, cedilha....etc)

# In[ ]:


nome = "Semana do Python na Prática"
print(nome)


# In[ ]:


numero1 = 10
numero2 = 20
resultado = numero1 + numero2
print(resultado)


# In[ ]:


nome = input("Digite o nome: ")
idade = input("Digite a sua idade: ")
peso = input("Digite o seu peso: ")


# In[ ]:


# CUIDADO! Todos os dados que digitamos no input() são TEXTO, mesmo os números!
type(nome)


# In[ ]:


type(idade)


# In[ ]:


type(peso)


# <img src="https://i.imgur.com/zf1e1Ys.png" alt="Convertendo tipos"/>

# - Para converter números em texto, podemos utilizar a função **str**.
# - Para converter textos em número, podemos utilizar as funções:
#     - **int:** para converter em um número inteiro
#     - **float:** para convert em um número com casas decimais

# In[ ]:


print(int(idade) + 10)


# In[ ]:


print(float(peso) + 10)


# In[ ]:


print(float("10.34"))


# In[ ]:


type(10)


# In[ ]:


type(str(10))


# <h3 style="color: #2F666F">Juntando textos com variáveis</h3>
# 
# - Para juntar textos com os dados de uma variável, podemos utilizar os **textos formatados**.
#     - basta utilizar um **f** antes das aspas do texto e colocar a **variável dentro de chaves**.

# In[ ]:


nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")


# In[ ]:


print(f"Meu nome é {nome} e eu tenho {idade} anos!")


# <img src="https://i.imgur.com/4tAd850.png" alt="Projeto da Aula" />

# <h3 style="color: #2F666F">Desenvolvendo as entradas de dados</h3>
# 
# - Descrição do projeto
# - Total de horas estimadas
# - Valor da hora de trabalho
# - Prazo de entrega estimado

# In[1]:


projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite o total de horas estimadas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo_estimado = input("Digite o prazo estimado: ")


# <h3 style="color: #2F666F">Criando o cálculo do valor total estimado</h3>
# 
# - **Cálculo:** `valor total estimado = total de horas estimadadas x valor da hora de trabalho`

# In[2]:


valor_total_estimado = int(horas_estimadas) * int(valor_hora)


# In[3]:


print(valor_total_estimado)


# <h3 style="color: #2F666F">Gerando o PDF com o orçamento</h3>

# <h4>Instalando a biblioteca</h4>

# In[4]:


get_ipython().system('pip install fpdf')


# In[5]:


# importando a biblioteca
from fpdf import FPDF


# <h4>Criando um arquivo PDF</h4>

# In[6]:


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")


# <h4>Inserindo os dados no PDF</h4>

# In[7]:


# utilizando um template
pdf.image("template.png", x=0, y=0 )

# inserindo os dados do projeto
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo_estimado)
pdf.text(115, 205, str(valor_total_estimado))


# <h4>Salvando o arquivo</h4>

# In[8]:


pdf.output("orçamento.pdf")
print("Orçamento gerado com sucesso!")


# <img src="https://i.imgur.com/Eff30Hw.png" alt="Parabéns" />
