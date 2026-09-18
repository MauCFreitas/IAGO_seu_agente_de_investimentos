# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no IAGO |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores - Base de dados sobre atendimentos passados |
| `perfil_investidor2.json` | JSON | Personalizar recomendações - Base de adaptação de linguagem usada com o cliente |
| `produtos_investimentos.json` | JSON | Sugerir produtos adequados ao perfil - Conhecimento dos produtos |
| `movimentacoes.csv` | CSV | Analisar padrão de gastos do cliente - Compreender o histórico do cliente |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados foram atualizados para uma melhor adaptação as necessidades. 
Os dados mockados anteriores traziam clientes e referencias prévias baseados em um agente que atendesse em todos os sentidos,
Uma vez que IAGO faz suporte apenas para investidores, houveram necessidades de alteração no histórico, produtos e formato de interações (transações para movimentações)

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Para a leitura destes dados, o agente usará a linguagem Python para assimilar as informações contidas no banco de dados Em formato CSV e JSON:
```python
import pandas as pd
import json

## CSV
movimentações = pd.read_csv(r'data\movimentacoes.csv')
historico = pd.read_csv(r'data\historico_atendimento.csv')

## JSON
produtos = json.load(open(r'data\produtos_investimentos.json'))
perfil = json.load(open(r'data\perfil_investidor.json'))

```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```text
DADOS DO CLIENTE (data/perfil_investidor.json):
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado"
  }

MOVIMENTAÇÕES (data/transacoes.csv):
data,descricao,categoria,valor,tipo 
2026-11-03,Aporte CDB Liquidez Diária,renda\_fixa,1000.00,saida 
2026-11-05,Rendimento FIIs (Proventos),renda\_variavel,125.50,entrada 
2026-11-10,Aplicação Tesouro Selic 2029,renda\_fixa,500.00,saida 
2026-11-15,Resgate Parcial CDB,renda\_fixa,300.00,entrada 
2026-11-18,Compra Ações Bradesco (BBDC4),renda\_variavel,450.00,saida 
2026-11-22,Dividendo Ações,renda\_variavel,35.20,entrada 
2026-11-25,Aporte LCI - Imobiliário,renda\_fixa,1500.00,saida 
2026-11-28,Aporte Tesouro IPCA+,renda\_fixa,250.00,saida 
2026-12-02,Rendimento Caderneta de Poupança,renda\_fixa,18.40,entrada 
2026-12-05,Aporte LCA - Agronegócio,renda\_fixa,1000.00,saida



PRODUTOS DISPONÍVELS (data/produtos_financeiros.json):
[
    {
    "nome": "Poupança",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "0,5% ao mês; ou 70% da SELIC",
    "aporte_minimo": 0.0,
    "indicado_para": "curto prazo"
    },
    {
    "nome": "Tesouro Direto",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "Prefixada",
    "aporte_minimo": 30.0,
    "indicado_para": "iniciantes ou metas de longo prazo"
    },
    {
    "nome": "CDB",
    "categoria": "renda_fixa",
    "risco": "baixo a moderado",
    "rentabilidade": "Prefixada",
    "aporte_minimo": 1.0,
    "indicado_para": "metas de medio/longo prazo"        
    },
    {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "Prefixada isenta de IR",
    "aporte_minimo": 50.0,
    "indicado_para": "meta de longo prazo"        
    },
    {
    "nome": "CRI/CRA",
    "categoria": "renda_fixa",
    "risco": "medio",
    "rentabilidade": "Prefixada isenta de IR",
    "aporte_minimo": 1000.0,
    "indicado_para": "investidores experientes"
    },
    {
    "nome": "Debêntures",
    "categoria": "renda_fixa",
    "risco": "credito da empresa",
    "rentabilidade": "Superior a renda fixa, isenta de IR",
    "aporte_minimo": 1000.0,
    "indicado_para": "investidores experientes"
    },
    {
    "nome": "Renda Fixa",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "flutuante",
    "aporte_minimo": 30.0,
    "indicado_para": "investidores geridos profissionalmente"
    },
    {
    "nome": "Fundos Imobiliários",
    "categoria": "renda_variável",
    "risco": "médio",
    "rentabilidade": "dividendos mensais",
    "aporte_minimo": 100.0,
    "indicado_para": "investidores em busca de renda passiva mensal"
    },
    {
    "nome": "Ações",
    "categoria": "renda_variável",
    "risco": "alto",
    "rentabilidade": "valorização dos papeis em bolsa",
    "aporte_minimo": 10.0,
    "indicado_para": "clientes em busca de crescimento patrimonial"
    },
    {
    "nome": "ETFs",
    "categoria": "renda_variável ou fixa",
    "risco": "médio/alto",
    "rentabilidade": "Ibovespa e S&P",
    "aporte_minimo": 100.0,
    "indicado_para": "investidores geridos profissionalmente"
    },
    {
    "nome": "Fundos Multimercado",
    "categoria": "Renda Híbrida",
    "risco": "médio/alto",
    "rentabilidade": "ações, moedas, commodities",
    "aporte_minimo": 100.0,
    "indicado_para": "investidores que buscam menores riscos de investimento"
    }

]

HISTÓRICO DE ATENDIMENTO (data/historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade de CDBs,sim
2025-09-22,telefone,Dificuldade em entender investimento,Não encontrava informação disponibilizada,sim
2025-10-01,chat,Poupança,Cliente pediu explicação sobre o funcionamento taxa SELIC,sim
2025-10-12,chat,Metas financeiras,Cliente gostaria de compreender qual meta mais se encaixava em seu objetivo,sim

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Objetivo: Descobrir qual o melhor investimento para o seu perfil
- Meta: Investimento de longo prazo para melhorar a renda

Último investimento:
- 2026-12-05, Aporte LCA - Agronegócio, 1000.00, saida

Último retorno financeiro de investimentos:
- 2026-12-02, Rendimento Caderneta de Poupança, 18.40, entrada
```
