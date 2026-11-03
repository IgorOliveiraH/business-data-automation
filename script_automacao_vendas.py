import pandas as pd
from datetime import datetime

def processar_relatorio_vendas(caminho_entrada, caminho_saida):
    """
    Lê uma base de dados bruta de vendas/estoque, realiza a limpeza, 
    agrupa os dados por produto e exporta um relatório consolidado.
    """
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando processamento dos dados...")
    
    try:
        # Carregar os dados (simulando um dump de ERP ou plataforma de E-commerce)
        df = pd.read_csv(caminho_entrada, sep=';', encoding='utf-8')
        
        # Limpeza de dados: remover linhas com valores nulos nas colunas críticas
        df = df.dropna(subset=['Produto', 'Quantidade', 'Valor_Unitario'])
        
        # Criar coluna de Faturamento Total por linha
        df['Faturamento_Total'] = df['Quantidade'] * df['Valor_Unitario']
        
        # Agrupar por Produto para obter o total vendido e o faturamento global
        resumo = df.groupby('Produto').agg({
            'Quantidade': 'sum',
            'Faturamento_Total': 'sum'
        }).reset_index()
        
        # Ordenar pelos produtos que mais geraram faturamento
        resumo = resumo.sort_values(by='Faturamento_Total', ascending=False)
        
        # Exportar para Excel para a equipe de negócios/PCP
        resumo.to_excel(caminho_saida, index=False, sheet_name='Consolidado')
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Sucesso! Relatório salvo em: {caminho_saida}")
        
    except FileNotFoundError:
        print("Erro: Arquivo de entrada não encontrado. Verifique o caminho especificado.")
    except Exception as e:
        print(f"Ocorreu um erro durante a automação: {e}")

if __name__ == "__main__":
    # Nomes dos arquivos de teste (você pode criar um vendas_brutas.csv falso para testar)
    ARQUIVO_ENTRADA = 'vendas_brutas.csv'
    ARQUIVO_SAIDA = 'relatorio_consolidado_automatizado.xlsx'
    
    processar_relatorio_vendas(ARQUIVO_ENTRADA, ARQUIVO_SAIDA)
