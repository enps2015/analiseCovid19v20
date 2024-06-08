# analiseCovid19v20
Este repositório contém os arquivos do novo aplicativo Streamlit da Análise da Covid-19 versão 2.0

## Explorando o Impacto da COVID-19 no Brasil: Uma Análise por Estado

### Descrição do Projeto

Este projeto de Ciência de Dados, desenvolvido com Python e Streamlit, analisa o impacto da pandemia da COVID-19 no Brasil, com foco na propagação do vírus em cada estado. O objetivo é fornecer um dashboard interativo que permita aos usuários explorar os dados e obter insights relevantes sobre a crise. 

**Acesse o aplicativo online:** [https://aplicativocovid19ericv20.streamlit.app/](https://aplicativocovid19ericv20.streamlit.app/)

### Funcionalidades

- **Visualização de Dados por Estado:** O dashboard exibe um gráfico de barras interativo que compara diferentes métricas (total de casos, óbitos e taxa de mortalidade por 100 mil habitantes) entre os estados brasileiros.
- **Análise Geográfica:** As barras do gráfico são coloridas por região, permitindo identificar padrões regionais na propagação da COVID-19.
- **Storytelling:** O aplicativo inclui textos explicativos que contextualizam a análise e destacam a importância de entender o impacto da pandemia em diferentes áreas do país.
- **Interface Intuitiva:**  O Streamlit proporciona uma interface amigável e fácil de usar, tornando a análise acessível a um público amplo.

### Como Executar o Projeto

1. **Requisitos:** Certifique-se de ter o Python instalado em sua máquina.
2. **Bibliotecas:** Instale as bibliotecas necessárias: `streamlit`, `pandas`, `plotly`.
3. **Clone o Repositório:** Clone este repositório para o seu computador.
4. **Executar o Aplicativo:** Navegue até a pasta do projeto no seu terminal e execute o comando `streamlit run seu_script.py`, substituindo `seu_script.py` pelo nome do arquivo Python do projeto.

### Desafios Encontrados

- **Integração de Mapa Interativo:** Inicialmente, o projeto previa um mapa de calor interativo do Brasil, mas a implementação apresentou desafios inesperados, levando à escolha de uma visualização alternativa (gráfico de barras com cores por região).
- **Responsividade da Imagem na Barra Lateral:** Foi necessário usar CSS para garantir que a imagem na barra lateral se ajustasse corretamente ao espaço disponível em diferentes tamanhos de tela.

### Soluções Encontradas

- **Visualização Alternativa:**  Em vez do mapa de calor, optou-se por um gráfico de barras interativo, que se mostrou mais eficiente para a comparação direta entre os estados.
- **CSS para Responsividade:** O uso de CSS permitiu controlar o tamanho da imagem na barra lateral, tornando-a responsiva e visualmente agradável.

### Lições Aprendidas e Próximos Passos

- **Flexibilidade na Visualização de Dados:**  A experiência com o mapa de calor reforçou a importância de ser flexível e buscar alternativas quando uma visualização se mostra problemática.
- **Poder do CSS no Streamlit:** O projeto permitiu explorar as capacidades de personalização do Streamlit com CSS, abrindo portas para designs mais sofisticados no futuro.
- **Próximos Passos:** Expandir o dashboard com mais dados e funcionalidades, como a análise temporal da pandemia e a inclusão de outros indicadores de saúde.

### Captura de Telas

**Tela Principal:**

Imagem do dashboard principal

![capturaTela001](https://github.com/enps2015/analiseCovid19v20/assets/84017071/9027d1fe-a442-4227-a528-bdd0c46896a4)

![capturaTela002](https://github.com/enps2015/analiseCovid19v20/assets/84017071/c55827b8-ca63-4ea1-9bf9-bdb5a5826d82)

![capturaTela003](https://github.com/enps2015/analiseCovid19v20/assets/84017071/49a388d4-02d3-478b-95b3-5684f4dc5b07)

![capturaTela004](https://github.com/enps2015/analiseCovid19v20/assets/84017071/4024ff74-1a4d-4d25-9ddf-d36157512b38)

https://github.com/enps2015/analiseCovid19v20/assets/84017071/e7612e45-98f8-44e5-ad7e-c0d434a94a65


**Barra Lateral:**

Imagem da barra lateral

![capturaTela005](https://github.com/enps2015/analiseCovid19v20/assets/84017071/5f743176-401c-47bd-a44e-309adff98581)



