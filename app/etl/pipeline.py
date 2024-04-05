"""This module contains functions for the ETL process."""

from extract import extrair_dados_excel
from transform import concatenat_arquivos_em_dataframe
from load import criar_novo_excel


def executar_pipeline_completa(input_folder, output_folder, output_file_name):
    """
    Função ETL: Extrai, Transforma e Carrega dados de arquivos Excel.

    type: input_folder: strs
    """
    data = extrair_dados_excel(input_folder)
    consolidated_df = concatenat_arquivos_em_dataframe(data)
    criar_novo_excel(consolidated_df, output_folder, output_file_name)