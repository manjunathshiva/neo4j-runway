from typing import List, Dict, Union, Any

from pydantic import BaseModel

from objects.property import Property

class Relationship(BaseModel):
    """
    Relationship representation.
    """

    type: str
    properties: List[Property] = []
    # unique_constraints: Union[List[Union[str, None]], None] = []
    source: str
    target: str

    def __init__(self, *a, **kw) -> None:
        super().__init__(*a, **kw)

        if self.properties is None:
            self.properties = []

    @property
    def property_names(self) -> List[str]:
        """
        The relationship's property names.
        """

        return [prop.name for prop in self.properties]
    
    @property
    def property_column_mapping(self) -> Dict[str, str]:
        """
        Map of properties to their respective csv columns.
        """

        return {prop.name: prop.csv_mapping for prop in self.properties}

    @property
    def unique_constraints(self) -> List[str]:
        """
        The relationship's unique constraints.
        """

        return [prop.name for prop in self.properties if prop.is_unique]
    
    @property
    def unique_constraints_column_mapping(self) -> Dict[str, str]:
        """
        Map of unique constraints to their respective csv columns.
        """

        return {prop.name: prop.csv_mapping for prop in self.properties if prop.is_unique}

    def validate_properties(self, csv_columns: List[str]) -> List[Union[str, None]]:
        errors = []
        if self.properties is not None:
            for prop in self.properties:
                if prop.csv_mapping not in csv_columns:
                    # raise ValueError(
                    errors.append(f"The relationship {self.type} the property {prop.name} mapped to csv column {prop.csv_mapping} which does not exist. {prop} should be edited or removed from relationship {self.type}.")
                        # )
        return errors
    
    # def validate_unique_constraints(self, csv_columns: List[str]) -> List[Union[str, None]]:
    #     errors = []
    #     if self.unique_constraints is not None:
    #         for prop in self.unique_constraints:
    #             if prop not in csv_columns:
    #                 # raise ValueError(
    #                 errors.append(f"The relationship {self.type} has a unique constraint {prop} which does not exist in csv columns. {prop} should be removed from relationship {self.type}.")
    #                 # )
    #     return errors
