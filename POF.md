Proof of Concept: Verificando Acessibilidade da Escola Após Alagamentos Usando Grafos

1. Introdução
Este POC aborda o problema da acessibilidade escolar de Júlia e seus amigos (Antônio e Rafaela) após fortes chuvas que alagaram ruas do bairro. A proposta é representar o bairro como um grafo e usar ferramentas para verificar se todos ainda conseguem acessar a escola sem sair do bairro, mesmo com ruas bloqueadas.

2. Objetivo
Demonstrar a viabilidade de usar a biblioteca NetworkX para:

Representar um bairro como um grafo.
Simular alagamentos por meio da remoção de arestas (ruas bloqueadas).
Avaliar a conectividade dos nós (casas e escola) antes e depois dos alagamentos.

3. Ferramentas e Metodologia
Ferramenta utilizada: NetworkX.

Metodologia:
Criar o grafo representando as conexões do bairro.
Avaliar a conectividade inicial.
Simular alagamentos removendo arestas.
Avaliar a conectividade após os bloqueios.

4. Implementação


5. Resultados
Conectividade Inicial
Antes dos bloqueios:

Julia -> Escola: 2
Rafaela -> Escola: 2
Antonio -> Escola: 1
Júlia e Rafaela possuem múltiplos caminhos para a escola.
Antônio possui apenas um caminho..

Conectividade após a remoção das ruas alagadas:

Julia -> Escola: 1
Rafaela -> Escola: 1
Antonio -> Escola: 0
Júlia e Rafaela ainda conseguem acessar a escola, mas agora possuem apenas um caminho.
Antônio não consegue mais acessar a escola.

6. Dificuldades Encontradas
Modelagem do Problema no Grafo:
Representar um problema real (bairro com ruas alagadas) em um grafo exige cuidado para garantir que os nós e arestas refletem a situação corretamente.

Desempenho em Grafos Densos:
Quando o grafo contém muitas arestas, a complexidade computacional dos algoritmos de conectividade pode aumentar consideravelmente. Isso pode resultar em tempos de execução mais longos e, em casos extremos, causar sobrecarga de processamento, dificultando a análise de conectividade, especialmente em grafos de grande escala.

7. Conclusão
A POC comprovou a eficácia do uso de grafos para modelar problemas de acessibilidade em um bairro após alagamentos. A biblioteca NetworkX forneceu ferramentas poderosas para simular o problema e calcular a conectividade.

Os resultados mostram que, apesar dos bloqueios, Júlia e Rafaela podem acessar a escola, mas Antônio ficou isolado.