from Pessoa import PessoaFisica, Endereco, PessoaJuridica       
from datetime import date, datetime

def main():
    lista_pf = []
    lista_pj = []

    while True:
        opcao = int(input("Escolha uma opcao: 1 - Pessoa Fisica / 2 - Pessoa Juridica / 0 - Sair: "))
        if opcao == 1:
            while True:
                opcao_pf = int(input("Escolha uma opcao: 1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 3 - Remover CPF / 4 - Voltar ao menu anterior: "))

                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("Digite o nome da pessoa fisica: ")
                    novapf.cpf = input("Digite o CPF: ")
                    novapf.rendimento = float(input("Digite o rendimento mensal (Digite somente numeros): "))

                    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos.")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")
                        continue 

                    novo_end_pf.logradouro = input("Digite o logradouro: ")
                    novo_end_pf.numero = input("Digite o numero: ")
                    end_comercial = input("Este endereco é comercial? S/N: ")
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == "S"

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                    print("Cadastro realizado com sucesso!!")

                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome}")
                            print(f"CPF: {cada_pf.cpf}")
                            print(f"Endereco: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}")
                            print(f"Data Nascimento: {cada_pf.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print("Digite 0 para sair.")
                            input()
                    else:
                        print("Lista Vazia")

                elif opcao_pf == 3:
                    remover_cpf = input("Digite o CPF da pessoa fisica que deseja excluir: ") 
                    pessoa_encontrada = False

                    for cada_pf in lista_pf:
                        if cada_pf.cpf == remover_cpf:
                            lista_pf.remove(cada_pf)
                            print(f"CPF {remover_cpf} foi removido.")
                            pessoa_encontrada = True
                            break

                    if not pessoa_encontrada:
                        print("Nenhum CPF foi encontrado.")

                elif opcao_pf == 4:
                    print("Voltando ao menu anterior.")
                    break

                else:
                    print("Opcao invalida, por favor digite uma das opcoes indicadas.")
                    
        elif opcao == 2:
            while True:
                opcao_juridica = int(input("Escolha uma opcao: 1 - Cadastrar Pessoa Juridica / 2 - Listar Pessoa Juridica / 3 - Remover CNPJ / 4 - Atualizar lista / 0 - Voltar ao menu anterior: "))
                if opcao_juridica == 1:
                    novapj = PessoaJuridica()
                    nova_end_pj = Endereco()

                    novapj.nome = input("Digite o nome da empresa: ")
                    novapj.cnpj = input("Digite o CNPJ: ")
                    novapj.rendimento = float(input("Digite o rendimento mensal: "))

                    nova_end_pj.logradouro = input("Digite o logradouro: ")
                    nova_end_pj.numero = input("Digite o numero: ")
                    novapj.nomeFantasia = input("Digite o nome fantasia: ")
                    end_comercial = input("Esse endereco é comercial? S/N: ")
                    nova_end_pj.endereco_Comercial = end_comercial.strip().upper() == "S"
                    
                    novapj.endereco = nova_end_pj

                    lista_pj.append(novapj)

                    print("Cadastro realizado com sucesso!!")

                elif opcao_juridica == 2:
                    if lista_pj: 
                        for cada_pj in lista_pj:
                            print(f"Nome da empresa: {cada_pj.nome}")
                            print(f"CNPJ: {cada_pj.cnpj}")
                            print(f"Endereco: {cada_pj.endereco.logradouro}, {cada_pj.endereco.numero}")
                            print(f"Imposto a ser pago: {cada_pj.calcular_imposto(cada_pj.rendimento)}")
                            print("Digite 0 para sair.")
                            input()
                    else:
                        print("Lista Vazia")

                elif opcao_juridica == 3:
                    remover_cnpj = input("Digite o CNPJ da empresa que deseja excluir: ") 
                    empresa_encontrada = False

                    for cada_pj in lista_pj:
                        if cada_pj.cnpj == remover_cnpj:
                            lista_pj.remove(cada_pj)
                            print(f"CNPJ {remover_cnpj} foi removido.")
                            empresa_encontrada = True
                            break

                    if not empresa_encontrada:
                        print("Nenhum CNPJ foi encontrado.")

                elif opcao_juridica == 4:
                    # Código para atualizar lista, se necessário
                    pass

                elif opcao_juridica == 0:
                    print("Voltando ao menu anterior.")
                    break
                else:
                    print("Opcao invalida, por favor digite uma das opcoes indicadas.")
        
        elif opcao == 0:
            print("Obrigado por utilizar nosso sistema!")
            break
        else:
            print("Opcao invalida, por favor digite uma das opcoes indicadas.")

if __name__ == "__main__":
    main()