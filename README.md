# benford
Comparação dos dados eleitorais de 2018 com o esperado da lei de Benford

Lei de Benford (fonte: wikipedia)
A lei de Benford, também chamada de lei do primeiro dígito,lei de Newcomb-Benford e lei números anômalos refere-se à distribuição de dígitos em várias fontes de casos reais. Ao contrário da homogeneidade esperada, a lei afirma que em muitas coleções de números que ocorrem naturalmente, o primeiro dígito significativo provavelmente será pequeno. Sem homogeneidade, esta distribuição mostra que o dígito 1 tem 30% de chance de aparecer em um conjunto de dados estatísticos enquanto valores maiores tem menos possibilidade de aparecer.
Resumindo, para um conjunto grande de valores que acontecem naturalmente, o primeiro número desses valores (1 em 1543, 6 em 645, por exemplo) tende a ser um número pequeno. É uma tendência que surge quando esses valores podem variar em muitas ordens de grandeza, isto é, os valores podem ser perto de 1, 10, 100, 1000, 10000, ou assim por diante. 
Se for um conjunto pequeno de valores ou se os valores forem muito próximos (poucas ordens de grandeza), a distribuição não vai seguir essa tendência.

Dados de entrada:
Os dados para a eleição de 2018 foram obtidos da página Repositório de Dados Eleitorais, do TSE, no link "Votação nominal por município e zona (formato ZIP)". Para presidente, usei como entrada apenas o arquivo terminado em 'BR'.
Nesse arquivo, cada linha tem o número de votos AA que o candidato BB recebeu na zona eleitoral CC, na cidade DD e estado EE.
No total, foram mais de 80 mil zonas, com a votação de cada um dos 13 candidatos. Não constam os votos nulos e brancos, que só aparecem nos boletins de urna, também disponíveis no site do TSE.

Dados de saída:
Exporta gráficos com a distribuição dos primeiros dígitos das votações por zona eleitoral em cada candidato.
Gera um gráfico com os dados nacionais para cada candidato (cand_XX.png) e um com os dados separados por estado para cada candidato (cand_XX_YY.png). O estado ZZ aponta as zonas de votação no Exterior.

Funcionamento do programa:
Para cada arquivo na pasta 'dados/', ele varre cada linha buscando o número de votos AA que o candidato BB recebeu na zona eleitoral CC, na cidade DD e estado EE.
Depois cria para cada candidato um contador que mede o número de vezes que cada dígito aparece em cada uma das zonas. Um contador nacional, um contador para cada estado e um para cada região do Brasil. Para facilitar a comparação, isso é normalizado para cada contador, de modo que tenhamos o percentual de vezes que cada dígito apareceu e não o número total.
Calcula a distribuição esperada da lei de Benford.
É criado um gráfico com uma linha azul (lei de Benford) e pontos vermelhos (dados reais). O título é "'Candidato N: XX" para os gráficos com os dados nacionais, "Candidato N: XX no estado: YY" com os dados estaduais, e "Candidato N: XX na regiao: YY" com os dados regionais. 
Dentro do gráfico, temos um valor de sigma, que é a distância média dos pontos para a linha azul. Se sigma = 2%, isso quer dizer que os pontos vermelhos estão, em média, 2% a mais ou a menos do que o esperado. Por exemplo, o digito '5' deve aparecer com 8% de probabilidade. Com sigma = 2%, o ponto vermelho deve estar entre 6% e 10%.
No total, são criados 442 gráficos: 1 Nacional, 5 Regionais, 26 estaduais, 1 Distrito Federal e 1 Exterior, para cada candidato.

Avaliação dos resultados:
Devemos lembrar que: "Se for um conjunto pequeno de valores ou se os valores forem muito próximos (poucas ordens de grandeza), a distribuição não vai seguir essa tendência." Vemos que os valores de sigma aumentam para os menores estados e para os candidatos com o menor número de votos. Quanto maior o conjunto de dados (SP, por exemplo), mais próximos os pontos vermelha estão da linha azul.
Se aparecer um sigma alto em um dos conjuntos grandes de dados, isso pode (pode, não deve) ser indicio de uma alteração dos dados. Se os pontos vermelhos para os números 7, 8 ou 9 estiver muito longe da reta azul, por exemplo.

Lição aprendida: 
O modelo matemático funciona para aquilo que ele se propõe: distribuição de muitos números em várias ordens de grandeza. Se isso não é verdade, o modelo não vai bater.

"Não importa quão bonita é a sua teoria, não importa quão inteligente você é. Se não concorda com o experimento, está errado." - Richard P. Feynman 


obs.:
esse código foi um teste para saber se já consigo programar alguma coisa que preste em Python. Não deve estar otimizado e deve ter maneiras mais espertas de fazer.
