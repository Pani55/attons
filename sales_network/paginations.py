from rest_framework.pagination import PageNumberPagination


class ObjectListPagination(PageNumberPagination):
    """ Pagination for network objects. """

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 20
