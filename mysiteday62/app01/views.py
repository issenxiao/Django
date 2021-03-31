from django.shortcuts import HttpResponse, render, redirect
from app01 import models
from django.urls import reverse
from utils.mypage import Page
# Create your views here.


# 展示出版社列表
def publisher_list(request):
    # 去数据库查出所有的出版社,填充到HTML中,给用户返回
    #ret = models.Publisher.objects.all().order_by("id")
    #return render(request, "publisher_list.html", {"publisher_list": ret})
    page_num = request.GET.get("page")
    print(page_num, type(page_num))
    # 总数据是多少
    total_count = models.Publisher.objects.all().count()
    
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/publisher_list/", max_page=9,)

    all_publisher = models.Publisher.objects.all()[page_obj.start:page_obj.end]

    page_html = page_obj.page_html()

    return render(request, "publisher_list.html", {"publisher_list": all_publisher, "page_html": page_html})

# 添加新的出版社
def add_publisher(request):
    error_msg = ""
    # 如果是POST请求,我就取到用户填写的数据
    if request.method == "POST":
        new_name = request.POST.get("publisher_name", None)
        if new_name:
            # 通过ORM去数据库里新建一条记录
            models.Publisher.objects.create(name=new_name)
            # 引导用户访问出版社列表页,查看是否添加成功  --> 跳转
            return redirect("/publisher_list/")
        else:
            error_msg = "出版社名字不能为空!"
    # 用户第一次来,我给他返回一个用来填写的HTML页面
    return render(request, "add_publisher.html", {"error": error_msg})


from django.views import View
# CBV版 添加新的出版社
class AddPublisher(View):
    def get(self, request):
        print(request.path_info)
        print(request.body)
        print("=" * 120)
        return render(request, "add_publisher.html")

    def post(self, request):
        print(request.body)
        print("=" * 120)
        new_name = request.POST.get("publisher_name", None)
        if new_name:
            # 通过ORM去数据库里新建一条记录
            models.Publisher.objects.create(name=new_name)
            # 引导用户访问出版社列表页,查看是否添加成功  --> 跳转
            return redirect("/publisher_list/")
        else:
            error_msg = "出版社名字不能为空!"
            return render(request, "add_publisher.html", {"error": error_msg})



# 删除出版社的函数
def delete_publisher(request):
    # print(request.GET)
    # print("=" * 120)
    # 删除指定的数据
    # 1. 从GET请求的参数里面拿到将要删除的数据的ID值
    del_id = request.GET.get("id", None)  # 字典取值,娶不到默认为None
    # 如果能取到id值
    if del_id:
        # 去数据库删除当前id值的数据
        # 根据id值查找到数据
        del_obj = models.Publisher.objects.get(id=del_id)
        # 删除
        del_obj.delete()
        # 返回删除后的页面,跳转到出版社的列表页,查看删除是否成功
        # return redirect("/publisher_list/")
        return HttpResponse("删除成功！")
    else:
        return HttpResponse("要删除的数据不存在!")


# 编辑出版社
def edit_publisher(request):
    # 用户修改完出版社的名字,点击提交按钮,给我发来新的出版社名字
    if request.method == "POST":
        print(request.POST)
        # 取新出版社名字
        edit_id = request.POST.get("id")
        new_name = request.POST.get("publisher_name")
        # 更新出版社
        # 根据id取到编辑的是哪个出版社
        edit_publisher = models.Publisher.objects.get(id=edit_id)
        edit_publisher.name = new_name
        edit_publisher.save()  # 把修改提交到数据库
        # 跳转出版社列表页,查看是否修改成功
        return redirect("/publisher_list/")
    # 从GET请求的URL中取到id参数
    edit_id = request.GET.get("id")
    if edit_id:
        # 获取到当前编辑的出版社对象
        publisher_obj = models.Publisher.objects.get(id=edit_id)
        return render(request, "edit_publisher.html", {"publisher": publisher_obj})
    else:
        return HttpResponse("编辑的出版社不存在!")


# 展示书的列表
def book_list(request):
    # 去数据库中查询所有的书籍
    #all_book = models.Book.objects.all()
    # 在HTML页面完成字符串替换(渲染数据)
    #return render(request, "book_list.html", {"all_book": all_book})
    # 从URL取参数
    page_num = request.GET.get("page")
    #print(page_num, type(page_num))
    # 总数据是多少
    total_count = models.Book.objects.all().count()
    
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/book_list/", max_page=9,)

    all_book = models.Book.objects.all()[page_obj.start:page_obj.end]

    page_html = page_obj.page_html()

    return render(request, "book_list.html", {"all_book": all_book, "page_html": page_html})

# 删除书籍
def delete_book(request):
    # 从URL里面获取要删除的书籍的id值(注意请求类型)
    delete_id = request.POST.get("id")  # 从URL里面取数据
    # 去删除数据库中删除指定id的数据
    models.Book.objects.get(id=delete_id).delete()
    # 返回书籍列表页面, 查看是否删除成功
    #return redirect("/book_list/")
    return HttpResponse("删除成功！")


# 添加书籍
def add_book(request):
    if request.method == "POST":
        print(request.POST)
        print("=" * 120)
        # {"book_title": "跟金老板学开车", "publisher": 9}
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        # 创建新书对象,自动提交
        models.Book.objects.create(title=new_title, publisher_id=new_publisher_id)

        # 用出版社对象创建
        # publisher_obj = models.Publisher.objects.get(id=new_publisher_id)
        # models.Book.objects.create(title=new_title, publisher=publisher_obj)

        # 返回到书籍列表页
        return redirect("/book_list/")

    # 取到所有的出版社
    ret = models.Publisher.objects.all()
    return render(request, "add_book.html", {"publisher_list": ret})


# 编辑书籍
def edit_book(request):
    if request.method == "POST":
        # 从提交的数据里面取,书名和书关联的出版社
        edit_id = request.POST.get("id")
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        # 更新
        edit_book_obj = models.Book.objects.get(id=edit_id)
        edit_book_obj.title = new_title  # 更新书名
        edit_book_obj.publisher_id = new_publisher_id  # 更新书籍关联的出版社
        # 将修改提交到数据库
        edit_book_obj.save()
        # 返回书籍列表页面,查看是否编辑成功
        return redirect("/book_list/")

    # 返回一个页面,让用户编辑书籍信息
    # 取到编辑的书的id值
    edit_id = request.GET.get("id")
    # 根据id去数据库中把具体的书籍对象拿到
    edit_book_obj = models.Book.objects.get(id=edit_id)
    print(edit_book_obj.id)
    print(edit_book_obj.title)
    print(edit_book_obj.publisher)  # 取到当前书籍对象关联的出版社对象
    print(edit_book_obj.publisher_id)  # 取到当前书籍对象关联的出版社的id值

    ret = models.Publisher.objects.all()
    url = reverse("edit_book")
    print(url)
    return render(
        request,
        "edit_book.html",
        {"publisher_list": ret, "book_obj": edit_book_obj}
    )



# 作者列表
def author_list(request):
    # author_obj = models.Author.objects.get(id=1)
    # print(author_obj.book.all())
    # print("=" * 120)

    # 查询所有的作者
    #all_author = models.Author.objects.all()
    #return render(request, "author_list.html", {"author_list": all_author})
    page_num = request.GET.get("page")
    print(page_num, type(page_num))
    # 总数据是多少
    total_count = models.Author.objects.all().count()
    
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/author_list/", max_page=9,)

    all_author = models.Author.objects.all()[page_obj.start:page_obj.end]

    page_html = page_obj.page_html()

    return render(request, "author_list.html", {"author_list": all_author, "page_html": page_html})

# 添加作者
def add_author(request):
    if request.method == "POST":
        print("in post...")
        # 取到提交的数据
        new_author_name = request.POST.get("author_name")
        # post提交的数据是多个值的时候一定会要用getlist,如多选的checkbox和多选的select
        books = request.POST.getlist("books")
        # 创建作者
        new_author_obj = models.Author.objects.create(name=new_author_name)
        # 把新作者和书籍建立对应关系,自动提交
        new_author_obj.book.set(books)
        # 跳转到作者列表页面,查看是否添加成功!
        return redirect("/author_list/")

    # 查询所有的书籍
    ret = models.Book.objects.all()
    return render(request, "add_author.html", {"book_list": ret})


# 删除作者
def delete_author(request):
    # 从URL里面取到要删除的作者id
    delete_id = request.GET.get("id")
    #根据ID值取到要删除的作者对象,直接删除
    # 1. 去作者表把作者删了
    # 2. 去作者和书的关联表,把对应的关联记录删除了
    models.Author.objects.get(id=delete_id).delete()
    # 返回作者列表页面
    # return redirect("/author_list/")
    return HttpResponse("删除成功！")


# 编辑作者
def edit_author(request):

    # 如果编辑完提交数据过来
    if request.method == "POST":
        # 拿到提交过来的编辑后的数据
        edit_author_id = request.POST.get("author_id")
        new_author_name = request.POST.get("author_name")
        # 拿到编辑后作者关联的书籍信息
        new_books = request.POST.getlist("books")
        # 根据ID找到当前编辑的作者对象
        edit_author_obj = models.Author.objects.get(id=edit_author_id)
        # 更新作者的名字
        edit_author_obj.name = new_author_name
        # 更新作者关联的书的对应关系
        edit_author_obj.book.set(new_books)
        # 将修改提交到数据库
        edit_author_obj.save()
        # 返回作者列表页,查看是否编辑成功
        return redirect("/author_list/")

    # 从URL里面取要编辑的作者的id信息
    edit_id = request.GET.get("id")
    # 找到要编辑的作者对象
    edit_author_obj = models.Author.objects.get(id=edit_id)

    # 查询所有的书籍对象
    ret = models.Book.objects.all()
    return render(request, "edit_author.html", {"book_list": ret, "author": edit_author_obj})



def test(request):
    print(request.GET)
    print(request.GET.get("id"))
    url = reverse("book_list")
    # return HttpResponse("OK")
    # return redirect("test.html")
    return render(request, "test.html")


# 处理上传文件的函数
def upload(request):
    """
    保存上传文件前，数据需要存放在某个位置。默认当上传文件小于2.5M时，django会将上传文件的全部内容读进内存。从内存读取一次，写磁盘一次。
    但当上传文件很大时，django会把上传文件写到临时文件中，然后存放到系统临时文件夹中。
    :param request:
    :return:
    """
    if request.method == "POST":
        print(request.FILES)
        print(request.FILES["upload_file"].name)
        # 从请求的FILES中获取上传文件的文件名，file为页面上type=files类型input的name属性值
        filename = request.FILES["upload_file"].name
        # # 在项目目录下新建一个文件
        with open(filename, "wb") as f:
            # 从上传的文件对象中一点一点读
            for i in request.FILES["upload_file"].chunks():
                # 写入本地文件
                f.write(i)
        return HttpResponse("上传OK")

    else:
        return render(request, "upload.html")


# 商品展示
def store(request):
    # 去数据库中查询所有的书籍
    all_goods = models.Goods.objects.all()
    # 在HTML页面完成字符串替换(渲染数据)
    return render(request, "store.html", {"all_goods": all_goods})

def show(request):
    return render(request,"show.html")