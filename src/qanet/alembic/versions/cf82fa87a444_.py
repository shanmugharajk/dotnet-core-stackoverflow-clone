"""creates post_tag table

Revision ID: cf82fa87a444
Revises: 6f2a8b3c68fa
Create Date: 2021-04-14 07:32:08.475770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "cf82fa87a444"
down_revision = "6f2a8b3c68fa"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "post_tag",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("last_editor_user_id", sa.String(), nullable=True),
        sa.Column("owner_user_id", sa.String(), nullable=True),
        sa.Column("created_date", sa.DateTime(), nullable=True),
        sa.Column("modified_date", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["last_editor_user_id"],
            ["qanet_user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["owner_user_id"],
            ["qanet_user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("post_tag")
    # ### end Alembic commands ###
