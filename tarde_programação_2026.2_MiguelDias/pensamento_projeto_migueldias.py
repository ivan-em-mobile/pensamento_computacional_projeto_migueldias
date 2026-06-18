'''
>> Projeto Açaiteria

>PO (Product Owner)
Como proprietário do negócio, desejo um sistema de gestão para minha açaiteria,
 permitindo acompanhar vendas,
 controlar produtos e administrar as operações de forma organizada.
 
>QA (Quality Assurance)
Como cliente, desejo utilizar um sistema de compras simples e eficiente,
 para adquirir meus produtos preferidos com rapidez,
 praticidade e segurança.

>Tech (Tecnologia)
Como desenvolvedor, desejo criar uma plataforma de vendas para a açaiteria, garantindo que o sistema seja estável,
eficiente e atenda às necessidades do negócio.

>Dev (Desenvolvimento)
Como programador, desejo implementar os recursos necessários no sistema,
 assegurando que ele suporte as demandas da empresa e proporcione uma boa experiência aos clientes.

>UX (Experiência do Usuário)
Como designer de experiência do usuário, desejo desenvolver uma interface moderna,
 intuitiva e agradável, facilitando a navegação e tornando o processo de compra mais satisfatório.

>IA (Inteligência Analítica)
Como analista de dados, desejo que o sistema registre e processe informações sobre as vendas,
 permitindo identificar tendências de consumo e auxiliar na tomada de decisões sobre estoque e marketing.

 '''

# Ufa, quebrei a maldição
# print('Olá mundo!')
# print('\n------------------------------------------------\n')


print('-' * 48 + '\n')
print('Bem-vindo ao Sistema de vendas - açaiteria!\n')
print('1 - Cadastrar produto')
print('2 - Listar produtos')
print('3 - Realizar venda')
print('4 - Combos de açai')
print('5 - Bebidas')
print('6 - Sobre nós')
print('7 - Fale conosco')
print('8 - Envie seu feedback')
print('9 - Recomendações')
print('0 - Sair do sistema')
print('\n-------------------------------------------------------\n')
 
opcao__definida = int(input('Digite a opção desejada:'))

if opcao__definida == 1: 
    print('Cadastrando poduto...')

elif opcao__definida == 2: 
    print('Listando poduto...')

elif opcao__definida == 3: 
    print('Realizando venda...')

elif opcao__definida == 4: 
    print('Combos de açai...')

elif opcao__definida == 5: 
    print('Bebidas...')

elif opcao__definida == 6: 
    print('Sobre nós...')

elif opcao__definida == 7: 
    print('Fale conosco...')

elif opcao__definida == 8: 
    print('Envie seu feedback...')

elif opcao__definida == 9: 
    print('Recomendações...')

elif opcao__definida == 0: 
    print('Sair do sistema...')
    
else: print('A interação falhou, tente novamente')

        