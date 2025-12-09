import streamlit as st

def main():
    # --- 1. CONFIGURAÇÃO INICIAL E ESTILIZAÇÃO ---
    st.set_page_config(page_title="Apuração de Conformidade UG", layout="wide")

    # CSS para os cabeçalhos, títulos e cor do texto (Azul Escuro/Fundo Azul Claro)
    st.markdown("""
        <style>
        /* Estilo para simular o cabeçalho das colunas (Linha 7) */
        .header-item {
            background-color: #E6F0FF; /* Azul de tom mais claro */
            color: #003366; /* Azul escuro */
            padding: 8px;
            font-weight: bold;
            text-align: center;
            border-radius: 5px;
            margin-bottom: 5px;
            border: 1px solid #003366;
            height: 100%;
        }
        /* Estilo para o título da seção (Linha 6) */
        .main-title {
            background-color: #B3D9FF; 
            color: #003366;
            padding: 10px;
            font-size: 1.5em;
            font-weight: bold;
            text-align: center;
            border-radius: 5px;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        /* Estilo para o texto dos Itens (Azul Escuro) */
        .item-text {
            color: #003366;
            font-size: small;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # --- 2. LAYOUT DO CABEÇALHO (A1:F4) ---
    # Distribuição de largura: Logo/Título (2), Botão (1), Botão (1), Metadados (3)
    col1, col2, col3, col4 = st.columns([2, 1, 1, 3]) 

    # A1:B3 - TÍTULO EM TEXTO SUBSTITUINDO A LOGO
    with col1:
        st.markdown(
            """
            <h2 style='color: #003366; padding-top: 10px;'>Controladoria Geral</h2>
            <p style='color: #003366;'>Setor de Conformidade UG</p>
            """, 
            unsafe_allow_html=True
        )

    # C3:C4 - Botão CRIAR PASTA DO MÊS
    with col2:
        st.write(" ")
        if st.button("CRIAR PASTA DO MÊS", use_container_width=True):
            st.info("Ação: Pasta do mês criada!")

    # D3:D4 - Botão CONCLUIR CONFORMIDADE
    with col3:
        st.write(" ")
        if st.button("CONCLUIR CONFORMIDADE", use_container_width=True):
            st.success("Ação: Conformidade marcada como concluída!")

    # E3:F4 - Metadados (UNIDADE GESTORA e PERÍODO)
    with col4:
        # E3:F3 - UNIDADE GESTORA
        col_e3, col_f3 = st.columns([1, 2])
        with col_e3:
            st.markdown("<p style='text-align: right; margin-top: 10px; color: #003366; font-weight: bold;'>UNIDADE GESTORA:</p>", unsafe_allow_html=True)
        with col_f3:
            unidade_gestora = st.selectbox(
                'UG', 
                ['Selecione UG', '100001 SMG', '110001 CVL', '110006 ARQUIVO', '110008 SUBPAR', '120001 CGM'], 
                label_visibility="collapsed"
            )

        # E4:F4 - PERÍODO DE APURAÇÃO
        col_e4, col_f4 = st.columns([1, 2])
        with col_e4:
            st.markdown("<p style='text-align: right; margin-top: 10px; color: #003366; font-weight: bold;'>PERÍODO DE APURAÇÃO:</p>", unsafe_allow_html=True)
        with col_f4:
            periodo = st.text_input(
                'Período', 
                value='Insira a data aqui. Ex. DEZ-2025', 
                label_visibility="collapsed"
            )

    # --- 3. TÍTULO PRINCIPAL (LINHA 6) ---
    st.markdown('<div class="main-title">APURAÇÃO DA CONFORMIDADE DE UG</div>', unsafe_allow_html=True)
    
    # --- 4. FORMULÁRIO PRINCIPAL (st.form) ---
    with st.form(key='formulario_conformidade'):
        
        # A7:F7 - CABEÇALHOS DA TABELA (Linha 7)
        col_a7, col_b7, col_c7, col_d7, col_e7, col_f7 = st.columns([0.5, 2, 2, 3, 1.5, 3])

        # Usando CSS customizado para os cabeçalhos coloridos
        col_a7.markdown('<div class="header-item"> ITEM</div>', unsafe_allow_html=True)
        col_b7.markdown('<div class="header-item"> TÓPICO</div>', unsafe_allow_html=True)
        col_c7.markdown('<div class="header-item"> BASE PARA CONFERÊNCIA</div>', unsafe_allow_html=True)
        col_d7.markdown('<div class="header-item"> TESTE À REALIZAR</div>', unsafe_allow_html=True)
        col_e7.markdown('<div class="header-item"> CONFORMIDADE</div>', unsafe_allow_html=True)
        col_f7.markdown('<div class="header-item"> OBSERVAÇÕES</div>', unsafe_allow_html=True)
        
        # --- 5. ITEM 1: CONCILIAÇÃO BANCÁRIA (A8:F8) ---
        st.markdown('<div style="background-color: #B3D9FF; color: #003366; padding: 5px; font-weight: bold; margin-top: 10px;"> - 1- CONCILIAÇÃO BANCÁRIA</div>', unsafe_allow_html=True)

        # A9:F9 - SUB-ITEM 1.1
        col_a9, col_b9, col_c9, col_d9, col_e9, col_f9 = st.columns([0.5, 2, 2, 3, 1.5, 3])

        # A9: Número
        with col_a9:
            st.markdown("<p style='color: #003366; font-weight: bold; padding-top: 10px;'>1.1-</p>", unsafe_allow_html=True)

        # B9: Tópico/Pergunta (B9)
        with col_b9:
            st.markdown("<p class='item-text'>TODOS OS VALORES IDENTIFICADOS COMO RECEITAS QUE INGRESSARAM NAS CONTAS BANCÁRIAS FORAM DEVIDAMENTE REGISTRADOS NA CONTABILIDADE COM O DOCUMENTO SIAFIC (GR/OBR) CORRESPONDENTE?</p>", unsafe_allow_html=True)

        # C9: Base para Conferência (C9)
        with col_c9:
            st.markdown("<p class='item-text'>APLICAÇÃO SIAFIC CARIOCA: EXECUÇÃO > EXECUÇÃO FINANCEIRA > CONCILIAÇÃO BANCÁRIA</p>", unsafe_allow_html=True)

        # D9: Teste a Realizar (D9)
        with col_d9:
            st.markdown("<p class='item-text'>Verificar se todas as receitas recebidas e depositadas foram devidamente registradas, utilizando os documentos SIAFIC apropriados...</p>", unsafe_allow_html=True)

        # E9: CONFORMIDADE (Menu Suspenso E a Simulação de Cor)
        with col_e9:
            resposta_1_1 = st.selectbox(
                'Resposta 1.1',
                options=['Selecione', 'SIM', 'NÃO', 'N/A'],
                index=0,
                label_visibility="collapsed"
            )
            
            # SIMULAÇÃO DA COR DO FUNDO
            if resposta_1_1 == 'SIM':
                st.markdown('<div style="background-color: #D4EDDA; color: #155724; padding: 5px; border-radius: 5px; text-align: center;">✅ SIM (Fundo Verde)</div>', unsafe_allow_html=True)
            elif resposta_1_1 == 'NÃO':
                st.markdown('<div style="background-color: #F8D7DA; color: #721C24; padding: 5px; border-radius: 5px; text-align: center;">❌ NÃO (Fundo Vermelho)</div>', unsafe_allow_html=True)
            elif resposta_1_1 == 'N/A':
                 st.markdown('<div style="background-color: #F8F9FA; color: #6C757D; padding: 5px; border-radius: 5px; text-align: center;">⚪ N/A (Fundo Branco)</div>', unsafe_allow_html=True)

        # F9: OBSERVAÇÕES (Campo de Texto)
        with col_f9:
            observacoes_1_1 = st.text_area(
                "Observações 1.1", 
                height=100,
                label_visibility="collapsed"
            )

        # Botão de Envio do Formulário (Obrigatório)
        submitted = st.form_submit_button("Salvar Itens de Conformidade")
        
    # --- 6. PROCESSAMENTO DOS DADOS (APÓS SUBMISSÃO) ---
    if submitted:
        if unidade_gestora == 'UG Selecione' or resposta_1_1 == 'Selecione':
            st.error("Por favor, selecione a **Unidade Gestora** e responda ao **Item 1.1**.")
        else:
            st.success(f"✅ Formulário submetido para {unidade_gestora} no período {periodo}!")
            st.subheader("Dados Recebidos:")
            st.json({
                "Unidade Gestora": unidade_gestora,
                "Periodo de Apuracao": periodo,
                "Resposta 1.1 - Conformidade": resposta_1_1,
                "Observações 1.1": observacoes_1_1
            })


if __name__ == "__main__":
    main()
