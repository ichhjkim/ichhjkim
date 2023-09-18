import feedparser, datetime
 
tistory_blog_uri="https://keep-developing.tistory.com/"
feed = feedparser.parse(tistory_blog_uri+"/rss")
 
markdown_text = """
### Hi there 👋   

### 📖 Interest   
  - BackEnd
  - Devops 

### 🌱 I’m currently learning ...
- Kotlin Spring
- MySql
- Domain Driven Design


### 📕 Latest Blog Posts   

""" 
 
for content in feed['entries'][:5]:
    markdown_text += f"<a href =\"{content['link']}\"> {content['title']} </a> <br>"
    print(content['link'], content['title'])
    print(content)
 
f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
