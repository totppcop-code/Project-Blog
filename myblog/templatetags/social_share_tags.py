from django import template
from urllib.parse import quote

register = template.Library()

@register.simple_tag
def share_url(platform, url, title=''):
    encoded_url = quote(url)
    encoded_title = quote(title)

    templates = {
        'facebook': f'https://www.facebook.com/sharer/sharer.php?u={encoded_url}',
        'line': f'https://social-plugins.line.me/lineit/share?url={encoded_url}',
        'twitter': f'https://twitter.com/intent/tweet?url={encoded_url}&text={encoded_title}',
        'linkedin': f'https://www.linkedin.com/shareArticle?url={encoded_url}&title={encoded_title}',
        'email': f'mailto:?subject={encoded_title}&body={encoded_url}',
    }

    return templates.get(platform, '#')  # 若平台不支援，回傳 #
