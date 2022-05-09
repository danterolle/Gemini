from django.contrib import admin
from .models import Post, Category, Comment, UpVote, DownVote


class PostCategoryInline(admin.TabularInline):
    model = Post.categories.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'summary', 'content', 'author', 'created_on', 'slug')
    search_fields = ['title', 'content', 'categories']
    prepopulated_fields = {'slug': ('title',)}
    inlines = (PostCategoryInline,)
    exclude = ('categories',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(UpVote)
class UpVoteAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')


@admin.register(DownVote)
class DownVoteAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')
