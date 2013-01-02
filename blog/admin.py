from django.contrib import admin
from blog.models import User,Post#,Comment

class UserAdmin(admin.ModelAdmin):
	pass

#class CommentInline(admin.TabularInline):
#	model = Comment
#	date_hierarchy = 'pub_date'
#	raw_id_fiels = ('author','post')
#	search_fields = ['author__nick']

#class CommentAdmin(admin.ModelAdmin):
#	date_hierarchy = 'pub_date'
#	list_display = ('author', 'post', 'pub_date')
#	list_filter = ('author', 'post', 'pub_date')
#	raw_id_fiels = ('author','post')
#	search_fields = ['author__nick', 'post__title']

class PostAdmin(admin.ModelAdmin):
	date_hierarchy = 'pub_date'
	list_display = ('title', 'pub_date')
	#inlines = [CommentInline,]
	search_fields = ['title']

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
#admin.site.register(Comment, CommentAdmin)
