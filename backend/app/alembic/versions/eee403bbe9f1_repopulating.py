"""repopulating

Revision ID: eee403bbe9f1
Revises: d60013fd162b
Create Date: 2024-09-08 03:58:20.185318

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = 'eee403bbe9f1'
down_revision = 'd60013fd162b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dieta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercicio',
    sa.Column('exercicio', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('grupo_muscular', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('refeicao',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('calorias', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sessao',
    sa.Column('data', sa.DateTime(), nullable=False),
    sa.Column('duracao_minutos', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('telefone',
    sa.Column('telefone', sqlmodel.sql.sqltypes.AutoString(length=11), nullable=False),
    sa.PrimaryKeyConstraint('telefone')
    )
    op.create_table('treino',
    sa.Column('calorias', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dieta_refeicoes',
    sa.Column('id_dieta', sa.Integer(), nullable=False),
    sa.Column('id_ref_manha', sa.Integer(), nullable=False),
    sa.Column('id_ref_tarde', sa.Integer(), nullable=False),
    sa.Column('id_ref_noite', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_dieta'], ['dieta.id'], ),
    sa.ForeignKeyConstraint(['id_ref_manha'], ['refeicao.id'], ),
    sa.ForeignKeyConstraint(['id_ref_noite'], ['refeicao.id'], ),
    sa.ForeignKeyConstraint(['id_ref_tarde'], ['refeicao.id'], ),
    sa.PrimaryKeyConstraint('id_dieta', 'id_ref_manha', 'id_ref_tarde', 'id_ref_noite')
    )
    op.create_table('treinador',
    sa.Column('telefone', sqlmodel.sql.sqltypes.AutoString(length=11), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.Column('especialidade', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.AutoString(length=11), nullable=False),
    sa.ForeignKeyConstraint(['telefone'], ['telefone.telefone'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('telefone')
    )
    op.create_table('treino_exercicio',
    sa.Column('id_treino', sa.Integer(), nullable=False),
    sa.Column('id_exercicio', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_exercicio'], ['exercicio.id'], ),
    sa.ForeignKeyConstraint(['id_treino'], ['treino.id'], ),
    sa.PrimaryKeyConstraint('id_treino', 'id_exercicio')
    )
    op.create_table('treino_sessao',
    sa.Column('id_treino1', sa.Integer(), nullable=False),
    sa.Column('id_treino2', sa.Integer(), nullable=False),
    sa.Column('id_treino3', sa.Integer(), nullable=False),
    sa.Column('id_sessao', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_sessao'], ['sessao.id'], ),
    sa.ForeignKeyConstraint(['id_treino1'], ['treino.id'], ),
    sa.ForeignKeyConstraint(['id_treino2'], ['treino.id'], ),
    sa.ForeignKeyConstraint(['id_treino3'], ['treino.id'], ),
    sa.PrimaryKeyConstraint('id_treino1', 'id_treino2', 'id_treino3', 'id_sessao')
    )
    op.create_table('plano',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Uuid(), nullable=False),
    sa.Column('id_sessao_treino', sa.Integer(), nullable=True),
    sa.Column('id_treinador', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id_avaliacao', sa.Integer(), nullable=True),
    sa.Column('id_dieta', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_avaliacao'], ['avaliacao.id'], ),
    sa.ForeignKeyConstraint(['id_dieta'], ['dieta.id'], ),
    sa.ForeignKeyConstraint(['id_sessao_treino'], ['sessao.id'], ),
    sa.ForeignKeyConstraint(['id_treinador'], ['treinador.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('treinador_telefones',
    sa.Column('treinador_id', sqlmodel.sql.sqltypes.AutoString(length=11), nullable=False),
    sa.Column('telefone_id', sqlmodel.sql.sqltypes.AutoString(length=11), nullable=False),
    sa.ForeignKeyConstraint(['telefone_id'], ['telefone.telefone'], ),
    sa.ForeignKeyConstraint(['treinador_id'], ['treinador.id'], ),
    sa.PrimaryKeyConstraint('treinador_id', 'telefone_id')
    )
    #op.add_column('avaliacao', sa.Column('shape_id', sa.Integer(), nullable=True))
    #op.create_foreign_key(None, 'avaliacao', 'shape', ['shape_id'], ['id'])
    #op.add_column('shape', sa.Column('id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shape', 'id')
    op.drop_constraint(None, 'avaliacao', type_='foreignkey')
    op.drop_column('avaliacao', 'shape_id')
    op.drop_table('treinador_telefones')
    op.drop_table('plano')
    op.drop_table('treino_sessao')
    op.drop_table('treino_exercicio')
    op.drop_table('treinador')
    op.drop_table('dieta_refeicoes')
    op.drop_table('treino')
    op.drop_table('telefone')
    op.drop_table('sessao')
    op.drop_table('refeicao')
    op.drop_table('exercicio')
    op.drop_table('dieta')
    # ### end Alembic commands ###
