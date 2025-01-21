# filter_sisu_courses

## Contexto e Objetivo
Ao precisar filtrar cursos cadastrados no MEC/disponibilizados no SISU para identificar quais possuem a possibilidade de serem realizados na modalidade EaD, iniciei a busca por uma API oficial do SISU/MEC que facilitasse essa filtragem. No entanto, não obtive sucesso em localizar uma documentação oficial ou uma API específica para essa finalidade. Durante minha pesquisa, encontrei no GitHub alguns scripts que utilizavam endpoints de uma API não documentada, mas ainda funcional.

O script que desenvolvi utiliza esses endpoints para filtrar os cursos conforme minha necessidade inicial. Como o objetivo era obter resultados rápidos e visualizáveis, não implementei funcionalidades adicionais, como a exportação dos dados para um arquivo CSV ou outros formatos de armazenamento.

## Usabilidade
Este script tem como principal função retornar/imprimir os cursos EaD disponíveis no SISU. No entanto, ele pode ser facilmente adaptado para realizar outros tipos de filtragem, conforme a conveniência do usuário. Para isso, basta modificar a lógica da função ``get_institution_offers_data``, utilizando os dados retornados pelos endpoints. Prints de exemplos de dados estão disponíveis para referência no último tópico dessa documentação.

## Pré-requisitos
- Python
- Lib: Requests

## Exemplos de dados retornados
![image](https://github.com/user-attachments/assets/44045981-8c4a-4a9a-beda-ad0947b08936)
![image](https://github.com/user-attachments/assets/5416f61d-0048-407e-a70b-37f19f51eaa4)
