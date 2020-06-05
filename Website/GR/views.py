from django.shortcuts import render

# Create your views here.

# class GRPage(RoutablePageMixin, Page):
#     @route(r'^search/$')
#     def post_search(self, request, *args, **kwargs):
#         search_query = request.GET.get('q', None)
#         self.posts = self.get_posts()
#         if search_query:
#             self.posts = self.posts.filter(body__contains=search_query)
#             self.search_term = search_query
#             self.search_type = 'search'
#         return Page.serve(self, request, *args, **kwargs)