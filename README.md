# Calculadora de Média com TDD
Este projeto implementa uma calculadora para calcular a média de três notas utilizando Test-Driven Development (TDD). Este guia explica como configurar o ambiente e executar os testes para verificar a corretude do código.

# Pré-requisitos
Python: Certifique-se de ter o Python instalado em seu sistema. Você pode verificar a instalação executando python --version no terminal.
Visual Studio Code (VS Code): É recomendado usar o VS Code como ambiente de desenvolvimento.
Extensão Python para VS Code: No VS Code, instale a extensão oficial de Python da Microsoft, que oferece suporte a testes e outras funcionalidades.

# Estrutura do Projeto
calcula_media.py: Arquivo com a função calcula_media, que calcula a média de três notas.
test_calcula_media.py: Arquivo contendo os testes unitários para validar o cálculo da média.
refatoracao_calcula_media.py: Versão refatorada da função calcula_media para melhorar a legibilidade.
Passo a Passo para Executar os Testes
## 1. Abra o Projeto no VS Code
Extraia o projeto para uma pasta no seu computador.
Abra o VS Code e selecione a pasta do projeto através de File > Open Folder.
## 2. Configurar o Ambiente de Testes
No VS Code, abra a Command Palette usando Ctrl + Shift + P (ou Cmd + Shift + P no macOS).
Digite Python: Configure Tests e selecione esta opção.
Escolha Unittest como o framework de testes.
Defina a pasta onde o arquivo de teste (test_calcula_media.py) está localizado. Geralmente, isso é a raiz do projeto.
## 3. Executar os Testes
Após configurar o ambiente, vá para a aba de Testes (ícone de tubo de ensaio) no lado esquerdo do VS Code.
Você verá o arquivo test_calcula_media.py listado com cada teste individual.
Para executar todos os testes, clique em Run All Tests.
Para executar um teste específico, clique no ícone de play ao lado do nome do teste.
##4. Interpretar os Resultados dos Testes
Check Verde: O teste foi executado com sucesso.
X Vermelho: O teste falhou. Clique na mensagem de erro para obter mais detalhes sobre o motivo da falha.

# Rodando os Testes pelo Terminal (Opcional)
Se preferir, você também pode executar os testes pelo terminal:
1. Abra o terminal no VS Code (ou qualquer terminal no seu sistema).
2. Navegue até a pasta do projeto.
3. Execute o comando:
python -m unittest test_calcula_media.py
4. Os resultados dos testes serão exibidos no terminal.
