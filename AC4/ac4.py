from abc import ABC, abstractmethod


class Pessoa (ABC):

    def __init__(self, nome, cpf, tel):
        self.nome = nome
        self.__cpf = cpf
        self.tel = tel

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    @abstractmethod
    def exibir_dados(self):
        pass


class Quarto():

    def __init__(self, numero, andar):
        self.numero = numero
        self.andar = andar


class Medico(Pessoa):

    def __init__(self, nome, cpf, tel, crm, salario, especialidade):
        super().__init__(nome, cpf, tel)
        self.crm = crm
        self.salario = salario
        self.especialidade = especialidade
        self.lista_especialidades = []

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'CRM: {self.crm}')
        print(f'Especialidade em exercício: {self.especialidade}')
        print(f'Formação: {self.lista_especialidades}')
        print(f'Salário: {self.salario}')
        print(f'Telefone: {self.tel}')

    def inserir_especilidade(self, especialidade):
        self.lista_especialidades.append(especialidade)


class Visita_medica():

    def __init__(self, data, horario, medico, paciente, observacoes):
        self.data = data
        self.horario = horario
        self.medico = medico
        self.paciente = paciente
        self.observacoes = observacoes


class Paciente (Pessoa):

    def __init__(self, nome, cpf, tel, rg, endereco, nascimento,
                 quarto, medico_responsavel):

        super().__init__(nome, cpf, tel)
        self.rg = rg
        self.endereco = endereco
        self.nascimento = nascimento
        self.quarto = quarto
        self.medico_responsavel = medico_responsavel
        self.historico = {}

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.tel}')
        print(f'Endereço: {self.endereco}')
        print(f'RG: {self.rg}')
        print(f'Data de Nascimento: {self.nascimento}')
        print(f'Quarto: {self.quarto}')
        print(f'Médico Responsável: {self.medico_responsavel}')

    def inserir_historico(self, chave, visita_medica):
        if self.nome == visita_medica.paciente:
            self.historico.update({chave: visita_medica})
        else:
            msg = 'Nome do paciente diverge do nome cadastrado!'
            raise ValueError(msg)
