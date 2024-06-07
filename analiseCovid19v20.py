# Importando as ferramentas essenciais
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

# Definindo a cor de fundo para preto
st.markdown("""
<style>
body {
    background-color: #121212; /* Preto fosco */
}
</style>
""", unsafe_allow_html=True)

# Carregando e exibindo a imagem do mapa
st.image('mapaBrasil01.jpg', caption='Mapa do Brasil')

# Título e Introdução
st.title('Explorando o Impacto da Covid-19 no Brasil: Uma Análise por Estado')

st.write('A pandemia da COVID-19 impactou profundamente o Brasil, revelando disparidades regionais na propagação do vírus e seus efeitos. Este dashboard interativo permite explorar a progressão da pandemia em cada estado brasileiro, fornecendo insights valiosos para a compreensão da crise e a tomada de decisões estratégicas.')

# Carregando o dataset
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Análise Exploratória e Limpeza de Dados

# Olhando os dados de perto
st.write('## Vamos conhecer quais são os dados que vamos analizar?')
st.dataframe(df.head())

# Limpeza e Seleção
impacto_por_estado = df[['state', 'totalCases', 'deaths', 'totalCases_per_100k_inhabitants']].copy()
impacto_por_estado.dropna(inplace=True)
impacto_por_estado['totalCases'] = impacto_por_estado['totalCases'].astype(int)
impacto_por_estado['deaths'] = impacto_por_estado['deaths'].astype(int)

estados_agrupados = impacto_por_estado.groupby('state').sum()
estados_agrupados['deaths_per_100k_inhabitants'] = (estados_agrupados['deaths'] / estados_agrupados['totalCases']) * 100000
estados_agrupados = estados_agrupados.reset_index()


# Definindo as Regiões para Cada Estado
regioes = {
    'RO': 'Norte', 'AC': 'Norte', 'AM': 'Norte', 'RR': 'Norte', 'PA': 'Norte', 'AP': 'Norte', 'TO': 'Norte',
    'MA': 'Nordeste', 'PI': 'Nordeste', 'CE': 'Nordeste', 'RN': 'Nordeste', 'PB': 'Nordeste', 'PE': 'Nordeste', 'AL': 'Nordeste', 'SE': 'Nordeste', 'BA': 'Nordeste',
    'MG': 'Sudeste', 'ES': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'DF': 'Centro-Oeste', 
    'PR': 'Sul', 'SC': 'Sul', 'RS': 'Sul'
}
estados_agrupados['Regiao'] = estados_agrupados['state'].map(regioes)

# Criando o Dashboard Interativo com Streamlit

# Visualizando a Propagação Geográfica com Gráfico de Barras Interativo
st.write('## Visualizando a Propagação Geográfica')

# Storytelling: Justificando a Análise Geográfica
st.markdown("A análise geográfica da COVID-19 é crucial para entender como o vírus se espalhou pelo Brasil. Ao visualizar os dados por estado, podemos identificar regiões com maior ou menor incidência da doença, o que auxilia na aplicação de recursos, na implementação de políticas públicas e na tomada de decisões estratégicas.")

metrica_selecionada = st.selectbox('Selecione uma Métrica:', ['totalCases', 'deaths', 'deaths_per_100k_inhabitants'])

fig = px.bar(estados_agrupados, 
             x='state', 
             y=metrica_selecionada,
             color='Regiao',  # Colorindo as barras por região
             title='Impacto da COVID-19 por Estado',
             color_discrete_map={  # Personalizando as cores das regiões
                 'Norte': '#E3CF57', 
                 'Nordeste': '#00CED1', 
                 'Sudeste': '#9370DB', 
                 'Sul': '#32CD32', 
                 'Centro-Oeste': '#FF8C00'
             })

fig.update_layout(xaxis_title="Estado",
                  yaxis_title="Valor",
                  legend_title="Região")

st.plotly_chart(fig)

# Carregando e exibindo a imagem da COVID-19
imagem_covid = Image.open("virusCovid19.jpg") 

# Barra Lateral: Imagem e Storytelling
st.sidebar.markdown(
    """
    <style>
    /* Ajusta a largura da imagem na barra lateral */
    .sidebar .element-container img {
        width: 100% !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.image(imagem_covid)

st.sidebar.markdown(
    """
    <div style="text-align: justify;">
        A pandemia da COVID-19, causada pelo novo coronavírus (SARS-CoV-2), 
        impactou profundamente o mundo a partir de 2020. Desde então, 
        temos testemunhado os desafios e as transformações que este vírus 
        trouxe para a saúde global, a economia e o nosso dia a dia. 
    </div>
    """,
    unsafe_allow_html=True,
)


# Comparando o Impacto por Estados
st.write('## Comparando o Impacto por Estados')

numero_de_estados = st.slider("Selecione o Número de Estados a Exibir:", 5, len(estados_agrupados), 10)

top_estados = estados_agrupados.sort_values(by=metrica_selecionada, ascending=False).head(numero_de_estados)

fig = px.bar(top_estados.reset_index(),
            x="state",
            y=[ "totalCases", "deaths", 'deaths_per_100k_inhabitants'],
            title=f"Top {numero_de_estados} Estados por {metrica_selecionada}",
            barmode='group')

fig.update_layout(xaxis_title="Estado",
                yaxis_title="Valor",
                legend_title="Métrica")

st.plotly_chart(fig)

# Rodapé com Fonte de Dados
st.markdown("---")
st.write("**Fonte dos Dados:** [https://github.com/enps2015/covid19br]") 

# Rodapé com Créditos e Foto com Link para o LinkedIn
st.markdown("---")
st.markdown(
    """
    <div style="display: flex; align-items: center;">
        <p>Desenvolvido por <strong>@Eric Pimentel</strong>.</p>
        <a href="https://www.linkedin.com/in/eric-np-santos/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" 
                 style="width: 30px; height: 30px; margin-left: 10px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)