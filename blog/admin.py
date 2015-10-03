from django.contrib import admin
from .models import Post, PostContent, BlogTitleContent

class PostContentInline(admin.StackedInline):
	model = PostContent
	extra = 1
	
class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields' :['post_title', 'active_revision_id']}),
	]
	inlines = [PostContentInline]
	list_display = ('post_title', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['post_title']

#admin.site.register(PostContent)
admin.site.register(Post, PostAdmin)
admin.site.register(BlogTitleContent)