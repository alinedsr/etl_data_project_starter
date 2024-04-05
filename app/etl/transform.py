"""modulo com todas as transformações necessárias para consolidar os dados de entrada."""
import pandas as pd

def concatenat_arquivos_em_dataframe(all_data):
    """
    função para consolidar os dados de arquivos Excel.

    type: all_data: list
    """
    if not all_data:
        raise ValueError("No data to transform")
    consolidated_df = pd.concat(all_data, axis=0, ignore_index=True)
    return consolidated_df