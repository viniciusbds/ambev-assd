# ambev assd <img src="/ufcg.png" alt="drawing" width="30"/>


<img src="/icon.png" alt="drawing" width="120"/> 



O ambev **ASSD** é um algoritmo de distribuição de estoques que busca equilibrar os SKUs dos depósitos da Ambev sejam eles dos centros de distribuição **(CDD)** ou das fábricas. O ASSD é consciente da natureza não linear das vendas dos produtos Ambev, que pode variar de acordo com cenarios, como por exemplo: um maior calor em determinada região, feriados regionais, ou simplesmente um desequilibrio em um CDD causado por grandes demandas de grandes supermercados ou revendedores.

O algoritmo implementa um mecanismo de otimização baseado em prioridades, no qual prioriza os depósitos com menor nível de estoque desejado, que pode variar com a demanda prevista esperada.

#### Objetivos / Métricas de interesse

- Garantir a disponibilidade dos SKUS em todos os estoques
- Evitar vencimento de produtos
- Reduzir custos de transporte durante a escolha dos fornecedores 
- Rebalancear os estoques de acordo com as demandas locais repentinas


#### Otimização

A otimização é feita em dois níveis:

1) A nível de distribuição, onde as produções das fábricas são distribuidas entre os CDDs buscando otimizar as métricas de interesse
2) A nível de depósito, onde se busca equilibrar os depósitos de acordo com a necessidade, quando um depósito fica desequilibrado, seja por:  
   - uma alta demanda, por exemplo, devido a grandes carradas feita por uma grande rede de supermercados;
   - ou quando um CDD não vende um SKU como esperava e fica com estoque excedente.


## Arquivo de apresentação

A apresentação em PDF deverá conter:

- [ ] Nome dos membros do time;

- [ ] Descrição do problema que a equipe selecionou para resolver durante o programa;

- [ ] Solução proposta para este problema, contendo descrição do cenário explorado durante o
desenvolvimento;

- [ ] Desenho da arquitetura da solução desenvolvida;

- [ ] Lista de bibliotecas utilizadas e ferramentas integradas (caso existam) da solução;

- [ ] Lista de features utilizadas durante o desenvolvimento da solução;

- [ ] Imagens da solução desenvolvida, mostrando o funcionamento do protótipo;

- [ ] Propostas futuras, indicando o que pode ser melhorado e proposta de novas funcionalidades.

- [ ] Inserir link do github no último slide da apresentação do projeto.

Importante: Desenvolvam a apresentação já pensando como base para um possível deck para ser
apresentado no evento Demoday, caso sua equipe seja selecionada.

## Repositório de código

O repositório no github deverá conter todo o código desenvolvido no protótipo, para que os mentores
possam avaliar corretamente o trabalho desenvolvido. Este repositório não deve conter a base de
dados disponibilizada no programa, conforme documento de confidencialidade assinado pelos membros
do time.
Além do código desenvolvido, as equipes devem disponibilizar documentação estilo markdown
contendo:

- [ ] Visão geral do projeto;

- [ ] Desenho da arquitetura da solução desenvolvida;

- [ ] Requisitos para execução da solução, como versão de sistema operacional ou de bibliotecas
externa (caso exista);

- [ ] Instrução de instalação ou arquivo de criação do ambiente (virtual environment);

- [ ] Instrução de execução do sistema;

- [ ] Link da apresentação descrita neste documento;

- [ ] Nome dos membros do projeto, podendo indicar a conta pessoal de github de cada membro.

Para ajudar a compreender a estrutura recomendada, segue exemplo de documentação disponibilizada
pela equipe AcademyHack: https://github.com/lahbs/modelo_academy_hack.

<img src="/ufcg.png" alt="drawing" width="100"/>


###### [Icon](./icon.png) made by [Freepik](https://www.flaticon.com/br/autores/freepik) from [www.flaticon.com](https://www.flaticon.com/br/)
