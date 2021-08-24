from radiojavanapi.mixins.private import PrivateRequest
from radiojavanapi.models import SearchResults
from radiojavanapi.extractors import extract_search_results

from typing import List
from urllib.parse import quote_plus

class SearchMixin(PrivateRequest):
    def search(self, query: str) -> SearchResults:
        """
        Search and get results as SearchResults object.

        Arguments
        ----------
            query: Search query

        Returns
        -------
            SearchResults: An object of SearchResults type

        """
        response = self.private_request('search',
                        params='query={}'.format(quote_plus(query))).json()
        return extract_search_results(response)

    def get_trending_searches(self) -> List[str]:
        """
        Get list of trending searches

        Returns
        -------
            List: A string list

        """
        return self.private_request('search_trending').json()