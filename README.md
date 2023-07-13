# PythonScripts
Small Python Scripts designed to automate everyday tasks

Primeiros Passos em Python <img src="https://img.icons8.com/?size=512&id=13441&format=png" width="40" height="40"/> 
Em versão <img src="https://img.icons8.com/?size=512&id=FSg5vsN-OnMt&format=png" width="40" height="40"/>

## Project Moodle Data Converter
### Sobre o Projeto
O Moodle (Modular Object-Oriented Dynamic Learning Environment) é um Ambiente Virtual de Aprendizagem (AVA) de código aberto (open source), ou seja, seu código fonte é aberto para a comunidade de usuários, tornando possível alterá-lo e customizá-lo, criando funcionalidades totalmente inovadoras e que venham a suprimir as necessidades das instituições de ensino, além, é claro, de contribuir com o seu desenvolvimento. 

Outro ponto é sua gratuidade, portanto, qualquer instituição pode ter o seu próprio Ambiente Virtual de Aprendizagem, bastando apenas que faça download do código fonte do Moodle no site oficial (https://moodle.org) e o instale e um servidor Web com PHP e MySQL.

Atualmente grande parte das instituições de ensino privadas ou públicas, de ensino básico ou superior, utilizam o Moodle, dado a sua confiabilidade e robustez em termos de funcionalidade. O Moodle permite que novos recursos possam ser incorporados através de plugins e add-ons. 

Pensando em processos que auxiliem professores, mentores e criadores de curso, iniciei um pequeno projeto em Python, com o objetivo de expandir conhecimentos e habilidades para minha graduação em Engenharia de Software e cursos de pós-graduação em andamento.

### Objetivo
Atualmente atuo como professor conteudista, coordenador e design educacional de cursos de graduação e pós-graduação. A ideia nasceu como parte de auxiliar no processo de conversão de bancos de questões em em formato Microsoft Word (.docx) ou Plain Text (.txt) para a sintaxe GIFT do Moodle.

Outro módulo adicionado, ainda em processo de testes é a conversão dos relatórios de notas em formato Microsoft Excel (.xlsx) para HTML e Excel, porém, organizando os alunos e agrupandos pela condição de <i>"Aprovado"</i> ou <i>"Reprovado"</i>.

Todos os dias importamos conteúdos para o banco de questões do Moodle. Os professores disponibilizam as questões em formato Microsoft Word (.docx) ou Plain Text (.txt).

### Versões
Todos os scripts estão em desenvolvimento. Algumas delas, as executadas via terminal, são funcionais e podem ser utilizadas, basta observar a correta inserção dos nomes dos arquivos.

### Critérios
#### Conversão de Questões para sintaxe GIFT
Para conversão dos arquivo para a sintaxe GIFT do Moodle, as questões em formato .docx devem ter alguns requisitos de formatação e organização:
 - Sempre a alternativa A deve ser a correta.
 - 5 alternativas, de A até E.
 - As alternativas devem ser digitadas, ou seja, sem o uso de numeração automática.
 - Os mesmos critérios valem para arquivos de texto (.txt)


#### Somatória e Organização de Notas
Para a somatória de notas e organização dos alunos em aprovados e reprovados, você deve exportar do sistema de relatórios do Moodle, o arquivo em formato .csv ou , caso o faça em formato .xlsx.

Atualmente o script não está vinculado efetivamente ao script desktop(Tkinter), porém, o script calcular-notas-export-excel.py e calcular-notas-export-html.py são funcionais, basta observar o nome do arquivo de entrada.