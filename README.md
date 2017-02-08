#Tutorial Django

#setup environment
  ```
    install python3
    pip install djanggo
  ```
  Note : pastikan install python-pip

#Setup project
- Bikin project
  ```
    django-admin startproject tutorial_bioskop
  ```
  NOte : pastikan install python-django-common
- add project ke text editor
- migrate database, secara default dia pake SQLite:
  ```
    python manage.py migrate
  ```
- Bikin superuser
  ```
    python manage.py createsuperuser
  ```

#Run project
- jalankan aplikasi :
  ```
    python manage.py runserver
  ```
- run aplikasi di browser :
  ```
    localhost:8000
  ```
  Note : buat accsess admin localhost:8000/admin, kalo mau ganti di urls.py

#Bikin apps movie
- bikin apps :
  ```
    python manage.py startapp movie
  ```
- bikin model (movie/models.py):
  ```
    from __future__ import unicode_literals

    from django.db import models
    from django.contrib.auth.models import User

    class  Genre(object):
        title = models.CharField(max_length=200)
        description = models.TextField(null=True, blank=True)

    class  movie(object):
        title = models.Charfield(max_length=200)
        description = models.TextField(null=True, blank=True)
        show_from = models.DateField()
        show_until = models.DateField()
        genres = models.ManyToManyField(Genre)
        posted_by = models.ForeignKey(user)
        created_at = models.DataField(auto_now_add=True)
        updated_at = models.DateField(auto_now=True)
  ```
- setting app (settings.py)
  ```
    'movie' ke INSTALLED_APPS
  ```
- setting admin(admin.py)
  ```
    from django.contrib import admin
    from .models import Genre, Movie

    class  GenreAdmin(admin.ModelAdmin):
        pass

    class  MovieAdmin(admin,ModelAdmin):
        list_display = {'title', 'posted_by', 'show_from', 'show_until', 'created_at'}

        admin.site.register(Genre, GenreAdmin)
        admin.site.register(Movie, GenreAdmin)
  ```
- buat skrip migrasi :
  ```
    python manage.py makemigrations
  ```
- migrasi ke database :
  ```
    python manage.py migrate
  ```

#Hari ke 2

#Setting UI untuk Movie
- untuk mengganti nama variabel yang ada di system menjadi berbeda di UI, bisa menggunakan verbose_name, atau menulis di parameter pertama(movie/models.py)
  ```
    title = models.CharField(max_length=200, verbose_name="judul") #verbose_name digunakaan untuk mengubah nama di UI
    description = models.TextField("deskripsi",null=True, blank=True)#mengubah nama di UI juga bisa di parameter pertama
    show_from = models.DateField()
    show_until = models.DateField()
    genres = models.ManyToManyField(Genre)
    posted_by = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)#ketika kita membuat pertama kali akan dibuat pawa waktu pertama kali, ketika ada baru gk update
    updated_at = models.DateField(auto_now=True)#ketika membuat pertambahan maka akan diupdate
  ```
- buat fungsi untuk  Menampilkan macam-macam genre (movie/models.py)
  ```
    #fungsi Menampilkan macam-macam genre
      def show_genres(self):
          genre = self.genres.all()
          text=''
          for data in genre:
              text += data.title+", "
          return text
  ```
- setting dependency movie(title, description dll) yang akan ditampilkan di UI (movie/admin.py)
  ```
    #menentukan field apa saja yang ditampilkan pada tabel UI Movie, termasuk kita bisa menampilkan methode dari model yang di return string
    list_display = ('title','show_genres', 'posted_by', 'show_from', 'show_until', 'created_at', 'show_status')

    #menentukan field apa saja yang ditampilkan pada form UI Movie
    fields = ('title','description', 'show_from', 'show_until', 'genres')

    #override pada prosedur simpan
    def save_model(self, request, obj, form, change):
        obj.posted_by = request.user
        super(MovieAdmin, self).save_model(request,obj,form, change)
  ```

#Service di sisi client berupa daftar movie
- setting directory template ke folder view (setting.py)
  ```
    TEMPLATES = [
        {
            ...
            'DIRS': ['view'],
            ...
        },
    ]
  ```
- bikin UI (index.html)
- bikin service show status movie (movie/models.py)
  ```
      #fungsi untuk menampilkan movie sedang tayang, sudah tayang atau segera tayang dengan representasi angka
      def in_show(self):
          now = datetime.now().date()
          if now >= self.show_from and now <= self.show_until:
              return 1 #sedang tayang
          elif now > self.show_until:
              return -1 #sudah tayang
          else :
              return 0 #segera tayang
      #fungsi untuk menampilkan movie sedang tayang, sudah tayang atau segera tayang dengan representasi angka
      def show_status(self):
          if self.in_show() == 1 :
              return "sedang tayang"
          elif self.in_show()== -1 :
              return "selesai tayang"
          else :
              return "segera tayang"
  ```
- setting view(movie/views.py)
  ```
    from django.shortcuts import render
    from django.views.generic import ListView, DetailView, TemplateView
    from .models import Movie

    class IndexView(ListView):
        model = Movie
        template_name = 'index.html'
  ```
- bikin mapping url (urls.py)
  ```
    urlpatterns = [
        url(r'^$',IndexView.as_view(),name="index")#dollar ($) merupakan regular expression, merujuk pada url yang didepanya gak ada dan setelahnya gak ada
    ]
  ```

#Hari 3

#Bootstrapping UI
- Add File Bootstrap ke folder static
- Setting default static files(settings.py)
  ```
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
  ```
- Load Static file ke UI (view/index.html)
  ```
    ...
    {%load static%}
    ...
    ...
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    ...
  ```
  Note :
  dengan memanggil {% load static %} kita dapat menimpor file folder static
  dengan memanggil {% static 'css/bootstrap.min.css' %}

#Template Inheritance
- Memasukkan komponen dari dashboard.html ke index.html menggunakan {% block nama-fungsi %}
  (view/index.html)
  ```
    <div class="row">
      <div class="col-md-9">
          {% block content %}

          {% endblock%}
      </div>
      <div class="col-md-3">
          {% block sidebar %}
            <div class="panel panel-default">
              <div class="panel-heading">
                Panel Sidebar
              </div>
              <div class="panel-body">
                Panel Content
              </div>
            </div>
          {% endblock%}
      </div>
    </div>
  ```
  Note :
  sintaks {% block content %}{% endblock%} akan memanggil fungsi yang ada di dashboard.html

(view/index.html)
  ```
    {% extends 'index.html' %}
    {% load static %}
    {% block content %}
      <h1>Tayang Sekarang</h1>
      <div class="row">
        {% for data in object_list %}
          {% if data.in_show == 1 %}
            <div class="col-md-4">
              <a href="">
                <img src="{% static 'images/no-pre.png' %}" alt="" />
                <h3>{{data.title}}</h3>
                <div>tayang : {{data.show_from}} - {{data.show_until}} </div>
              </a>
            </div>
          {% endif %}
        {% endfor %}
      </div>
    {% endblock%}
  ```

Hari ke 4
#Menambahkan Pengaturan untuk Upload Cover
- Menmbahkan variabel untuk cover (models.py)
  ```
    class  Movie(models.Model):
      cover = models.ImageField(uplod_to="movie_covers/", blank=True, default="no-pre.png")
  ```
  Note :
- Install pillow(CLI)
  ```
    pip install pillow
  ```
- migrasi database (CLI)
  ```
    python manage.py makemigrations
    python manage.py migrate
  ```
- tambahkan cover pada admin (admin.py)
  ```
      #yang ditampilkan di movie
      list_display = ('title','cover','show_genres', 'posted_by', 'show_from', 'show_until', 'created_at', 'show_status')

      #yang ditampilan di form
      fields = ('title','cover','description', 'show_from', 'show_until', 'genres')
  ```
- Menambah konfigurasi media (settings.py)
  Note : media digunakan sebagai storage untuk cover
  ```
    MEDIA_URL = '/media'
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

  ```
- Mengubungkan url media (urls.py)
  ```
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  ```
- ubah UI (dashboard.html)
  ```
    <img src="{{data.cover.url}}" alt="" />
  ```

#Setting User Authentificarion
- UI (index.html)
  ```
    <div class="col-md-3">
        {% block sidebar %}
        {% if user.is_authenticated %}
          <div class="panel panel-default">
            <div class="panel-heading">User Aktif</div>
            <div class="panel-body">
                Selamat Datang {{user.username}} di Pemesanan Tiket Online
                <br>
                <a href="{% url 'logout' %}" class="btn btn-danger">Logout</a>
            </div>
          </div>
        {% else %}
          <div class="panel panel-default">
            <div class="panel-heading">Login &nbsp; Register</div>
            <div class="panel-body">
                <a href="{% url 'login' %}" class="btn btn-success">Login</a>
                <br>
                <a href="{% url 'register' %}" class="btn btn-primary">Register</a>
            </div>
          </div>
        {% endif %}{% endblock %}
    </div>
  ```
- url (urls.py)
  ```
    url(r'^login/', auth_views.login , {'template_name': 'login.html'}, name="login"),
    url(r'^logout/', auth_views.logout , {'next_page':'/'} , name="logout"),
    url(r'^pendaftaran/',IndexView.as_view() , name="register"),
  ```
- setting redirect sehabis login/logout (settings.py)
  ```
    LOGIN_REDIRECT_URL = 'index  
  ```
- bikin ui login di sidebar (login.html)
  ```
    {% extends 'index.html' %}
    {% block sidebar %}
    <div class="panel panel-default">
      <div class="panel-body">
        <form action="index.html" method="post">
          {% csrf_token %}{{ form.as_p}}
          <button type="submit" class="btn btn-success">Login</button>
          <a href="{% url 'index' %}" class="btn btn-primary">Kembali Ke Beranda</a>
        </form>
      </div>
    </div>
    {% endblock %}
  ```

#Buat aplikasi member
- bikin aplikasi member(CLI)
  ```
    python manage.py startapp member
  ```
-  bikin model (member/models.py)
  ```
    from __future__ import unicode_literals

    from django.db import models
    from django.contrib.auth.models import User

    # Create your models here.
    class Member(models.Model):
        user = models.OneToOneField(User)
        address = models.CharField(max_length=200, null=True, blank=True)
        phone = models.CharField(max_length=20)
        prof_pic = models.ImageField(null=True, blank=True)
        register_at = models.DateTimeField(auto_now_add=True)

  ```
- tambahkan pada member apps (setting.py)
  ```
    INSTALLED_APPS = [
      'member'
    ]
  ```

- Custom member fields(member/forms.py)
  ```
    from django.forms import ModeForm
    from django import forms
    from django.contrib.auth.models import User
    from member.models import Member

    class UserForm(ModelForm):
        password1 = forms.CharField(max_length=40)
        password2 = forms.CharField(max_length=40)

        class Meta:
            model = User
            fields = ('username', 'password1','password2', 'first_name', 'last_name', 'email')#kalo dikosongkan dia ngambil semua

        def clean(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')

            if(password1 != password2):
                raise forms.ValidationError('Password dan konfirmasi harus sama')

            return self.cleaned_data

    class MemberForm(ModelForm):
        class Meta:
            model = Member
            fields = ('prof_pic', 'address', 'phone')

  ```
- UI register (register.html)
  ```
    {% extends index.html %}
    {% block content %}
    <form action="" method="post" enctype="multipart/form-data">
      {% csrf_token %}{{form.as_p}}
      <button class="btn btn-success" type="submit">Daftar Member</button>
      <a href="{% url 'index' %}" class="btn">Kembali Ke Beranda</a>

    </form>
    {% endblock %}
  ```
- controller register (member/view.html)
  ```
    from django.shortcuts import render
    from .forms import UserForm,MemberForm
    # Create your views here.
    #ada 2 buah view dlm djangon yaitu class based view atau function based view
    #kalo ini pake function based view

    def register(request):
        return render(request, 'register.html',{'userform':UserForm,'meberform':MemberForm})
  ```
- url
  ```
    url(r'^pendaftaran/',register , name="register"),
  ```
#Costumisasi UI dengan crispy form
- install crispy forms
  ```
    pip install django-crispy-forms
  ```
- setting.py
  ```
  INSTALLED_APPS [
    'crispy_forms'  
  ]
  CRISPY_TEMPLATE_PACK = 'bootstrap3'
  ```
- add crispy forms (register.html)
 {% load crispy_forms_tags %}
{{userform|crispy}} {{memberform|crispy}}

#Costumize TopUp
- UI (index.html)
  ```
  <div class="col-md-4">
      {% block sidebar %}
      {% if user.is_authenticated %}
        <div class="panel panel-default">
          <div class="panel-heading">User Aktif</div>
          <div class="panel-body">
              <img src="{{user.member.prof_pic.url}}" class="img-responsive" />
                Selamat Datang {{user.first_name}} {{user.last_name}} di Pemesanan Tiket Online
                <div>
              </div>
              <ul>
                <li>Sisa Saldo : Rp. 0</li>
                <li>
                  <a href="" class="btn btn-primary btn-xs">Cek List Top Up</a>
                  <a href="" class="btn btn-primary btn-xs">Top Up Saldo</a>
                </li>
              </ul>
              <br>
              <a href="{% url 'logout' %}" class="btn btn-danger">Logout</a>
          </div>
        </div>
      {% else %}
        <div class="panel panel-default">
          <div class="panel-heading">Login &nbsp; Register</div>
          <div class="panel-body">
              <a href="{% url 'login' %}" class="btn btn-success">Login</a>
              <br>
              <a href="{% url 'register' %}" class="btn btn-primary">Register</a>
          </div>
        </div>
      {% endif %}{% endblock %}
  </div>
  ```
- class Top Up(member/models.py)
  ```

  class TopUp(models.Model):
      STATUS_CHOICES = (('p','pending'),('v','valid'),('i','invalid'))
      member = models.ForeignKey(Member)
      amount = models.IntegerField()
      receipt = models.ImageField("Bukti Bayar", upload_to='receipts/')
      status = models.CharField(max_length=1)
      upload_at = models.DateTimeField(auto_now_add=True)
      validated_at = models.DateTimeField(auto_now=True)
      checked_by = models.ForeignKey(User, null=True,blank=True)
  ```
- migrasi database(CLI)
  ```
    python manage.py makemigrations
    python manage.py migrate
  ```
- add ke admin (member/admin.py)
  ```
    from django.contrib import admin
    from .models import TopUp,Member

    # Register your models here.
    class MemberAdmin(admin.ModelAdmin):
        list_display = ('user','phone','address')

    class TopUpAdmin(admin.ModelAdmin):
        list_display = ('member','amount','receipt','status','uploaded_at','validated_at')
        fields = ('member','amount','receipt','status')
        readonly_fields = ('member','amount','receipt')

        def save_model(self, request, obj, form, change):
            obj.checked_by = request.user
            super(TopUpAdmin, self).save_model(request, obj, form, change)

        def has_add_permission(self, request):
            return False

    admin.site.register(TopUp, TopUpAdmin)
    admin.site.register(Member, MemberAdmin)
  ```
