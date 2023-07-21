# Gerador de Relatório de Notas

## Descrição
O Moodle (Modular Object-Oriented Dynamic Learning Environment) é um Ambiente Virtual de Aprendizagem (AVA) de código aberto (open source) e, dentre suas várias funcionalidades, permite exportar relatórios de notas de atividades disponibilizadas para os alunos.

A principal função desta aplicação é trabalhar com arquivos exportados em formato Excel do sistema de relatório de notas com as seguintes funcionalidades:
- Unir as duas colunas Nome e Sobrenome em uma única definida como 'Nome do Aluno.
- Somar as nota das atividades conforme parâmetros definidos na função calcular_nota. A função atual realiza o cálculo de três atividades e, por meio de uma fórmula, defini se o aluno é considerado aprovado ou reprovado.
- Por padrão, o Moodle exporta o nome das atividades, portanto, caso quem venha utilizar esta aplicação não queira adotar o padrão estabelecido, ou até mesmo implementar um número maior de atividades, deve modificar a função calcular_nota ou a primeira coluna do arquivo em Excel. Os nomes das colunas que constam as notas devem ser as mesmas descritas na função.

## Requisitos
- Python 3.11 ou superior
- Módulos:
    - pandas
    - openpyxl
    - os
    - io
    - html
    - xlsxwriter

## Funcionamento
Ao executar a aplicação, um servidor Flask é iniciado e possibilita ao usuário calcular e gerar notas de alunos conforme regras descritas da função calcular_nota. 

O objetivo é trabalhar com arquivos exportados do sistema de Relatório de Notas do Moodle.
Poder ser executado via Terminal via py.exe ou python.exe app.py ou, para usuários do Windows, via arquivo .bat.

O arquivo do Excel enviado tem 4 colunas, Nome, Sobrenome, e os 3 tipos de notas. Irá juntar o nome e o sobrenome em uma única coluna e calcular a nota final do aluno.

O resultado, inicialmente será gerado em formato HTML, podendo o usuário optar em baixar em formato Excel através do botão *Baixar resultados em Excel*.

Os arquivos enviados são armazenados na pasta upload e os gerados em Excel na pasta Download.

Atualmente os arquivos result.html e result.xlsx armazenam apenas os últimos resultados, portanto, a cada novo processamento, os dados antigos são sobreescritos.
