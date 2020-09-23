# Conversor-de-bases
Projeto criado como parte do portfólio da matéria "Fundamentos da Informática"

# Explicação do código

O código inicia-se declarando variáveis globais e pedindo pelo input do número a ser convertido e sua base, e da base alvo.

A próxima sessão transforma o número inicial informado em um número na base decimal, primeiro colocando todos os caracteres em uma lista, invertendo a ordem da lista e somando o valor da base inicial elevado ao valor posicional do caractere multiplicado pelo caractere em sí.

Essa sessão também é responsável por informar o usuário se o número inserido não estiver na base indicada e parar a execução se este for o caso.

A sessão final transforma o número, agora em base 10, para a base desejada. Para cada iteração do while é dividido o número na base 10 pela base alvo e armazenado o resto da operação em uma lista. No fim desse processo a ordem da lista é invertida e seus elementos são concatenados em uma string. Após isso o resultado é mostrado como saída para o usuário.

# Comentários e limitações

Devido a quantidade restrita de caracteres, não é possível a inserção de alguns números de bases superiores a 10 como número a ser convertido. Exemplo:

•	11 (base decimal) na base 13 não é inserível como não existe um caractere único para 11.

Isso poderia ser resolvido implementando o uso de caracteres alfabéticos e um sistema de nomenclatura incremental para os algarismos, mas em função da rasa pertinência do projeto isso não será realizado.
