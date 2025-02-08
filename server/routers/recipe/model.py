from sqlmodel import Field

from server.db.models import AuditHistoryBaseTable, RecipeIdTable, RecipeIdType


class Recipe(AuditHistoryBaseTable, RecipeIdTable, table=True):
    recipe_id: RecipeIdType = Field(primary_key=True)
    name: str = Field(index=True)
    description: str | None = Field(default=None)
