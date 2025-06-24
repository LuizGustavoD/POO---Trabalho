class GerenciarAtividade:
    def __init__(self, atividade):
        self.atividade = atividade

    def criar_atividade(self):
        # Lógica para criar uma nova atividade
        print(f"Atividade '{self.atividade}' criada com sucesso.")

    def atualizar_atividade(self, nova_atividade):
        # Lógica para atualizar a atividade existente
        print(f"Atividade atualizada de '{self.atividade}' para '{nova_atividade}'.")
        self.atividade = nova_atividade

    def excluir_atividade(self):
        # Lógica para excluir a atividade
        print(f"Atividade '{self.atividade}' excluída com sucesso.")
        self.atividade = None