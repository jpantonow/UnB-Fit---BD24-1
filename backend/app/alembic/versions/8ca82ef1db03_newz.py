"""newz

Revision ID: 8ca82ef1db03
Revises: 10247b61fbc7
Create Date: 2024-09-08 11:54:56.007143

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '8ca82ef1db03'
down_revision = '10247b61fbc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("DROP TABLE plano;")
    op.execute("DROP TABLE dieta_refeicoes;")
    op.execute("DROP TABLE dieta;")
    op.execute("DROP TABLE refeicao;")
    op.execute("DROP TABLE avaliacao;")
    op.execute("DROP TABLE shape;")
    op.execute("DROP TABLE treinador_telefones;")
    op.execute("DROP TABLE treinador;")
    op.execute("DROP TABLE telefone;")
    op.execute("DROP TABLE treino_sessao;")
    op.execute("DROP TABLE treino_exercicio;")
    op.execute("DROP TABLE sessao;")
    op.execute("DROP TABLE treino;")
    op.execute("DROP TABLE exercicio;")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
