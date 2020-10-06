# Conversor-de-bases
Projeto criado como parte do portfólio da matéria "Fundamentos da Informática"

# Explicação do código

O código inicia-se declarando uma lista de símbolos a serem usados como algarismos. Essa lista pode ser incrementada indeterminadamente para adicionar mais símbolos, permitindo a diferenciação de letras maiúsculas e minúsculas, o uso de caracteres especiais ou a criação de algarismos representados por mais de um símbolo. O valor dos símbolos nessa lista varia em função do seu posicionamento na mesma de forma crescente, assim novos símbolos de valor mais alto devem ser adicionados no final da lista.

A primeira função transforma o número inicial informado em um número na base decimal, primeiro colocando todos os caracteres em uma lista, invertendo a ordem da lista e somando o valor da base inicial elevado ao valor posicional do caractere multiplicado pelo caractere em sí.

A segunda função transforma o número, agora em base 10, para a base desejada. Para cada iteração do while é dividido o número na base 10 pela base alvo e armazenado o resto da operação em uma lista. No fim desse processo a ordem da lista é invertida e seus elementos são concatenados em uma string.

A última função é uma combinação das duas funções anteriores criada visando a organização do código e simplicidade no uso das funções. Ela transforma um número de base qualquer em um número de outra base qualquer.

A sessão final recebe a entrada do usuário, usa as funções criadas para calcular o resultado desejado e o imprime na tela como saída.
