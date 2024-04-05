"""
Módulo de consolidação dos dados de entrada.

"""
import os

def criar_novo_excel(df, output_folder, output_file_name):
    """
    Carga: Salva um DataFrame em um arquivo Excel.

    type: df: pd.DataFrame
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df.to_excel(
        os.path.join(output_folder, output_file_name), index=False
    )  # Retirado engine='openpyxl'