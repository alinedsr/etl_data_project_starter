"""This module contains functions for the ETL process."""

from .extract import extrair_dados_excel
from .transform import concatenat_arquivos_em_dataframe
from .load import criar_novo_excel
from .pipeline import executar_pipeline_completa