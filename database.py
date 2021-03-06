"""Houses the database class"""
# 3rd party imports
import pymongo

# No Builtin Imports
# No internal Imports


class Database:
    """Main database utility class"""

    def __init__(self, connection_name: str, connection_port: int) -> None:
        """Contructor function for Database class,

        Creates a connection to connection_name and connection_port, using MongoClient()"""
        # Create a connection if available
        if isinstance(connection_name, str) and isinstance(connection_port, int):
            self.connection = pymongo.MongoClient(connection_name, connection_port)
        # Otherwise use the defaults
        else:
            self.connection = pymongo.MongoClient("localhost", 27017)

    def find_documents(
        self, database_name: str, collection_name: str, collection_filter: dict = {}
    ) -> list:
        """Finds documents within a collection according to the filter

        database_name is the name of the database to search
        collection_name is the collection to search
        filter are what to filer documents by
        Returns a list of matched documents"""
        if (
            isinstance(database_name, str)
            and isinstance(collection_name, str)
            and isinstance(collection_filter, dict)
        ):
            return [
                document
                for document in self.connection[database_name][collection_name].find(
                    collection_filter
                )
            ]
        return None

    def insert_documents(
        self, database_name: str, collection_name: str, documents: list or dict
    ) -> bool:
        """Inserts documents into user defined collection

        database_name is the name of the database to search
        collection_name is the collection to search
        documents is the list of documents to add
        Returns whether the insert succeeded or not"""
        if isinstance(database_name, str) and isinstance(collection_name, str):
            if isinstance(documents, dict):
                return (
                    self.connection[database_name][collection_name]
                    .insert_one(documents)
                    .acknowledged
                )
            if isinstance(documents, list):
                return (
                    self.connection[database_name][collection_name]
                    .insert_many(documents)
                    .acknowledged
                )
        return False

    def delete_documents(
        self, database_name: str, collection_name: str, collection_filter: dict
    ) -> bool:
        """Deletes documents in a collection according to a user-defined filter

        database_name is the name of the database to search
        collection_name is the collection to search
        filter is what to filer documents by
        Returns whether or not whether the deletions were successful"""
        if (
            isinstance(database_name, str)
            and isinstance(collection_name, str)
            and isinstance(collection_filter, dict)
        ):
            return (
                self.connection[database_name][collection_name]
                .delete_one(collection_filter)
                .acknowledged
            )
        return False
