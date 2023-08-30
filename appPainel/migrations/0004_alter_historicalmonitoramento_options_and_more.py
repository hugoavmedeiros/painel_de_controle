# Generated by Django 4.2.4 on 2023-08-30 20:05

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appPainel', '0003_municipio_historicalmunicipio_iniciativa_municipio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalmonitoramento',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical monitoramento', 'verbose_name_plural': 'historical Mon. de Iniciativas'},
        ),
        migrations.AlterModelOptions(
            name='historicalmonitoramentoetapa',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical monitoramento etapa', 'verbose_name_plural': 'historical Mon. de Etapas'},
        ),
        migrations.AlterModelOptions(
            name='monitoramento',
            options={'ordering': ('iniciativa',), 'verbose_name_plural': 'Mon. de Iniciativas'},
        ),
        migrations.AlterModelOptions(
            name='monitoramentoetapa',
            options={'ordering': ('etapa',), 'verbose_name_plural': 'Mon. de Etapas'},
        ),
        migrations.AddField(
            model_name='etapa',
            name='municipio',
            field=models.ManyToManyField(default='Recife', to='appPainel.municipio', verbose_name='Nome do Município'),
        ),
        migrations.AlterField(
            model_name='acao',
            name='acao',
            field=models.CharField(max_length=255, verbose_name='Nome da Ação'),
        ),
        migrations.AlterField(
            model_name='acao',
            name='acao_cd',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código da Ação'),
        ),
        migrations.AlterField(
            model_name='acao',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPainel.programa', verbose_name='Nome do Programa'),
        ),
        migrations.AlterField(
            model_name='eixo',
            name='eixo_estrategico',
            field=models.CharField(max_length=255, verbose_name='Nome do Eixo'),
        ),
        migrations.AlterField(
            model_name='eixo',
            name='eixo_estrategico_cd',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código do Eixo'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='etapa',
            field=models.TextField(default='teste', verbose_name='Nome da Etapa'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='etapa_cd',
            field=models.CharField(max_length=4, verbose_name='Código da Etapa'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='iniciativa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPainel.iniciativa', verbose_name='Nome da Iniciativa'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='populacao',
            field=models.IntegerField(verbose_name='População'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPainel.responsavel', verbose_name='Nome do(a) Responsável'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='tema',
            field=models.TextField(verbose_name='Tema'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='tipo',
            field=models.CharField(choices=[('AÇÃO', 'AÇÃO'), ('AQUISIÇÃO', 'AQUISIÇÃO'), ('OBRA', 'OBRA'), ('PROGRAMA', 'PROGRAMA'), ('PROJETO DE LEI', 'PROJETO DE LEI'), ('PROJETO TÉCNICO', 'PROJETO TÉCNICO'), ('OUTROS', 'OUTROS')], max_length=255, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='historicalacao',
            name='acao',
            field=models.CharField(max_length=255, verbose_name='Nome da Ação'),
        ),
        migrations.AlterField(
            model_name='historicalacao',
            name='acao_cd',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código da Ação'),
        ),
        migrations.AlterField(
            model_name='historicalacao',
            name='programa',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appPainel.programa', verbose_name='Nome do Programa'),
        ),
        migrations.AlterField(
            model_name='historicaleixo',
            name='eixo_estrategico',
            field=models.CharField(max_length=255, verbose_name='Nome do Eixo'),
        ),
        migrations.AlterField(
            model_name='historicaleixo',
            name='eixo_estrategico_cd',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código do Eixo'),
        ),
        migrations.AlterField(
            model_name='historicaletapa',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='historicaletapa',
            name='etapa',
            field=models.TextField(default='teste', verbose_name='Nome da Etapa'),
        ),
        migrations.AlterField(
            model_name='historicaletapa',
            name='etapa_cd',
            field=models.CharField(max_length=4, verbose_name='Código da Etapa'),
        ),
        migrations.AlterField(
            model_name='historicaletapa',
            name='iniciativa',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appPainel.iniciativa', verbose_name='Nome da Iniciativa'),
        ),
        migrations.AlterField(
            model_name='historicaletapa',
            name='populacao',
            field=models.IntegerField(verbose_name='População'),
        ),
        migrations.AlterField(
            model_name='historicaletapa',
            name='responsavel',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appPainel.responsavel', verbose_name='Nome do(a) Responsável'),
        ),
        migrations.AlterField(
            model_name='historicaletapa',
            name='tema',
            field=models.TextField(verbose_name='Tema'),
        ),
        migrations.AlterField(
            model_name='historicaletapa',
            name='tipo',
            field=models.CharField(choices=[('AÇÃO', 'AÇÃO'), ('AQUISIÇÃO', 'AQUISIÇÃO'), ('OBRA', 'OBRA'), ('PROGRAMA', 'PROGRAMA'), ('PROJETO DE LEI', 'PROJETO DE LEI'), ('PROJETO TÉCNICO', 'PROJETO TÉCNICO'), ('OUTROS', 'OUTROS')], max_length=255, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='historicaliniciativa',
            name='acao',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appPainel.acao', verbose_name='Nome da Ação'),
        ),
        migrations.AlterField(
            model_name='historicaliniciativa',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='historicaliniciativa',
            name='gestor',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Nome do(a) Gestor(a)'),
        ),
        migrations.AlterField(
            model_name='historicaliniciativa',
            name='iniciativa',
            field=models.TextField(default='teste', verbose_name='Nome da Iniciativa'),
        ),
        migrations.AlterField(
            model_name='historicaliniciativa',
            name='iniciativa_cd',
            field=models.CharField(max_length=4, verbose_name='Código da Iniciativa'),
        ),
        migrations.AlterField(
            model_name='historicaliniciativa',
            name='orgao',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appPainel.orgao', verbose_name='Nome do Órgão'),
        ),
        migrations.AlterField(
            model_name='historicaliniciativa',
            name='populacao',
            field=models.IntegerField(verbose_name='População'),
        ),
        migrations.AlterField(
            model_name='historicaliniciativa',
            name='responsavel',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appPainel.responsavel', verbose_name='Nome do(a) Responsável'),
        ),
        migrations.AlterField(
            model_name='historicaliniciativa',
            name='secretaria',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appPainel.secretaria', verbose_name='Nome da Secretaria'),
        ),
        migrations.AlterField(
            model_name='historicaliniciativa',
            name='tema',
            field=models.TextField(verbose_name='Tema'),
        ),
        migrations.AlterField(
            model_name='historicaliniciativa',
            name='tipo',
            field=models.CharField(choices=[('AÇÃO', 'AÇÃO'), ('AQUISIÇÃO', 'AQUISIÇÃO'), ('OBRA', 'OBRA'), ('PROGRAMA', 'PROGRAMA'), ('PROJETO DE LEI', 'PROJETO DE LEI'), ('PROJETO TÉCNICO', 'PROJETO TÉCNICO'), ('OUTROS', 'OUTROS')], max_length=255, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramento',
            name='data_inicio_atualizado',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data Atualizada - Início'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramento',
            name='data_inicio_planejado',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Planejada - Início'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramento',
            name='data_termino_atualizado',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data Atualizada - Término'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramento',
            name='data_termino_planejado',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Planejada - Término'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramento',
            name='execucao_fisica',
            field=models.DecimalField(decimal_places=1, default=Decimal('0'), max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Execução Física'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramento',
            name='iniciativa',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appPainel.iniciativa', verbose_name='Nome da Iniciativa'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramento',
            name='link_fotos',
            field=models.URLField(max_length=500, verbose_name='Link de Fotos'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramento',
            name='link_repositorio',
            field=models.URLField(max_length=500, verbose_name='Link do Repositório'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramento',
            name='observacao',
            field=models.TextField(verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramento',
            name='status',
            field=models.CharField(choices=[('CANCELADA', 'CANCELADA'), ('CONCLUÍDA', 'CONCLUÍDA'), ('EM EXECUÇÃO', 'EM EXECUÇÃO'), ('EM FORMULAÇÃO', 'EM FORMULAÇÃO'), ('EM LICITAÇÃO', 'EM LICITAÇÃO'), ('LICITAÇÃO CONCLUÍDA', 'LICITAÇÃO CONCLUÍDA'), ('PARALISADA', 'PARALISADA'), ('PROJETO TÉCNICO EM ELABORAÇÃO', 'PROJETO TÉCNICO EM ELABORAÇÃO'), ('SUSPENSA', 'SUSPENSA')], max_length=255, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramentoetapa',
            name='data_inicio_atualizado',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data Atualizada - Início'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramentoetapa',
            name='data_inicio_planejado',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Planejada - Início'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramentoetapa',
            name='data_termino_atualizado',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data Atualizada - Término'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramentoetapa',
            name='data_termino_planejado',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Planejada - Término'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramentoetapa',
            name='etapa',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appPainel.etapa', verbose_name='Nome da Etapa'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramentoetapa',
            name='execucao_fisica',
            field=models.DecimalField(decimal_places=1, default=Decimal('0'), max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Execução Física'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramentoetapa',
            name='link_fotos',
            field=models.URLField(max_length=500, verbose_name='Link de Fotos'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramentoetapa',
            name='link_repositorio',
            field=models.URLField(max_length=500, verbose_name='Link de Repositório'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramentoetapa',
            name='observacao',
            field=models.TextField(verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='historicalmonitoramentoetapa',
            name='status',
            field=models.CharField(choices=[('CANCELADA', 'CANCELADA'), ('CONCLUÍDA', 'CONCLUÍDA'), ('EM EXECUÇÃO', 'EM EXECUÇÃO'), ('EM FORMULAÇÃO', 'EM FORMULAÇÃO'), ('EM LICITAÇÃO', 'EM LICITAÇÃO'), ('LICITAÇÃO CONCLUÍDA', 'LICITAÇÃO CONCLUÍDA'), ('PARALISADA', 'PARALISADA'), ('PROJETO TÉCNICO EM ELABORAÇÃO', 'PROJETO TÉCNICO EM ELABORAÇÃO'), ('SUSPENSA', 'SUSPENSA')], max_length=255, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='historicalmunicipio',
            name='codigo',
            field=models.CharField(max_length=7, verbose_name='Código do Município'),
        ),
        migrations.AlterField(
            model_name='historicalmunicipio',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome do Município'),
        ),
        migrations.AlterField(
            model_name='historicalorgao',
            name='orgao',
            field=models.CharField(max_length=255, verbose_name='Nome do Órgão'),
        ),
        migrations.AlterField(
            model_name='historicalorgao',
            name='orgao_cd',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código do Órgão'),
        ),
        migrations.AlterField(
            model_name='historicalorgao',
            name='secretaria',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appPainel.secretaria', verbose_name='Nome da Secretaria'),
        ),
        migrations.AlterField(
            model_name='historicalprograma',
            name='eixo_estrategico',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appPainel.eixo', verbose_name='Nome do Eixo'),
        ),
        migrations.AlterField(
            model_name='historicalprograma',
            name='programa',
            field=models.CharField(max_length=255, verbose_name='Nome do Programa'),
        ),
        migrations.AlterField(
            model_name='historicalprograma',
            name='programa_cd',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código do Programa'),
        ),
        migrations.AlterField(
            model_name='historicalresponsavel',
            name='nome',
            field=models.CharField(max_length=255, verbose_name='Nome do(a) Responsável'),
        ),
        migrations.AlterField(
            model_name='historicalresponsavel',
            name='orgao',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appPainel.orgao', verbose_name='Nome do Órgão'),
        ),
        migrations.AlterField(
            model_name='historicalresponsavel',
            name='secretaria',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appPainel.secretaria', verbose_name='Nome da Secretaria'),
        ),
        migrations.AlterField(
            model_name='historicalsecretaria',
            name='secretaria',
            field=models.CharField(max_length=255, verbose_name='Nome da Secretaria'),
        ),
        migrations.AlterField(
            model_name='historicalsecretaria',
            name='secretaria_cd',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código da Secretaria'),
        ),
        migrations.AlterField(
            model_name='iniciativa',
            name='acao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPainel.acao', verbose_name='Nome da Ação'),
        ),
        migrations.AlterField(
            model_name='iniciativa',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='iniciativa',
            name='gestor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nome do(a) Gestor(a)'),
        ),
        migrations.AlterField(
            model_name='iniciativa',
            name='iniciativa',
            field=models.TextField(default='teste', verbose_name='Nome da Iniciativa'),
        ),
        migrations.AlterField(
            model_name='iniciativa',
            name='iniciativa_cd',
            field=models.CharField(max_length=4, verbose_name='Código da Iniciativa'),
        ),
        migrations.AlterField(
            model_name='iniciativa',
            name='municipio',
            field=models.ManyToManyField(default='Recife', to='appPainel.municipio', verbose_name='Nome do Município'),
        ),
        migrations.AlterField(
            model_name='iniciativa',
            name='orgao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appPainel.orgao', verbose_name='Nome do Órgão'),
        ),
        migrations.AlterField(
            model_name='iniciativa',
            name='populacao',
            field=models.IntegerField(verbose_name='População'),
        ),
        migrations.AlterField(
            model_name='iniciativa',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPainel.responsavel', verbose_name='Nome do(a) Responsável'),
        ),
        migrations.AlterField(
            model_name='iniciativa',
            name='secretaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPainel.secretaria', verbose_name='Nome da Secretaria'),
        ),
        migrations.AlterField(
            model_name='iniciativa',
            name='tema',
            field=models.TextField(verbose_name='Tema'),
        ),
        migrations.AlterField(
            model_name='iniciativa',
            name='tipo',
            field=models.CharField(choices=[('AÇÃO', 'AÇÃO'), ('AQUISIÇÃO', 'AQUISIÇÃO'), ('OBRA', 'OBRA'), ('PROGRAMA', 'PROGRAMA'), ('PROJETO DE LEI', 'PROJETO DE LEI'), ('PROJETO TÉCNICO', 'PROJETO TÉCNICO'), ('OUTROS', 'OUTROS')], max_length=255, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='monitoramento',
            name='data_inicio_atualizado',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data Atualizada - Início'),
        ),
        migrations.AlterField(
            model_name='monitoramento',
            name='data_inicio_planejado',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Planejada - Início'),
        ),
        migrations.AlterField(
            model_name='monitoramento',
            name='data_termino_atualizado',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data Atualizada - Término'),
        ),
        migrations.AlterField(
            model_name='monitoramento',
            name='data_termino_planejado',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Planejada - Término'),
        ),
        migrations.AlterField(
            model_name='monitoramento',
            name='execucao_fisica',
            field=models.DecimalField(decimal_places=1, default=Decimal('0'), max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Execução Física'),
        ),
        migrations.AlterField(
            model_name='monitoramento',
            name='iniciativa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPainel.iniciativa', verbose_name='Nome da Iniciativa'),
        ),
        migrations.AlterField(
            model_name='monitoramento',
            name='link_fotos',
            field=models.URLField(max_length=500, verbose_name='Link de Fotos'),
        ),
        migrations.AlterField(
            model_name='monitoramento',
            name='link_repositorio',
            field=models.URLField(max_length=500, verbose_name='Link do Repositório'),
        ),
        migrations.AlterField(
            model_name='monitoramento',
            name='observacao',
            field=models.TextField(verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='monitoramento',
            name='status',
            field=models.CharField(choices=[('CANCELADA', 'CANCELADA'), ('CONCLUÍDA', 'CONCLUÍDA'), ('EM EXECUÇÃO', 'EM EXECUÇÃO'), ('EM FORMULAÇÃO', 'EM FORMULAÇÃO'), ('EM LICITAÇÃO', 'EM LICITAÇÃO'), ('LICITAÇÃO CONCLUÍDA', 'LICITAÇÃO CONCLUÍDA'), ('PARALISADA', 'PARALISADA'), ('PROJETO TÉCNICO EM ELABORAÇÃO', 'PROJETO TÉCNICO EM ELABORAÇÃO'), ('SUSPENSA', 'SUSPENSA')], max_length=255, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='monitoramentoetapa',
            name='data_inicio_atualizado',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data Atualizada - Início'),
        ),
        migrations.AlterField(
            model_name='monitoramentoetapa',
            name='data_inicio_planejado',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Planejada - Início'),
        ),
        migrations.AlterField(
            model_name='monitoramentoetapa',
            name='data_termino_atualizado',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data Atualizada - Término'),
        ),
        migrations.AlterField(
            model_name='monitoramentoetapa',
            name='data_termino_planejado',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Planejada - Término'),
        ),
        migrations.AlterField(
            model_name='monitoramentoetapa',
            name='etapa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPainel.etapa', verbose_name='Nome da Etapa'),
        ),
        migrations.AlterField(
            model_name='monitoramentoetapa',
            name='execucao_fisica',
            field=models.DecimalField(decimal_places=1, default=Decimal('0'), max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Execução Física'),
        ),
        migrations.AlterField(
            model_name='monitoramentoetapa',
            name='link_fotos',
            field=models.URLField(max_length=500, verbose_name='Link de Fotos'),
        ),
        migrations.AlterField(
            model_name='monitoramentoetapa',
            name='link_repositorio',
            field=models.URLField(max_length=500, verbose_name='Link de Repositório'),
        ),
        migrations.AlterField(
            model_name='monitoramentoetapa',
            name='observacao',
            field=models.TextField(verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='monitoramentoetapa',
            name='status',
            field=models.CharField(choices=[('CANCELADA', 'CANCELADA'), ('CONCLUÍDA', 'CONCLUÍDA'), ('EM EXECUÇÃO', 'EM EXECUÇÃO'), ('EM FORMULAÇÃO', 'EM FORMULAÇÃO'), ('EM LICITAÇÃO', 'EM LICITAÇÃO'), ('LICITAÇÃO CONCLUÍDA', 'LICITAÇÃO CONCLUÍDA'), ('PARALISADA', 'PARALISADA'), ('PROJETO TÉCNICO EM ELABORAÇÃO', 'PROJETO TÉCNICO EM ELABORAÇÃO'), ('SUSPENSA', 'SUSPENSA')], max_length=255, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='codigo',
            field=models.CharField(max_length=7, verbose_name='Código do Município'),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome do Município'),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='orgao',
            field=models.CharField(max_length=255, verbose_name='Nome do Órgão'),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='orgao_cd',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código do Órgão'),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='secretaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPainel.secretaria', verbose_name='Nome da Secretaria'),
        ),
        migrations.AlterField(
            model_name='programa',
            name='eixo_estrategico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPainel.eixo', verbose_name='Nome do Eixo'),
        ),
        migrations.AlterField(
            model_name='programa',
            name='programa',
            field=models.CharField(max_length=255, verbose_name='Nome do Programa'),
        ),
        migrations.AlterField(
            model_name='programa',
            name='programa_cd',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código do Programa'),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='nome',
            field=models.CharField(max_length=255, verbose_name='Nome do(a) Responsável'),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='orgao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appPainel.orgao', verbose_name='Nome do Órgão'),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='secretaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPainel.secretaria', verbose_name='Nome da Secretaria'),
        ),
        migrations.AlterField(
            model_name='secretaria',
            name='secretaria',
            field=models.CharField(max_length=255, verbose_name='Nome da Secretaria'),
        ),
        migrations.AlterField(
            model_name='secretaria',
            name='secretaria_cd',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código da Secretaria'),
        ),
    ]
