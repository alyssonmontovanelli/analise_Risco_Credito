# Mapeamento de variaveis


# Mapeamento título de variáveis
map_titulo_variaveis = {
 'person_age': 'Idade',
 'person_income': 'Renda_Anual',
 'person_home_ownership': 'Tipo_Moradia',
 'person_emp_length':'Anos_no_Emprego',
 'loan_intent':'Motivo_Emprestimo',
 'loan_grade': 'Grau_Emprestimo',
 'loan_amnt': 'Valor',
 'loan_int_rate': 'Taxa_Juros',
 'loan_status': 'Status_Pagamento', # Classe que utilizarei para as previsões (0 = pagou o imprestimo, 1 = Não pagou)
 'loan_percent_income': 'Comprometimento_Renda',
 'cb_person_default_on_file': 'Inadimplencia_Historica',
 'cb_person_cred_hist_length': 'Duracao_Historico_Credito',
}


# Mapeamento Variavel Tipo_Moradia
map_tipo_moradia = {
 'RENT':'Aluguel',
 'OWN': 'Próprio',
 'MORTGAGE': 'Hipoteca',
 'OTHER': 'Outro'
}


# Mapeamento Variavel Motivo_Emprestimo
map_motivo_emprestimo = {
 'PERSONAL': 'Pessoal',
 'EDUCATION': 'Educação',
 'MEDICAL': 'Médico',
 'VENTURE': 'Empreendimento',
 'HOMEIMPROVEMENT': 'Reformas Domésticas',
 'DEBTCONSOLIDATION': 'Consolidação Dívidas'
}

map_inadimplencia_historica = {
 'N': 'Não',
 'Y': 'Sim'
}