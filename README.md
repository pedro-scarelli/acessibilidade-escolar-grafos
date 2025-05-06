# POC Acesso Escolar com Grafos

Este projeto é uma prova de conceito (POC) que demonstra como usar grafos para avaliar a acessibilidade de alunos à escola após bloqueios de ruas causados por fortes chuvas e alagamentos.

## 📖 Introdução

Após fortes chuvas, muitas ruas do bairro ficaram alagadas e intransitáveis. Este POC modela o bairro como um grafo, onde:

- **Nós** representam casas de alunos (Júlia, Antônio, Rafaela) e a escola.  
- **Arestas** representam ruas que ligam esses pontos.  

Bloqueios por alagamentos são simulados removendo-se arestas, e então avaliamos se cada aluno ainda consegue chegar à escola dentro do mesmo grafo (bairros sem sair dos limites).

---

## 🎯 Objetivo

- Representar o bairro como um grafo usando a biblioteca **NetworkX**.  
- Simular alagamentos removendo arestas.  
- Verificar a conectividade (número de caminhos) entre cada casa e a escola, antes e depois dos bloqueios.

---

## 📷 Representação visual do grafo

![image](https://github.com/user-attachments/assets/eec8d939-242a-41c5-9472-92704dd7064e)

---

## 🛠️ Ferramentas e Tecnologias

- **Python 3.7+**  
- **NetworkX** (para modelagem e análise de grafos)   ( https://networkx.org/documentation/stable/tutorial.html )

---

## 📦 Estrutura do Projeto

/
├── school_accessibility.py # Script principal que cria o grafo e faz as análises
├── requirements.txt # Dependências do projeto
└── README.md # Este arquivo


---

## ⚙️ Instalação e Uso

1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/poc-acesso-escolar-grafos.git
   cd poc-acesso-escolar-grafos
    ```
2. Crie um ambiente virtual e instale as dependências:  
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```  
3. Execute o script para ver os resultados:  
```bash
    python school_accessibility.py
```  
## 📊 Resultados
Conectividade Inicial (antes dos bloqueios)

    Júlia → Escola: 2 caminhos

    Rafaela → Escola: 2 caminhos

    Antônio → Escola: 1 caminho

## Conectividade Após Bloqueios (ruas alagadas removidas)

    Júlia → Escola: 1 caminho

    Rafaela → Escola: 1 caminho

    Antônio → Escola: 0 caminhos (acesso interrompido)

## ⚠️ Dificuldades Encontradas

    Modelagem no Grafo
    Traduzir um cenário real (ruas, alagamentos) em nós e arestas exige cuidado para garantir fidelidade da representação.

    Desempenho em Grafos Densos
    Em grafos com muitas conexões, a análise de conectividade pode ficar lenta, especialmente ao recalcular caminhos após cada remoção de aresta.

## 📝 Conclusão

Esta POC comprova que grafos são uma ferramenta eficaz para simular e avaliar acessibilidade em cenários de desastre (alagamentos). Usando NetworkX, conseguimos identificar rapidamente quais alunos perderam o acesso à escola e quantos caminhos alternativos permanecem disponíveis.
