"""Create quiz_table

Revision ID: f51bb89968c4
Revises: ff0e5e154541
Create Date: 2023-10-12 02:20:54.017759

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f51bb89968c4'
down_revision: Union[str, None] = 'ff0e5e154541'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quiz',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('question_text', sa.String(), nullable=True),
    sa.Column('answer_text', sa.String(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_quiz_answer_text'), 'quiz', ['answer_text'], unique=False)
    op.create_index(op.f('ix_quiz_id'), 'quiz', ['id'], unique=False)
    op.create_index(op.f('ix_quiz_question_id'), 'quiz', ['question_id'], unique=False)
    op.create_index(op.f('ix_quiz_question_text'), 'quiz', ['question_text'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_quiz_question_text'), table_name='quiz')
    op.drop_index(op.f('ix_quiz_question_id'), table_name='quiz')
    op.drop_index(op.f('ix_quiz_id'), table_name='quiz')
    op.drop_index(op.f('ix_quiz_answer_text'), table_name='quiz')
    op.drop_table('quiz')
    # ### end Alembic commands ###
