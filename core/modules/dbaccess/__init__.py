import json


from core.modules import GenericFeature


class Dbaccess(GenericFeature):
    """Dbaccess defines the interface to execute actions on a SQL server.
    """
    def get_records(self, query):
        """ Get information from accounts and accountsettings tables.

            args:
                :query (str): MySQL query to update records.

            returns
                An array contains headers table.
                An array contains query result.

        """
        self._res.db.cursor.execute(query)
        row_headers = [x[0] for x in self._res.db.cursor.description]  # this will extract row headers
        results = self._res.db.cursor.fetchall()
        return row_headers, results