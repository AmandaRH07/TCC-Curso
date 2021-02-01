from django.db import models

class Banco_Medicamento_Anvisa(models.Model):
    id_anvisa = models.AutoField(primary_key=True)
    nome = models.TextField("Nome Medicamento")

    def __str__(self):
        return self.nome

class Medicamentos(models.Model):
    id_medicamentos = models.AutoField(primary_key=True) 
    fk_nome = models.ForeignKey(Banco_Medicamento_Anvisa, verbose_name='nome', on_delete=models.CASCADE, default="")
    funcao = models.TextField("Função", blank=True)
    data_inicio = models.DateField("Data de Início", blank=True)
    data_final = models.DateField("Data Final", blank=True)
    # horario = models.TimeField("Horario Medicamento")
    infos_extras = models.TextField("Informações Extras", blank=True)

# id_fk_cadastro_user = models.ForeignKey(User, verbose_name='CadastroUser', on_delete=models.CASCADE, default="")
