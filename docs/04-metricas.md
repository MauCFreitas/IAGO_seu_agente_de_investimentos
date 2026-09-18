# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Recomendação de investimentos
- **Pergunta:** "qual opção de investimento me traria retorno mensal?"
- **Resposta esperada:**
"CDB – pode ter cupons periódicos, mas o mais comum é pagar no vencimento.
LCI/LCA – geralmente pagam no vencimento; algumas versões podem ter cupons.
CRI/CRA – costumam pagar juros periódicos, mas dependem do título.
Debêntures – costumam pagar juros periódicos, mas dependem do emissor e do papel.

Ponto importante
Como seu perfil está como(...)"


### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:**  
"Perdão, não possuo essa informação em meu banco de dados. Sou especializado em investimentos e não tenho acesso à previsão do tempo. 😊

Posso te ajudar com alguma dúvida sobre investimentos?"


### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:**
"Perdão, não possuo essa informação em meu banco de dados.

Se o seu interesse é investir em empresas ligadas ao setor de(...)

Mas é importante lembrar: não posso recomendar nenhuma delas. Posso explicar como funcionam, os riscos envolvidos e os indicadores que costumam ser analisados."
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Resultados
modelos utilizados:  
Qwen 2.5:0.5b - Não correspondeu as expectativas. Apesar de apresentar respostas rápidas, não respondia de maneira adequada.
Qwen 2.5:3b - Teve um desempenho melhor que a versão anterior, mas ainda parece meio despreparado.  
Por ausencia de características tecnológicas no computador, os testes pararam por aqui

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O agente respondeu de forma adequada aos questionamentos;
- Não aceitou fugir do tema;
- Apresentou dados baseados em fontes, apenas;

**O que pode melhorar:**
- Por serem versões mais fracas, e com baixo poder de processamento, as respostas, apesar de corretas pareceram meio cruas e sem preparo. - Melhores treinamentos podem resolver este ponto
- Uma interação mais adaptativa ao tipo de comunicação do usuário.