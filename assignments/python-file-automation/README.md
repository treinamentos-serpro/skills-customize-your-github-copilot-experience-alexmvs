# 📘 Assignment: File Organizer with Python

## 🎯 Objective

Pratique automação de tarefas com Python usando `pathlib`, funções e operações seguras com arquivos para criar um organizador que classifica arquivos e mostra um plano antes de movê-los.

## 📝 Tasks

### 🛠️ Task 1: Categorize Files

#### Descrição
Crie uma função que examine a extensão de um arquivo e determine sua categoria. Considere imagens (`.png`, `.jpg`, `.jpeg`), documentos (`.pdf`, `.txt`, `.docx`), planilhas (`.csv`, `.xlsx`) e uma categoria `Other` para as demais extensões. A comparação deve funcionar mesmo quando a extensão estiver em maiúsculas.

#### Requisitos
O programa concluído deve:

- Implementar `categorize_file(file_path)` para retornar o nome da categoria do arquivo.
- Usar `pathlib.Path` para consultar a extensão.
- Classificar extensões não listadas como `Other`.
- Demonstrar a função com pelo menos um arquivo de cada categoria.

### 🛠️ Task 2: Preview an Organization Plan

#### Descrição
Leia somente os arquivos que estão diretamente dentro de uma pasta escolhida e gere uma prévia indicando a categoria de destino de cada arquivo. Nesta etapa, o programa não deve criar pastas nem mover arquivos.

#### Requisitos
O programa concluído deve:

- Implementar `build_plan(source_dir)` para retornar os caminhos de origem e destino planejados.
- Usar `pathlib.Path.iterdir()` e ignorar subpastas e outros itens que não sejam arquivos.
- Planejar destinos dentro de `organized/<categoria>/`, sem incluir a pasta `organized` na própria organização.
- Exibir a prévia sem modificar a pasta de origem.

### 🛠️ Task 3: Organize Files Safely

#### Descrição
Adicione a opção de executar o plano depois que o usuário conferir a prévia e confirmar a operação. Use uma pasta de teste com cópias de arquivos durante o desenvolvimento.

#### Requisitos
O programa concluído deve:

- Manter a prévia como comportamento padrão e pedir confirmação antes de mover qualquer arquivo.
- Criar as pastas de categoria somente quando a organização for confirmada.
- Mover os arquivos para seus destinos usando `shutil` ou `pathlib`.
- Não sobrescrever um arquivo que já exista no destino; informe que esse arquivo foi ignorado.
- Informar quando o caminho escolhido não existir ou não for uma pasta válida.